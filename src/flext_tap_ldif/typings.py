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

from collections.abc import Mapping

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes

from flext_tap_ldif.constants import c


class FlextTapLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Singer LDIF tap-specific type definitions extending t.

    Domain-specific type system for Singer LDIF tap operations.
    Contains ONLY complex LDIF tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TapLdif:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[
            str,
            str | int | bool | dict[str, t.ContainerValue],
        ]
        type StreamConfiguration = dict[str, str | bool | dict[str, t.ContainerValue]]
        type CatalogDefinition = dict[str, str | list[dict[str, t.ContainerValue]]]
        type SchemaDefinition = dict[str, str | dict[str, t.ContainerValue] | bool]
        type MessageOutput = dict[str, str | dict[str, t.ContainerValue]]
        type StateManagement = dict[str, str | int | dict[str, t.ContainerValue]]

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = dict[
            str,
            str | int | bool | dict[str, t.ContainerValue],
        ]
        type EntryExtraction = dict[str, str | list[str] | dict[str, t.ContainerValue]]
        type EntryTransformation = list[dict[str, str | t.ContainerValue]]
        type EntryValidation = dict[
            str,
            bool | str | list[str] | dict[str, t.ContainerValue],
        ]
        type BatchProcessing = dict[str, int | bool | dict[str, t.ContainerValue]]
        type FileProcessing = dict[str, str | int | dict[str, t.ContainerValue]]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str,
            str | bool | dict[str, t.ContainerValue],
        ]
        type ExtractionFilter = dict[str, str | list[str] | dict[str, t.ContainerValue]]
        type ExtractionMapping = dict[str, str | dict[str, t.ContainerValue]]
        type ExtractionResult = dict[str, bool | list[dict[str, t.ContainerValue]]]
        type ExtractionMetrics = dict[str, int | float | dict[str, t.ContainerValue]]
        type ExtractionState = dict[str, str | int | dict[str, t.ContainerValue]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str,
            str | bool | int | dict[str, t.ContainerValue],
        ]
        type StreamMetadata = dict[str, str | dict[str, t.ContainerValue]]
        type StreamRecord = dict[str, t.ContainerValue | dict[str, t.ContainerValue]]
        type StreamRecordValue = str | int | list[str] | Mapping[str, list[str]]
        type StreamState = dict[str, str | int | dict[str, t.ContainerValue]]
        type StreamBookmark = dict[str, str | int | dict[str, t.ContainerValue]]
        type StreamSchema = dict[str, str | dict[str, t.ContainerValue] | bool]

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = dict[
            str,
            str | int | bool | dict[str, t.ContainerValue],
        ]
        type FileValidation = dict[str, bool | str | int | list[str]]
        type FileProcessing = dict[str, str | int | dict[str, t.ContainerValue]]
        type FileBatching = dict[str, int | bool | dict[str, t.ContainerValue]]
        type FileMonitoring = dict[str, bool | int | dict[str, t.ContainerValue]]
        type FileMetrics = dict[str, int | float | dict[str, t.ContainerValue]]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str,
            bool | str | int | dict[str, t.ContainerValue],
        ]
        type ErrorRecovery = dict[str, str | bool | dict[str, t.ContainerValue]]
        type ErrorReporting = dict[str, str | int | dict[str, t.ContainerValue]]
        type ErrorClassification = dict[str, str | int | dict[str, t.ContainerValue]]
        type ErrorMetrics = dict[str, int | float | dict[str, t.ContainerValue]]
        type ErrorTracking = list[dict[str, str | int | dict[str, t.ContainerValue]]]

    class Project:
        """Singer Tap LDIF-specific project types.

        Adds Singer tap LDIF-specific project types.
        Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type SingerTapLdifProjectConfig = dict[str, t.ContainerValue]
        type LdifExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[str, bool | str | dict[str, t.ContainerValue]]
        type TapLdifPipelineConfig = dict[str, t.ContainerValue]


t = FlextTapLdifTypes
__all__ = ["FlextTapLdifTypes", "t"]
