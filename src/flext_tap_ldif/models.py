# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Models Facade - LDIF Tap Models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels

from flext_tap_ldif._models.base import FlextModelsTapLdifBase
from flext_tap_ldif._models.config import FlextModelsTapLdifConfig


class FlextModelsTapLdif(
    FlextModelsTapLdifConfig,
    FlextMeltanoModels,
    FlextLdifModels,
    FlextModelsTapLdifBase,
):
    """Facade for tap-ldif data models."""


m = FlextModelsTapLdif
__all__: list[str] = ["FlextModelsTapLdif", "m"]
