# Trabalho 2: Breast Cancer Survival Risk Tasks

**Design**: `.specs/features/trabalho-2-breast-cancer/design.md`  
**Status**: Done

---

## Execution Plan

### Phase 1: Specification Foundation

```
T1 -> T2 -> T3
```

### Phase 2: Data Understanding

```
T3 -> T4 -> T5
```

### Phase 3: Modeling Core

```
T5 -> T6 -> T7 -> T8 -> T9
```

### Phase 4: Narrative and Project Sync

```
T9 -> T10 -> T11 -> T12
```

---

## Task Breakdown

### T1: Registrar spec TLC do Trabalho 2 ✅

**What**: Criar/atualizar `spec.md`, `design.md` e `tasks.md` com requisitos rastreaveis do Projeto 2.  
**Where**: `.specs/features/trabalho-2-breast-cancer/`  
**Depends on**: None  
**Reuses**: `.specs/features/trabalho-1/spec.md`, `.specs/project/STATE.md`  
**Requirement**: BC-01, BC-03, BC-04, BC-05, BC-08

**Tools**:
- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:
- [ ] `spec.md` declara objetivo corrigido e objetivo anteriormente testado.
- [ ] `spec.md` inclui requisitos para notebook, dicionario de dados e EDA de metadados/relações.
- [ ] `design.md` define componentes e artefatos.
- [ ] `tasks.md` tem tarefas atomicas com dependencias e gates.

**Tests**: docs
**Gate**: `test -f .specs/features/trabalho-2-breast-cancer/spec.md && test -f .specs/features/trabalho-2-breast-cancer/design.md && test -f .specs/features/trabalho-2-breast-cancer/tasks.md`

**Commit**: `docs: add spec driven plan for breast cancer project`

---

### T2: Criar harness de pacote e testes ✅

**What**: Criar pacote local `breast_cancer_survival`, paths centralizados e configuracao base de testes.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/`, `projeto_2_neuro_fuzzy/tests/`, `requirements.txt`  
**Depends on**: T1  
**Reuses**: `.specs/codebase/TESTING.md`, `.specs/codebase/CONVENTIONS.md`  
**Requirement**: BC-02

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `paths.py` define dataset, reports, figures, tables, docs, notebooks e models.
- [ ] `config.py` define `RANDOM_STATE`, `TEST_SIZE`, `TARGET_COLUMN`, `LEAKAGE_COLUMNS`.
- [ ] `pytest` consegue importar `breast_cancer_survival`.
- [ ] `pytest>=8` esta em `requirements.txt`.

**Tests**: unit
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_paths.py -q`

**Commit**: `test: add project 2 package harness`

---

### T3: Implementar sanitizacao e contrato do dataset ✅

**What**: Centralizar carga, limpeza, normalizacao de schema, mapeamento do alvo e contrato de dados.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/data.py`, `projeto_2_neuro_fuzzy/01_validate_data.py`  
**Depends on**: T2  
**Reuses**: `projeto_2_neuro_fuzzy/dataset/Breast_Cancer.csv`  
**Requirement**: BC-02

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `T Stage ` vira `t_stage`.
- [ ] `Reginol Node Positive` vira `regional_node_positive`.
- [ ] valores textuais sao stripados.
- [ ] `Status` vira `0/1`, com `Dead=1`.
- [ ] `Grade` vira inteiro ordinal 1-4.
- [ ] duplicatas sao reportadas e removidas do dataset analitico.
- [ ] `01_validate_data.py` imprime shape bruto, shape limpo, nulos, duplicatas e distribuicao do alvo.

**Tests**: unit
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_data_sanitization.py -q && python projeto_2_neuro_fuzzy/01_validate_data.py`

**Commit**: `feat: sanitize breast cancer dataset`

---

### T4: Criar dicionario de dados do Projeto 2 ✅

**What**: Gerar dicionario de dados especifico com colunas brutas, colunas sanitizadas, tipos, dominios, papel analitico, risco de vazamento e features derivadas.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/dictionary.py`, `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md`  
**Depends on**: T3  
**Reuses**: `docs/DATA_DICTIONARY.md` como referencia de formato, nao como conteudo do Projeto 2  
**Requirement**: BC-03

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `DATA_DICTIONARY.md` cobre todas as 16 colunas brutas.
- [ ] Cada coluna tem nome bruto, nome sanitizado, tipo bruto, tipo analitico, dominio/exemplos e papel.
- [ ] `Survival Months` esta marcado como `excluded_primary_model` e `leakage/follow_up_risk`.
- [ ] `Status` esta marcado como target.
- [ ] Features derivadas tem formula e racional.

**Tests**: unit + docs
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_data_dictionary.py -q`

**Commit**: `docs: add breast cancer data dictionary`

---

### T5: Implementar EDA com metadados e relacoes ✅

**What**: Gerar analise exploratoria completa com perfil de metadados, relacoes numericas/categoricas, tabelas e figuras.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/eda.py`, `projeto_2_neuro_fuzzy/02_eda.py`, `projeto_2_neuro_fuzzy/reports/`  
**Depends on**: T4  
**Reuses**: `02_eda.py` do Trabalho 1 como padrao de outputs  
**Requirement**: BC-04

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `metadata_profile.csv` contem dtype bruto/sanitizado, nulos, unicos, exemplos, papel e flag de vazamento.
- [ ] `numeric_relationships.csv` contem relacoes numericas com `status`.
- [ ] `categorical_relationships.csv` contem taxa de `Dead` por categoria e suporte.
- [ ] `data_quality_summary.json` contem linhas, colunas, duplicatas, nulos e distribuicao do alvo.
- [ ] Figuras incluem target, correlacao numerica, `Survival Months` vs `Status`, stage vs target e nodos/tumor vs target.
- [ ] A EDA destaca explicitamente que `Survival Months` nao deve entrar no modelo principal.

**Tests**: unit + script
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_eda_outputs.py -q && python projeto_2_neuro_fuzzy/02_eda.py`

**Commit**: `feat: add metadata and relationship EDA`

---

### T6: Implementar politica de features e engenharia clinica ✅

**What**: Separar feature set principal sem vazamento e criar features clinicas derivadas.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py`  
**Depends on**: T5  
**Reuses**: dicionario de dados e EDA  
**Requirement**: BC-01, BC-03, BC-06

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `split_features_target(include_survival_months=False)` exclui `status` e `survival_months`.
- [ ] `split_features_target(include_survival_months=True)` existe apenas para analise de sensibilidade.
- [ ] `add_clinical_features` cria `node_positive_ratio`, `advanced_stage_flag`, `hormone_receptor_negative`, `tumor_node_burden`.
- [ ] Dicionario de dados documenta as features derivadas.

**Tests**: unit
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_feature_policy.py projeto_2_neuro_fuzzy/tests/test_feature_engineering.py -q`

**Commit**: `feat: add feature policy and clinical features`

---

### T7: Implementar preprocessamento e metricas clinicas ✅

**What**: Criar preprocessor sem data leakage e avaliacao com foco em falsos negativos.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/preprocessing.py`, `projeto_2_neuro_fuzzy/src/breast_cancer_survival/evaluation.py`  
**Depends on**: T6  
**Reuses**: padrao `ColumnTransformer + Pipeline` do repo  
**Requirement**: BC-06

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] Numericas usam `StandardScaler`.
- [ ] Categoricas usam `OneHotEncoder(handle_unknown="ignore")`.
- [ ] `evaluate_predictions` retorna accuracy, balanced accuracy, precision, recall, F1, F2, ROC AUC, PR AUC, TP, TN, FP, FN.
- [ ] `scan_thresholds` gera tabela de thresholds.

**Tests**: unit
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_preprocessing.py projeto_2_neuro_fuzzy/tests/test_evaluation.py -q`

**Commit**: `feat: add preprocessing and clinical metrics`

---

### T8: Implementar suite de modelos tabulares ✅

**What**: Comparar modelos tabulares sem vazamento e com sensibilidade controlada para `Survival Months`.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/models.py`, `projeto_2_neuro_fuzzy/03_train_models.py`  
**Depends on**: T7  
**Reuses**: `baseline.py`, recomendacao do audio  
**Requirement**: BC-01, BC-06

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] Registry inclui Logistic Regression, Random Forest, ExtraTrees, HistGradientBoosting, SVM calibrado e MLP.
- [ ] `model_comparison_no_leakage.csv` e gerado.
- [ ] `model_comparison_with_survival_months.csv` e gerado como analise de sensibilidade.
- [ ] Saidas incluem `false_negatives`, `recall`, `precision`, `f2`, `pr_auc`.

**Tests**: unit + script
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_models.py projeto_2_neuro_fuzzy/tests/test_leakage_policy.py -q && python projeto_2_neuro_fuzzy/03_train_models.py`

**Commit**: `feat: compare tabular models for breast cancer`

---

### T9: Implementar ensemble ponderado e threshold tuning ✅

**What**: Combinar melhores modelos tabulares com pesos de validacao e selecionar threshold orientado a F2/recall/falsos negativos.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/ensemble.py`, `projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py`  
**Depends on**: T8  
**Reuses**: `evaluation.py`, `models.py`  
**Requirement**: BC-06

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] Pesos do ensemble somam 1.
- [ ] Modelo com melhor validacao recebe maior peso.
- [ ] `ensemble_threshold_scan.csv` e gerado.
- [ ] `ensemble_summary.csv` e gerado.
- [ ] O resumo informa threshold escolhido e falsos negativos.

**Tests**: unit + script
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_ensemble.py -q && python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py`

**Commit**: `feat: add weighted ensemble threshold tuning`

---

### T10: Refatorar neuro-fuzzy como comparativo academico ✅

**What**: Extrair funcoes fuzzy, rodar comparativo justo e manter wrapper de compatibilidade.  
**Where**: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/fuzzy.py`, `projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py`, `projeto_2_neuro_fuzzy/hybrid_neuro_fuzzy.py`  
**Depends on**: T9  
**Reuses**: `hybrid_neuro_fuzzy.py` atual  
**Requirement**: BC-07

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] `trimf` e `build_fuzzy_features` tem testes.
- [ ] Comparativo usa dados sanitizados, sem `Survival Months`, mesmo split e mesmas metricas.
- [ ] `neuro_fuzzy_comparison.csv` e gerado.
- [ ] Relatorio diferencia neuro-fuzzy cooperativo de ANFIS completo.

**Tests**: unit + script
**Gate**: `pytest projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py -q && python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py`

**Commit**: `fix: compare neuro fuzzy with shared pipeline`

---

### T11: Criar notebook Jupyter do Projeto 2 ✅

**What**: Criar notebook narrativo unico do Projeto 2 usando os mesmos modulos/scripts do pipeline.  
**Where**: `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`  
**Depends on**: T10  
**Reuses**: `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` como padrao narrativo  
**Requirement**: BC-05

**Tools**:
- MCP: filesystem
- Skill: NONE

**Done when**:
- [ ] Notebook tem secoes: contexto, objetivo, dicionario, metadados, EDA, sanitizacao, features, modelos, ensemble, neuro-fuzzy e conclusao.
- [ ] Notebook importa funcoes do pacote local, sem duplicar logica pesada.
- [ ] Notebook mostra `metadata_profile.csv`, `DATA_DICTIONARY.md` ou sua tabela equivalente, resultados de modelos e ensemble.
- [ ] Notebook executa via `nbconvert`.

**Tests**: notebook execution
**Gate**: `jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb`

**Commit**: `docs: add project 2 breast cancer notebook`

---

### T12: Sincronizar documentacao viva e relatorio final ✅

**What**: Atualizar README, relatorio, `.specs/project`, `.specs/codebase` e `STATUS.md` com o novo fluxo spec-driven.  
**Where**: `projeto_2_neuro_fuzzy/README.md`, `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`, `.specs/project/*`, `.specs/codebase/*`, `STATUS.md`  
**Depends on**: T11  
**Reuses**: `analise_audio_estrategia.md`, outputs de `reports/tables/`  
**Requirement**: BC-08

**Tools**:
- MCP: filesystem
- Skill: `tlc-spec-driven`

**Done when**:
- [ ] README lista ordem de execucao e papel do notebook.
- [ ] Relatorio final cita objetivo corrigido, dicionario de dados, metadados/relações, vazamento, ensemble e neuro-fuzzy.
- [ ] `.specs/project/ROADMAP.md` e `STATE.md` refletem Trabalho 2.
- [ ] `.specs/codebase/STRUCTURE.md`, `TESTING.md`, `CONVENTIONS.md` refletem pipeline do Projeto 2.
- [ ] `STATUS.md` separa Trabalho 1 e Trabalho 2.
- [ ] `run_pipeline.py` executa scripts principais.

**Tests**: docs + full pipeline
**Gate**: `pytest -q && python projeto_2_neuro_fuzzy/run_pipeline.py`

**Commit**: `docs: sync project 2 spec driven documentation`

---

## Parallel Execution Map

Neste projeto, a maior parte das tarefas e sequencial porque cada fase depende do contrato de dados e da politica de vazamento. Depois de T7, T8 e T10 nao devem rodar em paralelo porque o neuro-fuzzy precisa usar o mesmo criterio final dos modelos. O unico paralelismo seguro durante execucao e dentro de uma tarefa, por exemplo gerar tabelas e figuras independentes da EDA.

```
T1 -> T2 -> T3 -> T4 -> T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T11 -> T12
```

## Validation Tables

### Diagram-Definition Cross-Check

| Task | Depends on | Diagram predecessor | Status |
|---|---|---|---|
| T1 | None | Start | OK |
| T2 | T1 | T1 | OK |
| T3 | T2 | T2 | OK |
| T4 | T3 | T3 | OK |
| T5 | T4 | T4 | OK |
| T6 | T5 | T5 | OK |
| T7 | T6 | T6 | OK |
| T8 | T7 | T7 | OK |
| T9 | T8 | T8 | OK |
| T10 | T9 | T9 | OK |
| T11 | T10 | T10 | OK |
| T12 | T11 | T11 | OK |

### Test Co-location Validation

| Task | Creates/modifies | Tests co-located? | Gate |
|---|---|---|---|
| T1 | Specs/docs | Yes, docs gate | file presence |
| T2 | Package harness | Yes | pytest paths |
| T3 | Data layer | Yes | pytest + validation script |
| T4 | Dictionary layer | Yes | pytest dictionary |
| T5 | EDA layer | Yes | pytest + EDA script |
| T6 | Feature layer | Yes | pytest feature policy/engineering |
| T7 | Preprocessing/evaluation | Yes | pytest preprocessing/evaluation |
| T8 | Model layer | Yes | pytest + train script |
| T9 | Ensemble layer | Yes | pytest + ensemble script |
| T10 | Fuzzy layer | Yes | pytest + neuro-fuzzy script |
| T11 | Notebook | Yes | nbconvert execution |
| T12 | Docs/pipeline | Yes | pytest + full pipeline |

## Execution Summary

- `projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy/tests -q`: 17 passed.
- `projeto_2_neuro_fuzzy/.venv/bin/python -m pytest -q`: 19 passed.
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy/run_pipeline.py`: completed.
- `projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb`: completed.
