export default function EventLog({ messages }) {
  return (
    <section className="panel">
      <h2>Event Log</h2>
      <ul className="event-list">
        {(messages || []).map((message, index) => (
          <li key={`${message}-${index}`}>{message}</li>
        ))}
      </ul>
    </section>
  );
}
