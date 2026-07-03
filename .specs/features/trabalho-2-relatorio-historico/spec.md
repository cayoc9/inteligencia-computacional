# Trabalho 2: Relatorio Historico Canonico

## Problem Statement

O Trabalho 2 ja tem duas trilhas tecnicas materializadas:

1. `projeto_2_neuro_fuzzy/` como baseline SEER corrigido;
2. `projeto_2_neuro_fuzzy_metabric_clinico/` como evolucao canonica v2.

O problema agora nao e mais tecnico-operacional. O desafio passa a ser consolidar um **relatorio historico canonico** que explique, de forma coerente e defensavel:

- o que foi feito;
- por que foi feito;
- o que foi descartado;
- quais resultados valem de fato;
- quais trade-offs existem;
- como apresentar isso em banca, artigo e audio para o grupo.

Esse relatorio precisa ser construído com **subetapas iterativas de revisao critica**, simulando as perguntas, objecoes e buracos que uma professora de Inteligencia Computacional provavelmente apontaria em cada fase.

## Goals

- [x] Definir a feature canonica do relatorio historico do Trabalho 2.
- [x] Estruturar o processo em etapas TLC com revisoes iterativas professorais dentro de cada etapa.
- [x] Garantir que a narrativa final una SEER v1 e METABRIC v2 sem misturar baseline corrigido com evolucao canonica.
- [x] Planejar saídas reutilizaveis para apresentacao, artigo LaTeX e audio de repasse.
- [x] Tornar explicitos os checkpoints de lacunas metodologicas, inconsistencias narrativas e perguntas de banca.
- [x] Incluir sessoes de agentes como fonte complementar de processo, sem competir com os artefatos canonicos do repositorio.

## Out of Scope

| Feature | Reason |
|---|---|
| Redigir o artigo LaTeX completo nesta feature | Esta feature prepara a base canonica para ele. |
| Gerar slides finais nesta etapa | A estrutura de conteudo vira insumo para slides depois. |
| Reexecutar pipelines inteiros sem necessidade | O foco agora e consolidacao historica e narrativa defensavel. |

## User Stories

### P1: Consolidar a Historia Tecnica do Projeto 2

**User Story**: Como integrante do grupo, quero um relatorio historico unico para entender a linha do tempo completa do projeto e conseguir explicar a evolucao do trabalho.

**Acceptance Criteria**:

1. WHEN o relatorio historico for lido THEN ele SHALL distinguir claramente SEER v1 corrigido de METABRIC v2 canonico.
2. WHEN a linha do tempo for apresentada THEN ela SHALL mostrar decisoes, correcoes metodologicas, troca de dataset, resultados e pendencias residuais.
3. WHEN um leitor nao participou do desenvolvimento THEN ele SHALL conseguir entender o racional das principais mudancas.

### P1: Aplicar Revisao Professorial em Cada Etapa

**User Story**: Como autor do trabalho, quero validar cada etapa contra perguntas que uma professora de Inteligencia Computacional faria para reduzir buracos antes da apresentacao.

**Acceptance Criteria**:

1. WHEN uma etapa for concluida THEN ela SHALL passar por um checkpoint iterativo de perguntas criticas.
2. WHEN houver gap narrativo ou metodologico THEN ele SHALL ser registrado como ajuste antes de fechar a etapa.
3. WHEN a etapa for aprovada THEN o documento SHALL registrar as perguntas respondidas e os riscos remanescentes.

### P1: Produzir Base Reutilizavel para Tres Canais

**User Story**: Como mantenedor do trabalho, quero que o mesmo nucleo historico sirva de base para apresentacao, artigo em LaTeX e audio de repasse.

**Acceptance Criteria**:

1. WHEN o plano for fechado THEN ele SHALL prever secao-matriz para apresentacao oral.
2. WHEN o plano for fechado THEN ele SHALL prever secao-matriz para artigo em LaTeX.
3. WHEN o plano for fechado THEN ele SHALL prever roteiro-base para audio de onboarding do grupo.

### P1: Incorporar Fontes de Processo dos Agentes

**User Story**: Como autor do trabalho, quero incorporar as sessoes de agentes que conduziram parte do processo para que o relatorio historico capture tambem o racional operacional e as bifurcacoes da execucao.

**Acceptance Criteria**:

1. WHEN a coleta de fontes for executada THEN ela SHALL distinguir fonte canonica de entrega, fonte de processo dos agentes e fonte interpretativa.
2. WHEN sessoes de agentes forem usadas THEN o documento SHALL registrar os IDs e o papel analitico de cada sessao.
3. WHEN houver conflito entre fala de agente e artefato do projeto THEN os artefatos canonicos do repositorio SHALL prevalecer como fonte final de verdade.
4. WHEN a analise historica for escrita THEN ela SHALL considerar pelo menos as sessoes Codex `019f2525-5a79-7723-b4eb-8759cc32ce9f`, `019f255f-88a8-7a81-b002-957841c02760` e Antigravity `cd405d9c-1645-4090-8ada-150e8f2aea59`.

## Requirement Traceability

| Requirement ID | Story | Status |
|---|---|---|
| RHC-01 | Historia tecnica consolidada | Completed |
| RHC-02 | Revisao professorial iterativa | Completed |
| RHC-03 | Base reutilizavel multi-canal | Completed |
| RHC-04 | Fontes de processo dos agentes incorporadas | Completed |

## Success Criteria

- [x] Existe feature TLC para o relatorio historico.
- [x] O processo contem subetapas iterativas de revisao critica por etapa.
- [x] O plano distingue entrega historica, apresentacao, artigo e audio.
- [x] As perguntas de banca foram promovidas a gate explicito do processo.
- [x] A feature registra um mapa de fontes com sessoes de agentes como evidencias complementares de processo.
- [x] O relatorio tecnico final consolidado foi materializado fora da feature em `reports/consolidados/`.
- [x] O pacote NotebookLM com fontes e prompts numerados foi gerado.
- [x] O template inicial do artigo foi adaptado a partir de `projeto_sleep_health_rf_vs_rn/docs/template/Sleep_Health/`.

## Closing Status

Esta feature passou do estado de planejamento para estado de consolidacao executada.

Ela agora cobre:

- historia tecnica consolidada;
- checkpoints professorais;
- base para apresentacao;
- base para artigo;
- base para audio;
- mapeamento de fontes canonicas e fontes de processo;
- transicao da trilha SEER corrigida para a trilha canonica METABRIC.

Os gaps restantes deixaram de ser de definicao e passaram a ser de fechamento final de entrega:

1. revisar autores e referencias bibliograficas reais do artigo;
2. compilar o LaTeX no Overleaf ou ambiente com `pdflatex`;
3. acompanhar a conclusao dos audios do NotebookLM;
4. transformar a base documental em apresentacao final da equipe.
