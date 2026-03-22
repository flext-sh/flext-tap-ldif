"""Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_tap_ldif import FlextTapLdifConstants as _c, FlextTapLdifTypes


class FlextTapLdifTestTypes(FlextTestsTypes, FlextTapLdifTypes):
    """Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

    Architecture: Uses composition (not inheritance) with FlextTestsTypes and FlextTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - FlextTapLdifTestTypes.Tests.* = flext_tests test types (via composition)
    - FlextTapLdifTestTypes.TapLdifTest.* = flext-tap-ldif-specific test types
    - FlextTapLdifTestTypes.* = FlextTestsTypes types (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsTypes deprecates subclassing)
    - flext-tap-ldif-specific types go in TapLdifTest namespace
    - Generic types accessed via Tests namespace
    """

    class TapLdifTest:
        """Tap LDIF test types - domain-specific for LDIF tap testing.

        Contains test types specific to LDIF tap functionality including:
        - Test configuration types
        - Mock LDIF data types
        - Test scenario types
        """

        type TestLdifFilePath = _c.TestLdifFilePath
        type TestLdifEncoding = _c.TestLdifEncoding
        type TestObjectClass = _c.TestObjectClass
        type MockLdifEntry = dict[str, str | dict[str, list[str]]]
        type MockLdifFile = list[dict[str, str | dict[str, list[str]]]]
        type TestLdifScenario = dict[str, object]
        type TestLdifValidationResult = dict[str, bool | str | list[str]]
        type TestLdifParsingResult = dict[str, object]


t = FlextTapLdifTestTypes
__all__ = ["FlextTapLdifTestTypes", "t"]
