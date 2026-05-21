export default function CameraView({ telemetry }) {
  return (
    <section className="panel">
      <h2>Camera</h2>
      <div className="camera-placeholder">Camera placeholder</div>
      <div className="metric-grid">
        <div className="metric">
          Camera
          <strong>{telemetry.camera_status}</strong>
        </div>
        <div className="metric">
          AI
          <strong>{telemetry.ai_status}</strong>
        </div>
        <div className="metric">
          Target
          <strong>{telemetry.target_detected ? "Detected" : "None"}</strong>
        </div>
        <div className="metric">
          Confidence
          <strong>{telemetry.target_confidence}</strong>
        </div>
      </div>
    </section>
  );
}
