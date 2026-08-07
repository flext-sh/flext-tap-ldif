# AGENTS.md — flext-tap-ldif

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_tap_ldif` · deps: `flext-core`, `flext-ldif`, `flext-meltano`, `flext-observability`

## Overview

Singer **tap** (extractor) for LDIF-format data. Thin driver over `flext-meltano` (ADR-006), delegating parsing to `flext-ldif`.

## Structure

```text
src/flext_tap_ldif/
├── tap.py            # FlextTapLdif(m.Meltano.SingerTapBase) — discover_streams() → EntriesStream
├── api.py cli.py     # FlextTapLdifService(FlextMeltanoTapServiceBase)
├── _utilities/       # entries_stream.py, processor.py, state_management.py (LDIF processing)
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _models/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextTapLdif` | class | `tap.py` | `m.Meltano.SingerTapBase`; `discover_streams()` → `EntriesStream` |
| `FlextTapLdifService` | class | `api.py` | `FlextMeltanoTapServiceBase` |

## Anti-Patterns / Gotchas

- The **active** entrypoint is `tap.py` (not a `.bak`). LDIF parsing is delegated to `flext-ldif`'s registry.

## Conventions (specific to this package)

- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Commands

```bash
make check PROJECT=flext-tap-ldif
make test  PROJECT=flext-tap-ldif       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
