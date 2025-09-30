"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_ldif.constants import FlextLdifConstants

from flext_core import FlextConstants


class FlextTapLdifConstants(FlextConstants):
    """LDIF tap extraction-specific constants following flext-core patterns.

    Composes with FlextTapLdifConstants to avoid duplication and ensure consistency.
    """

    # Import LDIF-specific constants from flext-ldif (composition pattern)
    from flext_ldif.constants import FlextTapLdifConstants

    # LDIF File Configuration using composition
    DEFAULT_LDIF_ENCODING = FlextLdifConstants.Encoding.DEFAULT_ENCODING
    SUPPORTED_ENCODINGS: ClassVar[list[str]] = list(
        FlextLdifConstants.Encoding.SUPPORTED_ENCODINGS
    )

    # Singer Tap Configuration - using FlextConstants composition
    DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
    MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS
    MAX_FILE_SIZE_MB = 100

    # LDIF Change Types from FlextTapLdifConstants
    LDIF_CHANGE_TYPES: ClassVar[list[str]] = [
        FlextLdifConstants.EntryModification.ADD,
        FlextLdifConstants.EntryModification.MODIFY,
        FlextLdifConstants.EntryModification.DELETE,
        FlextLdifConstants.EntryModification.MODRDN,
    ]

    class Processing:
        """LDIF processing configuration."""

        MIN_WORKERS_FOR_PARALLEL = (
            FlextLdifConstants.Processing.MIN_WORKERS_FOR_PARALLEL
        )
        MAX_WORKERS_LIMIT = FlextLdifConstants.Processing.MAX_WORKERS_LIMIT
        PERFORMANCE_MIN_CHUNK_SIZE = (
            FlextLdifConstants.Processing.PERFORMANCE_MIN_CHUNK_SIZE
        )
        MIN_PRODUCTION_ENTRIES = FlextLdifConstants.Processing.MIN_PRODUCTION_ENTRIES

    class Format:
        """LDIF format specifications."""

        DN_ATTRIBUTE = FlextLdifConstants.Format.DN_ATTRIBUTE
        ATTRIBUTE_SEPARATOR = FlextLdifConstants.Format.ATTRIBUTE_SEPARATOR
        MAX_LINE_LENGTH = FlextLdifConstants.Format.MAX_LINE_LENGTH
        BASE64_PREFIX = FlextLdifConstants.Format.BASE64_PREFIX
        COMMENT_PREFIX = FlextLdifConstants.Format.COMMENT_PREFIX

    class Validation:
        """LDIF validation constants."""

        MIN_DN_COMPONENTS = FlextLdifConstants.LdifValidation.MIN_DN_COMPONENTS
        MAX_DN_LENGTH = FlextLdifConstants.LdifValidation.MAX_DN_LENGTH
        MAX_ATTRIBUTES_PER_ENTRY = (
            FlextLdifConstants.LdifValidation.MAX_ATTRIBUTES_PER_ENTRY
        )


__all__ = ["FlextTapLdifConstants"]
