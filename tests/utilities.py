"""Test utilities for flext-tap-ldif - uses u.TapLdif.* namespace pattern.

This module provides test-specific utilities that extend the main flext-tap-ldif utilities.
Uses the unified namespace pattern u.TapLdif.* for test-only utilities.
Combines FlextTestsUtilities functionality with project-specific test utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_ldif import FlextMeltanoTapLdifUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextMeltanoTapLdifUtilities(
    FlextTestsUtilities, FlextMeltanoTapLdifUtilities
):
    """Test utilities combining FlextTestsUtilities with flext-tap-ldif utilities."""

    class TapLdif:
        """TapLdif test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = TestsFlextMeltanoTapLdifUtilities

__all__ = ["TestsFlextMeltanoTapLdifUtilities", "u"]
