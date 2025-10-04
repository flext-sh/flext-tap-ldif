"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import importlib.metadata

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

# Backward compatibility aliases
FlextTapLDIF = TapLDIF
TapLDIFConfig = FlextTapLdifConfig
FlextTapLDIFConfig = FlextTapLdifConfig
LDIFTap = TapLDIF
TapConfig = FlextTapLdifConfig

try:
    __version__ = importlib.metadata.version("flext-tap-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "FlextLdifProcessor",
    "FlextLdifProcessorWrapper",
    "FlextLogger",
    "FlextModels",
    "FlextResult",
    "FlextTapLDIF",
    "FlextTapLDIFConfig",
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
    "FlextTypes",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LDIFTap",
    "LegacyTapLDIF",
    "TapConfig",
    "TapLDIF",
    "TapLDIFConfig",
]
