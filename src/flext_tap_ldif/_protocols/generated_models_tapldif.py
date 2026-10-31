# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_ldif/_protocols/generated_models_tapldif
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence as collections_abc_Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from flext_tap_ldif._protocols import (
        FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule,
    )


class FlextTapLdifProtocolsGeneratedModelsTapLdif:
    """Own the structural model contract declared by this module."""

    @runtime_checkable
    class TapLdif(Protocol):
        """Structural data contract projected from the owning model."""

        streams: collections_abc_Sequence[
            FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule.StreamRule
        ]


__all__: list[str] = [
    "FlextTapLdifProtocolsGeneratedModelsTapLdif",
]
