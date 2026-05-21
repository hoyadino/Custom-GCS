import asyncio
import time
from typing import Any, AsyncIterator

from telemetry_state import TelemetryState


class LteJsonInput:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        lte_config = config.get("lte", {})
        self.listen_ip = lte_config.get("listen_ip", "0.0.0.0")
        self.listen_port = int(lte_config.get("listen_port", 15000))

    async def stream(self) -> AsyncIterator[TelemetryState]:
        # TODO: Listen for Jetson/LTE JSON packets.
        # TODO: Validate packet fields and map them into the common TelemetryState format.
        while True:
            yield TelemetryState(
                connected=False,
                source="lte",
                mode="LTE_JSON_TODO",
                event_messages=[
                    f"LTE JSON input not implemented: {self.listen_ip}:{self.listen_port}",
                ],
                timestamp=time.time(),
            )
            await asyncio.sleep(1.0)
