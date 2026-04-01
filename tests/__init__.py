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
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests import (
        conftest,
        constants,
        models,
        protocols,
        test_tap,
        typings,
        utilities,
    )
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

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextTapLdifTestConstants": "tests.constants",
    "FlextTapLdifTestModels": "tests.models",
    "FlextTapLdifTestProtocols": "tests.protocols",
    "FlextTapLdifTestTypes": "tests.typings",
    "FlextTapLdifTestUtilities": "tests.utilities",
    "MockLDIFParser": "tests.conftest",
    "MockLDIFTap": "tests.conftest",
    "basic_tap_config": "tests.conftest",
    "benchmark_config": "tests.conftest",
    "binary_ldif_content": "tests.conftest",
    "binary_ldif_file": "tests.conftest",
    "c": ("tests.constants", "FlextTapLdifTestConstants"),
    "changes_tap_config": "tests.conftest",
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_tests",
    "directory_tap_config": "tests.conftest",
    "docker_control": "tests.conftest",
    "e": "flext_tests",
    "filtered_tap_config": "tests.conftest",
    "h": "flext_tests",
    "invalid_ldif_content": "tests.conftest",
    "invalid_ldif_file": "tests.conftest",
    "large_ldif_file": "tests.conftest",
    "ldif_directory": "tests.conftest",
    "m": ("tests.models", "FlextTapLdifTestModels"),
    "mock_ldif_parser": "tests.conftest",
    "mock_ldif_tap": "tests.conftest",
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTapLdifTestProtocols"),
    "performance_tap_config": "tests.conftest",
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_tests",
    "s": "flext_tests",
    "sample_ldif_changes": "tests.conftest",
    "sample_ldif_changes_file": "tests.conftest",
    "sample_ldif_content": "tests.conftest",
    "sample_ldif_file": "tests.conftest",
    "set_test_environment": "tests.conftest",
    "shared_ldap_container": "tests.conftest",
    "singer_catalog_config": "tests.conftest",
    "singer_state": "tests.conftest",
    "t": ("tests.typings", "FlextTapLdifTestTypes"),
    "test_discover_streams": "tests.test_tap",
    "test_tap": "tests.test_tap",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTapLdifTestUtilities"),
    "utf16_ldif_file": "tests.conftest",
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
