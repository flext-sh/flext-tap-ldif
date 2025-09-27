"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextTapLdifConstants(FlextConstants):
    """LDIF tap extraction-specific constants following flext-core patterns."""

    # LDIF File Configuration
    DEFAULT_LDIF_ENCODING = "utf-8"
    SUPPORTED_ENCODINGS: ClassVar[list[str]] = ["utf-8", "utf-16", "latin-1"]

    # Singer Tap Configuration - using FlextConstants composition
    DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
    MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS
    MAX_FILE_SIZE_MB = 100

    # LDIF Change Types
    LDIF_CHANGE_TYPES: ClassVar[list[str]] = ["add", "modify", "delete", "moddn"]


__all__ = ["FlextTapLdifConstants"]
