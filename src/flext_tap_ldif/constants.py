"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
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

        # === Regex authority for the TapLdif domain ===
        ATTRIBUTE_NORMALIZE_RE: ClassVar[re.Pattern[str]] = re.compile(
            r"[^a-zA-Z0-9]"
        )

        DEFAULT_LDIF_ENCODING: Final[str] = FlextLdifConstants.Ldif.Encoding.UTF8
        DEFAULT_FILE_PATTERN: Final[str] = "*.ldif"
        DEFAULT_STRICT_PARSING: Final[bool] = True
        MAX_FILE_SIZE_MB: Final[int] = 100

        @unique
        class LdifChangeType(StrEnum):
            """Supported LDIF changetype tokens for tap processing."""

            ADD = "add"
            MODIFY = "modify"
            DELETE = "delete"
            MODRDN = "modrdn"

        class Format:
            """LDIF format specifications."""

            MAX_LINE_LENGTH: Final[int] = FlextLdifConstants.Ldif.DEFAULT_LINE_WIDTH
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


c = FlextTapLdifConstants
__all__: tuple[str, ...] = ("FlextTapLdifConstants", "c")
