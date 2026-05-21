# Architecture

Custom GCS uses a shared telemetry pipeline:

```text
Input Adapter -> TelemetryState -> WebSocket -> Frontend
```

Each input adapter is responsible for converting its source data into the same `TelemetryState` shape.

The `demo`, `sitl`, and `real` modes share the same `TelemetryState` format. The frontend does not need to know whether the data came from Demo Mode, PX4 SITL, a real flight controller, or Jetson/LTE.

`demo` currently produces virtual telemetry for UI demonstration. `sitl` is reserved for PX4 MAVLink UDP input. `real` is reserved for Jetson/LTE JSON input.

LTE does not replace MAVLink by itself. It can be a data delivery path, or it can carry Jetson-generated JSON telemetry into the backend. The backend should normalize whichever input path is used into `TelemetryState`.
