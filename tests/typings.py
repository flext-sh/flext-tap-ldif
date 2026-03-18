"""Types for flext-tap-ldif tests - uses composition with t.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_ldif import c, t


class TestsFlextTapLdifTypes(t):
    """Types for flext-tap-ldif tests - uses composition with t.

    Architecture: Uses composition (not inheritance) with t and FlextTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - TestsFlextTapLdifTypes.Tests.* = flext_tests test types (via composition)
    - TestsFlextTapLdifTypes.TapLdif.* = flext-tap-ldif-specific test types
    - TestsFlextTapLdifTypes.* = t types (via composition)

    Rules:
    - Use composition, not inheritance (t deprecates subclassing)
    - flext-tap-ldif-specific types go in TapLdif namespace
    - Generic types accessed via Tests namespace
    """

    class TapLdif:
        """Tap LDIF test types - domain-specific for LDIF tap testing.

        Contains test types specific to LDIF tap functionality including:
        - Test configuration types
        - Mock LDIF data types
        - Test scenario types
        """

        type TestLdifFilePath = c.TestLdifFilePath
        type TestLdifEncoding = c.TestLdifEncoding
        type TestObjectClass = c.TestObjectClass
        type MockLdifEntry = dict[str, str | dict[str, list[str]]]
        type MockLdifFile = list[dict[str, str | dict[str, list[str]]]]
        type TestLdifScenario = dict[str, object]
        type TestLdifValidationResult = dict[str, bool | str | list[str]]
        type TestLdifParsingResult = dict[str, object]


tt = TestsFlextTapLdifTypes
__all__ = ["TestsFlextTapLdifTypes", "t", "tt"]

t = TestsFlextTapLdifTypes
