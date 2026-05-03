"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import ClassVar, Final

from flext_ldif import FlextLdifConstants
from flext_meltano import c


class FlextTapLdifConstants(c, FlextLdifConstants):
    """LDIF tap extraction-specific constants following flext-core patterns.

    Composes with FlextTapLdifConstants to avoid duplication and ensure consistency.
    """

    class TapLdif:
        """LDIF tap processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        DEFAULT_LDIF_ENCODING: Final[str] = FlextLdifConstants.Ldif.Encoding.UTF8
        DEFAULT_FILE_PATTERN: Final[str] = "*.ldif"
        DEFAULT_STRICT_PARSING: Final[bool] = True
        SUPPORTED_ENCODINGS: ClassVar[frozenset[str]] = frozenset({
            FlextLdifConstants.Ldif.Encoding.UTF8,
            FlextLdifConstants.Ldif.Encoding.ASCII,
            FlextLdifConstants.Ldif.Encoding.LATIN1,
            FlextLdifConstants.Ldif.Encoding.UTF16,
        })
        MAX_FILE_SIZE_MB: Final[int] = 100

        @unique
        class LdifChangeType(StrEnum):
            """Supported LDIF changetype tokens for tap processing."""

            ADD = "add"
            MODIFY = "modify"
            DELETE = "delete"
            MODRDN = "modrdn"

        LDIF_CHANGE_TYPES: ClassVar[tuple[str, ...]] = tuple(
            member.value for member in LdifChangeType.__members__.values()
        )

        MIN_WORKERS_FOR_PARALLEL: Final[int] = 2
        MAX_WORKERS_LIMIT: Final[int] = 8
        PERFORMANCE_MIN_CHUNK_SIZE: Final[int] = 100
        MIN_ENTRIES: Final[int] = 1

        class Format:
            """LDIF format specifications."""

            DN_ATTRIBUTE: Final[str] = "dn"
            ATTRIBUTE_SEPARATOR: Final[str] = ": "
            MAX_LINE_LENGTH: Final[int] = FlextLdifConstants.Ldif.DEFAULT_LINE_WIDTH
            BASE64_PREFIX: Final[str] = ":: "
            COMMENT_PREFIX: Final[str] = "#"
            LINE_CONTINUATION: Final[str] = " "

        class TapLdifPerformance:
            """Tap LDIF performance constants."""

            DEFAULT_BATCH_SIZE: Final[int] = 1000

        class EntrySchema:
            """LDIF entry schema field names."""

            DN_FIELD: Final[str] = "dn"
            ATTRIBUTES_FIELD: Final[str] = "attributes"
            OBJECT_CLASS_FIELD: Final[str] = "object_class"
            CHANGE_TYPE_FIELD: Final[str] = "change_type"
            SOURCE_FILE_FIELD: Final[str] = "source_file"
            LINE_NUMBER_FIELD: Final[str] = "line_number"
            ENTRY_SIZE_FIELD: Final[str] = "entry_size"
            DEFAULT_CHANGE_TYPE: Final[str] = "None"
            DEFAULT_LINE_NUMBER: Final[int] = 0
            DEFAULT_ENTRY_SIZE: Final[int] = 0


c = FlextTapLdifConstants
__all__: tuple[str, ...] = ("FlextTapLdifConstants", "c")
