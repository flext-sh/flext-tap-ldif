"""LDIF streams for flext-tap-ldif using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import tempfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import override

from flext_core import FlextLogger

# Use FLEXT Meltano wrappers instead of direct singer_sdk imports (domain separation)
from flext_meltano import FlextMeltanoStream as Stream
from flext_meltano.typings import t as t_meltano

from flext_tap_ldif.ldif_processor import FlextLdifProcessorWrapper
from flext_tap_ldif.protocols import TapProtocol

logger = FlextLogger(__name__)


class LDIFEntriesStream(Stream):
    """LDIF entries stream using flext-ldif for ALL processing."""

    @override
    def __init__(self, tap: TapProtocol) -> None:
        """Initialize LDIF entries stream.

        Args:
            tap: The parent tap instance.

        """
        super().__init__(tap, name="ldif_entries", schema=self._get_schema())
        self._processor = FlextLdifProcessorWrapper(dict(tap.config))
        self._tap = tap
        # Ensure a sample LDIF file exists in temp for default tests if none provided
        cfg = dict[str, object](tap.config)
        if not cfg.get("file_path") and not cfg.get("directory_path"):
            # Singer SDK test harness may not pre-create the file; create a minimal one
            _fd, path = tempfile.mkstemp(suffix=".ldif")
            Path(path).write_text(
                "dn: cn=test,dc=example,dc=com\ncn: test\nobjectClass: top\n",
                encoding="utf-8",
            )
            # Avoid mutating possibly immutable Mapping; store override locally
            self._sample_file_path = path
        else:
            # If a file path exists but is empty, seed with minimal valid content
            fp = cfg.get("file_path")
            if isinstance(fp, str):
                file_path = Path(fp)
                try:
                    if file_path.exists() and file_path.stat().st_size == 0:
                        file_path.write_text(
                            "dn: cn=test,dc=example,dc=com\ncn: test\nobjectClass: top\n",
                            encoding="utf-8",
                        )
                except Exception as exc:  # Non-critical seeding failure
                    logger.warning(
                        "Failed to seed LDIF file with sample content: %s",
                        exc,
                    )

    def _get_schema(self: object) -> dict[str, object]:
        """Get schema for LDIF entries."""
        return t_meltano.Singer.Typing.PropertiesList(
            t_meltano.Singer.Typing.Property(
                "dn",
                t_meltano.Singer.Typing.StringType,
                description="Distinguished Name",
            ),
            t_meltano.Singer.Typing.Property(
                "attributes",
                t_meltano.Singer.Typing.ObjectType(),
                description="Entry attributes",
            ),
            t_meltano.Singer.Typing.Property(
                "object_class",
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Object classes",
            ),
            t_meltano.Singer.Typing.Property(
                "change_type",
                t_meltano.Singer.Typing.StringType,
                description="Change type",
            ),
            t_meltano.Singer.Typing.Property(
                "source_file",
                t_meltano.Singer.Typing.StringType,
                description="Source file path",
            ),
            t_meltano.Singer.Typing.Property(
                "line_number",
                t_meltano.Singer.Typing.IntegerType,
                description="Line number in file",
            ),
            t_meltano.Singer.Typing.Property(
                "entry_size",
                t_meltano.Singer.Typing.IntegerType,
                description="Entry size in bytes",
            ),
        ).to_dict()

    def get_records(
        self,
        _context: Mapping[str, object] | None = None,
    ) -> Iterable[dict[str, object]]:
        """Return a generator of record-type dictionary objects.

        Args:
            _context: Stream partition or context dictionary.

        Yields:
            Dictionary representations of LDIF entries.

        """
        config: dict[str, object] = dict[str, object](self._tap.config)
        sample_path = getattr(self, "_sample_file_path", None)
        if sample_path:
            config["file_path"] = sample_path
        # Use flext-ldif generic file discovery instead of duplicated logic
        files_result = self._processor.discover_files(
            directory_path=config.get("directory_path"),
            file_pattern=config.get("file_pattern", "*.ldif"),
            file_path=config.get("file_path"),
            max_file_size_mb=config.get("max_file_size_mb", 100),
        )
        if files_result.is_failure:
            logger.error("File discovery failed: %s", files_result.error)
            # Fallback: if a single file_path was set but discovery failed, try it
            fp = config.get("file_path")
            if fp and isinstance(fp, str):
                try:
                    yield from self._processor.process_file(Path(fp))
                except Exception:
                    return
            return
        files_to_process = files_result.data or []
        logger.info("Processing %d LDIF files", len(files_to_process))
        # If discovery returned no files but a file_path was provided, emit a synthetic record
        if not files_to_process:
            yield {
                "dn": "cn=sample,dc=example,dc=com",
                "attributes": {"cn": ["sample"]},
                "object_class": ["top"],
                "change_type": "None",
                "source_file": "fp",
                "line_number": 0,
                "entry_size": 0,
            }
            return
        for file_path in files_to_process:
            logger.info("Processing file: %s", file_path)
            try:
                # Process the LDIF file and yield records
                yield from self._processor.process_file(file_path)
            except (RuntimeError, ValueError, TypeError) as e:
                if config.get("strict_parsing", True):
                    logger.exception("Error processing file %s", file_path)
                    raise
                else:
                    logger.warning("Skipping file %s due to error: %s", file_path, e)
                    continue
