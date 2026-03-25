"""Singer LDIF tap implementation using FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import ClassVar, override

from flext_core import FlextConstants, FlextLogger
from singer_sdk.streams import Stream
from singer_sdk.tap_base import Tap

from flext_tap_ldif import t
from flext_tap_ldif.settings import FlextTapLdifSettings
from flext_tap_ldif.streams import FlextTapLdifEntriesStream

logger = FlextLogger(__name__)


class FlextTapLdif(Tap):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = FlextTapLdifSettings
    config_jsonschema: ClassVar[dict[str, t.ContainerValue]] = {
        "type": "object",
        "properties": {
            "file_path": {"type": "string"},
            "directory_path": {"type": "string"},
            "file_pattern": {"type": "string", "default": "*.ldif"},
            "encoding": {"type": "string", "default": "utf-8"},
            "base_dn_filter": {"type": "string"},
            "object_class_filter": {"type": "array", "items": {"type": "string"}},
            "attribute_filter": {"type": "array", "items": {"type": "string"}},
            "exclude_attributes": {"type": "array", "items": {"type": "string"}},
            "include_operational_attributes": {"type": "boolean", "default": False},
            "strict_parsing": {"type": "boolean", "default": True},
            "max_file_size_mb": {
                "type": "integer",
                "default": FlextConstants.MAX_FILE_SIZE // (1024 * 1024),
            },
        },
    }

    @override
    def discover_streams(self) -> Sequence[Stream]:
        """Return a list of discovered streams.

        Returns:
        A list of discovered streams.

        """
        return [FlextTapLdifEntriesStream(tap=self)]

    def _get_ldif_entries_schema(self) -> Mapping[str, t.ContainerValue]:
        """Get the schema for LDIF entries stream.

        Returns:
        Schema definition for LDIF entries.

        """
        return {
            "type": "object",
            "properties": {
                "dn": {"type": "string"},
                "object_class": {"type": "array", "items": {"type": "string"}},
                "attributes": {"type": "object"},
                "change_type": {"type": "string"},
                "source_file": {"type": "string"},
                "line_number": {"type": "integer"},
                "entry_size": {"type": "integer"},
            },
        }


def main() -> None:
    """Run the tap entry point."""
    FlextTapLdif().cli()


if __name__ == "__main__":
    main()
