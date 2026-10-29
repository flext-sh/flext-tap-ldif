# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_ldif/_protocols/generated_models_tapldif_streamrule
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence as collections_abc_Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

import pydantic

if TYPE_CHECKING:
    from flext_tap_ldif import t as flext_tap_ldif_t


class FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule:
    """Own the structural model contract declared by this module."""

    @runtime_checkable
    class StreamRule(Protocol):
        """Structural data contract projected from the owning model."""

        name: str
        primary_keys: collections_abc_Sequence[str]
        stream_schema: flext_tap_ldif_t.MappingKV[str, pydantic.JsonValue]


__all__: list[str] = [
    "FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule",
]
