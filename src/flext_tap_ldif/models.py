"""Module docstring."""

from __future__ import annotations

import os
from pathlib import Path

"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from flext_core import FlextModels


class FlextTapLdifModels(FlextModels):
    """Models for LDIF tap operations.

    Extends FlextModels to avoid duplication and ensure consistency.
    All LDIF tap models benefit from FlextModels patterns.
    """

    LdifRecord = dict["str", "object"]
    LdifRecords = list[LdifRecord]


import pathlib

from flext_core import FlextResult, FlextUtilities


class FlextTapLdifUtilities(FlextUtilities):
    """Unified LDIF tap utilities extending FlextUtilities.

    Provides comprehensive utilities for LDIF Singer tap operations including:
    - LDIF file validation and format checking
    - Singer tap configuration generation for LDIF processing
    - LDIF-to-Singer schema mapping and transformation
    - File size and encoding validation
    - Performance optimization for LDIF extraction operations
    - Error handling and recovery mechanisms for LDIF processing
    """

    class _LdifFileHelper:
        """Helper for LDIF file validation and management."""

        @staticmethod
        def validate_ldif_file_accessibility(file_path: str) -> FlextResult[dict]:
            """Validate LDIF file accessibility, size, and basic format."""
            if not isinstance(file_path, str) or not file_path.strip():
                return FlextResult[dict].fail(
                    "LDIF file path must be a non-empty string"
                )

            file_path_obj = Path(file_path)

            # Check file existence
            if not file_path_obj.exists():
                return FlextResult[dict].fail(f"LDIF file does not exist: {file_path}")

            # Check if it's a file (not directory)
            if not file_path_obj.is_file():
                return FlextResult[dict].fail(f"Path is not a file: {file_path}")

            # Check file readability
            if not os.access(file_path, os.R_OK):
                return FlextResult[dict].fail(f"LDIF file is not readable: {file_path}")

            try:
                # Get file stats
                file_stats = file_path_obj.stat()
                file_size_bytes = file_stats.st_size
                file_size_mb = file_size_bytes / (1024 * 1024)

                # Check if file is empty
                if file_size_bytes == 0:
                    return FlextResult[dict].fail(f"LDIF file is empty: {file_path}")

                # Basic format validation - check for LDIF characteristics
                format_validation = (
                    FlextTapLdifUtilities._LdifFileHelper._validate_basic_ldif_format(
                        file_path
                    )
                )
                if format_validation.is_failure:
                    return FlextResult[dict].fail(
                        f"LDIF format validation failed: {format_validation.error}"
                    )

                file_info = {
                    "file_path": str(file_path_obj.resolve()),
                    "file_size_bytes": file_size_bytes,
                    "file_size_mb": round(file_size_mb, 2),
                    "is_accessible": True,
                    "format_valid": True,
                    "modified_time": file_stats.st_mtime,
                }

                # Add warnings for large files
                if file_size_mb > 100:
                    file_info["warning"] = (
                        f"Large LDIF file detected ({file_size_mb:.1f}MB). Consider batch processing."
                    )
                elif file_size_mb > 500:
                    file_info["warning"] = (
                        f"Very large LDIF file detected ({file_size_mb:.1f}MB). Processing may be slow."
                    )

                return FlextResult[dict].ok(file_info)

            except OSError as e:
                return FlextResult[dict].fail(
                    f"Error accessing LDIF file {file_path}: {e}"
                )

        @staticmethod
        def _validate_basic_ldif_format(file_path: str) -> FlextResult[bool]:
            """Perform basic LDIF format validation by checking file content."""
            try:
                with pathlib.Path(file_path).open(
                    encoding="utf-8", errors="ignore"
                ) as f:
                    # Read first few lines to check LDIF characteristics
                    lines_checked = 0
                    has_dn_line = False

                    for line in f:
                        lines_checked += 1
                        line = line.strip()

                        # Skip empty lines and comments
                        if not line or line.startswith("#"):
                            continue

                        # Look for DN line (required in LDIF)
                        if line.lower().startswith("dn:"):
                            has_dn_line = True

                        # Look for attribute lines (name: value)
                        if ":" in line and not line.startswith("dn:"):
                            pass

                        # Check enough lines to validate format
                        if lines_checked > 50 and has_dn_line:
                            break

                        # Avoid reading entire large files
                        if lines_checked > 100:
                            break

                    if not has_dn_line:
                        return FlextResult[bool].fail(
                            "No valid DN entries found in LDIF file"
                        )

                    return FlextResult[bool].ok(True)

            except UnicodeDecodeError:
                # Try with different encoding
                try:
                    with pathlib.Path(file_path).open(encoding="iso-8859-1") as f:
                        # Basic check with fallback encoding
                        content_sample = f.read(1024)
                        if "dn:" in content_sample.lower():
                            return FlextResult[bool].ok(True)
                        return FlextResult[bool].fail(
                            "No DN entries found with fallback encoding"
                        )
                except Exception as e:
                    return FlextResult[bool].fail(
                        f"Encoding error reading LDIF file: {e}"
                    )

            except Exception as e:
                return FlextResult[bool].fail(f"Error validating LDIF format: {e}")

        @staticmethod
        def detect_ldif_encoding(file_path: str) -> FlextResult[str]:
            """Detect the encoding of an LDIF file."""
            import chardet

            try:
                # Read a sample of the file for encoding detection
                with pathlib.Path(file_path).open("rb") as f:
                    raw_data = f.read(
                        min(32768, pathlib.Path(file_path).stat().st_size)
                    )  # Read up to 32KB

                # Use chardet to detect encoding
                encoding_result = chardet.detect(raw_data)
                detected_encoding = encoding_result.get("encoding")
                confidence = encoding_result.get("confidence", 0)

                if detected_encoding and confidence > 0.7:
                    # Validate detected encoding by trying to read the file
                    try:
                        with pathlib.Path(file_path).open(
                            encoding=detected_encoding
                        ) as f:
                            f.read(1024)  # Try to read some content
                        return FlextResult[str].ok(detected_encoding)
                    except UnicodeDecodeError:
                        pass

                # Fallback to common encodings
                for encoding in ["utf-8", "iso-8859-1", "cp1252", "utf-16"]:
                    try:
                        with pathlib.Path(file_path).open(encoding=encoding) as f:
                            f.read(1024)  # Try to read some content
                        return FlextResult[str].ok(encoding)
                    except UnicodeDecodeError:
                        continue

                return FlextResult[str].fail(
                    "Could not detect valid encoding for LDIF file"
                )

            except Exception as e:
                return FlextResult[str].fail(f"Error detecting LDIF encoding: {e}")

    class _SingerLdifConfigHelper:
        """Helper for Singer tap configuration generation for LDIF processing."""

        @staticmethod
        def generate_ldif_singer_catalog(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Generate Singer catalog for LDIF tap with proper schema definitions."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            if not isinstance(config, dict):
                return FlextResult[dict].fail("Configuration must be a dictionary")

            # Analyze sample LDIF files for schema discovery
            schema_analysis = (
                FlextTapLdifUtilities._SingerLdifConfigHelper._analyze_ldif_schema(
                    file_paths[:3], config
                )
            )
            if schema_analysis.is_failure:
                return FlextResult[dict].fail(
                    f"Schema analysis failed: {schema_analysis.error}"
                )

            schema_info = schema_analysis.unwrap()

            # Generate Singer catalog stream
            catalog_stream = {
                "tap_stream_id": "ldif_entries",
                "stream": "ldif_entries",
                "schema": {
                    "type": "object",
                    "properties": {
                        "dn": {
                            "type": "string",
                            "description": "Distinguished Name (primary key)",
                        },
                        "objectClass": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "LDAP object classes",
                        },
                        "_ldif_file_path": {
                            "type": "string",
                            "description": "Source LDIF file path",
                        },
                        "_ldif_processing_timestamp": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Processing timestamp",
                        },
                    },
                    "required": ["dn"],
                    "additionalProperties": True,
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "replication-method": "FULL_TABLE",
                            "inclusion": "available",
                            "selected": True,
                            "forced-replication-method": "FULL_TABLE",
                        },
                    }
                ],
            }

            # Add discovered attributes to schema
            for attr_name, attr_info in schema_info.get(
                "discovered_attributes", {}
            ).items():
                if attr_name not in catalog_stream["schema"]["properties"]:
                    catalog_stream["schema"]["properties"][attr_name] = {
                        "type": attr_info.get("type", "string"),
                        "description": f"LDIF attribute: {attr_name}",
                    }

            catalog = {"version": 1, "streams": [catalog_stream]}

            return FlextResult[dict].ok(catalog)

        @staticmethod
        def _analyze_ldif_schema(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Analyze LDIF files to discover schema information."""
            discovered_attributes = {}
            total_entries = 0
            object_classes = set()

            for file_path in file_paths:
                try:
                    # Detect encoding
                    encoding_result = (
                        FlextTapLdifUtilities._LdifFileHelper.detect_ldif_encoding(
                            file_path
                        )
                    )
                    encoding = (
                        encoding_result.unwrap()
                        if encoding_result.is_success
                        else "utf-8"
                    )

                    entries_analyzed = 0
                    with pathlib.Path(file_path).open(
                        encoding=encoding, errors="ignore"
                    ) as f:
                        current_entry = {}
                        current_attr = None

                        for line in f:
                            line = line.rstrip("\n\r")

                            # Skip comments and empty lines
                            if not line or line.startswith("#"):
                                continue

                            # Handle continuation lines
                            if line.startswith(" ") and current_attr:
                                current_entry[current_attr] = (
                                    current_entry.get(current_attr, "") + line[1:]
                                )
                                continue

                            # Parse attribute lines
                            if ":" in line:
                                attr_name, attr_value = line.split(":", 1)
                                attr_name = attr_name.strip()
                                attr_value = attr_value.strip()

                                if attr_name.lower() == "dn":
                                    # Process previous entry if exists
                                    if current_entry:
                                        FlextTapLdifUtilities._SingerLdifConfigHelper._process_entry_for_schema(
                                            current_entry,
                                            discovered_attributes,
                                            object_classes,
                                        )
                                        total_entries += 1

                                    # Start new entry
                                    current_entry = {"dn": attr_value}
                                    current_attr = "dn"
                                else:
                                    # Add attribute to current entry
                                    if attr_name in current_entry:
                                        # Convert to list if multiple values
                                        if not isinstance(
                                            current_entry[attr_name], list
                                        ):
                                            current_entry[attr_name] = [
                                                current_entry[attr_name]
                                            ]
                                        current_entry[attr_name].append(attr_value)
                                    else:
                                        current_entry[attr_name] = attr_value
                                    current_attr = attr_name

                            entries_analyzed += 1
                            # Limit analysis to avoid performance issues
                            if entries_analyzed > 1000:
                                break

                        # Process last entry
                        if current_entry:
                            FlextTapLdifUtilities._SingerLdifConfigHelper._process_entry_for_schema(
                                current_entry, discovered_attributes, object_classes
                            )
                            total_entries += 1

                except Exception:
                    continue  # Skip problematic files

            schema_info = {
                "discovered_attributes": discovered_attributes,
                "object_classes": list(object_classes),
                "total_entries_analyzed": total_entries,
                "files_analyzed": len(file_paths),
            }

            return FlextResult[dict].ok(schema_info)

        @staticmethod
        def _process_entry_for_schema(
            entry: dict, discovered_attributes: dict, object_classes: set
        ) -> None:
            """Process an LDIF entry to extract schema information."""
            for attr_name, attr_value in entry.items():
                if attr_name.lower() == "objectclass":
                    # Handle objectClass specially
                    if isinstance(attr_value, list):
                        object_classes.update(attr_value)
                    else:
                        object_classes.add(attr_value)

                # Track attribute types
                if attr_name not in discovered_attributes:
                    discovered_attributes[attr_name] = {
                        "type": "array" if isinstance(attr_value, list) else "string",
                        "count": 1,
                    }
                else:
                    discovered_attributes[attr_name]["count"] += 1

        @staticmethod
        def validate_ldif_tap_config(tap_config: dict) -> FlextResult[dict]:
            """Validate Singer tap configuration for LDIF processing."""
            if not isinstance(tap_config, dict):
                return FlextResult[dict].fail("LDIF tap config must be a dictionary")

            # Validate file path configuration (one of these must be specified)
            file_path = tap_config.get("file_path")
            directory_path = tap_config.get("directory_path")
            file_pattern = tap_config.get("file_pattern")

            file_config_count = sum(
                1 for path in [file_path, directory_path, file_pattern] if path
            )
            if file_config_count == 0:
                return FlextResult[dict].fail(
                    "Must specify one of: file_path, directory_path+file_pattern, or file_pattern"
                )

            # Validate file paths exist
            if file_path:
                validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if validation.is_failure:
                    return FlextResult[dict].fail(
                        f"File validation failed: {validation.error}"
                    )

            if directory_path:
                from pathlib import Path

                dir_path = Path(directory_path)
                if not dir_path.exists() or not dir_path.is_dir():
                    return FlextResult[dict].fail(
                        f"Directory does not exist: {directory_path}"
                    )

            # Validate processing configuration
            batch_size = tap_config.get("batch_size", 1000)
            if not isinstance(batch_size, int) or batch_size < 1 or batch_size > 10000:
                return FlextResult[dict].fail(
                    "batch_size must be an integer between 1 and 10000"
                )

            max_file_size_mb = tap_config.get("max_file_size_mb", 100)
            if (
                not isinstance(max_file_size_mb, int)
                or max_file_size_mb < 1
                or max_file_size_mb > 1000
            ):
                return FlextResult[dict].fail(
                    "max_file_size_mb must be an integer between 1 and 1000"
                )

            # Validate encoding
            encoding = tap_config.get("encoding", "utf-8")
            if not isinstance(encoding, str):
                return FlextResult[dict].fail("encoding must be a string")

            return FlextResult[dict].ok(tap_config)

    class _LdifProcessingHelper:
        """Helper for LDIF processing optimization and error handling."""

        @staticmethod
        def estimate_processing_performance(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Estimate LDIF processing performance and resource requirements."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            total_size_mb = 0
            total_files = len(file_paths)
            file_analysis = []

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    file_info = file_validation.unwrap()
                    total_size_mb += file_info["file_size_mb"]
                    file_analysis.append({
                        "file_path": file_path,
                        "size_mb": file_info["file_size_mb"],
                        "processable": True,
                    })
                else:
                    file_analysis.append({
                        "file_path": file_path,
                        "size_mb": 0,
                        "processable": False,
                        "error": file_validation.error,
                    })

            # Performance estimation
            batch_size = config.get("batch_size", 1000)
            entries_per_mb = 1000  # Rough estimate
            estimated_entries = total_size_mb * entries_per_mb
            estimated_batches = max(1, int(estimated_entries / batch_size))

            # Processing time estimation (entries per second)
            processing_rate = 500  # Conservative estimate
            estimated_processing_seconds = estimated_entries / processing_rate
            estimated_processing_minutes = estimated_processing_seconds / 60

            # Memory estimation
            entry_memory_kb = 2  # Rough estimate per entry
            batch_memory_mb = (batch_size * entry_memory_kb) / 1024
            total_memory_estimate_mb = batch_memory_mb * 1.5  # Safety factor

            performance_estimate = {
                "total_files": total_files,
                "total_size_mb": round(total_size_mb, 2),
                "estimated_entries": int(estimated_entries),
                "estimated_batches": estimated_batches,
                "estimated_processing_seconds": round(estimated_processing_seconds, 1),
                "estimated_processing_minutes": round(estimated_processing_minutes, 1),
                "estimated_memory_mb": round(total_memory_estimate_mb, 1),
                "batch_size": batch_size,
                "processing_rate_eps": processing_rate,
                "file_analysis": file_analysis,
                "performance_warnings": [],
            }

            # Add performance warnings
            if total_size_mb > 500:
                performance_estimate["performance_warnings"].append(
                    f"Large dataset ({total_size_mb:.1f}MB) may require significant processing time"
                )

            if estimated_processing_minutes > 60:
                performance_estimate["performance_warnings"].append(
                    f"Estimated processing time ({estimated_processing_minutes:.1f} minutes) is substantial"
                )

            if total_memory_estimate_mb > 500:
                performance_estimate["performance_warnings"].append(
                    f"Estimated memory usage ({total_memory_estimate_mb:.1f}MB) is high"
                )

            return FlextResult[dict].ok(performance_estimate)

        @staticmethod
        def optimize_batch_size_for_files(
            file_paths: list[str], target_memory_mb: int = 50
        ) -> FlextResult[dict]:
            """Optimize batch size based on file characteristics and memory constraints."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            if (
                not isinstance(target_memory_mb, int)
                or target_memory_mb < 10
                or target_memory_mb > 1000
            ):
                return FlextResult[dict].fail(
                    "target_memory_mb must be between 10 and 1000"
                )

            total_size_mb = 0
            largest_file_mb = 0

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    file_info = file_validation.unwrap()
                    file_size = file_info["file_size_mb"]
                    total_size_mb += file_size
                    largest_file_mb = max(largest_file_mb, file_size)

            # Calculate optimal batch size
            # Assumption: 1MB of LDIF ≈ 1000 entries, 2KB memory per entry
            entries_per_mb = 1000
            memory_per_entry_kb = 2

            # Target memory in KB
            target_memory_kb = target_memory_mb * 1024

            # Calculate batch size to stay within memory target
            optimal_batch_size = int(target_memory_kb / memory_per_entry_kb)

            # Apply constraints
            min_batch_size = 100
            max_batch_size = 10000

            optimal_batch_size = max(
                min_batch_size, min(max_batch_size, optimal_batch_size)
            )

            # Performance analysis
            total_entries_estimate = total_size_mb * entries_per_mb
            total_batches = max(1, int(total_entries_estimate / optimal_batch_size))
            actual_memory_mb = (optimal_batch_size * memory_per_entry_kb) / 1024

            optimization_result = {
                "optimal_batch_size": optimal_batch_size,
                "target_memory_mb": target_memory_mb,
                "actual_memory_mb": round(actual_memory_mb, 1),
                "total_files": len(file_paths),
                "total_size_mb": round(total_size_mb, 2),
                "largest_file_mb": round(largest_file_mb, 2),
                "estimated_total_entries": int(total_entries_estimate),
                "estimated_total_batches": total_batches,
                "optimization_factors": {
                    "memory_constraint": f"{target_memory_mb}MB memory limit",
                    "file_size_influence": f"Largest file: {largest_file_mb:.1f}MB",
                    "batch_size_range": f"{min_batch_size}-{max_batch_size}",
                },
            }

            return FlextResult[dict].ok(optimization_result)

        @staticmethod
        def generate_error_recovery_config(file_paths: list[str]) -> FlextResult[dict]:
            """Generate error recovery configuration based on file analysis."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            problematic_files = []
            total_files = len(file_paths)
            accessible_files = 0

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    accessible_files += 1
                else:
                    problematic_files.append({
                        "file_path": file_path,
                        "error": file_validation.error,
                    })

            # Determine recovery strategy
            if len(problematic_files) == 0:
                recovery_strategy = "strict"
                recommended_config = {
                    "strict_parsing": True,
                    "fail_on_first_error": True,
                    "max_errors_per_file": 0,
                }
            elif (
                len(problematic_files) / total_files < 0.1
            ):  # Less than 10% problematic
                recovery_strategy = "lenient"
                recommended_config = {
                    "strict_parsing": False,
                    "fail_on_first_error": False,
                    "max_errors_per_file": 10,
                    "skip_malformed_entries": True,
                }
            else:  # Many problematic files
                recovery_strategy = "diagnostic"
                recommended_config = {
                    "strict_parsing": False,
                    "fail_on_first_error": False,
                    "max_errors_per_file": 100,
                    "skip_malformed_entries": True,
                    "detailed_error_logging": True,
                }

            recovery_config = {
                "recovery_strategy": recovery_strategy,
                "total_files": total_files,
                "accessible_files": accessible_files,
                "problematic_files_count": len(problematic_files),
                "problematic_files": problematic_files,
                "recommended_config": recommended_config,
                "error_analysis": {
                    "file_access_issues": len(problematic_files),
                    "recovery_approach": recovery_strategy,
                    "risk_level": "low"
                    if len(problematic_files) == 0
                    else "medium"
                    if len(problematic_files) / total_files < 0.1
                    else "high",
                },
            }

            return FlextResult[dict].ok(recovery_config)


# Public API exports following FLEXT standardized patterns
__all__ = [
    "FlextTapLdifModels",  # Unified models class
    "FlextTapLdifUtilities",  # Standardized [Project]Utilities pattern
]
