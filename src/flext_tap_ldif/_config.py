"""FlextTapLdifConfig — frozen config singleton for flext-tap-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TapLdif:`` key and
are exposed through the open ``config.TapLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TapLdif.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m


class FlextTapLdifConfig(FlextMeltanoConfig):
    """TapLdif config auto-loaded model-less from ``config/*.yaml``.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); the class stays a frozen,
    YAML-validated config singleton.
    """

    TapLdif: Annotated[
        m.Meltano.MeltanoNamespace,
        m.Field(
            description="Open namespace exposing ``config/*.yaml`` under ``TapLdif``.",
        ),
    ] = m.Meltano.MeltanoNamespace()


config: FlextTapLdifConfig = FlextTapLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_ldif import config``."""

__all__: list[str] = ["FlextTapLdifConfig", "config"]
