#!/usr/bin/env bash
set -euo pipefail
# Run `uv` with the system `python3` interpreter so it uses the same
# site-packages as `python3` / `uvicorn` in this environment.
uv run --active --no-sync --python python3 fastapi dev app/main.py "$@"
