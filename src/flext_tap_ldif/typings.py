"""Typing definitions for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes


class FlextTapLdifTypes(FlextTypes):
    """Type definitions for flext-tap-ldif extending FlextTypes."""

    # Tap-specific type aliases
    LDIFEntry = dict[str, list[str]]
    LDIFEntries = list[LDIFEntry]
    LDIFData = dict[str, object]
