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
            t.Scalar | t.ContainerValueMapping,
        ]
        type StreamConfiguration = Mapping[str, str | bool | t.ContainerValueMapping]
        type CatalogDefinition = Mapping[str, str | Sequence[t.ContainerValueMapping]]
        type SchemaDefinition = Mapping[str, str | t.ContainerValueMapping | bool]
        type MessageOutput = Mapping[str, str | t.ContainerValueMapping]
        type StateManagement = Mapping[str, str | int | t.ContainerValueMapping]

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingConfiguration = Mapping[
            str,
            t.Scalar | t.ContainerValueMapping,
        ]
        type EntryExtraction = Mapping[
            str, str | t.StrSequence | t.ContainerValueMapping
        ]
        type EntryTransformation = Sequence[Mapping[str, str | t.ContainerValue]]
        type EntryValidation = Mapping[
            str,
            bool | str | t.StrSequence | t.ContainerValueMapping,
        ]
        type BatchProcessing = Mapping[str, int | bool | t.ContainerValueMapping]
        type FileProcessing = Mapping[str, str | int | t.ContainerValueMapping]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = Mapping[
            str,
            str | bool | t.ContainerValueMapping,
        ]
        type ExtractionFilter = Mapping[
            str, str | t.StrSequence | t.ContainerValueMapping
        ]
        type ExtractionMapping = Mapping[str, str | t.ContainerValueMapping]
        type ExtractionResult = Mapping[str, bool | Sequence[t.ContainerValueMapping]]
        type ExtractionMetrics = Mapping[str, int | float | t.ContainerValueMapping]
        type ExtractionState = Mapping[str, str | int | t.ContainerValueMapping]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = Mapping[
            str,
            str | bool | int | t.ContainerValueMapping,
        ]
        type StreamMetadata = Mapping[str, str | t.ContainerValueMapping]
        type StreamRecord = Mapping[str, t.ContainerValue | t.ContainerValueMapping]
        type StreamRecordValue = str | int | t.StrSequence | Mapping[str, t.StrSequence]
        type StreamState = Mapping[str, str | int | t.ContainerValueMapping]
        type StreamBookmark = Mapping[str, str | int | t.ContainerValueMapping]
        type StreamSchema = Mapping[str, str | t.ContainerValueMapping | bool]

    class FileHandling:
        """File handling complex types."""

        type FileConfiguration = Mapping[
            str,
            t.Scalar | t.ContainerValueMapping,
        ]
        type FileValidation = Mapping[str, bool | str | int | t.StrSequence]
        type FileProcessing = Mapping[str, str | int | t.ContainerValueMapping]
        type FileBatching = Mapping[str, int | bool | t.ContainerValueMapping]
        type FileMonitoring = Mapping[str, bool | int | t.ContainerValueMapping]
        type FileMetrics = Mapping[str, int | float | t.ContainerValueMapping]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = Mapping[
            str,
            bool | str | int | t.ContainerValueMapping,
        ]
        type ErrorRecovery = Mapping[str, str | bool | t.ContainerValueMapping]
        type ErrorReporting = Mapping[str, str | int | t.ContainerValueMapping]
        type ErrorClassification = Mapping[str, str | int | t.ContainerValueMapping]
        type ErrorMetrics = Mapping[str, int | float | t.ContainerValueMapping]
        type ErrorTracking = Sequence[Mapping[str, str | int | t.ContainerValueMapping]]

    class Project:
        """Singer Tap LDIF-specific project types.

        Adds Singer tap LDIF-specific project types.
        Follows domain separation principle:
        Singer tap LDIF domain owns LDIF extraction and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type SingerTapLdifProjectConfig = Mapping[str, t.ContainerValue]
        type LdifExtractorConfig = Mapping[str, t.Scalar | t.StrSequence]
        type SingerProtocolConfig = Mapping[str, bool | str | t.ContainerValueMapping]
        type TapLdifPipelineConfig = Mapping[str, t.ContainerValue]


StreamRecordValue = FlextTapLdifTypes.StreamProcessing.StreamRecordValue

t = FlextTapLdifTypes
__all__ = ["FlextTapLdifTypes", "StreamRecordValue", "t"]
