"""FLEXT service orchestrator for tap-ldif.

from flext_tap_ldif import u
Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
Only domain-specific tap creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoTapServiceBase
from flext_meltano.services.singer_sdk import FlextMeltanoSingerTapAdapter
from flext_tap_ldif import FlextTapLdif, p, t, u


class FlextTapLdifService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-ldif. All behavior from base via MRO."""

    tap_name: Annotated[
        t.NonEmptyStr, u.Field(description="Canonical Singer tap identifier.")
    ] = "tap-ldif"

    @override
    def create_tap_instance(
        self, settings: p.Settings | t.JsonMapping | None = None
    ) -> p.Meltano.SingerTapInstance:
        """Create the internal tap runtime backed by Singer SDK."""
        raw_config = (
            t.json_dict_adapter().validate_python(
                settings.model_dump() if hasattr(settings, "model_dump") else settings
            )
            if settings is not None
            else None
        )
        return FlextMeltanoSingerTapAdapter(FlextTapLdif(config=raw_config))


tap_ldif: FlextTapLdifService = FlextTapLdifService.fetch_global()
"""Shared FlextTapLdifService facade instance."""

__all__: list[str] = ["FlextTapLdifService", "tap_ldif"]
