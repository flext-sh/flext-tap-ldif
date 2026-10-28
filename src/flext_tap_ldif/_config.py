"""FlextTapLdifConfig — frozen config singleton for flext-tap-ldif (ADR-005 §7).

Business-rule SSOT: the stream contracts (name, Singer schema, primary keys)
live in the packaged ``flext_tap_ldif/config/tap-ldif.yaml`` under the ``TapLdif:``
key and are exposed through the open ``config.TapLdif`` namespace (``extra="allow"``).
The typed validated view of that namespace is built by the consumers in the
``u`` family (``u.TapLdif.tap_ldif()``) — config never imports the model layer
(ADR-005 §2).
Config holds the business rules; ``settings`` holds the adjustable runtime
parameters (``.env`` / env vars / local settings / CLI).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m


class FlextTapLdifConfig(FlextMeltanoConfig):
    """TapLdif config auto-loaded from ``config/*.yaml``.

    ``FlextMeltanoConfig`` already carries ``FlextSettings`` first (ENFORCE-042),
    so the class stays a frozen, YAML-validated config singleton. The YAML
    ``TapLdif:`` slice is exposed as an open namespace; the typed validated
    view lives behind ``u.TapLdif.tap_ldif()``.
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
