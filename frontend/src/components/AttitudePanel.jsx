export default function AttitudePanel({ telemetry }) {
  return (
    <section className="panel">
      <h2>Attitude</h2>
      <div className="metric-grid">
        <div className="metric">
          Roll
          <strong>{telemetry.roll_deg} deg</strong>
        </div>
        <div className="metric">
          Pitch
          <strong>{telemetry.pitch_deg} deg</strong>
        </div>
        <div className="metric">
          Yaw
          <strong>{telemetry.yaw_deg} deg</strong>
        </div>
      </div>
    </section>
  );
}
