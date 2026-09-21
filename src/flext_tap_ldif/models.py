"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from __future__ import annotations

from flext_ldif import m as _ldif_m
from flext_meltano import m

from ._models import (
    FlextTapLdifModelsBatch,
    FlextTapLdifModelsEntry,
    FlextTapLdifModelsFile,
    FlextTapLdifModelsRecord,
    FlextTapLdifModelsSettings,
)


class FlextTapLdifModels(m, _ldif_m):
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
