# Triagem SonarCloud — flext-sh/flext-tap-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.17`

## Resumo

**8 issues** — BLOCKER 0, CRITICAL 2, MAJOR 5, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 4 · **Debt total: 51min**

| regra | issues |
|---|---|
| `python:S3776` | 2 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S3358` | 1 |
| `python:S7504` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `python:S3776`
**Local**: `src/flext_tap_ldif/_utilities/data_processing.py:17` · **Effort**: 11min

> Refactor this function to reduce its Cognitive Complexity from 21 to the 15 allowed.

```python
       13      class LdifDataProcessing:
       14          """LDIF data processing utilities."""
       15  
       16          @staticmethod
>>>    17          def build_record_from_lines(
       18              entry_lines: t.StrSequence,
       19          ) -> t.MutableAttributeMapping:
       20              """Build record dict from LDIF lines."""
       21              record: t.MutableAttributeMapping = {}
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `python:S3776`
**Local**: `src/flext_tap_ldif/_utilities/entries_stream.py:33` · **Effort**: 10min

> Refactor this function to reduce its Cognitive Complexity from 20 to the 15 allowed.

```python
       29              )
       30              self._tap: m.Meltano.SingerTapBase = tap
       31  
       32          @override
>>>    33          def get_records(
       34              self, context: t.JsonMapping | None = None
       35          ) -> Iterable[m.Meltano.SingerRecord]:
       36              """Return a generator of record-type dictionary objects."""
       37              _ = context
```

**Decisão**: pendente

### 3 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 4 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 5 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 6 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 7 · 🟡 MAJOR · CODE_SMELL · `python:S3358`
**Local**: `src/flext_tap_ldif/api.py:34` · **Effort**: 5min

> Extract this nested conditional expression into an independent statement.

```python
       30      ) -> p.Meltano.SingerTapInstance:
       31          """Create the internal tap runtime backed by Singer SDK."""
       32          raw_config = (
       33              t.json_dict_adapter().validate_python(
>>>    34                  settings.model_dump() if hasattr(settings, "model_dump") else settings
       35              )
       36              if settings is not None
       37              else None
       38          )
```

**Decisão**: pendente

### 8 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente
