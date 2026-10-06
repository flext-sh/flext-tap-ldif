"""Singer tap utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_tap_ldif._utilities import (
    FlextTapLdifUtilitiesEntriesStream,
    FlextTapLdifUtilitiesProcessor,
)


class FlextTapLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Single unified utilities class for Singer tap LDIF operations."""

    class TapLdif(
        FlextTapLdifUtilitiesProcessor,
        FlextTapLdifUtilitiesEntriesStream,
    ):
        """Utility functions for LDIF data processing."""


u = FlextTapLdifUtilities

__all__: list[str] = ["FlextTapLdifUtilities", "u"]
