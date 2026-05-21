import asyncio
import time
from typing import Any, AsyncIterator

from telemetry_state import TelemetryState


class MavlinkUdpInput:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.connection = config.get("mavlink", {}).get("connection", "udp:127.0.0.1:14540")

    async def stream(self) -> AsyncIterator[TelemetryState]:
        # TODO: Connect to PX4 SITL MAVLink UDP using pymavlink.
        # TODO: Convert HEARTBEAT, GLOBAL_POSITION_INT, ATTITUDE, BATTERY_STATUS,
        # and mission messages into the common TelemetryState format.
        while True:
            yield TelemetryState(
                connected=False,
                source="sitl",
                mode="MAVLINK_TODO",
                event_messages=[f"MAVLink UDP input not implemented: {self.connection}"],
                timestamp=time.time(),
            )
            await asyncio.sleep(1.0)
