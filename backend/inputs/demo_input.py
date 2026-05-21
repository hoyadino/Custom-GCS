import asyncio
import json
import math
import time
from pathlib import Path
from typing import Any, AsyncIterator

from telemetry_state import TelemetryState


class DemoTelemetryInput:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.update_hz = float(config.get("app", {}).get("update_hz", 10))
        self.started_at = time.monotonic()
        self.stages = self._load_stages()

    def _load_stages(self) -> list[str]:
        scenario_path = Path(__file__).resolve().parents[2] / "demo" / "demo_scenario.json"
        fallback = [
            "System Ready",
            "Takeoff",
            "Search Area Entry",
            "Target Detection",
            "Mission Complete",
        ]

        if not scenario_path.exists():
            return fallback

        with scenario_path.open("r", encoding="utf-8") as scenario_file:
            scenario = json.load(scenario_file)

        stages = scenario.get("stages", [])
        names = [stage.get("name") for stage in stages if stage.get("name")]
        return names or fallback

    def _stage_index(self, elapsed: float) -> int:
        if elapsed < 5:
            return 0
        if elapsed < 15:
            return 1
        if elapsed < 25:
            return 2
        if elapsed < 40:
            return 3
        return 4

    def _event_messages(self, stage_index: int) -> list[str]:
        events = [
            "Demo telemetry stream started",
            "System checks complete",
            "Takeoff command accepted",
            "Search area reached",
            "Target candidate detected",
            "Mission complete",
        ]
        return events[max(0, stage_index) : stage_index + 2][-5:]

    async def stream(self) -> AsyncIterator[TelemetryState]:
        interval = 1.0 / max(self.update_hz, 1.0)
        mission_total = len(self.stages)

        while True:
            elapsed = time.monotonic() - self.started_at
            stage_index = min(self._stage_index(elapsed), mission_total - 1)
            target_detected = elapsed >= 25
            target_confidence = 0.0
            if target_detected:
                target_confidence = min(0.9, 0.45 + 0.45 * abs(math.sin(elapsed / 3.0)))

            altitude = min(30.0, elapsed * 2.0)
            if altitude >= 30.0:
                altitude += 0.5 * math.sin(elapsed / 4.0)

            speed = min(8.0, elapsed * 0.8) if elapsed < 10 else 4.0 + 3.0 * math.sin(elapsed / 4.5)
            speed = max(0.0, min(8.0, speed))

            yield TelemetryState(
                connected=True,
                source="demo",
                mode="DEMO",
                armed=elapsed >= 5,
                flight_time_sec=round(elapsed, 1),
                battery_percent=round(max(0.0, 100.0 - elapsed * 0.08), 1),
                voltage_v=round(max(14.0, 16.8 - elapsed * 0.005), 2),
                current_a=round(8.0 + 3.0 * abs(math.sin(elapsed / 2.0)), 2),
                altitude_m=round(altitude, 2),
                speed_mps=round(speed, 2),
                roll_deg=round(8.0 * math.sin(elapsed / 2.5), 2),
                pitch_deg=round(5.0 * math.sin(elapsed / 3.0), 2),
                yaw_deg=round((elapsed * 12.0) % 360.0, 2),
                mission_current=stage_index + 1,
                mission_total=mission_total,
                mission_stage=self.stages[stage_index],
                camera_status="DEMO",
                camera_fps=30.0,
                ai_status="DEMO",
                ai_fps=12.0,
                target_detected=target_detected,
                target_confidence=round(target_confidence, 2),
                event_messages=self._event_messages(stage_index),
                timestamp=time.time(),
            )

            await asyncio.sleep(interval)
