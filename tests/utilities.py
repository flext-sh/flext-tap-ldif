"""Test utilities for flext-tap-ldif - uses u.TapLdif.* namespace pattern.

Provides test-specific utilities extending the main flext-tap-ldif utilities.
Uses the unified namespace pattern u.TapLdif.* for test-only utilities.
Combines TestsFlextUtilities functionality with project-specific test utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from tests import FlextTapLdifUtilities


class TestsFlextTapLdifUtilities(FlextTestsUtilities, FlextTapLdifUtilities):
    """Test utilities combining TestsFlextUtilities with flext-tap-ldif utilities."""

    class Tests(FlextTestsUtilities.Tests):
        """Project-specific test utilities."""


u = TestsFlextTapLdifUtilities
__all__: list[str] = ["TestsFlextTapLdifUtilities", "u"]
