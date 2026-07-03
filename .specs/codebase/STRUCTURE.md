# Estrutura do Repositório (Projeto IC)

```text
.
├── materiais_de_aula/                        # PDFs oficiais da disciplina.
├── podcasts/                                 # Audios gerados via NotebookLM.
├── guia_de_acao_ic.md                        # Roteiro metodologico condensado.
├── STATUS.md                                 # Status executivo consolidado.
│
├── projeto_1_genetico_neural/                # PROJETO 1 - GA + MLP
│   ├── dataset/
│   ├── .venv/
│   ├── eda_heart_failure.py
│   ├── baseline.py
│   ├── hybrid_ga_mlp.py
│   ├── notebooks/
│   └── reports/
│
├── projeto_2_neuro_fuzzy/                    # PROJETO 2 - SEER corrigido
│   ├── dataset/
│   ├── .venv/
│   ├── 01_validate_data.py
│   ├── 02_eda.py
│   ├── 03_train_models.py
│   ├── 04_threshold_and_ensemble.py
│   ├── 05_neuro_fuzzy_comparison.py
│   ├── 06_explainability.py
│   ├── 07_stability_analysis.py
│   ├── run_pipeline.py
│   ├── baseline.py
│   ├── hybrid_neuro_fuzzy.py
│   ├── docs/
│   ├── notebooks/
│   ├── reports/
│   ├── src/breast_cancer_survival/
│   └── tests/
│
├── projeto_2_neuro_fuzzy_metabric_clinico/   # Fork clinico METABRIC
│   ├── dataset/
│   ├── docs/
│   ├── notebooks/
│   ├── reports/
│   ├── src/
│   └── tests/
│
└── .specs/                                   # Documentacao TLC
    ├── project/
    ├── codebase/
    └── features/
```

## Projeto 1

### Estrutura relevante

```text
projeto_1_genetico_neural/
├── dataset/heart_failure_clinical_records_dataset.csv
├── eda_heart_failure.py
├── baseline.py
├── hybrid_ga_mlp.py
├── notebooks/projeto_1_genetico_neural_ga_mlp.ipynb
└── reports/
    ├── figures/evolucao_genetica.png
    └── tables/
        ├── ga_mlp_results_quick.json
        ├── ga_mlp_results.json
        └── model_comparison.csv
```

### Specs do Projeto 1

| Artefato | Localizacao |
|---|---|
| Spec | `.specs/features/projeto-1-genetico-neural/spec.md` |
| Design | `.specs/features/projeto-1-genetico-neural/design.md` |
| Tasks | `.specs/features/projeto-1-genetico-neural/tasks.md` |

Status revisado: Projeto 1 esta implementado e validado tecnicamente; a pendencia principal e transformar o resultado em narrativa final de relatorio/apresentacao.

## Projeto 2 SEER

### Estrutura relevante

```text
projeto_2_neuro_fuzzy/
├── 01_validate_data.py
├── 02_eda.py
├── 03_train_models.py
├── 04_threshold_and_ensemble.py
├── 05_neuro_fuzzy_comparison.py
├── 06_explainability.py
├── 07_stability_analysis.py
├── run_pipeline.py
├── baseline.py
├── hybrid_neuro_fuzzy.py
├── dataset/Breast_Cancer.csv
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── PROJECT_EXECUTION_SUMMARY.md
├── notebooks/projeto_2_breast_cancer_survival.ipynb
├── reports/
│   ├── figures/
│   ├── tables/
│   │   ├── metadata_profile.csv
│   │   ├── numeric_relationships.csv
│   │   ├── categorical_relationships.csv
│   │   ├── model_comparison_no_leakage.csv
│   │   ├── model_comparison_no_leakage_validation.csv
│   │   ├── model_comparison_no_leakage_test.csv
│   │   ├── model_comparison_with_survival_months.csv
│   │   ├── ensemble_validation_summary.csv
│   │   ├── ensemble_test_summary.csv
│   │   ├── calibration_summary.csv
│   │   ├── stability_summary.csv
│   │   └── neuro_fuzzy_comparison.csv
│   └── relatorio_tecnico_projeto_2.md
├── src/breast_cancer_survival/
│   ├── config.py
│   ├── data.py
│   ├── dictionary.py
│   ├── eda.py
│   ├── ensemble.py
│   ├── evaluation.py
│   ├── explainability.py
│   ├── features.py
│   ├── fuzzy.py
│   ├── models.py
│   ├── paths.py
│   ├── preprocessing.py
│   └── splits.py
└── tests/test_*.py
```

### Specs do Projeto 2

| Artefato | Localizacao |
|---|---|
| Spec | `.specs/features/trabalho-2-breast-cancer/spec.md` |
| Design | `.specs/features/trabalho-2-breast-cancer/design.md` |
| Tasks | `.specs/features/trabalho-2-breast-cancer/tasks.md` |
| Relatorio de execucao | `.specs/features/trabalho-2-breast-cancer/relatorio_execucao.md` |

Status revisado: Projeto 2 SEER esta executado e documentado com split treino-validacao-teste, ensemble corrigido, explicabilidade, calibracao, estabilidade e notebook sincronizado.

## Projeto 2 METABRIC

### Papel no repositório

O diretório `projeto_2_neuro_fuzzy_metabric_clinico/` funciona como fork clinico do Projeto 2 para melhoria continua. Ele nao substitui o SEER como trilha historica corrigida, mas amplia a qualidade metodologica e o potencial de apresentacao.
