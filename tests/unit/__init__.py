# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif.tests.unit.test_tap import (
        TestsFlextTapLdifTap as TestsFlextTapLdifTap,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_tap": ("TestsFlextTapLdifTap",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
