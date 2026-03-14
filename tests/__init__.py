"""Test module for flext-tap-ldif.

This module provides test infrastructure for flext-tap-ldif with subnamespaces .Tests
following FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "p": ("protocols", "p"),
    "tm": ("models", "m"),
    "tt": ("typings", "t"),
    "u": ("utilities", "u"),
}
p
tm
tt
u
__all__ = ["p", "tm", "tt", "u"]


def __getattr__(name: str):
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
