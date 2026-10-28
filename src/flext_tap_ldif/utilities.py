# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Tap LDIF Utilities - LDIF tap extraction utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_tap_ldif._utilities.base import FlextTapLdifUtilitiesBase
from flext_tap_ldif._utilities.extract_support import (
    FlextTapLdifUtilitiesExtractSupport,
)


class FlextTapLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """LDIF tap extraction-specific utilities following flext-core patterns."""

    class TapLdif(FlextTapLdifUtilitiesExtractSupport, FlextTapLdifUtilitiesBase):
        """Tap LDIF utilities namespace."""


u = FlextTapLdifUtilities
__all__: list[str] = ["FlextTapLdifUtilities", "u"]
