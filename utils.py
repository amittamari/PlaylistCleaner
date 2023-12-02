#!/usr/bin/env python3

from pathlib import Path

def root_dir() -> Path:
    return Path.cwd()

def secrets_path() -> Path:
    return root_dir() / "secrets.json"
