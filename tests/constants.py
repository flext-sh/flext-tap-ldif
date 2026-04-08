"""Module skeleton for TestsFlextTapLdifConstants.

Test constants for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_tap_ldif import FlextTapLdifConstants


class TestsFlextTapLdifConstants(FlextTestsConstants, FlextTapLdifConstants):
    """Test constants for flext-tap-ldif."""


c = TestsFlextTapLdifConstants
__all__ = ["TestsFlextTapLdifConstants", "c"]
