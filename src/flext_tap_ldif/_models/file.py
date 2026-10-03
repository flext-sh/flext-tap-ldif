"""File and stream models for LDIF tap.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_ldif._models.file_metadata import FlextTapLdifModelsLdifFile
from flext_tap_ldif._models.file_stream import FlextTapLdifModelsFileStream


class FlextTapLdifModelsFile(
    FlextTapLdifModelsLdifFile,
    FlextTapLdifModelsFileStream.FlextTapLdifModelsLdifStream,
):
    """MRO mixin: LdifFile and LdifStream models."""
