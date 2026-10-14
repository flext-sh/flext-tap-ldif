"""Singer tap utilities for LDIF domain operations.

Composes the tap's ``_utilities`` helpers with the flext-meltano and
flext-ldif utility facades; consumers reach every helper via ``u.TapLdif.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_tap_ldif._utilities.base import FlextTapLdifUtilitiesBase
from flext_tap_ldif._utilities.entries_stream import FlextTapLdifUtilitiesEntriesStream
from flext_tap_ldif._utilities.processor import FlextTapLdifUtilitiesProcessor


class FlextTapLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Single unified utilities class for Singer tap LDIF operations."""

    class TapLdif(
        FlextTapLdifUtilitiesBase,
        FlextTapLdifUtilitiesProcessor,
        FlextTapLdifUtilitiesEntriesStream,
    ):
        """Utility functions for LDIF data processing."""


u = FlextTapLdifUtilities

__all__: list[str] = ["FlextTapLdifUtilities", "u"]
