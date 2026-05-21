import asyncio
import sys
from pathlib import Path
from typing import Any

import uvicorn
import yaml
from fastapi import FastAPI, WebSocket

from inputs.demo_input import DemoTelemetryInput
from inputs.lte_json_input import LteJsonInput
from inputs.mavlink_udp_input import MavlinkUdpInput
from services.websocket_manager import WebSocketManager
from telemetry_state import TelemetryState


def get_backend_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


BACKEND_DIR = get_backend_dir()
CONFIG_PATH = BACKEND_DIR / "config.yaml"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file) or {}


config = load_config()
app = FastAPI(title="Custom GCS Backend")
websocket_manager = WebSocketManager()
latest_state = TelemetryState()
telemetry_task: asyncio.Task | None = None


def create_input_adapter() -> object:
    app_config = config.get("app", {})
    mode = app_config.get("mode", "demo")

    if mode == "demo":
        return DemoTelemetryInput(config=config)
    if mode == "sitl":
        return MavlinkUdpInput(config=config)
    if mode == "real":
        return LteJsonInput(config=config)

    raise ValueError(f"Unsupported app.mode: {mode}")


async def telemetry_loop() -> None:
    global latest_state

    adapter = create_input_adapter()
    async for state in adapter.stream():
        latest_state = state
        await websocket_manager.broadcast(state.to_dict())


@app.on_event("startup")
async def start_background_tasks() -> None:
    global telemetry_task
    telemetry_task = asyncio.create_task(telemetry_loop())


@app.on_event("shutdown")
async def stop_background_tasks() -> None:
    if telemetry_task:
        telemetry_task.cancel()
        try:
            await telemetry_task
        except asyncio.CancelledError:
            pass


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "mode": config.get("app", {}).get("mode", "demo"),
    }


@app.websocket("/ws/telemetry")
async def telemetry_websocket(websocket: WebSocket) -> None:
    await websocket_manager.connect(websocket)
    await websocket.send_json(latest_state.to_dict())

    try:
        while True:
            await asyncio.sleep(60)
    finally:
        websocket_manager.disconnect(websocket)


if __name__ == "__main__":
    server_config = config.get("server", {})
    uvicorn.run(
        app,
        host=server_config.get("host", "127.0.0.1"),
        port=int(server_config.get("port", 8000)),
    )
