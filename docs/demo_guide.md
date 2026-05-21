# Demo Mode Guide

Demo Mode is for showing the UI during the next meeting or PPT without a real aircraft, PX4 SITL, or QGroundControl.

The telemetry shown in Demo Mode is generated virtual data. It is not real flight data.

## Run

1. Set up the backend virtual environment once:

   ```bash
   ./scripts/setup_backend_venv.sh
   ```

2. Run the backend:

   ```bash
   ./scripts/run_backend.sh
   ```

3. In another terminal, install frontend packages if needed and run Vite:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

The frontend connects to `ws://localhost:8000/ws/telemetry`.
