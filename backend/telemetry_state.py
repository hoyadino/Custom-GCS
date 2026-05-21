import time
from dataclasses import asdict, dataclass, field


@dataclass
class TelemetryState:
    connected: bool = False
    source: str = "none"
    mode: str = "UNKNOWN"
    armed: bool = False
    flight_time_sec: float = 0.0
    battery_percent: float = 0.0
    voltage_v: float = 0.0
    current_a: float = 0.0
    altitude_m: float = 0.0
    speed_mps: float = 0.0
    roll_deg: float = 0.0
    pitch_deg: float = 0.0
    yaw_deg: float = 0.0
    mission_current: int = 0
    mission_total: int = 0
    mission_stage: str = "Idle"
    camera_status: str = "UNKNOWN"
    camera_fps: float = 0.0
    ai_status: str = "UNKNOWN"
    ai_fps: float = 0.0
    target_detected: bool = False
    target_confidence: float = 0.0
    event_messages: list[str] = field(default_factory=list)
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return asdict(self)
