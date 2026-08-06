# Triagem SonarCloud — flext-sh/flext-tap-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.17`

## Resumo

**8 issues** — BLOCKER 0, CRITICAL 2, MAJOR 5, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 4

| regra | issues |
|---|---|
| `python:S3776` | 2 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S3358` | 1 |
| `python:S7504` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `python:S3776` | `src/flext_tap_ldif/_utilities/data_processing.py` | 17 | |
| 2 | CRITICAL | CODE_SMELL | `python:S3776` | `src/flext_tap_ldif/_utilities/entries_stream.py` | 33 | |
| 3 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 4 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 5 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 6 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 7 | MAJOR | CODE_SMELL | `python:S3358` | `src/flext_tap_ldif/api.py` | 34 | |
| 8 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-tap-ldif.json`

