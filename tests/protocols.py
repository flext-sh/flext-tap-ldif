"""Protocols for flext-tap-ldif tests - uses composition with FlextTestsProtocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_tap_ldif import t


class TestsFlextMeltanoTapLdifProtocols(FlextTestsProtocols):
    """Protocols for flext-tap-ldif tests - uses composition with FlextTestsProtocols.

    Architecture: Uses composition (not inheritance) with FlextTestsProtocols and FlextMeltanoTapLdifProtocols
    for flext-tap-ldif-specific protocol definitions.

    Access patterns:
    - TestsFlextMeltanoTapLdifProtocols.Tests.* = flext_tests test protocols (via composition)
    - TestsFlextMeltanoTapLdifProtocols.TapLdif.* = flext-tap-ldif-specific test protocols
    - TestsFlextMeltanoTapLdifProtocols.* = FlextTestsProtocols protocols (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsProtocols deprecates subclassing)
    - flext-tap-ldif-specific protocols go in TapLdif namespace
    - Generic protocols accessed via Tests namespace
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols."""

    # TapLdif-specific test protocols namespace
    class TapLdif:
        """Tap LDIF test protocols - domain-specific for LDIF tap testing.

        Contains test protocols specific to LDIF tap functionality including:
        - Mock LDIF file protocols for testing
        - Test data provider protocols
        - Test assertion protocols
        """

        @runtime_checkable
        class MockLdifFileProtocol(Protocol):
            """Protocol for mock LDIF file operations in tests."""

            def open_file(self, file_path: str) -> bool:
                """Open mock LDIF file."""
                ...

            def close_file(self) -> bool:
                """Close mock LDIF file."""
                ...

            def read_entries(self) -> list[dict[str, t.GeneralValueType]]:
                """Read entries from mock LDIF file."""
                ...

        @runtime_checkable
        class TestLdifDataProviderProtocol(Protocol):
            """Protocol for test LDIF data providers."""

            def get_test_entries(self) -> list[dict[str, t.GeneralValueType]]:
                """Get test LDIF entries."""
                ...

            def get_test_file_content(self) -> str:
                """Get test LDIF file content."""
                ...

            def get_test_config(self) -> dict[str, t.GeneralValueType]:
                """Get test LDIF configuration."""
                ...

        @runtime_checkable
        class TestLdifAssertionProtocol(Protocol):
            """Protocol for test LDIF assertions."""

            def assert_ldif_file_parsed(
                self, entries: list[dict[str, t.GeneralValueType]]
            ) -> None:
                """Assert LDIF file was parsed correctly."""
                ...

            def assert_ldif_entries_valid(
                self, entries: list[dict[str, t.GeneralValueType]]
            ) -> None:
                """Assert LDIF entries are valid."""
                ...

            def assert_ldif_stream_config_valid(
                self, stream: dict[str, t.GeneralValueType]
            ) -> None:
                """Assert LDIF stream configuration is valid."""
                ...


# Aliases for simplified usage
p = TestsFlextMeltanoTapLdifProtocols
tp = TestsFlextMeltanoTapLdifProtocols

__all__ = [
    "TestsFlextMeltanoTapLdifProtocols",
    "p",
    "tp",
]
