# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
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

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextTapLdifTestConstants,
        FlextTapLdifTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import FlextTapLdifTestModels, FlextTapLdifTestModels as m

    protocols = _tests_protocols
    import tests.test_tap as _tests_test_tap
    from tests.protocols import (
        FlextTapLdifTestProtocols,
        FlextTapLdifTestProtocols as p,
    )

    test_tap = _tests_test_tap
    import tests.typings as _tests_typings
    from tests.test_tap import test_discover_streams

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import FlextTapLdifTestTypes, FlextTapLdifTestTypes as t

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextTapLdifTestUtilities,
        FlextTapLdifTestUtilities as u,
    )
_LAZY_IMPORTS = {
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
    "d": ("flext_core.decorators", "FlextDecorators"),
    "directory_tap_config": "tests.conftest",
    "docker_control": "tests.conftest",
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "filtered_tap_config": "tests.conftest",
    "h": ("flext_core.handlers", "FlextHandlers"),
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
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
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
    "x": ("flext_core.mixins", "FlextMixins"),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
