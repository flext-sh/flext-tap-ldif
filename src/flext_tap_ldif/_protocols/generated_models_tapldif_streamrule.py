# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_ldif/_protocols/generated_models_tapldif_streamrule
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping as collections_abc_Mapping,
    Sequence as collections_abc_Sequence,
)
from typing import Protocol, runtime_checkable

import pydantic


class FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule:
    """Own the structural model contract declared by this module."""

    @runtime_checkable
    class StreamRule(Protocol):
        """Structural data contract projected from the owning model."""

        name: str
        primary_keys: collections_abc_Sequence[str]
        stream_schema: collections_abc_Mapping[str, pydantic.JsonValue]


__all__: list[str] = [
    "FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule",
]
