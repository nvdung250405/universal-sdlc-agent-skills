#!/usr/bin/env bash
# Cross-platform implementation lives in Python; this wrapper is for POSIX shells.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/install.py" "$@"
