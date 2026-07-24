"""FlextTapLdifConfig — frozen config singleton for flext-tap-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TapLdif:`` key and
are exposed through the open ``config.TapLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TapLdif.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _TapLdifNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextTapLdifConfig(FlextMeltanoConfig):
    """TapLdif config auto-loaded model-less from ``config/*.yaml``."""

    TapLdif: _TapLdifNamespace = _TapLdifNamespace()


config: FlextTapLdifConfig = FlextTapLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_ldif import config``."""

__all__: list[str] = ["FlextTapLdifConfig", "config"]
