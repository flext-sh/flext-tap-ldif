"""FLEXT service orchestrator for tap-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
Only domain-specific tap creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerTapAdapter, FlextMeltanoTapServiceBase
from flext_tap_ldif import FlextTapLdif, p, t


class FlextTapLdifService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-ldif. All behavior from base via MRO."""

    tap_name: t.NonEmptyStr = "tap-ldif"

    @override
    def create_tap_instance(
        self,
        config: t.ContainerMapping | None = None,
    ) -> p.Meltano.SingerTapInstance:
        """Create the internal tap runtime backed by Singer SDK."""
        raw_config = dict(config) if config is not None else None
        return FlextMeltanoSingerTapAdapter(FlextTapLdif(config=raw_config))


__all__ = ["FlextTapLdifService"]
