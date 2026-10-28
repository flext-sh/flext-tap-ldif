"""LDIF extract service — the record fetcher for the tap-ldif Singer streams.

Implements ``p.Meltano.RecordFetcher`` by discovering LDIF files and parsing them
through the injected flext-ldif facade (``self.ldif``). Records are packed into
the typed ``m.Meltano.FetchResult`` transport via railroad result operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from flext_tap_ldif import c, m, p, r, s, t, u


class FlextTapLdifExtractService(s):
    """Thin orchestrator: discover, parse, and pack LDIF records."""

    def fetch(self, request: m.Meltano.FetchRequest) -> p.Result[m.Meltano.FetchResult]:
        """Return the records for ``request.stream_name`` as a typed result.

        Args:
            request: Fetch request naming the stream and carrying the tap config.

        Returns:
            The resulting ``p.Result[m.Meltano.FetchResult]``.

        """
        config_map = dict(request.config)
        return (
            u.TapLdif
            .resolve_files(config_map)
            .flat_map(lambda files: self._parse_files(files, config_map))
            .map(lambda records: m.Meltano.FetchResult(records=tuple(records)))
        )

    def _parse_files(
        self,
        files: Sequence[Path],
        config_map: t.JsonMapping,
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Parse LDIF files and pack into Singer records.

        Args:
            files: Discovered LDIF file paths.
            config_map: Tap configuration mapping.

        Returns:
            The resulting ``p.Result[Sequence[t.JsonMapping]]``.

        """
        encoding_raw = config_map.get("encoding", c.DEFAULT_ENCODING)
        encoding = encoding_raw if isinstance(encoding_raw, str) else c.DEFAULT_ENCODING
        all_records: list[t.JsonMapping] = []

        for file_path in files:
            read_res = self._read_and_parse(file_path, encoding)
            if read_res.failure:
                return r[Sequence[t.JsonMapping]].from_failure(read_res)
            all_records.extend(read_res.value)

        return r[Sequence[t.JsonMapping]].ok(all_records)

    def _read_and_parse(
        self,
        file_path: Path,
        encoding: str,
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Read and parse one LDIF file into Singer records.

        Args:
            file_path: Source LDIF file path.
            encoding: Text encoding to use.

        Returns:
            The resulting ``p.Result[Sequence[t.JsonMapping]]``.

        """
        try:
            content = file_path.read_text(encoding=encoding)
        except OSError as exc:
            return r[Sequence[t.JsonMapping]].fail(
                f"Failed to read LDIF file {file_path}: {exc}",
            )

        parse_result = self.ldif.parse_ldif(content)
        if parse_result.failure:
            return r[Sequence[t.JsonMapping]].from_failure(parse_result)

        records: list[t.JsonMapping] = [
            u.TapLdif.pack_entry(
                m.Ldif.Entry.model_validate(raw_entry),
                file_path,
            )
            for raw_entry in parse_result.value.entries
        ]
        return r[Sequence[t.JsonMapping]].ok(records)


__all__: list[str] = ["FlextTapLdifExtractService"]
