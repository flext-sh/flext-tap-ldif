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

from collections.abc import Mapping, Sequence

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

        type TapConfiguration = Mapping[
            str,
            str | int | bool | Mapping[str, t.ContainerValue],
        ]
        type StreamConfiguration = Mapping[
            str, str | bool | Mapping[str, t.ContainerValue]
        ]
        type CatalogDefinition = Mapping[
            str, str | Sequence[Mapping[str, t.ContainerValue]]
        ]
        type SchemaDefinition = Mapping[
            str, str | Mapping[str, t.ContainerValue] | bool
        ]
        type MessageOutput = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type StateManagement = Mapping[str, str | int | Mapping[str, t.ContainerValue]]

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = Mapping[
            str,
            str | int | bool | Mapping[str, t.ContainerValue],
        ]
        type EntryExtraction = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type EntryTransformation = Sequence[Mapping[str, str | t.ContainerValue]]
        type EntryValidation = Mapping[
            str,
            bool | str | Sequence[str] | Mapping[str, t.ContainerValue],
        ]
        type BatchProcessing = Mapping[str, int | bool | Mapping[str, t.ContainerValue]]
        type FileProcessing = Mapping[str, str | int | Mapping[str, t.ContainerValue]]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = Mapping[
            str,
            str | bool | Mapping[str, t.ContainerValue],
        ]
        type ExtractionFilter = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type ExtractionMapping = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type ExtractionResult = Mapping[
            str, bool | Sequence[Mapping[str, t.ContainerValue]]
        ]
        type ExtractionMetrics = Mapping[
            str, int | float | Mapping[str, t.ContainerValue]
        ]
        type ExtractionState = Mapping[str, str | int | Mapping[str, t.ContainerValue]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = Mapping[
            str,
            str | bool | int | Mapping[str, t.ContainerValue],
        ]
        type StreamMetadata = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type StreamRecord = Mapping[
            str, t.ContainerValue | Mapping[str, t.ContainerValue]
        ]
        type StreamRecordValue = str | int | Sequence[str] | Mapping[str, Sequence[str]]
        type StreamState = Mapping[str, str | int | Mapping[str, t.ContainerValue]]
        type StreamBookmark = Mapping[str, str | int | Mapping[str, t.ContainerValue]]
        type StreamSchema = Mapping[str, str | Mapping[str, t.ContainerValue] | bool]

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = Mapping[
            str,
            str | int | bool | Mapping[str, t.ContainerValue],
        ]
        type FileValidation = Mapping[str, bool | str | int | Sequence[str]]
        type FileProcessing = Mapping[str, str | int | Mapping[str, t.ContainerValue]]
        type FileBatching = Mapping[str, int | bool | Mapping[str, t.ContainerValue]]
        type FileMonitoring = Mapping[str, bool | int | Mapping[str, t.ContainerValue]]
        type FileMetrics = Mapping[str, int | float | Mapping[str, t.ContainerValue]]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = Mapping[
            str,
            bool | str | int | Mapping[str, t.ContainerValue],
        ]
        type ErrorRecovery = Mapping[str, str | bool | Mapping[str, t.ContainerValue]]
        type ErrorReporting = Mapping[str, str | int | Mapping[str, t.ContainerValue]]
        type ErrorClassification = Mapping[
            str, str | int | Mapping[str, t.ContainerValue]
        ]
        type ErrorMetrics = Mapping[str, int | float | Mapping[str, t.ContainerValue]]
        type ErrorTracking = Sequence[
            Mapping[str, str | int | Mapping[str, t.ContainerValue]]
        ]

    class Project:
        """Singer Tap LDIF-specific project types.

        Adds Singer tap LDIF-specific project types.
        Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type SingerTapLdifProjectConfig = Mapping[str, t.ContainerValue]
        type LdifExtractorConfig = Mapping[str, str | int | bool | Sequence[str]]
        type SingerProtocolConfig = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]
        type TapLdifPipelineConfig = Mapping[str, t.ContainerValue]


StreamRecordValue = FlextTapLdifTypes.StreamProcessing.StreamRecordValue

t = FlextTapLdifTypes
__all__ = ["FlextTapLdifTypes", "StreamRecordValue", "t"]
