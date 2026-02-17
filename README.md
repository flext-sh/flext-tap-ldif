# FLEXT-Tap-LDIF

[![Singer SDK](https://img.shields.io/badge/singer--sdk-compliant-brightgreen.svg)](https://sdk.meltano.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-Tap-LDIF** extracts directory data directly from LDIF files. It enables batch ingestion of directory exports into modern data pipelines, parsing both regular entries and operational attributes.

Part of the [FLEXT](https://github.com/flext-sh/flext) ecosystem.

## 🚀 Key Features

- **File Handling**: Supports single files, directories, and glob patterns (`*.ldif`).
- **Parsing Logic**: Built on `flext-ldif` for robust parsing of varied schemas (Active Directory, OpenLDAP, etc.).
- **Filtering**: Selectively extract entries by `base_dn`, `objectClass`, or specific attributes.
- **Batching**: Memory-efficient batch processing for large export files (>1GB).
- **Error Tolerance**: Configurable strict/lenient modes for handling malformed entries.

## 📦 Installation

To usage in your Meltano project, add the extractor to your `meltano.yml`:

```yaml
plugins:
  extractors:
    - name: tap-ldif
      pip_url: flext-tap-ldif
      config:
        file_path: /data/exports/*.ldif
        batch_size: 2000
```

## 🛠️ Usage

### Basic Extraction

Extract data from a local LDIF file using a simple configuration:

```json
{
  "file_path": "./users_export.ldif",
  "encoding": "utf-8",
  "strict_parsing": false
}
```

Run discovery to generate a schema:

```bash
tap-ldif --config config.json --discover > catalog.json
```

### Advanced Filtering

Limit extraction to specific sub-trees or object types:

```json
{
  "directory_path": "/exports/daily/",
  "file_pattern": "users_*.ldif",
  "base_dn_filter": "ou=people,dc=example,dc=com",
  "object_class_filter": ["inetOrgPerson"],
  "attribute_filter": ["cn", "mail", "uid"]
}
```

## 🏗️ Architecture

The tap acts as a bridge between static files and streaming pipelines:

- **Stream Logic**: Represents all entries as a unified stream with `dn` as primary key.
- **Infrastructure**: Wraps `flext-ldif` capabilities for validation and parsing.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new parsing rules or enhancing test coverage.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
