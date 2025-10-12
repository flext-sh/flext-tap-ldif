"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_tap_ldif.__version__ import __version__, __version_info__
from flext_tap_ldif.config import FlextMeltanoTapLdifConfig
from flext_tap_ldif.exceptions import (
    FlextMeltanoTapLdifConfigurationError,
    FlextMeltanoTapLdifError,
    FlextMeltanoTapLdifFileError,
    FlextMeltanoTapLdifParseError,
    FlextMeltanoTapLdifProcessingError,
    FlextMeltanoTapLdifStreamError,
    FlextMeltanoTapLdifValidationError,
)
from flext_tap_ldif.ldif_processor import (
    FlextLdifProcessor,
    FlextLdifProcessorWrapper,
    LDIFProcessor,
)
from flext_tap_ldif.models import FlextMeltanoTapLdifModels
from flext_tap_ldif.protocols import FlextMeltanoTapLdifProtocols
from flext_tap_ldif.streams import LDIFEntriesStream
from flext_tap_ldif.tap import TapLDIF, TapLDIF as LegacyTapLDIF
from flext_tap_ldif.utilities import FlextMeltanoTapLdifUtilities

# Backward compatibility aliases
FlextMeltanoTapLDIF = TapLDIF
TapLDIFConfig = FlextMeltanoTapLdifConfig
FlextMeltanoTapLDIFConfig = FlextMeltanoTapLdifConfig
LDIFTap = TapLDIF
TapConfig = FlextMeltanoTapLdifConfig

__all__ = [
    "FlextCore.Logger",
    "FlextCore.Models",
    "FlextCore.Result",
    "FlextCore.Types",
    "FlextLdifProcessor",
    "FlextLdifProcessorWrapper",
    "FlextMeltanoTapLDIF",
    "FlextMeltanoTapLDIFConfig",
    "FlextMeltanoTapLdifConfig",
    "FlextMeltanoTapLdifConfigurationError",
    "FlextMeltanoTapLdifError",
    "FlextMeltanoTapLdifFileError",
    "FlextMeltanoTapLdifModels",
    "FlextMeltanoTapLdifParseError",
    "FlextMeltanoTapLdifProcessingError",
    "FlextMeltanoTapLdifProtocols",
    "FlextMeltanoTapLdifStreamError",
    "FlextMeltanoTapLdifUtilities",
    "FlextMeltanoTapLdifValidationError",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LDIFTap",
    "LegacyTapLDIF",
    "TapConfig",
    "TapLDIF",
    "TapLDIFConfig",
    "__version__",
    "__version_info__",
]
