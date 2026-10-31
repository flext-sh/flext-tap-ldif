# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit.test_extract_service import TestsFlextTapLdifExtractService
    from tests.unit.test_extract_support import TestsFlextTapLdifExtractSupport


__all__: tuple[str, ...] = (
    "TestsFlextTapLdifExtractService",
    "TestsFlextTapLdifExtractSupport",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextTapLdifExtractService": ".test_extract_service",
        "TestsFlextTapLdifExtractSupport": ".test_extract_support",
    }),
    public_exports=__all__,
)
