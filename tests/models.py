"""Test models for flext-tap-ldif - uses m.Tests.* namespace pattern.

This module provides test-specific models that extend the main flext-tap-ldif models.
Uses the unified namespace pattern m.Tests.* for test-only objects.
Combines TestsFlextModels functionality with project-specific test models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from tests import FlextTapLdifModels


class TestsFlextTapLdifModels(FlextTestsModels, FlextTapLdifModels):
    """Test models combining TestsFlextModels with flext-tap-ldif models."""

    class Tests(FlextTestsModels.Tests):
        """Project-specific test models."""


m = TestsFlextTapLdifModels

__all__: list[str] = ["TestsFlextTapLdifModels", "m"]
