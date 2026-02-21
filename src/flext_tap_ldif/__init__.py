"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextLogger, FlextModels, FlextResult

from flext_tap_ldif.__version__ import __version__, __version_info__
from flext_tap_ldif.ldif_processor import (
    FlextLdifProcessor,
    FlextLdifProcessorWrapper,
    LDIFProcessor,
)
from flext_tap_ldif.models import FlextMeltanoTapLdifModels, m, m_tap_ldif
from flext_tap_ldif.protocols import FlextMeltanoTapLdifProtocols
from flext_tap_ldif.settings import (
    FlextMeltanoTapLdifSettings,
    FlextMeltanoTapLdifSettings as FlextMeltanoTapLDIFSettings,
    FlextMeltanoTapLdifSettings as TapConfig,
    FlextMeltanoTapLdifSettings as TapLDIFConfig,
)
from flext_tap_ldif.streams import LDIFEntriesStream
from flext_tap_ldif.tap import (
    TapLDIF,
    TapLDIF as FlextMeltanoTapLDIF,
    TapLDIF as LDIFTap,
    TapLDIF as LegacyTapLDIF,
)
from flext_tap_ldif.typings import t
from flext_tap_ldif.utilities import FlextMeltanoTapLdifUtilities

__all__ = [
    "FlextLdifProcessor",
    "FlextLdifProcessorWrapper",
    "FlextLogger",
    "FlextMeltanoTapLDIF",
    "FlextMeltanoTapLDIFSettings",
    "FlextMeltanoTapLdifModels",
    "FlextMeltanoTapLdifProtocols",
    "FlextMeltanoTapLdifSettings",
    "FlextMeltanoTapLdifUtilities",
    "FlextModels",
    "FlextResult",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LDIFTap",
    "LegacyTapLDIF",
    "TapConfig",
    "TapLDIF",
    "TapLDIFConfig",
    "__version__",
    "__version_info__",
    "m",
    "m_tap_ldif",
    "t",
]
