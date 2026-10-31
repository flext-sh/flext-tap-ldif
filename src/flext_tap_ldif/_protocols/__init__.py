# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._protocols.generated_models_tapldif import (
        FlextTapLdifProtocolsGeneratedModelsTapLdif,
    )
    from flext_tap_ldif._protocols.generated_models_tapldif_streamrule import (
        FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule,
    )


__all__: tuple[str, ...] = (
    "FlextTapLdifProtocolsGeneratedModelsTapLdif",
    "FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapLdifProtocolsGeneratedModelsTapLdif": ".generated_models_tapldif",
        "FlextTapLdifTapLdifProtocolsGeneratedModelsStreamRule": (
            ".generated_models_tapldif_streamrule"
        ),
    }),
    public_exports=__all__,
)
