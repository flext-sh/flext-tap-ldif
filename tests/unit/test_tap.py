"""Behavior contract for FlextTapLdif — public API only.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_tests import tm

from flext_tap_ldif import FlextTapLdif
from tests import u


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
        ldif_file: str,
        field_name: str,
    ) -> None:
        """Test entries stream schema declares entry field."""
        tap = FlextTapLdif(config={"file_path": ldif_file})

        properties = tap.discover_streams()[0].schema["properties"]

        tm.that(properties, has=field_name)

    @staticmethod
    def test_processor_yields_records_parsed_by_flext_ldif(tmp_path: Path) -> None:
        """Entries in an LDIF file surface as Singer records keyed by DN."""
        dn = "uid=jdoe,ou=people,dc=example,dc=com"
        source = tmp_path / "people.ldif"
        source.write_text(
            f"dn: {dn}\nobjectClass: inetOrgPerson\nuid: jdoe\ncn: John Doe\nsn: Doe\n",
            encoding="utf-8",
        )

        records = list(u.TapLdif.Processor({}).process_file(source))

        tm.that([record["dn"] for record in records], eq=[dn])
        tm.that([record["source_file"] for record in records], eq=[str(source)])

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
