# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Test module for flext-tap-ldif.

This module provides test infrastructure for flext-tap-ldif with subnamespaces .Tests
following FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from .conftest import (
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
    from .constants import TestsFlextTapLdifConstants, TestsFlextTapLdifConstants as c
    from .models import TestsFlextTapLdifModels, TestsFlextTapLdifModels as m
    from .protocols import TestsFlextTapLdifProtocols, TestsFlextTapLdifProtocols as p
    from .test_tap import test_discover_streams
    from .typings import TestsFlextTapLdifTypes, TestsFlextTapLdifTypes as t, tt
    from .utilities import TestsFlextTapLdifUtilities, TestsFlextTapLdifUtilities as u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "MockLDIFParser": ("tests.conftest", "MockLDIFParser"),
    "MockLDIFTap": ("tests.conftest", "MockLDIFTap"),
    "TestsFlextTapLdifConstants": ("tests.constants", "TestsFlextTapLdifConstants"),
    "TestsFlextTapLdifModels": ("tests.models", "TestsFlextTapLdifModels"),
    "TestsFlextTapLdifProtocols": ("tests.protocols", "TestsFlextTapLdifProtocols"),
    "TestsFlextTapLdifTypes": ("tests.typings", "TestsFlextTapLdifTypes"),
    "TestsFlextTapLdifUtilities": ("tests.utilities", "TestsFlextTapLdifUtilities"),
    "basic_tap_config": ("tests.conftest", "basic_tap_config"),
    "benchmark_config": ("tests.conftest", "benchmark_config"),
    "binary_ldif_content": ("tests.conftest", "binary_ldif_content"),
    "binary_ldif_file": ("tests.conftest", "binary_ldif_file"),
    "c": ("tests.constants", "TestsFlextTapLdifConstants"),
    "changes_tap_config": ("tests.conftest", "changes_tap_config"),
    "directory_tap_config": ("tests.conftest", "directory_tap_config"),
    "docker_control": ("tests.conftest", "docker_control"),
    "filtered_tap_config": ("tests.conftest", "filtered_tap_config"),
    "invalid_ldif_content": ("tests.conftest", "invalid_ldif_content"),
    "invalid_ldif_file": ("tests.conftest", "invalid_ldif_file"),
    "large_ldif_file": ("tests.conftest", "large_ldif_file"),
    "ldif_directory": ("tests.conftest", "ldif_directory"),
    "m": ("tests.models", "TestsFlextTapLdifModels"),
    "mock_ldif_parser": ("tests.conftest", "mock_ldif_parser"),
    "mock_ldif_tap": ("tests.conftest", "mock_ldif_tap"),
    "p": ("tests.protocols", "TestsFlextTapLdifProtocols"),
    "performance_tap_config": ("tests.conftest", "performance_tap_config"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "sample_ldif_changes": ("tests.conftest", "sample_ldif_changes"),
    "sample_ldif_changes_file": ("tests.conftest", "sample_ldif_changes_file"),
    "sample_ldif_content": ("tests.conftest", "sample_ldif_content"),
    "sample_ldif_file": ("tests.conftest", "sample_ldif_file"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "shared_ldap_container": ("tests.conftest", "shared_ldap_container"),
    "singer_catalog_config": ("tests.conftest", "singer_catalog_config"),
    "singer_state": ("tests.conftest", "singer_state"),
    "t": ("tests.typings", "TestsFlextTapLdifTypes"),
    "test_discover_streams": ("tests.test_tap", "test_discover_streams"),
    "tt": ("tests.typings", "tt"),
    "u": ("tests.utilities", "TestsFlextTapLdifUtilities"),
    "utf16_ldif_file": ("tests.conftest", "utf16_ldif_file"),
}

__all__ = [
    "MockLDIFParser",
    "MockLDIFTap",
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "basic_tap_config",
    "benchmark_config",
    "binary_ldif_content",
    "binary_ldif_file",
    "c",
    "changes_tap_config",
    "directory_tap_config",
    "docker_control",
    "filtered_tap_config",
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
    "tt",
    "u",
    "utf16_ldif_file",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
