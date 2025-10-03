"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core.metadata import build_metadata_exports

globals().update(build_metadata_exports(__file__))
import importlib.metadata

from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextMeltanoService,
    FlextMeltanoTypes,
)

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_tap_ldif.config import FlextTapLdifConfig
from flext_tap_ldif.exceptions import (
    FlextTapLdifConfigurationError,
    FlextTapLdifError,
    FlextTapLdifFileError,
    FlextTapLdifParseError,
    FlextTapLdifProcessingError,
    FlextTapLdifStreamError,
    FlextTapLdifValidationError,
)
from flext_tap_ldif.ldif_processor import (
    FlextLdifProcessor,
    FlextLdifProcessorWrapper,
    LDIFProcessor,
)
from flext_tap_ldif.models import FlextTapLdifModels
from flext_tap_ldif.protocols import FlextTapLdifProtocols
from flext_tap_ldif.streams import LDIFEntriesStream
from flext_tap_ldif.tap import TapLDIF, TapLDIF as LegacyTapLDIF
from flext_tap_ldif.utilities import FlextTapLdifUtilities

FlextTapLDIF = TapLDIF
TapLDIFConfig = FlextTapLdifConfig
FlextTapLDIFConfig = FlextTapLdifConfig
LDIFTap = TapLDIF
TapConfig = FlextTapLdifConfig

try:
    __version__ = importlib.metadata.version("flext-tap-ldif")
    __version_info__: tuple[int | str, ...] = VERSION.version_info
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0-enterprise"


__all__: FlextTypes.StringList = [
    "FlextLdifProcessor",
    "FlextLdifProcessorWrapper",
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoService",
    "FlextMeltanoTypes",
    "FlextModels",
    "FlextResult",
    "FlextTapLDIF",
    "FlextTapLdifConfig",
    "FlextTapLdifConfigurationError",
    "FlextTapLdifError",
    "FlextTapLdifFileError",
    "FlextTapLdifModels",
    "FlextTapLdifParseError",
    "FlextTapLdifProcessingError",
    "FlextTapLdifProtocols",
    "FlextTapLdifStreamError",
    "FlextTapLdifUtilities",
    "FlextTapLdifValidationError",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LegacyTapLDIF",
    "TapLDIFConfig",
    "__version__",
    "__version_info__",
]
