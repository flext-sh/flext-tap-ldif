"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import m
from flext_tap_ldif import (
    FlextTapLdifModelsBatch,
    FlextTapLdifModelsEntry,
    FlextTapLdifModelsFile,
    FlextTapLdifModelsRecord,
    FlextTapLdifModelsSettings,
)


class FlextTapLdifModels(m, FlextLdifModels):
    """Complete models for LDIF tap operations using Pydantic BaseModel."""

    class TapLdif(
        FlextTapLdifModelsEntry,
        FlextTapLdifModelsFile,
        FlextTapLdifModelsBatch,
        FlextTapLdifModelsSettings,
        FlextTapLdifModelsRecord,
    ):
        """TapLdif domain namespace composed from models/ submodules."""


# Short aliases
m = FlextTapLdifModels

__all__: list[str] = ["FlextTapLdifModels", "m"]
