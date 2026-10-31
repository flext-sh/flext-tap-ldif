# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Tap LDIF Utilities - LDIF tap extraction utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import u as flext_ldif_u
from flext_meltano import u as flext_meltano_u

from flext_tap_ldif._utilities import (
    FlextTapLdifUtilitiesBase,
    FlextTapLdifUtilitiesExtractSupport,
)


class FlextTapLdifUtilities(flext_meltano_u, flext_ldif_u):
    """LDIF tap extraction-specific utilities following flext-core patterns."""

    class TapLdif(FlextTapLdifUtilitiesExtractSupport, FlextTapLdifUtilitiesBase):
        """Tap LDIF utilities namespace."""


u = FlextTapLdifUtilities
__all__: list[str] = ["FlextTapLdifUtilities", "u"]
