"""flext-tap-ldif config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/tap-ldif.yaml`` business-rule SSOT,
reusing the flext-meltano ``m`` base models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m, t


class FlextModelsTapLdifConfig:
    """Namespace of typed flext-tap-ldif config models."""

    class TapLdif(m.FrozenModel):
        """TapLdif business rules from ``config/tap-ldif.yaml``."""

        class StreamRule(m.FrozenModel):
            """One declarative stream business rule."""

            name: str = m.Field(description="Singer stream name")
            primary_keys: t.StrSequence = m.Field(description="Record primary keys")
            stream_schema: t.JsonMapping = m.Field(
                alias="schema",
                description="Singer stream JSON schema",
            )

        streams: t.SequenceOf[StreamRule] = m.Field(
            default=(),
            description="Declarative stream business rules",
        )

    class Root(m.FrozenModel):
        """Root flext-tap-ldif config validated from ``config/*.yaml``."""

        model_config = m.ConfigDict(extra="allow")

        TapLdif: FlextModelsTapLdifConfig.TapLdif = m.Field(
            description="TapLdif business-rule config domain",
        )


__all__: list[str] = ["FlextModelsTapLdifConfig"]
