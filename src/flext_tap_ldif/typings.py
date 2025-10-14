"""FLEXT Tap LDIF Types - Domain-specific Singer LDIF tap type definitions.

This module provides Singer LDIF tap-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# TAP LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF operations
# =============================================================================


# Singer LDIF tap domain TypeVars
class FlextMeltanoTapLdifTypes(FlextCore.Types):
    """Singer LDIF tap-specific type definitions extending FlextCore.Types.

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
            str, str | int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type CatalogDefinition = dict[
            str, str | list[dict[str, FlextCore.Types.JsonValue]]
        ]
        type SchemaDefinition = dict[
            str, str | dict[str, FlextCore.Types.JsonValue] | bool
        ]
        type MessageOutput = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type StateManagement = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # LDIF PROCESSING TYPES - Complex LDIF processing types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = dict[
            str, str | int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type EntryExtraction = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type EntryTransformation = list[dict[str, str | object]]
        type EntryValidation = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type BatchProcessing = dict[
            str, int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type FileProcessing = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # DATA EXTRACTION TYPES - Complex data extraction types
    # =========================================================================

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type ExtractionFilter = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ExtractionMapping = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type ExtractionResult = dict[str, bool | list[FlextCore.Types.Dict]]
        type ExtractionMetrics = dict[
            str, int | float | dict[str, FlextCore.Types.JsonValue]
        ]
        type ExtractionState = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextCore.Types.ConfigValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type StreamRecord = dict[str, FlextCore.Types.JsonValue | FlextCore.Types.Dict]
        type StreamState = dict[str, str | int | dict[str, FlextCore.Types.JsonValue]]
        type StreamBookmark = dict[str, str | int | FlextCore.Types.Dict]
        type StreamSchema = dict[str, str | dict[str, FlextCore.Types.JsonValue] | bool]

    # =========================================================================
    # FILE HANDLING TYPES - Complex file operation types
    # =========================================================================

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = dict[
            str, str | int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type FileValidation = dict[str, bool | str | int | FlextCore.Types.StringList]
        type FileProcessing = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type FileBatching = dict[
            str, int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type FileMonitoring = dict[
            str, bool | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type FileMetrics = dict[str, int | float | dict[str, FlextCore.Types.JsonValue]]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextCore.Types.ConfigValue]
        ]
        type ErrorRecovery = dict[str, str | bool | FlextCore.Types.Dict]
        type ErrorReporting = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type ErrorClassification = dict[str, str | int | FlextCore.Types.Dict]
        type ErrorMetrics = dict[
            str, int | float | dict[str, FlextCore.Types.JsonValue]
        ]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextCore.Types.JsonValue]]
        ]

    # =========================================================================
    # SINGER TAP LDIF PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """Singer Tap LDIF-specific project types extending FlextCore.Types.Project.

        Adds Singer tap LDIF-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        # Singer tap LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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
        type SingerTapLdifProjectConfig = dict[
            str, FlextCore.Types.ConfigValue | object
        ]
        type LdifExtractorConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type SingerProtocolConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type TapLdifPipelineConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Singer LDIF tap TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextMeltanoTapLdifTypes",
]
