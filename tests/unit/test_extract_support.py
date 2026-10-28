"""Behavioral tests for the tap-ldif extract-support helpers.

Expected values are read from the ``config.tap_ldif`` business-rule SSOT, so the
tests stay valid for any configured stream set.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_tap_ldif import config
from tests import c, tm, u


class TestsFlextTapLdifExtractSupport:
    """Public-contract behavior for ``u.TapLdif`` extract helpers."""

    @staticmethod
    def test_tap_spec_declares_every_configured_stream() -> None:
        """The tap spec mirrors the configured stream rules and tap name."""
        spec = u.TapLdif.tap_spec()

        tm.that(spec.tap_name, eq=c.TapLdif.TAP_NAME)
        tm.that(
            [stream.name for stream in spec.streams],
            eq=[rule.name for rule in config.tap_ldif.streams],
        )
        tm.that(
            [list(stream.primary_keys) for stream in spec.streams],
            eq=[list(rule.primary_keys) for rule in config.tap_ldif.streams],
        )

    @staticmethod
    def test_resolve_files_with_valid_file(tmp_path: Path) -> None:
        """A valid file path resolves into a singleton tuple."""
        sample = tmp_path / "sample.ldif"
        sample.write_text("dn: cn=test\n\n", encoding="utf-8")

        result = u.TapLdif.resolve_files({"file_path": str(sample)})
        files = tm.ok(result)
        tm.that(len(files), eq=1)
        tm.that(files[0], eq=sample)

    @staticmethod
    def test_resolve_files_fails_when_file_not_found(tmp_path: Path) -> None:
        """A nonexistent file path returns a typed failure."""
        missing = tmp_path / "nonexistent.ldif"
        result = u.TapLdif.resolve_files({"file_path": str(missing)})
        tm.fail(result)

    @staticmethod
    def test_resolve_files_fails_without_source() -> None:
        """An empty source mapping returns a typed failure, never an exception."""
        result = u.TapLdif.resolve_files({})
        tm.fail(result)


__all__: list[str] = ["TestsFlextTapLdifExtractSupport"]
