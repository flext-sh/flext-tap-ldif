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

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# TAP LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF operations
# =============================================================================


# Singer LDIF tap domain TypeVars
class FlextMeltanoTapLdifTypes(FlextTypes):
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

        type TapConfiguration = dict[str, str | int | bool | dict[str, object]]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue]
        ]
        type CatalogDefinition = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SchemaDefinition = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]
        type MessageOutput = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StateManagement = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # LDIF PROCESSING TYPES - Complex LDIF processing types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = dict[str, str | int | bool | dict[str, object]]
        type EntryExtraction = dict[
            str, str | list[str] | dict[str, FlextTypes.JsonValue]
        ]
        type EntryTransformation = list[dict[str, str | object]]
        type EntryValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type BatchProcessing = dict[str, int | bool | dict[str, object]]
        type FileProcessing = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DATA EXTRACTION TYPES - Complex data extraction types
    # =========================================================================

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[str, str | bool | dict[str, object]]
        type ExtractionFilter = dict[str, str | list[str] | dict[str, object]]
        type ExtractionMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ExtractionResult = dict[str, bool | list[dict[str, object]]]
        type ExtractionMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type ExtractionState = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[str, str | bool | int | dict[str, object]]
        type StreamMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamRecord = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type StreamState = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, object]]
        type StreamSchema = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]

    # =========================================================================
    # FILE HANDLING TYPES - Complex file operation types
    # =========================================================================

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = dict[str, str | int | bool | dict[str, object]]
        type FileValidation = dict[str, bool | str | int | list[str]]
        type FileProcessing = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type FileBatching = dict[str, int | bool | dict[str, object]]
        type FileMonitoring = dict[str, bool | int | dict[str, FlextTypes.JsonValue]]
        type FileMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[str, bool | str | int | dict[str, object]]
        type ErrorRecovery = dict[str, str | bool | dict[str, object]]
        type ErrorReporting = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type ErrorClassification = dict[str, str | int | dict[str, object]]
        type ErrorMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]

    # =========================================================================
    # SINGER TAP LDIF PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes):
        """Singer Tap LDIF-specific project types extending FlextTypes.

        Adds Singer tap LDIF-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        # Singer tap LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes
            "library",
            "application",
            "service",
            # Singer tap LDIF-specific types
            "singer-tap",
            "ldif-extractor",
            "data-extractor",
            "singer-tap-ldif",
            "tap-ldif",
            "ldif-connector",
            "data-connector",
            "singer-protocol",
            "ldif-processor",
            "file-extractor",
            "ldif-parser",
            "singer-stream",
            "etl-tap",
            "data-pipeline",
            "ldif-integration",
            "singer-integration",
        ]

        # Singer tap LDIF-specific project configurations
        type SingerTapLdifProjectConfig = dict[str, object]
        type LdifExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[str, bool | str | dict[str, object]]
        type TapLdifPipelineConfig = dict[str, object]


# =============================================================================
# PUBLIC API EXPORTS - Singer LDIF tap TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextMeltanoTapLdifTypes",
]
