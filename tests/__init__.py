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

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests import (
        conftest as conftest,
        constants as constants,
        models as models,
        protocols as protocols,
        test_tap as test_tap,
        typings as typings,
        utilities as utilities,
    )
    from tests.conftest import (
        MockLDIFParser as MockLDIFParser,
        MockLDIFTap as MockLDIFTap,
        basic_tap_config as basic_tap_config,
        benchmark_config as benchmark_config,
        binary_ldif_content as binary_ldif_content,
        binary_ldif_file as binary_ldif_file,
        changes_tap_config as changes_tap_config,
        directory_tap_config as directory_tap_config,
        docker_control as docker_control,
        filtered_tap_config as filtered_tap_config,
        invalid_ldif_content as invalid_ldif_content,
        invalid_ldif_file as invalid_ldif_file,
        large_ldif_file as large_ldif_file,
        ldif_directory as ldif_directory,
        mock_ldif_parser as mock_ldif_parser,
        mock_ldif_tap as mock_ldif_tap,
        performance_tap_config as performance_tap_config,
        pytest_configure as pytest_configure,
        sample_ldif_changes as sample_ldif_changes,
        sample_ldif_changes_file as sample_ldif_changes_file,
        sample_ldif_content as sample_ldif_content,
        sample_ldif_file as sample_ldif_file,
        set_test_environment as set_test_environment,
        shared_ldap_container as shared_ldap_container,
        singer_catalog_config as singer_catalog_config,
        singer_state as singer_state,
        utf16_ldif_file as utf16_ldif_file,
    )
    from tests.constants import (
        FlextTapLdifTestConstants as FlextTapLdifTestConstants,
        FlextTapLdifTestConstants as c,
    )
    from tests.models import (
        FlextTapLdifTestModels as FlextTapLdifTestModels,
        FlextTapLdifTestModels as m,
    )
    from tests.protocols import (
        FlextTapLdifTestProtocols as FlextTapLdifTestProtocols,
        FlextTapLdifTestProtocols as p,
    )
    from tests.test_tap import test_discover_streams as test_discover_streams
    from tests.typings import (
        FlextTapLdifTestTypes as FlextTapLdifTestTypes,
        FlextTapLdifTestTypes as t,
    )
    from tests.utilities import (
        FlextTapLdifTestUtilities as FlextTapLdifTestUtilities,
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
    "conftest": ["tests.conftest", ""],
    "constants": ["tests.constants", ""],
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
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextTapLdifTestProtocols"],
    "performance_tap_config": ["tests.conftest", "performance_tap_config"],
    "protocols": ["tests.protocols", ""],
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
    "test_tap": ["tests.test_tap", ""],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextTapLdifTestUtilities"],
    "utf16_ldif_file": ["tests.conftest", "utf16_ldif_file"],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
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
    "conftest",
    "constants",
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
    "models",
    "p",
    "performance_tap_config",
    "protocols",
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
    "test_tap",
    "typings",
    "u",
    "utf16_ldif_file",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
