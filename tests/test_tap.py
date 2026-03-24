"""Tests for FlextTapLdif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import tempfile
from pathlib import Path

from flext_tap_ldif.tap import FlextTapLdif


def test_discover_streams() -> None:
    """Test stream discovery."""
    with tempfile.NamedTemporaryFile(suffix=".ldif", delete=False) as tmp_file:
        config = {"file_path": tmp_file.name}
        tap = FlextTapLdif(config=config)
        streams = tap.discover_streams()
        if len(streams) != 1:
            msg: str = f"Expected {1}, got {len(streams)}"
            raise AssertionError(msg)
        assert streams[0].name == "ldif_entries"
        Path(tmp_file.name).unlink(missing_ok=True)
