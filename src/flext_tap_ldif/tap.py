"""Singer LDIF tap implementation using FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar, override

from flext_tap_ldif import FlextTapLdifSettings, c, m, t


class FlextTapLdif(m.Meltano.SingerTapBase):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = FlextTapLdifSettings
    config_jsonschema: ClassVar[t.JsonDict] = {
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
        from flext_tap_ldif import FlextTapLdifUtilities

        return [FlextTapLdifUtilities.TapLdif.EntriesStream(tap=self)]


__all__: list[str] = ["FlextTapLdif"]
