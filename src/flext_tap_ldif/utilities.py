# AUTO-GENERATED FILE — Regenerate with: make gen
"""Singer tap utilities for LDIF domain operations.

Composes the tap's ``_utilities`` helpers with the flext-meltano and
flext-ldif utility facades; consumers reach every helper via ``u.TapLdif.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_tap_ldif._utilities import (
    FlextTapLdifUtilitiesBase,
    FlextTapLdifUtilitiesEntriesStream,
    FlextTapLdifUtilitiesProcessor,
)


class FlextTapLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Single unified utilities class for Singer tap LDIF operations."""

    class TapLdif(
        FlextTapLdifUtilitiesBase,
        FlextTapLdifUtilitiesEntriesStream,
        FlextTapLdifUtilitiesProcessor,
    ):
        """Utility functions for LDIF data processing."""


u = FlextTapLdifUtilities
__all__: list[str] = ["FlextTapLdifUtilities", "u"]
