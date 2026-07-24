"""LDIF data processing utilities for the tap namespace."""

from __future__ import annotations

import base64

from flext_tap_ldif import c, p, r, t


class FlextTapLdifUtilitiesLdifDataProcessing:
    """MRO mixin exposing LdifDataProcessing under u.TapLdif."""

    class LdifDataProcessing:
        """LDIF data processing utilities."""

        @staticmethod
        def build_record_from_lines(
            entry_lines: t.StrSequence,
        ) -> t.MutableAttributeMapping:
            """Build record dict from LDIF lines."""
            record: t.MutableAttributeMapping = {}
            current_attr: str | None = None
            current_value: str = ""
            for line in (*entry_lines, ""):
                if line.startswith(c.TapLdif.Format.LINE_CONTINUATION):
                    if current_attr is not None:
                        current_value += line[1:]
                    continue
                if current_attr is not None and current_value:
                    normalized_attr = FlextTapLdifUtilitiesLdifDataProcessing.LdifDataProcessing.normalize_ldif_attribute_name(
                        current_attr
                    )
                    if normalized_attr in record:
                        existing_value = record[normalized_attr]
                        if isinstance(existing_value, list):
                            existing_value.append(current_value)
                        else:
                            record[normalized_attr] = [
                                str(existing_value),
                                current_value,
                            ]
                    else:
                        record[normalized_attr] = current_value
                parse_result = FlextTapLdifUtilitiesLdifDataProcessing.LdifDataProcessing.parse_ldif_line(
                    line
                )
                if parse_result.success:
                    a, v = parse_result.value
                    current_attr = a
                    current_value = v
                else:
                    current_attr = None
                    current_value = ""
            return record

        @staticmethod
        def convert_ldif_entry_to_record(
            entry_lines: t.StrSequence,
        ) -> p.Result[t.AttributeMapping]:
            """Convert LDIF entry lines to Singer record."""
            try:
                record = FlextTapLdifUtilitiesLdifDataProcessing.LdifDataProcessing.build_record_from_lines(
                    entry_lines
                )
                out: t.AttributeMapping = record
                return r[t.AttributeMapping].ok(out)
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                return r[t.AttributeMapping].fail(f"Error converting LDIF entry: {e}")

        @staticmethod
        def normalize_ldif_attribute_name(attr_name: str) -> str:
            """Normalize LDIF attribute name for JSON schema."""
            if not attr_name:
                return ""
            normalized: str = c.TapLdif.ATTRIBUTE_NORMALIZE_RE.sub(
                "_", attr_name.lower()
            )
            if normalized and normalized[0].isdigit():
                normalized = f"attr_{normalized}"
            return normalized

        @staticmethod
        def parse_ldif_line(line: str) -> p.Result[t.StrPair]:
            """Parse LDIF attribute line."""
            line = line.strip()
            if not line or line.startswith("#"):
                return r[t.StrPair].fail("Empty or comment line")
            if ":" not in line:
                return r[t.StrPair].fail("Invalid LDIF line format")
            if "::" in line:
                attr_name, encoded_value = line.split("::", 1)
                try:
                    decoded_value = base64.b64decode(encoded_value.strip()).decode(
                        c.DEFAULT_ENCODING
                    )
                    return r[t.StrPair].ok((attr_name.strip(), decoded_value))
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[t.StrPair].fail(f"Base64 decode error: {e}")
            if ":<" in line:
                attr_name, url_value = line.split(":<", 1)
                return r[t.StrPair].ok((attr_name.strip(), f"URL:{url_value.strip()}"))
            attr_name, value = line.split(":", 1)
            return r[t.StrPair].ok((attr_name.strip(), value.strip()))
