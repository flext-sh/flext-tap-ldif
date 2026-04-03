# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_tap_ldif import (
        conftest,
        constants,
        models,
        protocols,
        test_tap,
        typings,
        utilities,
    )
    from flext_tap_ldif.conftest import (
        additional_content,
        basic_tap_config,
        benchmark_config,
        binary_ldif_content,
        binary_ldif_file,
        changes_tap_config,
        directory_tap_config,
        docker_control,
        encoding,
        filtered_tap_config,
        invalid_ldif_content,
        invalid_ldif_file,
        large_ldif_file,
        ldif_dir,
        ldif_directory,
        mock_ldif_parser,
        mock_ldif_tap,
        performance_tap_config,
        sample_ldif_changes,
        sample_ldif_changes_file,
        sample_ldif_content,
        sample_ldif_file,
        set_test_environment,
        shared_ldap_container,
        singer_catalog_config,
        singer_state,
        utf16_ldif_file,
        written,
    )
    from flext_tap_ldif.constants import (
        FlextTapLdifTestConstants,
        FlextTapLdifTestConstants as c,
    )
    from flext_tap_ldif.models import (
        FlextTapLdifTestModels,
        FlextTapLdifTestModels as m,
    )
    from flext_tap_ldif.protocols import (
        FlextTapLdifTestProtocols,
        FlextTapLdifTestProtocols as p,
    )
    from flext_tap_ldif.test_tap import test_discover_streams
    from flext_tap_ldif.typings import FlextTapLdifTestTypes, FlextTapLdifTestTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifTestUtilities,
        FlextTapLdifTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTapLdifTestConstants": "flext_tap_ldif.constants",
    "FlextTapLdifTestModels": "flext_tap_ldif.models",
    "FlextTapLdifTestProtocols": "flext_tap_ldif.protocols",
    "FlextTapLdifTestTypes": "flext_tap_ldif.typings",
    "FlextTapLdifTestUtilities": "flext_tap_ldif.utilities",
    "additional_content": "flext_tap_ldif.conftest",
    "basic_tap_config": "flext_tap_ldif.conftest",
    "benchmark_config": "flext_tap_ldif.conftest",
    "binary_ldif_content": "flext_tap_ldif.conftest",
    "binary_ldif_file": "flext_tap_ldif.conftest",
    "c": ("flext_tap_ldif.constants", "FlextTapLdifTestConstants"),
    "changes_tap_config": "flext_tap_ldif.conftest",
    "conftest": "flext_tap_ldif.conftest",
    "constants": "flext_tap_ldif.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "directory_tap_config": "flext_tap_ldif.conftest",
    "docker_control": "flext_tap_ldif.conftest",
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "encoding": "flext_tap_ldif.conftest",
    "filtered_tap_config": "flext_tap_ldif.conftest",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "invalid_ldif_content": "flext_tap_ldif.conftest",
    "invalid_ldif_file": "flext_tap_ldif.conftest",
    "large_ldif_file": "flext_tap_ldif.conftest",
    "ldif_dir": "flext_tap_ldif.conftest",
    "ldif_directory": "flext_tap_ldif.conftest",
    "m": ("flext_tap_ldif.models", "FlextTapLdifTestModels"),
    "mock_ldif_parser": "flext_tap_ldif.conftest",
    "mock_ldif_tap": "flext_tap_ldif.conftest",
    "models": "flext_tap_ldif.models",
    "p": ("flext_tap_ldif.protocols", "FlextTapLdifTestProtocols"),
    "performance_tap_config": "flext_tap_ldif.conftest",
    "protocols": "flext_tap_ldif.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "sample_ldif_changes": "flext_tap_ldif.conftest",
    "sample_ldif_changes_file": "flext_tap_ldif.conftest",
    "sample_ldif_content": "flext_tap_ldif.conftest",
    "sample_ldif_file": "flext_tap_ldif.conftest",
    "set_test_environment": "flext_tap_ldif.conftest",
    "shared_ldap_container": "flext_tap_ldif.conftest",
    "singer_catalog_config": "flext_tap_ldif.conftest",
    "singer_state": "flext_tap_ldif.conftest",
    "t": ("flext_tap_ldif.typings", "FlextTapLdifTestTypes"),
    "test_discover_streams": "flext_tap_ldif.test_tap",
    "test_tap": "flext_tap_ldif.test_tap",
    "typings": "flext_tap_ldif.typings",
    "u": ("flext_tap_ldif.utilities", "FlextTapLdifTestUtilities"),
    "utf16_ldif_file": "flext_tap_ldif.conftest",
    "utilities": "flext_tap_ldif.utilities",
    "written": "flext_tap_ldif.conftest",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
