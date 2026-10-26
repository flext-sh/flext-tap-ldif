# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import c
from flext_meltano import c as flext_meltano_c

from flext_tap_ldif._constants import (
    FlextTapLdifConstantsBase,
    FlextTapLdifConstantsValues,
)


class FlextTapLdifConstants(flext_meltano_c, c):
    """LDIF tap extraction-specific constants following flext-core patterns.

    Composes with the flext-meltano and flext-ldif constant facades to avoid
    duplication and ensure consistency.
    """

    class TapLdif(
        FlextTapLdifConstantsBase,
        FlextTapLdifConstantsValues,
    ):
        """LDIF tap processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """


c = FlextTapLdifConstants
__all__: list[str] = ["FlextTapLdifConstants", "c"]
