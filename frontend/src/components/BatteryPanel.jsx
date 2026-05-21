export default function BatteryPanel({ telemetry }) {
  return (
    <section className="panel">
      <h2>Battery</h2>
      <div className="metric-grid">
        <div className="metric">
          Percent
          <strong>{telemetry.battery_percent}%</strong>
        </div>
        <div className="metric">
          Voltage
          <strong>{telemetry.voltage_v} V</strong>
        </div>
        <div className="metric">
          Current
          <strong>{telemetry.current_a} A</strong>
        </div>
      </div>
    </section>
  );
}
