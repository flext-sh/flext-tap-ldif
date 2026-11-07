# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_ldif/_protocols/config
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_tap_ldif import t


class FlextTapLdifProtocolsConfig:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class TapLdif(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def streams(self) -> Sequence[FlextTapLdifProtocolsConfig.TapLdifStreamRule]:
            """Declarative stream business rules."""
            ...

    @runtime_checkable
    class TapLdifStreamRule(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """Singer stream name."""
            ...

        @property
        def primary_keys(self) -> Sequence[str]:
            """Record primary keys."""
            ...

        @property
        def stream_schema(self) -> t.MappingKV[str, t.JsonValue]:
            """Singer stream JSON schema."""
            ...

    @runtime_checkable
    class Root(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def TapLdif(self) -> FlextTapLdifProtocolsConfig.TapLdif:
            """TapLdif business-rule config domain."""
            ...


__all__: list[str] = [
    "FlextTapLdifProtocolsConfig",
]
