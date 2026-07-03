# Project Execution Summary

**Projeto**: Breast Cancer Survival Risk - SEER  
**Ultima atualizacao**: 2026-07-03  
**Status**: Executado e documentado

## O que foi feito

O projeto foi reestruturado como pipeline spec-driven com sete etapas executaveis:

1. validacao e sanitizacao dos dados;
2. EDA com metadados e relacoes;
3. treino de modelos tabulares;
4. ensemble com validacao separada;
5. comparativo neuro-fuzzy;
6. explicabilidade e calibracao;
7. estabilidade por seeds.

## Scripts do pipeline

| Script | Papel |
|---|---|
| `01_validate_data.py` | contrato, limpeza e distribuicao do alvo |
| `02_eda.py` | metadados, relacoes e figuras |
| `03_train_models.py` | comparacao de modelos sem vazamento e com sensibilidade |
| `04_threshold_and_ensemble.py` | pesos/threshold na validacao e teste intocado |
| `05_neuro_fuzzy_comparison.py` | comparativo academico fuzzy + MLP |
| `06_explainability.py` | coeficientes, permutation importance e calibracao |
| `07_stability_analysis.py` | robustez em 5 seeds |
| `run_pipeline.py` | runner unico |

## Artefatos principais

### Dados e EDA

- `docs/DATA_DICTIONARY.md`
- `reports/tables/metadata_profile.csv`
- `reports/tables/numeric_relationships.csv`
- `reports/tables/categorical_relationships.csv`
- `reports/tables/data_quality_summary.json`

### Resultados de modelagem

- `reports/tables/model_comparison_no_leakage.csv`
- `reports/tables/model_comparison_no_leakage_validation.csv`
- `reports/tables/model_comparison_no_leakage_test.csv`
- `reports/tables/model_comparison_with_survival_months.csv`
- `reports/tables/ensemble_validation_summary.csv`
- `reports/tables/ensemble_test_summary.csv`
- `reports/tables/neuro_fuzzy_comparison.csv`

### Explicabilidade, calibracao e estabilidade

- `reports/tables/logistic_regression_top_coefficients.csv`
- `reports/tables/logistic_regression_permutation_importance.csv`
- `reports/tables/calibration_summary.csv`
- `reports/tables/stability_summary.csv`

### Narrativa e defesa

- `reports/relatorio_tecnico_projeto_2.md`
- `notebooks/projeto_2_breast_cancer_survival.ipynb`
- `.specs/features/trabalho-2-breast-cancer/`

## Validacao executada

- `pytest projeto_2_neuro_fuzzy/tests -q`
- `python projeto_2_neuro_fuzzy/run_pipeline.py`
- `jupyter nbconvert --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`

## Leitura correta do resultado

- `Survival Months` foi removido do modelo principal por risco de vazamento.
- O ensemble nao deve ser vendido como melhor discriminador global.
- A Logistic Regression segue como baseline forte e explicavel.
- O ensemble e um ponto operacional de maior sensibilidade.
- O neuro-fuzzy fica como comparativo academico.

## Pendencias reais

- consolidar PDF final;
- fechar narrativa da apresentacao;
- decidir o quanto do fork METABRIC entra na defesa final;
- se houver tempo, ampliar robustez e explicabilidade local.
