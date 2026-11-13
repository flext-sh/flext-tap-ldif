# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Models Facade - LDIF Tap Models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels

from flext_tap_ldif._models import FlextTapLdifModelsBase, FlextTapLdifModelsConfig


class FlextTapLdifModels(
    FlextMeltanoModels,
    FlextLdifModels,
    FlextTapLdifModelsBase,
    FlextTapLdifModelsConfig,
):
    """Facade for tap-ldif data models."""


m = FlextTapLdifModels
__all__: list[str] = ["FlextTapLdifModels", "m"]
