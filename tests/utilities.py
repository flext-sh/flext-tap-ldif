"""Test utilities for flext-tap-ldif - uses u.TapLdif.* namespace pattern.

This module provides test-specific utilities that extend the main flext-tap-ldif utilities.
Uses the unified namespace pattern u.TapLdif.* for test-only utilities.
Combines u functionality with project-specific test utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import u

from flext_tap_ldif import FlextTapLdifUtilities


class TestsFlextTapLdifUtilities(u, FlextTapLdifUtilities):
    """Test utilities combining u with flext-tap-ldif utilities."""

    class Tests(u.Tests):
        """Project-specific test utilities."""


u = TestsFlextTapLdifUtilities
__all__ = ["TestsFlextTapLdifUtilities", "u"]
