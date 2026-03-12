"""Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_tests import FlextTestsTypes

from flext_tap_ldif import t


class TestsFlextTapLdifTypes(FlextTestsTypes):
    """Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

    Architecture: Uses composition (not inheritance) with FlextTestsTypes and FlextTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - TestsFlextTapLdifTypes.Tests.* = flext_tests test types (via composition)
    - TestsFlextTapLdifTypes.TapLdif.* = flext-tap-ldif-specific test types
    - TestsFlextTapLdifTypes.* = FlextTestsTypes types (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsTypes deprecates subclassing)
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

        type TestLdifFilePath = Literal["/tmp/test.ldif", "/tmp/sample.ldif"]
        type TestLdifEncoding = Literal["utf-8", "ascii", "iso-8859-1"]
        type TestObjectClass = Literal["person", "organization", "groupOfNames"]
        type MockLdifEntry = dict[str, str | dict[str, list[str]]]
        type MockLdifFile = list[dict[str, str | dict[str, list[str]]]]
        type TestLdifScenario = dict[str, object]
        type TestLdifValidationResult = dict[str, bool | str | list[str]]
        type TestLdifParsingResult = dict[str, object]


tt = TestsFlextTapLdifTypes
__all__ = ["TestsFlextTapLdifTypes", "t", "tt"]
