# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Models Facade - LDIF Tap Models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import m as flext_ldif_m
from flext_meltano import m as flext_meltano_m

from flext_tap_ldif._models import FlextModelsTapLdifBase, FlextModelsTapLdifConfig


class FlextModelsTapLdif(
    FlextModelsTapLdifBase,
    FlextModelsTapLdifConfig,
    flext_meltano_m,
    flext_ldif_m,
):
    """Facade for tap-ldif data models."""


m = FlextModelsTapLdif
__all__: list[str] = ["FlextModelsTapLdif", "m"]
