#!/usr/bin/env python3

from pathlib import Path

def get_root_dir() -> Path:
    return Path.cwd()

def get_secrets_path() -> Path:
    return get_root_dir() / "secrets.json"
