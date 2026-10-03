"""CLI entrypoint for flext-tap-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_ldif import FlextTapLdifService, t


class FlextTapLdifCli:
    """Canonical CLI wrapper for tap-ldif service execution."""

    @classmethod
    def run(cls, args: t.StrSequence | None = None) -> int:
        """Run the tap entry point through the FLEXT service facade.

        Returns:
            The resulting ``int``.
        """
        _ = cls
        exit_code: int = FlextTapLdifService().cli_main(args)
        return exit_code


def main(args: t.StrSequence | None = None) -> int:
    """Run the canonical tap-ldif CLI.

    Returns:
        The resulting ``int``.
    """
    return FlextTapLdifCli.run(args)


__all__: list[str] = ["FlextTapLdifCli", "main"]
