"""FLEXT service orchestrator for tap-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
Only domain-specific tap creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerTapBase, FlextMeltanoTapServiceBase

from flext_tap_ldif import t
from flext_tap_ldif.tap import FlextTapLdif


class FlextTapLdifService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-ldif. All behavior from base via MRO."""

    tap_name: t.NonEmptyStr = "tap-ldif"

    @override
    def create_tap_instance(
        self,
        config: t.ContainerMapping | None = None,
    ) -> FlextMeltanoSingerTapBase:
        """Create the FlextTapLdif singer_sdk.Tap instance."""
        return FlextTapLdif()


__all__ = ["FlextTapLdifService"]
