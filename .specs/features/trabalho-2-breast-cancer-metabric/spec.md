# Trabalho 2: Evolucao Clinica METABRIC do Projeto 2

## Problem Statement

A trilha original do Projeto 2 em `projeto_2_neuro_fuzzy/` corrigiu o pipeline SEER e resolveu problemas metodologicos importantes: saneamento, EDA, politica de vazamento, split treino/validacao/teste, ensemble sem contaminar o teste, explicabilidade e estabilidade minima.

Mesmo assim, a base SEER continua limitada para a pergunta academica e clinica do trabalho. Ela tem menos profundidade biologica, nao traz biomarcadores moleculares essenciais e responde melhor como baseline educacional corrigido do que como melhor base para melhoria de desempenho.

Por isso, a evolucao natural do Projeto 2 passa a ser o fork clinico `projeto_2_neuro_fuzzy_metabric_clinico/`, agora tratado como feature canonica da fase v2. O objetivo deixa de ser apenas "consertar o SEER" e passa a ser "evoluir o experimento para uma base real mais rica, mantendo a mesma disciplina metodologica".

## Goals

- [x] Registrar a evolucao METABRIC como continuacao canonica do Projeto 2 v1, sem apagar a rastreabilidade do SEER.
- [x] Formalizar que o SEER permanece baseline educacional corrigido e o METABRIC vira trilha principal de melhoria continua.
- [x] Garantir no METABRIC o mesmo nivel de completude metodologica da trilha SEER: saneamento, dicionario, EDA, modelagem, ensemble corrigido, explicabilidade, calibracao, estabilidade e notebook.
- [x] Documentar por que o dataset METABRIC e mais adequado ao caso do que o dataset SEER original.
- [x] Validar explicitamente a aplicacao de boas praticas de ciencia de dados na trilha v2.
- [x] Deixar a trilha pronta para alimentar relatorio historico, apresentacao, artigo em LaTeX e audio de repasse ao grupo.

## Out of Scope

| Feature | Reason |
|---|---|
| Substituir silenciosamente o SEER | O SEER continua importante como baseline corrigido e evidencia de evolucao metodologica. |
| Validacao clinica externa prospectiva | O projeto continua academico e baseado em dataset publico. |
| Survival analysis formal | A base tem `overall_survival_months`, mas o pipeline atual continua enquadrado como classificacao supervisionada. |
| Explicabilidade local por paciente | Seria uma extensao util, mas nao bloqueia a completude atual da trilha. |

## User Stories

### P1: Definir a Fonte Canonica da v2

**User Story**: Como mantenedor do trabalho, quero que a evolucao METABRIC tenha spec propria para que a v2 tenha fonte canonica, em vez de existir apenas como pasta paralela.

**Acceptance Criteria**:

1. WHEN a documentacao do projeto for lida THEN ela SHALL distinguir `trabalho-2-breast-cancer/` como baseline corrigido v1 e `trabalho-2-breast-cancer-metabric/` como evolucao canonica v2.
2. WHEN o estado global do repositorio for consultado THEN `ROADMAP.md`, `STATE.md` e `STATUS.md` SHALL registrar essa hierarquia.
3. WHEN a trilha v2 for descrita THEN ela SHALL referenciar explicitamente a v1 como predecessor metodologico.

### P1: Completar Paridade Metodologica entre SEER e METABRIC

**User Story**: Como avaliador, quero que a trilha METABRIC tenha o mesmo rigor da trilha SEER para que a comparacao entre datasets nao seja injusta.

**Acceptance Criteria**:

1. WHEN a trilha METABRIC for executada THEN ela SHALL conter scripts `01` a `07`, notebook proprio, README, data dictionary e relatorio tecnico.
2. WHEN o ensemble METABRIC for reportado THEN pesos e threshold SHALL vir da validacao e o teste SHALL permanecer intocado.
3. WHEN a trilha METABRIC for validada THEN `pytest`, `run_pipeline.py` e `nbconvert` SHALL concluir sem erro.
4. WHEN a trilha METABRIC for comparada com a SEER THEN a documentacao SHALL mostrar equivalencia de fases de completude.

### P1: Justificar a Escolha do Novo Dataset

**User Story**: Como autor do trabalho, quero demonstrar por que o METABRIC e melhor para esse caso do que o dataset anterior.

**Acceptance Criteria**:

1. WHEN o dataset for descrito THEN a documentacao SHALL citar tratamento, biomarcadores, PAM50, NPI e mutation count como ganhos de informacao.
2. WHEN o dataset anterior for comparado THEN a documentacao SHALL explicar a limitacao do SEER para aprendizagem clinica mais profunda.
3. WHEN os resultados forem apresentados THEN o texto SHALL separar "dataset melhor" de "modelo melhor", sem atribuir toda melhora apenas ao algoritmo.

### P1: Auditoria de Boas Praticas de Ciencia de Dados

**User Story**: Como revisor metodologico, quero uma auditoria objetiva das boas praticas aplicadas para saber se a trilha esta pronta para virar base de apresentacao e artigo.

**Acceptance Criteria**:

1. WHEN a auditoria for gerada THEN ela SHALL cobrir contrato de dados, EDA, leakage policy, split, metricas, threshold tuning, explicabilidade, calibracao, estabilidade, reprodutibilidade e documentacao.
2. WHEN uma pratica estiver apenas parcialmente coberta THEN a auditoria SHALL dizer isso explicitamente.
3. WHEN a auditoria concluir "pronto" THEN ela SHALL deixar pendencias residuais separadas do nucleo metodologico.

## Requirement Traceability

| Requirement ID | Story | Status |
|---|---|---|
| BCM-01 | Fonte canonica da v2 | Verified |
| BCM-02 | Paridade metodologica SEER vs METABRIC | Verified |
| BCM-03 | Justificativa do novo dataset | Verified |
| BCM-04 | Auditoria de boas praticas | Verified |

## Success Criteria

- [x] Existe feature TLC propria para a evolucao METABRIC.
- [x] `ROADMAP.md`, `STATE.md` e `STATUS.md` apontam a v2 como evolucao canonica do Projeto 2.
- [x] `projeto_2_neuro_fuzzy_metabric_clinico/` tem as mesmas fases essenciais de completude do SEER corrigido.
- [x] A validacao atual da v2 passou em testes, pipeline e notebook.
- [x] Existe auditoria consolidada de boas praticas de ciencia de dados para o Trabalho 2.
