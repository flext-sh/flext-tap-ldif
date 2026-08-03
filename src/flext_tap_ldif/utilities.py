"""Singer tap utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import u
from flext_tap_ldif._utilities.data_processing import (
    FlextTapLdifUtilitiesLdifDataProcessing,
)
from flext_tap_ldif._utilities.entries_stream import FlextTapLdifUtilitiesEntriesStream
from flext_tap_ldif._utilities.processor import FlextTapLdifUtilitiesProcessor
from flext_tap_ldif._utilities.state_management import (
    FlextTapLdifUtilitiesStateManagement,
)


class FlextTapLdifUtilities(u, FlextLdifUtilities):
    """Single unified utilities class for Singer tap LDIF operations."""

    class TapLdif(
        FlextTapLdifUtilitiesLdifDataProcessing,
        FlextTapLdifUtilitiesStateManagement,
        FlextTapLdifUtilitiesProcessor,
        FlextTapLdifUtilitiesEntriesStream,
    ):
        """Utility functions for LDIF data processing."""


u = FlextTapLdifUtilities

__all__: list[str] = ["FlextTapLdifUtilities", "u"]
