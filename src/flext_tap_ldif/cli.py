"""CLI entrypoint for flext-tap-ldif."""

from __future__ import annotations

from flext_tap_ldif import FlextTapLdifService, t


class FlextTapLdifCli:
    """Canonical CLI wrapper for tap-ldif service execution."""

    @classmethod
    def run(cls, args: t.StrSequence | None = None) -> int:
        """Run the tap entry point through the FLEXT service facade."""
        _ = cls
        return FlextTapLdifService().cli_main(args)


def main(args: t.StrSequence | None = None) -> int:
    """Run the canonical tap-ldif CLI."""
    return FlextTapLdifCli.run(args)


__all__: list[str] = ["FlextTapLdifCli", "main"]
