# AUTO-GENERATED FILE — Regenerate with: make gen
"""Package version and metadata for flext-tap-ldif.

Subclass of ``FlextVersion`` — overrides only ``_metadata``.
All derived attributes (``__version__``, ``__title__``, etc.) are
computed automatically via ``FlextVersion.__init_subclass__``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from importlib.metadata import PackageMetadata, metadata

from flext_core import FlextVersion


class FlextTapLdifVersion(FlextVersion):
    """flext-tap-ldif version — MRO-derived from FlextVersion."""

    _metadata: PackageMetadata = metadata("flext-tap-ldif")


__version__ = FlextTapLdifVersion.__version__
__version_info__ = FlextTapLdifVersion.__version_info__
__title__ = FlextTapLdifVersion.__title__
__description__ = FlextTapLdifVersion.__description__
__author__ = FlextTapLdifVersion.__author__
__author_email__ = FlextTapLdifVersion.__author_email__
__license__ = FlextTapLdifVersion.__license__
__url__ = FlextTapLdifVersion.__url__
__all__: list[str] = [
    "FlextTapLdifVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
