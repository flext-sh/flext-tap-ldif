"""Tap LDIF extract-support helpers — stream rules, tap spec, file discovery.

All the tap's non-trivial logic lives here as a ``_utilities`` mixin composed
into the ``u`` facade; ``services/*`` stay thin orchestrators. Business rules are
read from ``config.tap_ldif`` and packed into flext-meltano transport models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from flext_meltano import u

from flext_tap_ldif import c, config, m, p, r, settings, t


class FlextTapLdifUtilitiesExtractSupport:
    """Extract helpers consumed by the tap services and CLI facade."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

    @staticmethod
    def tap_spec() -> m.Meltano.TapSpec:
        """Build the Singer tap spec: config streams + settings config schema.

        Returns:
            The resulting ``m.Meltano.TapSpec``.

        """
        streams = tuple(
            m.Meltano.StreamSpec(
                name=rule.name,
                json_schema=rule.stream_schema,
                primary_keys=tuple(rule.primary_keys),
            )
            for rule in config.tap_ldif.streams
        )
        return m.Meltano.TapSpec(
            tap_name=c.TapLdif.TAP_NAME,
            config_jsonschema=type(settings).model_json_schema(),
            streams=streams,
        )

    @staticmethod
    def _resolve_single_file(
        path_str: str,
        max_bytes: int,
    ) -> p.Result[t.SequenceOf[Path]]:
        path = Path(path_str)
        if not path.exists():
            return r[t.SequenceOf[Path]].fail(f"File not found: {path}")
        if path.stat().st_size > max_bytes:
            return r[t.SequenceOf[Path]].fail(f"File exceeds max size: {path}")
        return r[t.SequenceOf[Path]].ok((path,))

    @staticmethod
    def _resolve_dir_files(
        dir_str: str,
        pattern: str,
        max_bytes: int,
    ) -> p.Result[t.SequenceOf[Path]]:
        dir_path = Path(dir_str)
        if not dir_path.is_dir():
            return r[t.SequenceOf[Path]].fail(f"Directory not found: {dir_path}")
        matched = tuple(
            f
            for f in sorted(dir_path.glob(pattern))
            if f.is_file() and f.stat().st_size <= max_bytes
        )
        if not matched:
            return r[t.SequenceOf[Path]].fail("No LDIF files discovered")
        return r[t.SequenceOf[Path]].ok(matched)

    @staticmethod
    def resolve_files(source: t.JsonMapping) -> p.Result[t.SequenceOf[Path]]:
        """Discover LDIF files from the tap runtime config mapping.

        Args:
            source: Tap runtime config mapping.

        Returns:
            The resulting ``p.Result[t.SequenceOf[Path]]``.

        """
        file_path_raw = source.get("file_path")
        dir_path_raw = source.get("directory_path")
        pattern_raw = source.get("file_pattern", "*.ldif")
        pattern = pattern_raw if isinstance(pattern_raw, str) else "*.ldif"
        max_size_mb = source.get("max_file_size_mb", c.TapLdif.MAX_FILE_SIZE_MB)
        max_bytes = (
            (
                max_size_mb
                if isinstance(max_size_mb, int)
                else c.TapLdif.MAX_FILE_SIZE_MB
            )
            * 1024
            * 1024
        )

        if isinstance(file_path_raw, str) and file_path_raw:
            return FlextTapLdifUtilitiesExtractSupport._resolve_single_file(
                file_path_raw,
                max_bytes,
            )

        if isinstance(dir_path_raw, str) and dir_path_raw:
            return FlextTapLdifUtilitiesExtractSupport._resolve_dir_files(
                dir_path_raw,
                pattern,
                max_bytes,
            )

        return r[t.SequenceOf[Path]].fail("No file_path or directory_path specified")

    @staticmethod
    def pack_entry(
        entry: p.Ldif.Entry,
        file_path: Path,
    ) -> t.JsonMapping:
        """Pack one flext-ldif entry into a Singer-native JSON record.

        Args:
            entry: flext-ldif entry to convert.
            file_path: Source LDIF file path.

        Returns:
            The resulting ``t.JsonMapping``.

        """
        dn_val = entry.dn.value if entry.dn is not None else ""
        attrs_dict: t.JsonMapping = u.Cli.JSON_MAPPING_ADAPTER.validate_python(
            {k: list(v) for k, v in entry.attributes.attributes.items()}
            if entry.attributes is not None
            else {},
        )
        return u.Cli.JSON_MAPPING_ADAPTER.validate_python({
            c.TapLdif.EntrySchema.DN_FIELD: dn_val,
            c.TapLdif.EntrySchema.ATTRIBUTES_FIELD: attrs_dict,
            c.TapLdif.EntrySchema.OBJECT_CLASS_FIELD: attrs_dict.get(
                "objectClass",
                [],
            ),
            c.TapLdif.EntrySchema.CHANGE_TYPE_FIELD: (
                c.TapLdif.EntrySchema.DEFAULT_CHANGE_TYPE
            ),
            c.TapLdif.EntrySchema.SOURCE_FILE_FIELD: str(file_path),
            c.TapLdif.EntrySchema.LINE_NUMBER_FIELD: (
                c.TapLdif.EntrySchema.DEFAULT_LINE_NUMBER
            ),
            c.TapLdif.EntrySchema.ENTRY_SIZE_FIELD: len(
                str(entry).encode(c.DEFAULT_ENCODING),
            ),
        })


__all__: list[str] = ["FlextTapLdifUtilitiesExtractSupport"]
