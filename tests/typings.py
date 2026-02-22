"""Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_tests import FlextTestsTypes

from flext_tap_ldif import t


class TestsFlextMeltanoTapLdifTypes(FlextTestsTypes):
    """Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

    Architecture: Uses composition (not inheritance) with FlextTestsTypes and FlextMeltanoTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - TestsFlextMeltanoTapLdifTypes.Tests.* = flext_tests test types (via composition)
    - TestsFlextMeltanoTapLdifTypes.TapLdif.* = flext-tap-ldif-specific test types
    - TestsFlextMeltanoTapLdifTypes.* = FlextTestsTypes types (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsTypes deprecates subclassing)
    - flext-tap-ldif-specific types go in TapLdif namespace
    - Generic types accessed via Tests namespace
    """

    # Composition: expose FlextTestsTypes
    # Tests = FlextTestsTypes  # Avoid override issues

    # TapLdif-specific test types namespace
    class TapLdif:
        """Tap LDIF test types - domain-specific for LDIF tap testing.

        Contains test types specific to LDIF tap functionality including:
        - Test configuration types
        - Mock LDIF data types
        - Test scenario types
        """

        # Test configuration literals
        type TestLdifFilePath = Literal["/tmp/test.ldif", "/tmp/sample.ldif"]
        type TestLdifEncoding = Literal["utf-8", "ascii", "iso-8859-1"]
        type TestObjectClass = Literal["person", "organization", "groupOfNames"]

        # Test data types
        type MockLdifEntry = dict[str, str | dict[str, list[str]]]
        type MockLdifFile = list[MockLdifEntry]
        type TestLdifScenario = dict[str, t.GeneralValueType]

        # Test result types
        type TestLdifValidationResult = dict[str, bool | str | list[str]]
        type TestLdifParsingResult = dict[str, t.GeneralValueType]


# Alias for simplified usage
tt = TestsFlextMeltanoTapLdifTypes

__all__ = [
    "TestsFlextMeltanoTapLdifTypes",
    "tt",
]
