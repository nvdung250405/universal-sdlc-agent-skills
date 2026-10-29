#!/usr/bin/env python3
"""Backward-compatible alias for the full pack linter."""
from __future__ import annotations
import os
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("lint_pack.py")
os.execv(sys.executable, [sys.executable, str(SCRIPT), *sys.argv[1:]])
