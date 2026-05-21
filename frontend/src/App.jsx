import { useEffect, useState } from "react";

import { connectTelemetry } from "./api/websocket.js";
import AttitudePanel from "./components/AttitudePanel.jsx";
import BatteryPanel from "./components/BatteryPanel.jsx";
import CameraView from "./components/CameraView.jsx";
import EventLog from "./components/EventLog.jsx";
import FlightInfoPanel from "./components/FlightInfoPanel.jsx";
import MissionProgress from "./components/MissionProgress.jsx";
import StatusBar from "./components/StatusBar.jsx";

const initialTelemetry = {
  connected: false,
  source: "none",
  mode: "UNKNOWN",
  armed: false,
  flight_time_sec: 0,
  battery_percent: 0,
  voltage_v: 0,
  current_a: 0,
  altitude_m: 0,
  speed_mps: 0,
  roll_deg: 0,
  pitch_deg: 0,
  yaw_deg: 0,
  mission_current: 0,
  mission_total: 0,
  mission_stage: "Idle",
  camera_status: "UNKNOWN",
  camera_fps: 0,
  ai_status: "UNKNOWN",
  ai_fps: 0,
  target_detected: false,
  target_confidence: 0,
  event_messages: [],
  timestamp: 0
};

export default function App() {
  const [telemetry, setTelemetry] = useState(initialTelemetry);
  const [backendStatus, setBackendStatus] = useState("disconnected");

  useEffect(() => {
    return connectTelemetry(setTelemetry, setBackendStatus);
  }, []);

  const backendConnected = backendStatus === "connected";

  return (
    <main className="app-shell">
      <style>{styles}</style>
      <StatusBar telemetry={telemetry} backendConnected={backendConnected} />
      {!backendConnected && <div className="disconnect-banner">Backend disconnected</div>}
      <section className="dashboard-grid">
        <BatteryPanel telemetry={telemetry} />
        <FlightInfoPanel telemetry={telemetry} />
        <AttitudePanel telemetry={telemetry} />
        <MissionProgress telemetry={telemetry} />
        <CameraView telemetry={telemetry} />
        <EventLog messages={telemetry.event_messages} />
      </section>
    </main>
  );
}

const styles = `
  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    background: #101418;
    color: #f4f7fb;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .app-shell {
    min-height: 100vh;
    padding: 20px;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-top: 14px;
  }

  .panel {
    min-height: 150px;
    border: 1px solid #26313c;
    border-radius: 8px;
    background: #171d24;
    padding: 16px;
  }

  .panel h2 {
    margin: 0 0 14px;
    font-size: 16px;
    font-weight: 700;
  }

  .metric-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
  }

  .metric {
    color: #9eabb8;
    font-size: 12px;
  }

  .metric strong {
    display: block;
    margin-top: 4px;
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
  }

  .status-bar {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 10px;
    border: 1px solid #2c3944;
    border-radius: 8px;
    background: #1b232b;
    padding: 12px;
  }

  .status-item {
    color: #9eabb8;
    font-size: 12px;
  }

  .status-item strong {
    display: block;
    margin-top: 4px;
    color: #ffffff;
    font-size: 15px;
  }

  .disconnect-banner {
    margin-top: 14px;
    border: 1px solid #a74d4d;
    border-radius: 8px;
    background: #321c1c;
    color: #ffd7d7;
    padding: 12px 14px;
  }

  .progress-track {
    height: 10px;
    overflow: hidden;
    border-radius: 999px;
    background: #2b353f;
  }

  .progress-fill {
    height: 100%;
    background: #43b883;
    transition: width 160ms linear;
  }

  .camera-placeholder {
    display: grid;
    min-height: 190px;
    place-items: center;
    border: 1px dashed #455463;
    border-radius: 8px;
    background: #11171d;
    color: #9eabb8;
  }

  .event-list {
    display: grid;
    gap: 8px;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .event-list li {
    border-radius: 6px;
    background: #202933;
    padding: 8px 10px;
    color: #d9e3ec;
    font-size: 13px;
  }

  @media (max-width: 900px) {
    .dashboard-grid,
    .status-bar {
      grid-template-columns: 1fr;
    }
  }
`;
