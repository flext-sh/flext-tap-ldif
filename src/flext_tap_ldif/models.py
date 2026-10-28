# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Models Facade - LDIF Tap Models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels

from flext_tap_ldif._models.base import FlextTapLdifModelsBase
from flext_tap_ldif._models.config import FlextTapLdifConfigModels


class FlextTapLdifModels(
    FlextTapLdifConfigModels,
    FlextMeltanoModels,
    FlextLdifModels,
    FlextTapLdifModelsBase,
):
    """Facade for tap-ldif data models."""


m = FlextTapLdifModels
__all__: list[str] = ["FlextTapLdifModels", "m"]
