"""FLEXT Tap LDIF Constants - LDIF tap extraction constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import ClassVar, Final

from flext_core import FlextConstants
from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants


class FlextTapLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF tap extraction-specific constants following flext-core patterns.

    Composes with FlextTapLdifConstants to avoid duplication and ensure consistency.
    """

    DEFAULT_LDIF_ENCODING: Final[str] = FlextLdifConstants.Ldif.DEFAULT_ENCODING
    SUPPORTED_ENCODINGS: ClassVar[frozenset[str]] = frozenset({
        FlextLdifConstants.Ldif.Encoding.UTF8,
        FlextLdifConstants.Ldif.Encoding.ASCII,
        FlextLdifConstants.Ldif.Encoding.LATIN1,
        FlextLdifConstants.Ldif.Encoding.UTF16,
    })
    MAX_BATCH_SIZE: Final[int] = FlextConstants.Performance.BatchProcessing.MAX_ITEMS
    MAX_FILE_SIZE_MB: Final[int] = 100
    LDIF_CHANGE_TYPES: ClassVar[list[str]] = [
        FlextLdifConstants.Ldif.EntryModification.ADD,
        FlextLdifConstants.Ldif.EntryModification.MODIFY,
        FlextLdifConstants.Ldif.EntryModification.DELETE,
        FlextLdifConstants.Ldif.EntryModification.MODRDN,
    ]

    class TapLdif:
        """LDIF tap processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        MIN_WORKERS_FOR_PARALLEL: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.MIN_WORKERS_FOR_PARALLEL
        )
        MAX_WORKERS_LIMIT: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.MAX_WORKERS_LIMIT
        )
        PERFORMANCE_MIN_CHUNK_SIZE: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.PERFORMANCE_MIN_CHUNK_SIZE
        )
        MIN_ENTRIES: Final[int] = FlextLdifConstants.Ldif.LdifProcessing.MIN_ENTRIES

    class Format:
        """LDIF format specifications."""

        DN_ATTRIBUTE: Final[str] = FlextLdifConstants.Ldif.Format.DN_ATTRIBUTE
        ATTRIBUTE_SEPARATOR: Final[str] = (
            FlextLdifConstants.Ldif.Format.ATTRIBUTE_SEPARATOR
        )
        MAX_LINE_LENGTH: Final[int] = FlextLdifConstants.Ldif.Format.MAX_LINE_LENGTH
        BASE64_PREFIX: Final[str] = FlextLdifConstants.Ldif.Format.BASE64_PREFIX
        COMMENT_PREFIX: Final[str] = FlextLdifConstants.Ldif.Format.COMMENT_PREFIX
        LINE_CONTINUATION: Final[str] = " "

    class TapLdifPerformance:
        """Tap LDIF performance constants."""

        DEFAULT_BATCH_SIZE: Final[int] = 1000

    class TapLdifValidation:
        """LDIF tap validation constants.

        Note: Does not override parent Validation class to avoid inheritance conflicts.
        """

        MIN_DN_COMPONENTS: Final[int] = (
            FlextLdifConstants.Ldif.LdifValidation.MIN_DN_COMPONENTS
        )
        MAX_DN_LENGTH: Final[int] = FlextLdifConstants.Ldif.LdifValidation.MAX_DN_LENGTH
        MAX_ATTRIBUTES_PER_ENTRY: Final[int] = (
            FlextLdifConstants.Ldif.LdifValidation.MAX_ATTRIBUTES_PER_ENTRY
        )

    class EntrySchema:
        """LDIF entry schema field names."""

        DN_FIELD: Final[str] = "dn"
        ATTRIBUTES_FIELD: Final[str] = "attributes"
        OBJECT_CLASS_FIELD: Final[str] = "object_class"
        CHANGE_TYPE_FIELD: Final[str] = "change_type"
        SOURCE_FILE_FIELD: Final[str] = "source_file"
        LINE_NUMBER_FIELD: Final[str] = "line_number"
        ENTRY_SIZE_FIELD: Final[str] = "entry_size"
        DEFAULT_CHANGE_TYPE: Final[str] = "None"
        DEFAULT_LINE_NUMBER: Final[int] = 0
        DEFAULT_ENTRY_SIZE: Final[int] = 0

    class SampleEntry:
        """Sample LDIF entry for fallback/testing."""

        DN: Final[str] = "cn=sample,dc=example,dc=com"
        ATTRIBUTES: Final[dict[str, list[str]]] = {"cn": ["sample"]}
        OBJECT_CLASS: Final[list[str]] = ["top"]
        SOURCE_FILE: Final[str] = "fp"

    @unique
    class ProjectType(StrEnum):
        LIBRARY = "library"
        APPLICATION = "application"
        SERVICE = "service"
        SINGER_TAP = "singer-tap"
        LDIF_EXTRACTOR = "ldif-extractor"
        DATA_EXTRACTOR = "data-extractor"
        SINGER_TAP_LDIF = "singer-tap-ldif"
        TAP_LDIF = "tap-ldif"
        LDIF_CONNECTOR = "ldif-connector"
        DATA_CONNECTOR = "data-connector"
        SINGER_PROTOCOL = "singer-protocol"
        LDIF_PROCESSOR = "ldif-processor"
        FILE_EXTRACTOR = "file-extractor"
        LDIF_PARSER = "ldif-parser"
        SINGER_STREAM = "singer-stream"
        ETL_TAP = "etl-tap"
        DATA_PIPELINE = "data-pipeline"
        LDIF_INTEGRATION = "ldif-integration"
        SINGER_INTEGRATION = "singer-integration"

    @unique
    class TestLdifFilePath(StrEnum):
        TMP_TEST_LDIF = "/tmp/test.ldif"
        TMP_SAMPLE_LDIF = "/tmp/sample.ldif"

    @unique
    class TestLdifEncoding(StrEnum):
        UTF_8 = "utf-8"
        ASCII = "ascii"
        ISO_8859_1 = "iso-8859-1"

    @unique
    class TestObjectClass(StrEnum):
        PERSON = "person"
        ORGANIZATION = "organization"
        GROUP_OF_NAMES = "groupOfNames"


c = FlextTapLdifConstants
__all__ = ["FlextTapLdifConstants", "c"]
