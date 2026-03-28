"""Re-export shim — canonical implementation lives in _utilities.tap."""

from __future__ import annotations

from flext_tap_ldif._utilities.tap import FlextTapLdif, logger, main

__all__ = ["FlextTapLdif", "logger", "main"]
