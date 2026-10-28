"""FLEXT service orchestrator for tap-ldif — declarative Singer tap.

Thin facade over ``meltano.Tap``: declares the tap by building a
``m.Meltano.TapSpec`` from config business rules and delegating record fetching
to ``FlextTapLdifExtractService``. flext-meltano owns every ``singer_sdk`` detail.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoTapServiceBase

from flext_tap_ldif import c, m, p, t, u
from flext_tap_ldif.services.extract import FlextTapLdifExtractService


class FlextTapLdifService(FlextMeltanoTapServiceBase):
    """Declarative tap-ldif orchestrator built from config + settings SSOT."""

    tap_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical Singer tap identifier."),
    ] = c.TapLdif.TAP_NAME

    @override
    def create_tap_instance(
        self,
        settings: p.Settings | None = None,
    ) -> p.Meltano.SingerTapInstance:
        """Build the declarative Singer tap from config streams + a fetcher.

        Args:
            settings: Unused; the tap is built from the config SSOT.

        Returns:
            The resulting ``p.Meltano.SingerTapInstance``.

        """
        _ = settings
        tap: p.Meltano.SingerTapInstance = self.build_declarative_tap(
            u.TapLdif.tap_spec(),
            FlextTapLdifExtractService(),
        )
        return tap


tap_ldif: FlextTapLdifService = FlextTapLdifService.fetch_global()
"""Process-wide FlextTapLdifService facade singleton from the service container."""

__all__: list[str] = ["FlextTapLdifService", "tap_ldif"]
