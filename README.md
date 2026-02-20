# FLEXT Tap LDIF

Singer Tap para extracao de dados a partir de arquivos LDIF.

Descricao oficial atual: "FLEXT Tap LDIF - Singer Tap for LDIF file format data extraction".

## O que este projeto entrega

- Converte conteudo LDIF em stream Singer.
- Padroniza estrutura de schema para pipeline.
- Permite ingestao de cargas historicas de diretorio.

## Contexto operacional

- Entrada: arquivos LDIF de origem.
- Saida: eventos Singer para persistencia/transformacao.
- Dependencias: flext-ldif e fluxo de orquestracao Singer.

## Estado atual e risco de adocao

- Qualidade: **Alpha**
- Uso recomendado: **Nao produtivo**
- Nivel de estabilidade: em maturacao funcional e tecnica, sujeito a mudancas de contrato sem garantia de retrocompatibilidade.

## Diretriz para uso nesta fase

Aplicar este projeto somente em desenvolvimento, prova de conceito e homologacao controlada, com expectativa de ajustes frequentes ate maturidade de release.
