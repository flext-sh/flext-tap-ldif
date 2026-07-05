"""Behavior contract for FlextTapLdif — public API only."""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_tests import tm

from flext_tap_ldif import FlextTapLdif

__all__: list[str] = ["TestsFlextTapLdifTap"]


class TestsFlextTapLdifTap:
    """Public-contract behavior for FlextTapLdif."""

    @pytest.fixture
    def ldif_file(self, tmp_path: Path) -> str:
        """Return the path of an empty ``.ldif`` file usable as tap config."""
        target = tmp_path / "sample.ldif"
        target.write_text("", encoding="utf-8")
        return str(target)

    def test_tap_advertises_canonical_singer_name(self, ldif_file: str) -> None:
        tap = FlextTapLdif(config={"file_path": ldif_file})
        tm.that(tap.name, eq="tap-ldif")

    def test_discover_streams_returns_single_ldif_entries_stream(
        self,
        ldif_file: str,
    ) -> None:
        tap = FlextTapLdif(config={"file_path": ldif_file})

        streams = tap.discover_streams()

        tm.that(streams, len=1)
        tm.that(streams[0].name, eq="ldif_entries")

    def test_discover_streams_is_idempotent_across_calls(
        self,
        ldif_file: str,
    ) -> None:
        tap = FlextTapLdif(config={"file_path": ldif_file})

        first = [stream.name for stream in tap.discover_streams()]
        second = [stream.name for stream in tap.discover_streams()]

        tm.that(first, eq=second)
        tm.that(first, eq=["ldif_entries"])

    def test_entries_stream_schema_is_object_type(self, ldif_file: str) -> None:
        tap = FlextTapLdif(config={"file_path": ldif_file})

        schema = tap.discover_streams()[0].schema

        tm.that(schema, kv={"type": "object"})

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
        self,
        ldif_file: str,
        field_name: str,
    ) -> None:
        tap = FlextTapLdif(config={"file_path": ldif_file})

        properties = tap.discover_streams()[0].schema["properties"]

        tm.that(properties, has=field_name)

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
        self,
        config_field: str,
    ) -> None:
        properties = FlextTapLdif.config_jsonschema["properties"]

        tm.that(properties, has=config_field)
