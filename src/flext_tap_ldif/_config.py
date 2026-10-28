"""FlextTapLdifConfig — frozen config singleton for flext-tap-ldif (ADR-005 §7).

Business-rule SSOT: the stream contracts (name, Singer schema, primary keys)
live in the packaged ``flext_tap_ldif/config/tap-ldif.yaml`` under the ``TapLdif:``
key and are exposed through the open ``config.TapLdif`` namespace (``extra="allow"``).
``config.tap_ldif`` is the validated typed view of that namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from functools import cached_property
from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_tap_ldif._models.config import FlextModelsTapLdifConfig


class FlextTapLdifConfig(FlextMeltanoConfig):
    """TapLdif config auto-loaded from ``config/*.yaml``.

    The YAML ``TapLdif:`` slice is exposed as an open namespace and validated
    into the typed config models behind ``config.tap_ldif``.
    """

    TapLdif: Annotated[
        m.Meltano.MeltanoNamespace,
        m.Field(
            description="Open namespace exposing ``config/*.yaml`` under ``TapLdif``.",
        ),
    ] = m.Meltano.MeltanoNamespace()

    @cached_property
    def tap_ldif(self) -> FlextModelsTapLdifConfig.TapLdif:
        """Validated TapLdif business-rule config (streams and their contracts)."""
        payload = self.TapLdif.model_dump()
        return FlextModelsTapLdifConfig.TapLdif.model_validate(payload)


config: FlextTapLdifConfig = FlextTapLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_ldif import config``."""

__all__: list[str] = ["FlextTapLdifConfig", "config"]
