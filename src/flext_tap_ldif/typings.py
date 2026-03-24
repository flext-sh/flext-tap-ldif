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
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamConfiguration = Mapping[
            str, str | bool | FlextMeltanoTypes.ContainerValueMapping
        ]
        type CatalogDefinition = Mapping[
            str, str | Sequence[FlextMeltanoTypes.ContainerValueMapping]
        ]
        type SchemaDefinition = Mapping[
            str, str | FlextMeltanoTypes.ContainerValueMapping | bool
        ]
        type MessageOutput = Mapping[str, str | FlextMeltanoTypes.ContainerValueMapping]
        type StateManagement = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type EntryExtraction = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type EntryTransformation = Sequence[
            Mapping[str, str | FlextMeltanoTypes.ContainerValue]
        ]
        type EntryValidation = Mapping[
            str,
            bool
            | str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type BatchProcessing = Mapping[
            str, int | bool | FlextMeltanoTypes.ContainerValueMapping
        ]
        type FileProcessing = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = Mapping[
            str,
            str | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ExtractionFilter = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ExtractionMapping = Mapping[
            str, str | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ExtractionResult = Mapping[
            str, bool | Sequence[FlextMeltanoTypes.ContainerValueMapping]
        ]
        type ExtractionMetrics = Mapping[
            str, int | float | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ExtractionState = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = Mapping[
            str,
            str | bool | int | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamMetadata = Mapping[
            str, str | FlextMeltanoTypes.ContainerValueMapping
        ]
        type StreamRecord = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamRecordValue = (
            str
            | int
            | FlextMeltanoTypes.StrSequence
            | Mapping[str, FlextMeltanoTypes.StrSequence]
        )
        type StreamState = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type StreamBookmark = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type StreamSchema = Mapping[
            str, str | FlextMeltanoTypes.ContainerValueMapping | bool
        ]

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type FileValidation = Mapping[
            str, bool | str | int | FlextMeltanoTypes.StrSequence
        ]
        type FileProcessing = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type FileBatching = Mapping[
            str, int | bool | FlextMeltanoTypes.ContainerValueMapping
        ]
        type FileMonitoring = Mapping[
            str, bool | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type FileMetrics = Mapping[
            str, int | float | FlextMeltanoTypes.ContainerValueMapping
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = Mapping[
            str,
            bool | str | int | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ErrorRecovery = Mapping[
            str, str | bool | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ErrorReporting = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ErrorClassification = Mapping[
            str, str | int | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ErrorMetrics = Mapping[
            str, int | float | FlextMeltanoTypes.ContainerValueMapping
        ]
        type ErrorTracking = Sequence[
            Mapping[str, str | int | FlextMeltanoTypes.ContainerValueMapping]
        ]

    class Project:
        """Singer Tap LDIF-specific project types.

        Adds Singer tap LDIF-specific project types.
        Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type SingerTapLdifProjectConfig = Mapping[str, FlextMeltanoTypes.ContainerValue]
        type LdifExtractorConfig = Mapping[
            str, FlextMeltanoTypes.Scalar | FlextMeltanoTypes.StrSequence
        ]
        type SingerProtocolConfig = Mapping[
            str, bool | str | FlextMeltanoTypes.ContainerValueMapping
        ]
        type TapLdifPipelineConfig = Mapping[str, FlextMeltanoTypes.ContainerValue]


StreamRecordValue = FlextTapLdifTypes.StreamProcessing.StreamRecordValue

t = FlextTapLdifTypes
__all__ = ["FlextTapLdifTypes", "StreamRecordValue", "t"]
