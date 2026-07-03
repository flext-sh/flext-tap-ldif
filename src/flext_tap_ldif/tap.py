"""Singer LDIF tap implementation using FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar, override

from flext_tap_ldif import FlextTapLdifSettings, c, m, t, u
from flext_tap_ldif.utilities import FlextTapLdifUtilities

logger = u.fetch_logger(__name__)


class FlextTapLdif(m.Meltano.SingerTapBase):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = FlextTapLdifSettings
    config_jsonschema: ClassVar[t.JsonMapping] = {
        "type": "object",
        "properties": {
            "file_path": {"type": "string"},
            "directory_path": {"type": "string"},
            "file_pattern": {"type": "string", "default": "*.ldif"},
            "encoding": {"type": "string", "default": c.DEFAULT_ENCODING},
            "base_dn_filter": {"type": "string"},
            "object_class_filter": {"type": "array", "items": {"type": "string"}},
            "attribute_filter": {"type": "array", "items": {"type": "string"}},
            "exclude_attributes": {"type": "array", "items": {"type": "string"}},
            "include_operational_attributes": {"type": "boolean", "default": False},
            "strict_parsing": {"type": "boolean", "default": True},
            "max_file_size_mb": {
                "type": "integer",
                "default": c.MAX_FILE_SIZE // (1024 * 1024),
            },
        },
    }

    @override
    def discover_streams(self) -> t.SequenceOf[m.Meltano.SingerStreamBase]:
        """Return a list of discovered streams.

        Returns:
        A list of discovered streams.

        """
        return [FlextTapLdifUtilities.TapLdif.EntriesStream(tap=self)]

    def _get_ldif_entries_schema(self) -> t.JsonMapping:
        """Get the schema for LDIF entries stream.

        Returns:
        Schema definition for LDIF entries.

        """
        return t.Cli.JSON_MAPPING_ADAPTER.validate_python({
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
        })


if __name__ == "__main__":
    from flext_tap_ldif import main as _main

    raise SystemExit(_main())


__all__: list[str] = ["FlextTapLdif"]
