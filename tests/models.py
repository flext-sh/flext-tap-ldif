"""Test models for flext-tap-ldif - uses m.TapLdif.Tests.* namespace pattern.

This module provides test-specific models that extend the main flext-tap-ldif models.
Uses the unified namespace pattern m.TapLdif.Tests.* for test-only objects.
Combines m functionality with project-specific test models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import m

from flext_tap_ldif import m as _tap_ldif_m


class TestsFlextTapLdifModels(m, _tap_ldif_m):
    """Test models combining m with flext-tap-ldif models."""

    class Tests(m.Tests):
        """Project-specific test models."""


m = TestsFlextTapLdifModels

__all__ = ["TestsFlextTapLdifModels", "m"]
