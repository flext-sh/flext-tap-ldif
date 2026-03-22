"""Test models for flext-tap-ldif - uses m.TapLdif.Tests.* namespace pattern.

This module provides test-specific models that extend the main flext-tap-ldif models.
Uses the unified namespace pattern m.TapLdif.Tests.* for test-only objects.
Combines FlextTestsModels functionality with project-specific test models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_tap_ldif import FlextTapLdifModels


class FlextTapLdifTestModels(FlextTestsModels, FlextTapLdifModels):
    """Test models combining FlextTestsModels with flext-tap-ldif models."""

    class TapLdif(FlextTapLdifModels.TapLdif):
        """TapLdif domain models extending project models."""

        class Tests:
            """Project-specific test models."""


m = FlextTapLdifTestModels

__all__ = ["FlextTapLdifTestModels", "m"]
