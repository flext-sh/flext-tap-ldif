"""Protocols for flext-tap-ldif to avoid circular dependencies.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol


class TapConfigProtocol(Protocol):
    """Protocol for tap configuration interface."""

    def get(self, key: str, default: object = None) -> object:
        """Get configuration value by key.

        Args:
            key: Configuration key.
            default: Default value if key not found.

        Returns:
            Configuration value or default.

        """
        ...

    def __getitem__(self, key: str) -> object:
        """Get configuration value by key using dict-like access.

        Args:
            key: Configuration key.

        Returns:
            Configuration value.

        """
        ...

    def __iter__(self) -> object:
        """Iterate over configuration keys.

        Returns:
            Iterator over configuration keys.

        """
        ...


class TapProtocol(Protocol):
    """Protocol for tap interface used by streams.

    Defines the minimal interface that streams need from tap instances,
    avoiding circular dependencies without using TYPE_CHECKING.
    """

    @property
    def config(self) -> TapConfigProtocol:
        """Get tap configuration.

        Returns:
            Tap configuration object.

        """
        ...
