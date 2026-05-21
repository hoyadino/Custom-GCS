export function connectTelemetry(onTelemetry, onStatus) {
  const url = "ws://localhost:8000/ws/telemetry";
  let socket = null;
  let reconnectTimer = null;
  let active = true;

  const connect = () => {
    onStatus("connecting");
    socket = new WebSocket(url);

    socket.onopen = () => {
      onStatus("connected");
    };

    socket.onmessage = (event) => {
      try {
        onTelemetry(JSON.parse(event.data));
      } catch (error) {
        console.error("Invalid telemetry payload", error);
      }
    };

    socket.onerror = () => {
      onStatus("disconnected");
    };

    socket.onclose = () => {
      onStatus("disconnected");
      if (active) {
        reconnectTimer = window.setTimeout(connect, 1500);
      }
    };
  };

  connect();

  return () => {
    active = false;
    window.clearTimeout(reconnectTimer);
    if (socket) {
      socket.close();
    }
  };
}
