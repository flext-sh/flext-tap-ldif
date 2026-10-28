"""CLI entrypoint for flext-tap-ldif.

Dispatches the flat Singer CLI through FlextTapLdifService.cli_main, the
meltano.Tap-provided entry point of the tap service facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_ldif import t, tap_ldif


class FlextTapLdifCli:
    """Canonical CLI wrapper for tap-ldif service execution."""

    @classmethod
    def run(cls, args: t.StrSequence | None = None) -> int:
        """Run the tap entry point through the FLEXT service facade.

        Args:
            args: Optional CLI arguments; None delegates argv handling to
                the Singer CLI.

        Returns:
            The resulting int.

        """
        _ = cls
        exit_code: int = tap_ldif.cli_main(args)  # pyright: ignore[reportUnknownMemberType]
        return exit_code


def main(args: t.StrSequence | None = None) -> int:
    """Run the canonical tap-ldif CLI.

    Args:
        args: Optional CLI arguments; None delegates argv handling to the
            Singer CLI.

    Returns:
        The resulting int.

    """
    return FlextTapLdifCli.run(args)


if __name__ == "__main__":
    raise SystemExit(main())

__all__: list[str] = ["FlextTapLdifCli", "main"]
