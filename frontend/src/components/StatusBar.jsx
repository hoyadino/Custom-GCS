export default function StatusBar({ telemetry, backendConnected }) {
  return (
    <section className="status-bar">
      <div className="status-item">
        Connected
        <strong>{backendConnected && telemetry.connected ? "Connected" : "Disconnected"}</strong>
      </div>
      <div className="status-item">
        Source
        <strong>{telemetry.source}</strong>
      </div>
      <div className="status-item">
        Mode
        <strong>{telemetry.mode}</strong>
      </div>
      <div className="status-item">
        Armed
        <strong>{telemetry.armed ? "ARMED" : "DISARMED"}</strong>
      </div>
    </section>
  );
}
