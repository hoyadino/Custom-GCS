#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
BACKEND_DIR="${PROJECT_ROOT}/backend"

echo "Demo Mode uses generated telemetry only."
echo "Start the frontend in another terminal with: ./scripts/run_frontend.sh"

if [ ! -d "${BACKEND_DIR}/venv" ]; then
  echo "backend/venv not found. Run ./scripts/setup_backend_venv.sh first."
  exit 1
fi

cd "${BACKEND_DIR}"
source venv/bin/activate
python main.py
