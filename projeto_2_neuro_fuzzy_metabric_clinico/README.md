# Projeto 2 Fork: Breast Cancer METABRIC Clinico

Este fork usa o dataset clinico METABRIC do Kaggle (`gunesevitan/breast-cancer-metabric`) para manter o mesmo tema de cancer de mama, mas com variaveis clinicas, moleculares e de tratamento mais ricas que o dataset SEER original.

## Objetivo

Prever `Overall Survival Status = Deceased` a partir de atributos clinicos, moleculares e de tratamento, sem usar `Overall Survival (Months)` no modelo principal.

`Overall Survival (Months)`, recidiva e status vital pos-acompanhamento ficam fora do modelo primario. Eles entram apenas em experimento de sensibilidade para demonstrar inflacao por informacao de acompanhamento.

## Artefatos

- `dataset/Breast Cancer METABRIC.csv`: dataset clinico baixado do Kaggle.
- `docs/DATA_DICTIONARY.md`: dicionario de dados e politica de vazamento.
- `docs/PROJECT_EXECUTION_SUMMARY.md`: resumo executivo do que foi implementado e validado.
- `reports/tables/metadata_profile.csv`: metadados, nulos, cardinalidade e exemplos.
- `reports/tables/model_comparison_no_leakage.csv`: modelos sem sobrevida como preditor.
- `reports/tables/ensemble_validation_summary.csv`: threshold e pesos escolhidos na validacao.
- `reports/tables/ensemble_test_summary.csv`: metricas finais no teste intocado.
- `reports/tables/calibration_summary.csv`: comparativo de calibracao e Brier score.
- `reports/tables/stability_summary.csv`: media/desvio por seed para baseline e ensemble.
- `reports/relatorio_tecnico_projeto_2_metabric.md`: sintese tecnica do fork.
- `notebooks/projeto_2_metabric_clinico.ipynb`: notebook narrativo do fork.

## Execucao

Use o ambiente ja preparado em `projeto_2_neuro_fuzzy/.venv`:

```bash
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/run_pipeline.py
```

Ou por etapas:

```bash
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/01_validate_data.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/02_eda.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/03_train_models.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/04_threshold_and_ensemble.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/05_neuro_fuzzy_comparison.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/06_explainability.py
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/07_stability_analysis.py
```

## Validacao

```bash
PYTHONPATH=projeto_2_neuro_fuzzy_metabric_clinico/src projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy_metabric_clinico/tests -q
projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb --output /tmp/projeto_2_metabric_clinico.executed.ipynb
```

## Resultado principal

Sem usar meses de sobrevida, o melhor modelo individual foi `gradient_boosting`: F2 `0.7787`, recall `0.7953`, precision `0.7185` e PR AUC `0.7600`.

O ensemble agora segue `treino / validacao / teste`, com pesos e threshold congelados na validacao antes do reporte final. No teste intocado, o threshold `0.16` entregou recall `0.9953`, F2 `0.8770` e apenas `1` falso negativo, ao custo de `146` falsos positivos.
