# Projeto 2: Breast Cancer Survival Risk

Este projeto corrige a trilha do Trabalho 2 para o dataset SEER Breast Cancer.

## Objetivo corrigido

Classificar risco de obito observado (`Status = Dead`) a partir de variaveis clinico-patologicas registradas no dataset. O modelo principal nao usa `Survival Months`, porque essa coluna representa acompanhamento posterior e pode contaminar a predicao.

## Artefatos principais

- `docs/DATA_DICTIONARY.md`: dicionario de dados do Projeto 2.
- `docs/PROJECT_EXECUTION_SUMMARY.md`: resumo executivo do que foi implementado e validado.
- `reports/tables/metadata_profile.csv`: perfil de metadados do dataset.
- `reports/tables/numeric_relationships.csv`: relacoes numericas com o alvo.
- `reports/tables/categorical_relationships.csv`: relacoes categoricas com o alvo.
- `reports/tables/ensemble_validation_summary.csv`: ponto operacional escolhido na validacao.
- `reports/tables/ensemble_test_summary.csv`: metricas finais do ensemble no teste intocado.
- `reports/tables/calibration_summary.csv`: comparativo de calibracao e Brier score.
- `reports/tables/logistic_regression_top_coefficients.csv`: explicabilidade linear do baseline.
- `reports/tables/stability_summary.csv`: media/desvio por seed para baseline e ensemble.
- `notebooks/projeto_2_breast_cancer_survival.ipynb`: notebook narrativo do Projeto 2.

## Ordem de execucao

```bash
python projeto_2_neuro_fuzzy/01_validate_data.py
python projeto_2_neuro_fuzzy/02_eda.py
python projeto_2_neuro_fuzzy/03_train_models.py
python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py
python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py
python projeto_2_neuro_fuzzy/06_explainability.py
python projeto_2_neuro_fuzzy/07_stability_analysis.py
```

Ou:

```bash
python projeto_2_neuro_fuzzy/run_pipeline.py
```

## Validacao do notebook

```bash
jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb
```
