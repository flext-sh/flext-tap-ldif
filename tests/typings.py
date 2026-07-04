"""Types for flext-tap-ldif tests - uses composition with TestsFlextTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_tap_ldif import FlextTapLdifTypes


class TestsFlextTapLdifTypes(FlextTestsTypes, FlextTapLdifTypes):
    """Types for flext-tap-ldif tests - uses composition with TestsFlextTypes.

    Architecture: Uses composition (not inheritance) with TestsFlextTypes and FlextTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - TestsFlextTapLdifTypes.Tests.* = flext_tests test types (via composition)
    - TestsFlextTapLdifTypes.TapLdifTest.* = flext-tap-ldif-specific test types
    - TestsFlextTapLdifTypes.* = TestsFlextTypes types (via composition)

    Rules:
    - Use composition, not inheritance (TestsFlextTypes deprecates subclassing)
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

        type MockLdifEntry = t.MappingKV[
            str,
            str | t.MappingKV[str, FlextTestsTypes.StrSequence],
        ]
        type MockLdifFile = t.SequenceOf[
            t.MappingKV[
                str,
                str | t.MappingKV[str, FlextTestsTypes.StrSequence],
            ]
        ]
        type TestLdifScenario = FlextTestsTypes.JsonMapping
        type TestLdifValidationResult = t.MappingKV[
            str,
            bool | str | FlextTestsTypes.StrSequence,
        ]
        type TestLdifParsingResult = FlextTestsTypes.JsonMapping


t = TestsFlextTapLdifTypes
__all__: list[str] = ["TestsFlextTapLdifTypes", "t"]
