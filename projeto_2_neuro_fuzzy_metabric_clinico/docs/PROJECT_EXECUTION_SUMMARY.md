# Project Execution Summary

**Projeto**: Breast Cancer Survival Risk - METABRIC Clinico  
**Ultima atualizacao**: 2026-07-03  
**Status**: Executado e documentado

## O que foi feito

O fork clinico foi elevado ao mesmo fluxo metodologico do Projeto 2 SEER:

1. validacao e sanitizacao dos dados;
2. EDA com metadados e relacoes;
3. treino de modelos tabulares;
4. ensemble com `treino / validacao / teste`;
5. comparativo neuro-fuzzy;
6. explicabilidade e calibracao;
7. estabilidade por seeds;
8. suite de graficos comparaveis ao projeto `sleep_health`.

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
| `08_generate_sleep_health_equivalent_graphs.py` | suite visual comparavel ao projeto sleep_health |
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

### Suite visual comparavel ao Sleep Health

- `reports/figures/comparacao_metricas.png`
- `reports/figures/curvas_roc.png`
- `reports/figures/curvas_pr.png`
- `reports/figures/threshold_otimizacao.png`
- `reports/figures/confusion_matrix_ensemble.png`
- `reports/figures/feature_importance.png`

### Narrativa e defesa

- `reports/relatorio_tecnico_projeto_2_metabric.md`
- `notebooks/projeto_2_metabric_clinico.ipynb`

## Validacao executada

- `PYTHONPATH=projeto_2_neuro_fuzzy_metabric_clinico/src projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy_metabric_clinico/tests -q`
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/run_pipeline.py`
- `projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --execute projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb`

## Leitura correta do resultado

- `survival_months` foi removido do modelo principal por risco de vazamento.
- O fork agora segue o mesmo padrao metodologico do SEER para o ensemble.
- A Logistic Regression segue como baseline explicavel.
- O ensemble e um ponto operacional de alta sensibilidade.
- O neuro-fuzzy continua como comparativo academico.

## Resultado principal atual

- Melhor modelo individual sem vazamento: `gradient_boosting`
  - F2 `0.7787`
  - recall `0.7953`
  - precision `0.7185`
  - PR AUC `0.7600`
- Ensemble corrigido no teste:
  - threshold `0.16`
  - recall `0.9953`
  - F2 `0.8770`
  - falsos negativos `1`
  - falsos positivos `146`

## Pendencias reais

- consolidar PDF final da disciplina;
- decidir o peso do METABRIC na defesa final;
- se houver tempo, evoluir o fork para analise de sobrevivencia formal.
