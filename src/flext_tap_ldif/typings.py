"""FLEXT Tap LDIF Types - Domain-specific Singer LDIF tap type definitions.

This module provides Singer LDIF tap-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TypeVar

from flext_core import FlextTypes

# =============================================================================
# TAP LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF operations
# =============================================================================

# Singer LDIF tap domain TypeVars
TTapLdif = TypeVar("TTapLdif")
TLdifStream = TypeVar("TLdifStream")
TLdifCatalog = TypeVar("TLdifCatalog")
TLdifConfig = TypeVar("TLdifConfig")
TLdifProcessor = TypeVar("TLdifProcessor")
TLdifExtractor = TypeVar("TLdifExtractor")
TSingerMessage = TypeVar("TSingerMessage")
TSingerRecord = TypeVar("TSingerRecord")


class FlextTapLdifTypes(FlextTypes):
    """Singer LDIF tap-specific type definitions extending FlextTypes.

    Domain-specific type system for Singer LDIF tap operations.
    Contains ONLY complex LDIF tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TAP TYPES - Complex Singer protocol types
    # =========================================================================

    class SingerTap:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.JsonValue]
        ]
        type CatalogDefinition = dict[
            str, str | list[dict[str, FlextTypes.Core.JsonValue]]
        ]
        type SchemaDefinition = dict[
            str, str | dict[str, FlextTypes.Core.JsonValue] | bool
        ]
        type MessageOutput = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type StateManagement = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # LDIF PROCESSING TYPES - Complex LDIF processing types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type EntryExtraction = dict[
            str, str | list[str] | dict[str, FlextTypes.Core.JsonValue]
        ]
        type EntryTransformation = list[dict[str, str | object]]
        type EntryValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type BatchProcessing = dict[
            str, int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type FileProcessing = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # DATA EXTRACTION TYPES - Complex data extraction types
    # =========================================================================

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ExtractionFilter = dict[str, str | list[str] | dict[str, object]]
        type ExtractionMapping = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type ExtractionResult = dict[str, bool | list[dict[str, object]]]
        type ExtractionMetrics = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ExtractionState = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type StreamRecord = dict[str, FlextTypes.Core.JsonValue | dict[str, object]]
        type StreamState = dict[str, str | int | dict[str, FlextTypes.Core.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, object]]
        type StreamSchema = dict[str, str | dict[str, FlextTypes.Core.JsonValue] | bool]

    # =========================================================================
    # FILE HANDLING TYPES - Complex file operation types
    # =========================================================================

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type FileValidation = dict[str, bool | str | int | list[str]]
        type FileProcessing = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type FileBatching = dict[
            str, int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type FileMonitoring = dict[
            str, bool | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type FileMetrics = dict[str, int | float | dict[str, FlextTypes.Core.JsonValue]]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ErrorRecovery = dict[str, str | bool | dict[str, object]]
        type ErrorReporting = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ErrorClassification = dict[str, str | int | dict[str, object]]
        type ErrorMetrics = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextTypes.Core.JsonValue]]
        ]


# =============================================================================
# PUBLIC API EXPORTS - Singer LDIF tap TypeVars and types
# =============================================================================

__all__: list[str] = [
    # LDIF Tap Types class
    "FlextTapLdifTypes",
    # Singer LDIF tap-specific TypeVars
    "TLdifCatalog",
    "TLdifConfig",
    "TLdifExtractor",
    "TLdifProcessor",
    "TLdifStream",
    "TSingerMessage",
    "TSingerRecord",
    "TTapLdif",
]
