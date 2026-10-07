"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from flext_tap_ldif._constants import FlextTapLdifConstantsValues

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

        class EntrySchema(FlextTapLdifConstantsValues.TapLdif.EntrySchema):
            """LDIF entry schema field names."""


c = FlextTapLdifConstants
__all__: t.StrSequence = ("FlextTapLdifConstants", "c")
