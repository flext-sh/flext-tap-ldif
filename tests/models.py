"""Test models for flext-tap-ldif tests.

Provides TestsFlextTapLdifModels, extending FlextTestsModels with
flext-tap-ldif-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.models import FlextTestsModels

from flext_tap_ldif.models import FlextMeltanoTapLdifModels


class TestsFlextTapLdifModels(FlextTestsModels, FlextMeltanoTapLdifModels):
    """Models for flext-tap-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextMeltanoTapLdifModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Tap LDIF domain models)
    - m.* (production models via alternative alias)
    """

    class Tests:
        """Project-specific test fixtures namespace."""

        class TapLdif:
            """Tap LDIF-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextTapLdifModels
m = TestsFlextTapLdifModels

__all__ = [
    "TestsFlextTapLdifModels",
    "m",
    "tm",
]
