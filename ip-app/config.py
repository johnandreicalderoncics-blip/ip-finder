"""API key configuration for the IP address app.

The ipify key is OPTIONAL: the free ipify endpoints work without any
key, and providing one only raises the rate limits. It is resolved in
this order:
  1. IPIFY_KEY environment variable
  2. config.ini file next to this script ([ipify] key = ...)

If a key is configured it must never be committed to GitHub: config.ini
is listed in .gitignore. Copy config.sample.ini to config.ini to add one.

Free key (optional): https://www.ipify.org/  (dashboard sign-up)
"""

import configparser
import os
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent / "config.ini"


def get_api_key() -> str:
    """Return the optional ipify API key ('' when not configured)."""
    # 1) Environment variable wins (handy for CI and quick testing).
    key = os.environ.get("IPIFY_KEY", "").strip()
    if key:
        return key

    # 2) Fall back to config.ini (git-ignored so the key stays private).
    parser = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        parser.read(CONFIG_FILE, encoding="utf-8")
        key = parser.get("ipify", "key", fallback="").strip()
        if key and key.upper() != "YOUR_KEY_HERE":
            return key

    # No key found - that is fine for this app, so return empty and
    # let the caller decide how to proceed (no exit here).
    return ""
