"""Behavior contract for FlextTapLdif — public API only.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_tests import tm

from flext_tap_ldif import FlextTapLdif


class TestsFlextTapLdifTap:
    """Public-contract behavior for FlextTapLdif."""

    @staticmethod
    @pytest.fixture
    def ldif_file(tmp_path: Path) -> str:
        """Return the path of an empty ``.ldif`` file usable as tap config."""
        target = tmp_path / "sample.ldif"
        target.write_text("", encoding="utf-8")
        return str(target)

    @staticmethod
    def test_tap_advertises_canonical_singer_name(ldif_file: str) -> None:
        """Test tap advertises canonical singer name."""
        tap = FlextTapLdif(config={"file_path": ldif_file})
        tm.that(tap.name, eq="tap-ldif")

    @staticmethod
    def test_discover_streams_returns_single_ldif_entries_stream(
        ldif_file: str,
    ) -> None:
        """Test discover streams returns single ldif entries stream."""
        tap = FlextTapLdif(config={"file_path": ldif_file})

        streams = tap.discover_streams()

        names = [stream.name for stream in streams]
        tm.that(names, eq=["ldif_entries"])

    @staticmethod
    def test_discover_streams_is_idempotent_across_calls(ldif_file: str) -> None:
        """Test discover streams is idempotent across calls."""
        tap = FlextTapLdif(config={"file_path": ldif_file})

        first = [stream.name for stream in tap.discover_streams()]
        second = [stream.name for stream in tap.discover_streams()]

        tm.that(first, eq=second)
        tm.that(first, eq=["ldif_entries"])

    @staticmethod
    def test_entries_stream_schema_is_object_type(ldif_file: str) -> None:
        """Test entries stream schema is object type."""
        tap = FlextTapLdif(config={"file_path": ldif_file})

        schema = tap.discover_streams()[0].schema

        tm.that(schema, kv={"type": "object"})

    @staticmethod
    @pytest.mark.parametrize(
        "field_name",
        [
            "dn",
            "attributes",
            "object_class",
            "change_type",
            "source_file",
            "line_number",
            "entry_size",
        ],
    )
    def test_entries_stream_schema_declares_entry_field(
        ldif_file: str, field_name: str,
    ) -> None:
        """Test entries stream schema declares entry field."""
        tap = FlextTapLdif(config={"file_path": ldif_file})

        properties = tap.discover_streams()[0].schema["properties"]

        tm.that(properties, has=field_name)

    @staticmethod
    @pytest.mark.parametrize(
        "config_field",
        [
            "file_path",
            "directory_path",
            "file_pattern",
            "encoding",
            "strict_parsing",
            "max_file_size_mb",
        ],
    )
    def test_config_jsonschema_publishes_supported_option(
        config_field: str,
    ) -> None:
        """Test config jsonschema publishes supported option."""
        properties = FlextTapLdif.config_jsonschema["properties"]

        tm.that(properties, has=config_field)
