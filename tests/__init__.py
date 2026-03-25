# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Test module for flext-tap-ldif.

This module provides test infrastructure for flext-tap-ldif with subnamespaces .Tests
following FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests.conftest import (
        MockLDIFParser,
        MockLDIFTap,
        basic_tap_config,
        benchmark_config,
        binary_ldif_content,
        binary_ldif_file,
        changes_tap_config,
        directory_tap_config,
        docker_control,
        filtered_tap_config,
        invalid_ldif_content,
        invalid_ldif_file,
        large_ldif_file,
        ldif_directory,
        mock_ldif_parser,
        mock_ldif_tap,
        performance_tap_config,
        pytest_configure,
        sample_ldif_changes,
        sample_ldif_changes_file,
        sample_ldif_content,
        sample_ldif_file,
        set_test_environment,
        shared_ldap_container,
        singer_catalog_config,
        singer_state,
        utf16_ldif_file,
    )
    from tests.constants import (
        FlextTapLdifTestConstants,
        FlextTapLdifTestConstants as c,
    )
    from tests.models import FlextTapLdifTestModels, FlextTapLdifTestModels as m
    from tests.protocols import (
        FlextTapLdifTestProtocols,
        FlextTapLdifTestProtocols as p,
    )
    from tests.test_tap import test_discover_streams
    from tests.typings import FlextTapLdifTestTypes, FlextTapLdifTestTypes as t
    from tests.utilities import (
        FlextTapLdifTestUtilities,
        FlextTapLdifTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTapLdifTestConstants": ["tests.constants", "FlextTapLdifTestConstants"],
    "FlextTapLdifTestModels": ["tests.models", "FlextTapLdifTestModels"],
    "FlextTapLdifTestProtocols": ["tests.protocols", "FlextTapLdifTestProtocols"],
    "FlextTapLdifTestTypes": ["tests.typings", "FlextTapLdifTestTypes"],
    "FlextTapLdifTestUtilities": ["tests.utilities", "FlextTapLdifTestUtilities"],
    "MockLDIFParser": ["tests.conftest", "MockLDIFParser"],
    "MockLDIFTap": ["tests.conftest", "MockLDIFTap"],
    "basic_tap_config": ["tests.conftest", "basic_tap_config"],
    "benchmark_config": ["tests.conftest", "benchmark_config"],
    "binary_ldif_content": ["tests.conftest", "binary_ldif_content"],
    "binary_ldif_file": ["tests.conftest", "binary_ldif_file"],
    "c": ["tests.constants", "FlextTapLdifTestConstants"],
    "changes_tap_config": ["tests.conftest", "changes_tap_config"],
    "d": ["flext_tests", "d"],
    "directory_tap_config": ["tests.conftest", "directory_tap_config"],
    "docker_control": ["tests.conftest", "docker_control"],
    "e": ["flext_tests", "e"],
    "filtered_tap_config": ["tests.conftest", "filtered_tap_config"],
    "h": ["flext_tests", "h"],
    "invalid_ldif_content": ["tests.conftest", "invalid_ldif_content"],
    "invalid_ldif_file": ["tests.conftest", "invalid_ldif_file"],
    "large_ldif_file": ["tests.conftest", "large_ldif_file"],
    "ldif_directory": ["tests.conftest", "ldif_directory"],
    "m": ["tests.models", "FlextTapLdifTestModels"],
    "mock_ldif_parser": ["tests.conftest", "mock_ldif_parser"],
    "mock_ldif_tap": ["tests.conftest", "mock_ldif_tap"],
    "p": ["tests.protocols", "FlextTapLdifTestProtocols"],
    "performance_tap_config": ["tests.conftest", "performance_tap_config"],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_ldif_changes": ["tests.conftest", "sample_ldif_changes"],
    "sample_ldif_changes_file": ["tests.conftest", "sample_ldif_changes_file"],
    "sample_ldif_content": ["tests.conftest", "sample_ldif_content"],
    "sample_ldif_file": ["tests.conftest", "sample_ldif_file"],
    "set_test_environment": ["tests.conftest", "set_test_environment"],
    "shared_ldap_container": ["tests.conftest", "shared_ldap_container"],
    "singer_catalog_config": ["tests.conftest", "singer_catalog_config"],
    "singer_state": ["tests.conftest", "singer_state"],
    "t": ["tests.typings", "FlextTapLdifTestTypes"],
    "test_discover_streams": ["tests.test_tap", "test_discover_streams"],
    "u": ["tests.utilities", "FlextTapLdifTestUtilities"],
    "utf16_ldif_file": ["tests.conftest", "utf16_ldif_file"],
    "x": ["flext_tests", "x"],
}

__all__ = [
    "FlextTapLdifTestConstants",
    "FlextTapLdifTestModels",
    "FlextTapLdifTestProtocols",
    "FlextTapLdifTestTypes",
    "FlextTapLdifTestUtilities",
    "MockLDIFParser",
    "MockLDIFTap",
    "basic_tap_config",
    "benchmark_config",
    "binary_ldif_content",
    "binary_ldif_file",
    "c",
    "changes_tap_config",
    "d",
    "directory_tap_config",
    "docker_control",
    "e",
    "filtered_tap_config",
    "h",
    "invalid_ldif_content",
    "invalid_ldif_file",
    "large_ldif_file",
    "ldif_directory",
    "m",
    "mock_ldif_parser",
    "mock_ldif_tap",
    "p",
    "performance_tap_config",
    "pytest_configure",
    "r",
    "s",
    "sample_ldif_changes",
    "sample_ldif_changes_file",
    "sample_ldif_content",
    "sample_ldif_file",
    "set_test_environment",
    "shared_ldap_container",
    "singer_catalog_config",
    "singer_state",
    "t",
    "test_discover_streams",
    "u",
    "utf16_ldif_file",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
