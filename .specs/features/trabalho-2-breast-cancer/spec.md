# Trabalho 2: Breast Cancer Survival Risk Specification

## Problem Statement

O Projeto 2 foi iniciado com scripts que treinam modelos sobre o dataset SEER Breast Cancer, mas ainda nao tem especificacao canonica, notebook narrativo, dicionario de dados, EDA completa de metadados/relações nem politica clara de vazamento. O baseline atual tambem usa `Survival Months` como feature para prever `Status`, o que mistura informacao posterior ao acompanhamento com uma pergunta de predicao em diagnostico.

Este trabalho corrige a trilha metodologica para que o projeto fique reprodutivel, auditavel e defensavel: primeiro especificacao e EDA, depois saneamento, engenharia de features, modelos tabulares, ensemble ponderado, threshold tuning e comparativo neuro-fuzzy.

## Goals

- [ ] Definir objetivo corrigido e objetivo historicamente testado, separando predicao em diagnostico de analise de acompanhamento.
- [ ] Criar um notebook Jupyter proprio do Projeto 2, mantendo a convencao "um notebook narrativo por projeto".
- [ ] Criar dicionario de dados especifico do `Breast_Cancer.csv`, incluindo significado, tipo bruto, tipo sanitizado, dominio, papel analitico e risco de vazamento.
- [ ] Implementar analise de metadados e relacoes como parte da EDA, nao como apendice posterior.
- [ ] Corrigir sanitizacao, features, modelagem e avaliacao para priorizar falsos negativos da classe `Dead`.
- [ ] Manter neuro-fuzzy como comparativo academico e nao como modelo campeao assumido.

## Out of Scope

| Feature | Reason |
|---|---|
| Validacao clinica real | O dataset e publico/educacional; nao ha revisao medica nem validacao prospectiva. |
| Predicao causal | O projeto mede associacoes preditivas, nao causalidade. |
| CNN para imagens | O dataset e tabular e nao contem imagens. |
| LSTM como modelo principal | O CSV nao tem sequencia temporal por paciente; LSTM so entraria se houver justificativa experimental separada. |
| Deploy de API/app | O objetivo e trabalho academico reprodutivel, nao produto em producao. |

---

## User Stories

### P1: Objetivo e Politica de Vazamento ⭐ MVP

**User Story**: Como autor do trabalho, quero distinguir claramente o objetivo corrigido do objetivo que foi testado antes para que o relatorio nao defenda um experimento contaminado por vazamento.

**Why P1**: Sem essa decisao, todo resultado posterior fica metodologicamente fragil.

**Acceptance Criteria**:

1. WHEN a especificacao for lida THEN ela SHALL declarar que `Status = Dead` e a classe positiva.
2. WHEN o pipeline principal montar `X` THEN ele SHALL excluir `Status` e `Survival Months`.
3. WHEN `Survival Months` for usado THEN o sistema SHALL marcar o experimento como analise de sensibilidade/vazamento, nao como resultado principal.
4. WHEN o relatorio final explicar a trilha anterior THEN ele SHALL dizer que o baseline anterior usava `Survival Months` e por isso respondia a outra pergunta.

**Independent Test**: Ler `.specs/features/trabalho-2-breast-cancer/spec.md` e executar teste unitario de `split_features_target(include_survival_months=False)`.

---

### P1: Sanitizacao e Contrato do Dataset ⭐ MVP

**User Story**: Como implementador, quero uma camada unica de sanitizacao para que EDA, notebook, modelos e relatorio usem os mesmos nomes, tipos e regras.

**Why P1**: O CSV tem nomes e valores inconsistentes (`T Stage `, `Reginol Node Positive`, `Single `, `Grade` textual), e repetir limpeza em scripts diferentes causa drift.

**Acceptance Criteria**:

1. WHEN o CSV bruto for carregado THEN o sistema SHALL preservar uma copia bruta para auditoria.
2. WHEN os dados forem sanitizados THEN colunas SHALL usar `snake_case`.
3. WHEN `Reginol Node Positive` for sanitizado THEN a coluna resultante SHALL ser `regional_node_positive`.
4. WHEN valores textuais forem sanitizados THEN espacos laterais SHALL ser removidos.
5. WHEN `Grade` for sanitizado THEN ele SHALL virar inteiro ordinal 1-4.
6. WHEN duplicatas existirem THEN elas SHALL ser reportadas e removidas no dataset analitico.

**Independent Test**: Executar `pytest projeto_2_neuro_fuzzy/tests/test_data_sanitization.py -q`.

---

### P1: Dicionario de Dados ⭐ MVP

**User Story**: Como leitor do relatorio, quero um dicionario de dados especifico do projeto para entender cada coluna, sua origem, seu papel e seu risco metodologico.

**Why P1**: O dicionario deveria orientar a EDA e a engenharia de features; sem ele, decisões como usar/remover `Survival Months` ficam implícitas.

**Acceptance Criteria**:

1. WHEN o dicionario for gerado THEN ele SHALL existir em `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md`.
2. WHEN o dicionario for gerado THEN ele SHALL conter todas as colunas brutas do CSV.
3. WHEN uma coluna for renomeada THEN o dicionario SHALL mostrar nome bruto e nome sanitizado.
4. WHEN uma coluna tiver risco de vazamento THEN o dicionario SHALL marcar esse risco explicitamente.
5. WHEN uma coluna for alvo, feature, metadado ou exclusao THEN o dicionario SHALL declarar seu papel analitico.
6. WHEN features derivadas forem criadas THEN o dicionario SHALL documentar formula, racional e dependencias.

**Independent Test**: Verificar que `DATA_DICTIONARY.md` contem `Survival Months`, `status`, `regional_node_positive`, `node_positive_ratio` e `risco de vazamento`.

---

### P1: EDA com Metadados e Relacoes ⭐ MVP

**User Story**: Como avaliador do trabalho, quero que a EDA inclua metadados, cardinalidade, dominios, distribuicoes, relacoes e suspeitas de vazamento para confiar na escolha dos modelos.

**Why P1**: O audio analisado recomendou EDA antes de escolher ferramentas; a EDA atual do Projeto 2 ainda nao existe como artefato versionado.

**Acceptance Criteria**:

1. WHEN a EDA rodar THEN ela SHALL gerar `metadata_profile.csv` com coluna, dtype bruto/sanitizado, nulos, unicos, exemplos e papel analitico.
2. WHEN a EDA rodar THEN ela SHALL gerar `categorical_relationships.csv` com relacoes entre categoricas e `Status`.
3. WHEN a EDA rodar THEN ela SHALL gerar `numeric_relationships.csv` com correlacoes/associacoes numericas com `Status`.
4. WHEN a EDA rodar THEN ela SHALL destacar a associacao de `Survival Months` com `Status` como possivel vazamento/follow-up.
5. WHEN a EDA rodar THEN ela SHALL gerar figuras para distribuicao do alvo, distribuicoes clinicas, relacoes por stage/nodos e matriz de correlacao.
6. WHEN o notebook for executado THEN ele SHALL exibir a analise de metadados antes da modelagem.

**Independent Test**: Executar `python projeto_2_neuro_fuzzy/02_eda.py` e confirmar arquivos em `projeto_2_neuro_fuzzy/reports/tables/` e `projeto_2_neuro_fuzzy/reports/figures/`.

---

### P1: Notebook Jupyter do Projeto 2 ⭐ MVP

**User Story**: Como aluno/apresentador, quero um notebook Jupyter proprio para o Projeto 2 para reunir narrativa, EDA, saneamento, modelos e conclusao em um artefato revisavel.

**Why P1**: O repositorio ja usa notebook consolidado para o Trabalho 1; o Projeto 2 deve manter a mesma convencao de um notebook por projeto.

**Acceptance Criteria**:

1. WHEN o Projeto 2 for executado THEN SHALL existir `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`.
2. WHEN o notebook for aberto THEN ele SHALL conter secoes de contexto, objetivo, dicionario de dados, metadados, EDA, sanitizacao, features, modelos, ensemble, neuro-fuzzy e conclusao.
3. WHEN scripts e notebook divergirem THEN os scripts SHALL ser fonte executavel e o notebook SHALL reutilizar as mesmas funcoes do pacote `breast_cancer_survival`.
4. WHEN o notebook for validado THEN `jupyter nbconvert --to notebook --execute` SHALL completar sem erro.

**Independent Test**: Executar `jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb`.

---

### P1: Modelagem Tabular e Ensemble Ponderado ⭐ MVP

**User Story**: Como responsavel pelo experimento, quero comparar modelos tabulares e ensemble ponderado para seguir a estrategia sugerida no audio e reduzir falsos negativos.

**Why P1**: O projeto atual testa RF, MLP e neuro-fuzzy, mas nao implementa ensemble nem avalia diretamente o risco clinico principal.

**Acceptance Criteria**:

1. WHEN modelos forem treinados THEN no minimo Logistic Regression, Random Forest, ExtraTrees, HistGradientBoosting, SVM calibrado e MLP SHALL ser comparados.
2. WHEN metricas forem calculadas THEN elas SHALL incluir accuracy, balanced accuracy, precision, recall, F1, F2, ROC AUC, PR AUC e falsos negativos.
3. WHEN threshold tuning rodar THEN ele SHALL gerar tabela de thresholds e selecionar criterio orientado a F2/recall/falsos negativos.
4. WHEN ensemble ponderado rodar THEN pesos SHALL derivar de desempenho de validacao, nao de escolha arbitraria.
5. WHEN o resultado for apresentado THEN acuracia SHALL nao ser criterio principal.

**Independent Test**: Executar `python projeto_2_neuro_fuzzy/03_train_models.py` e `python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py`.

---

### P2: Neuro-Fuzzy como Comparativo Academico

**User Story**: Como aluno da disciplina, quero manter o neuro-fuzzy no trabalho para dialogar com o tema de sistemas hibridos, mas comparado de forma justa.

**Why P2**: O tema academico importa, mas o modelo atual teve pior recall e mais falsos negativos.

**Acceptance Criteria**:

1. WHEN o neuro-fuzzy rodar THEN ele SHALL usar a mesma sanitizacao, mesmo split e mesmas metricas do pipeline principal.
2. WHEN o relatorio citar ANFIS THEN ele SHALL diferenciar ANFIS completo de fuzzificacao manual + MLP.
3. WHEN o neuro-fuzzy performar pior THEN o relatorio SHALL declarar isso, sem forcar conclusao favoravel.

**Independent Test**: Executar `python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py`.

---

### P2: Documentacao Viva e Status

**User Story**: Como mantenedor do repositorio, quero que `.specs/`, `STATUS.md` e README reflitam o estado real para continuar o projeto em outra sessao sem perder contexto.

**Why P2**: O usuario ja estabeleceu que docs/status fazem parte da entrega.

**Acceptance Criteria**:

1. WHEN a implementacao for concluida THEN `.specs/project/ROADMAP.md` SHALL marcar Trabalho 2 com status atualizado.
2. WHEN a implementacao for concluida THEN `.specs/project/STATE.md` SHALL registrar decisoes sobre objetivo, vazamento, notebook e metrica principal.
3. WHEN a implementacao for concluida THEN `.specs/codebase/STRUCTURE.md`, `TESTING.md` e `CONVENTIONS.md` SHALL mencionar o pipeline do Projeto 2.
4. WHEN o usuario consultar `STATUS.md` THEN ele SHALL enxergar Trabalho 1 e Trabalho 2 separados.

**Independent Test**: Ler os documentos e executar testes de presenca de strings essenciais.

---

## Edge Cases

- WHEN `Survival Months` tiver alto poder preditivo THEN o sistema SHALL tratar isso como evidencia de vazamento/follow-up, nao como feature campea.
- WHEN uma categoria rara existir THEN o preprocessor SHALL lidar com ela sem quebrar (`OneHotEncoder(handle_unknown="ignore")`).
- WHEN o dataset tiver duplicatas THEN o contrato SHALL reportar quantidade e o dataset analitico SHALL remover duplicatas.
- WHEN uma coluna numerica tiver distribuicao extrema THEN a EDA SHALL registrar outliers/quantis antes de feature engineering.
- WHEN o modelo com maior acuracia tiver muitos falsos negativos THEN ele SHALL nao ser automaticamente considerado melhor.
- WHEN notebook e scripts divergirem THEN a divergencia SHALL ser corrigida reutilizando funcoes comuns.

---

## Requirement Traceability

| Requirement ID | Story | Phase | Status |
|---|---|---|---|
| BC-01 | Objetivo e Politica de Vazamento | Design | Pending |
| BC-02 | Sanitizacao e Contrato do Dataset | Design | Pending |
| BC-03 | Dicionario de Dados | Design | Pending |
| BC-04 | EDA com Metadados e Relacoes | Design | Pending |
| BC-05 | Notebook Jupyter do Projeto 2 | Design | Pending |
| BC-06 | Modelagem Tabular e Ensemble Ponderado | Design | Pending |
| BC-07 | Neuro-Fuzzy como Comparativo Academico | Design | Pending |
| BC-08 | Documentacao Viva e Status | Design | Pending |

**Coverage:** 8 total, 8 mapped to design, 0 unmapped.

---

## Success Criteria

- [ ] `pytest -q` passa.
- [ ] `python projeto_2_neuro_fuzzy/run_pipeline.py` conclui.
- [ ] `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` existe e cobre colunas brutas, sanitizadas e derivadas.
- [ ] `projeto_2_neuro_fuzzy/reports/tables/metadata_profile.csv` existe.
- [ ] `projeto_2_neuro_fuzzy/reports/tables/categorical_relationships.csv` existe.
- [ ] `projeto_2_neuro_fuzzy/reports/tables/numeric_relationships.csv` existe.
- [ ] `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb` executa via `nbconvert`.
- [ ] Resultado principal exclui `Survival Months`.
- [ ] Relatorio final explica o objetivo testado antes e o objetivo corrigido.

