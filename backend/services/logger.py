from pathlib import Path

from telemetry_state import TelemetryState


class CsvTelemetryLogger:
    def __init__(self, enabled: bool, directory: str | Path) -> None:
        self.enabled = enabled
        self.directory = Path(directory)
        self.session_path: Path | None = None

    def start_session(self) -> None:
        if not self.enabled:
            return

        self.directory.mkdir(parents=True, exist_ok=True)
        # TODO: Create a timestamped CSV file and write the header row.

    def write_state(self, state: TelemetryState) -> None:
        if not self.enabled or self.session_path is None:
            return

        # TODO: Append selected TelemetryState fields as a CSV row.
        _ = state
