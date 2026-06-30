# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_TAP_LDIF_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._models": ("_models",),
        "._utilities": ("_utilities",),
        ".api": (
            "FlextTapLdifService",
            "tap_ldif",
        ),
        ".cli": (
            "FlextTapLdifCli",
            "main",
        ),
        ".constants": (
            "FlextTapLdifConstants",
            "c",
        ),
        ".models": (
            "FlextTapLdifModels",
            "m",
        ),
        ".protocols": (
            "FlextTapLdifProtocols",
            "p",
        ),
        ".settings": ("FlextTapLdifSettings",),
        ".tap": ("FlextTapLdif",),
        ".typings": (
            "FlextTapLdifTypes",
            "t",
        ),
        ".utilities": (
            "FlextTapLdifUtilities",
            "u",
        ),
    },
)

__all__: list[str] = ["FLEXT_TAP_LDIF_LAZY_IMPORTS_PART_01"]
