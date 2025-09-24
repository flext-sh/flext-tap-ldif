"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import importlib.metadata

# flext-core imports
from flext_core import FlextLogger, FlextModels, FlextResult

# flext-core imports
# === FLEXT-MELTANO COMPLETE INTEGRATION ===
# Re-export ALL flext-meltano facilities for full ecosystem integration
from flext_meltano import (
    # Bridge integration
    FlextMeltanoBridge,
    # Configuration and validation
    FlextMeltanoConfig,
    # Enterprise services
    FlextMeltanoService,
    # Typing definitions
    FlextMeltanoTypes,
)

# Legacy imports for backward compatibility - maintain ALL existing imports
from flext_tap_ldif.config import TapLDIFConfig, TapLDIFConfig as LegacyTapLDIFConfig
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
from flext_tap_ldif.streams import LDIFEntriesStream

# === PEP8 REORGANIZATION: Import from new structure ===
from flext_tap_ldif.tap import TapLDIF, TapLDIF as LegacyTapLDIF

# Enterprise-grade aliases for backward compatibility
FlextTapLDIF = TapLDIF
FlextTapLDIFConfig = TapLDIFConfig
LDIFTap = TapLDIF
TapConfig = TapLDIFConfig

# Version following semantic versioning
try:
    __version__ = importlib.metadata.version("flext-tap-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0-enterprise"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Complete public API exports
__all__: list[str] = [
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
    "FlextTapLdifConfigurationError",
    "FlextTapLdifError",
    "FlextTapLdifFileError",
    "FlextTapLdifParseError",
    "FlextTapLdifProcessingError",
    "FlextTapLdifStreamError",
    "FlextTapLdifValidationError",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LegacyTapLDIF",
    "LegacyTapLDIFConfig",
    "__version__",
    "__version_info__",
]
