"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from enum import StrEnum, unique
from typing import TYPE_CHECKING, ClassVar

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from flext_tap_ldif._constants.values import FlextTapLdifConstantsValues

if TYPE_CHECKING:
    from flext_tap_ldif import t


class FlextTapLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF tap extraction-specific constants following flext-core patterns.

    Composes with FlextTapLdifConstants to avoid duplication and ensure consistency.
    """

    class TapLdif(FlextTapLdifConstantsValues.TapLdif):
        """LDIF tap processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        # === Regex authority for the TapLdif domain ===
        ATTRIBUTE_NORMALIZE_RE: ClassVar[t.RegexPattern] = re.compile(r"[^a-zA-Z0-9]")

        @unique
        class ChangeType(StrEnum):
            """Supported LDIF changetype tokens for tap processing."""

            ADD = "add"
            MODIFY = "modify"
            DELETE = "delete"
            MODRDN = "modrdn"

        class Format(FlextTapLdifConstantsValues.TapLdif.Format):
            """LDIF format specifications."""

        class TapLdifPerformance(
            FlextTapLdifConstantsValues.TapLdif.TapLdifPerformance,
        ):
            """Tap LDIF performance constants."""

        class EntrySchema(FlextTapLdifConstantsValues.TapLdif.EntrySchema):
            """LDIF entry schema field names."""


c = FlextTapLdifConstants
__all__: t.StrSequence = ("FlextTapLdifConstants", "c")
