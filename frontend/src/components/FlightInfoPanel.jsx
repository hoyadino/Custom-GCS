export default function FlightInfoPanel({ telemetry }) {
  return (
    <section className="panel">
      <h2>Flight Info</h2>
      <div className="metric-grid">
        <div className="metric">
          Flight Time
          <strong>{telemetry.flight_time_sec}s</strong>
        </div>
        <div className="metric">
          Altitude
          <strong>{telemetry.altitude_m} m</strong>
        </div>
        <div className="metric">
          Speed
          <strong>{telemetry.speed_mps} m/s</strong>
        </div>
      </div>
    </section>
  );
}
