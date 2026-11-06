"""flext-tap-ldif config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/tap-ldif.yaml`` business-rule SSOT,
reusing the flext-meltano ``m`` base models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated

from flext_meltano import m

from flext_tap_ldif import p, t


class FlextTapLdifModelsConfig:
    """Namespace of typed flext-tap-ldif config models."""

    class TapLdif(m.FrozenModel):
        """TapLdif business rules from ``config/tap-ldif.yaml``."""

        class StreamRule(m.FrozenModel):
            """One declarative stream business rule."""

            name: str = m.Field(description="Singer stream name")
            primary_keys: Sequence[str] = m.Field(description="Record primary keys")
            stream_schema: t.MappingKV[str, t.JsonValue] = m.Field(
                alias="schema",
                description="Singer stream JSON schema",
            )

        streams: Sequence[StreamRule] = m.Field(
            default=(),
            description="Declarative stream business rules",
        )

    class Root(m.StrictModel):
        """Root flext-tap-ldif config validated from ``config/*.yaml``."""

        model_config = m.ConfigDict(extra="allow")

        TapLdif: Annotated[
            p.TapLdif, t.schema_for_model(FlextTapLdifModelsConfig.TapLdif)
        ] = m.Field(
            description="TapLdif business-rule config domain",
        )


__all__: list[str] = ["FlextTapLdifModelsConfig"]
