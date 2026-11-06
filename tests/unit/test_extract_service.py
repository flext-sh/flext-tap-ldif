"""Behavioral tests for FlextTapLdifExtractService.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_tap_ldif.services.extract import FlextTapLdifExtractService
from tests import m, tm


class TestsFlextTapLdifExtractService:
    """Public-contract behavior for FlextTapLdifExtractService."""

    @staticmethod
    def test_fetch_extracts_ldif_records(tmp_path: Path) -> None:
        """Fetch extracts records from LDIF files into FetchResult."""
        service = FlextTapLdifExtractService()
        sample = tmp_path / "people.ldif"
        dn = "uid=jdoe,ou=people,dc=example,dc=com"
        content = (
            f"dn: {dn}\n"
            "objectClass: inetOrgPerson\n"
            "uid: jdoe\n"
            "cn: John Doe\n"
            "sn: Doe\n\n"
        )
        sample.write_text(content, encoding="utf-8")

        request = m.Meltano.FetchRequest(
            stream_name="ldif_entries",
            config={"file_path": str(sample)},
        )

        result = service.fetch(request)
        fetch_result = tm.ok(result)
        tm.that(len(fetch_result.records), eq=1)
        first = fetch_result.records[0]
        tm.that(first["dn"], eq=dn)
        tm.that(first["source_file"], eq=str(sample))

    @staticmethod
    def test_fetch_fails_when_file_not_found(tmp_path: Path) -> None:
        """Fetch returns a typed failure when LDIF file is missing."""
        service = FlextTapLdifExtractService()
        missing = tmp_path / "missing.ldif"
        request = m.Meltano.FetchRequest(
            stream_name="ldif_entries",
            config={"file_path": str(missing)},
        )

        result = service.fetch(request)
        tm.fail(result)


__all__: list[str] = ["TestsFlextTapLdifExtractService"]
