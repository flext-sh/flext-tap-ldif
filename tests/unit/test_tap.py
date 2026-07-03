"""Behavior contract for FlextTapLdif — public API only."""

from __future__ import annotations

import tempfile
from pathlib import Path

from flext_tests import tm

from flext_tap_ldif import FlextTapLdif


class TestsFlextTapLdifTap:
    """Behavior contract for FlextTapLdif.discover_streams."""

    def test_discover_streams_returns_ldif_entries_stream(self) -> None:
        with tempfile.NamedTemporaryFile(suffix=".ldif", delete=False) as tmp_file:
            tap = FlextTapLdif(config={"file_path": tmp_file.name})
            streams = tap.discover_streams()
            tm.that(len(streams), eq=1)
            tm.that(streams[0].name, eq="ldif_entries")
            Path(tmp_file.name).unlink(missing_ok=True)
