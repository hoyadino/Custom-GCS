export default function MissionProgress({ telemetry }) {
  const total = Math.max(telemetry.mission_total || 0, 1);
  const current = Math.max(telemetry.mission_current || 0, 0);
  const percent = Math.min(100, Math.round((current / total) * 100));

  return (
    <section className="panel">
      <h2>Mission Progress</h2>
      <div className="metric">
        Stage
        <strong>{telemetry.mission_stage}</strong>
      </div>
      <div className="progress-track" aria-label="Mission progress">
        <div className="progress-fill" style={{ width: `${percent}%` }} />
      </div>
      <p>
        {current} / {total}
      </p>
    </section>
  );
}
