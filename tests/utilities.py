"""Test utilities for flext-tap-ldif - uses u.TapLdif.* namespace pattern.

This module provides test-specific utilities that extend the main flext-tap-ldif utilities.
Uses the unified namespace pattern u.TapLdif.* for test-only utilities.
Combines TestsFlextUtilities functionality with project-specific test utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_ldif import FlextTapLdifUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextTapLdifUtilities(FlextTestsUtilities, FlextTapLdifUtilities):
    """Test utilities combining TestsFlextUtilities with flext-tap-ldif utilities."""

    class TapLdif(FlextTapLdifUtilities.TapLdif):
        """TapLdif test utilities namespace."""

        class Tests:
            """Project-specific test utilities."""


u = TestsFlextTapLdifUtilities
__all__: list[str] = ["TestsFlextTapLdifUtilities", "u"]
