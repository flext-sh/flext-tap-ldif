"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels

from flext_tap_ldif._models.base import FlextTapLdifModelsBase
from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
from flext_tap_ldif._models.config import FlextTapLdifModelsConfig
from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
from flext_tap_ldif._models.file import FlextTapLdifModelsFile
from flext_tap_ldif._models.record import FlextTapLdifModelsRecord


class FlextTapLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Complete models for LDIF tap operations using Pydantic BaseModel.

    Provides standardized models for all LDIF tap domain entities including:
    - Singer stream metadata and LDIF file configuration
    - LDIF file parsing and change record processing
    - Entry validation and transformation operations
    - Performance monitoring and batch processing metrics
    - LDIF format compliance and schema validation
    - All utility functions for LDIF data processing

    All nested classes use Pydantic BaseModel validation and patterns.
    Consolidates ALL models for LDIF file extraction and processing.
    """

    class TapLdif(
        FlextTapLdifModelsBase,
        FlextTapLdifModelsEntry,
        FlextTapLdifModelsFile,
        FlextTapLdifModelsBatch,
        FlextTapLdifModelsConfig,
        FlextTapLdifModelsRecord,
    ):
        """TapLdif domain namespace composed from _models/ submodules."""


# Short aliases
m = FlextTapLdifModels
