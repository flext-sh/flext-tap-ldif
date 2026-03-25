"""Module skeleton for FlextTapLdifTestConstants.

Test constants for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_tap_ldif import FlextTapLdifConstants


class FlextTapLdifTestConstants(FlextTestsConstants, FlextTapLdifConstants):
    """Test constants for flext-tap-ldif."""


c = FlextTapLdifTestConstants
__all__ = ["FlextTapLdifTestConstants", "c"]
