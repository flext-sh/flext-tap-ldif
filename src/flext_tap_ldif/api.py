"""FLEXT service orchestrator for tap-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
Only domain-specific tap creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoSingerTapAdapter, FlextMeltanoTapServiceBase

from flext_tap_ldif import FlextTapLdif, m, p, t, u


class FlextTapLdifService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-ldif. All behavior from base via MRO."""

    tap_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical Singer tap identifier."),
    ] = "tap-ldif"

    @override
    def create_tap_instance(
        self,
        settings: p.Settings | t.JsonMapping | None = None,
    ) -> p.Meltano.SingerTapInstance:
        """Create the internal tap runtime backed by Singer SDK.

        Args:
            settings: Optional settings payload (model or mapping) for the tap;
                ``None`` starts the tap with its default config.

        Returns:
            The resulting ``p.Meltano.SingerTapInstance``.

        """
        raw_config = (
            u.json_dict_adapter().validate_python(
                settings.model_dump()
                if isinstance(settings, p.HasModelDump)
                else settings,
            )
            if settings is not None
            else None
        )
        return FlextMeltanoSingerTapAdapter(FlextTapLdif(config=raw_config))


tap_ldif: FlextTapLdifService = FlextTapLdifService.fetch_global()
"""Shared FlextTapLdifService facade instance."""

__all__: list[str] = ["FlextTapLdifService", "tap_ldif"]
