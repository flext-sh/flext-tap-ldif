"""FLEXT Tap LDIF Types - Domain-specific Singer LDIF tap type definitions.

This module provides Singer LDIF tap-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes


class FlextTapLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Singer LDIF tap-specific type definitions extending t.

    Domain-specific type system for Singer LDIF tap operations.
    Contains ONLY complex LDIF tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TapLdif:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[str, str | int | bool | dict[str, object]]
        type StreamConfiguration = dict[str, str | bool | dict[str, object]]
        type CatalogDefinition = dict[str, str | list[dict[str, object]]]
        type SchemaDefinition = dict[str, str | dict[str, object] | bool]
        type MessageOutput = dict[str, str | dict[str, object]]
        type StateManagement = dict[str, str | int | dict[str, object]]

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = dict[str, str | int | bool | dict[str, object]]
        type EntryExtraction = dict[str, str | list[str] | dict[str, object]]
        type EntryTransformation = list[dict[str, str | object]]
        type EntryValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type BatchProcessing = dict[str, int | bool | dict[str, object]]
        type FileProcessing = dict[str, str | int | dict[str, object]]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[str, str | bool | dict[str, object]]
        type ExtractionFilter = dict[str, str | list[str] | dict[str, object]]
        type ExtractionMapping = dict[str, str | dict[str, object]]
        type ExtractionResult = dict[str, bool | list[dict[str, object]]]
        type ExtractionMetrics = dict[str, int | float | dict[str, object]]
        type ExtractionState = dict[str, str | int | dict[str, object]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[str, str | bool | int | dict[str, object]]
        type StreamMetadata = dict[str, str | dict[str, object]]
        type StreamRecord = dict[str, object | dict[str, object]]
        type StreamState = dict[str, str | int | dict[str, object]]
        type StreamBookmark = dict[str, str | int | dict[str, object]]
        type StreamSchema = dict[str, str | dict[str, object] | bool]

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = dict[str, str | int | bool | dict[str, object]]
        type FileValidation = dict[str, bool | str | int | list[str]]
        type FileProcessing = dict[str, str | int | dict[str, object]]
        type FileBatching = dict[str, int | bool | dict[str, object]]
        type FileMonitoring = dict[str, bool | int | dict[str, object]]
        type FileMetrics = dict[str, int | float | dict[str, object]]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[str, bool | str | int | dict[str, object]]
        type ErrorRecovery = dict[str, str | bool | dict[str, object]]
        type ErrorReporting = dict[str, str | int | dict[str, object]]
        type ErrorClassification = dict[str, str | int | dict[str, object]]
        type ErrorMetrics = dict[str, int | float | dict[str, object]]
        type ErrorTracking = list[dict[str, str | int | dict[str, object]]]

    class Project:
        """Singer Tap LDIF-specific project types.

        Adds Singer tap LDIF-specific project types.
        Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
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
        type SingerTapLdifProjectConfig = dict[str, object]
        type LdifExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[str, bool | str | dict[str, object]]
        type TapLdifPipelineConfig = dict[str, object]


t = FlextTapLdifTypes
__all__ = ["FlextTapLdifTypes", "t"]
