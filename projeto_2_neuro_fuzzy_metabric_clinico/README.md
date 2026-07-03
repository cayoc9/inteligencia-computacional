# Projeto 2 Fork: Breast Cancer METABRIC Clinico

Este fork usa o dataset clinico METABRIC do Kaggle (`gunesevitan/breast-cancer-metabric`) para manter o mesmo tema de cancer de mama, mas com variaveis clinicas, moleculares e de tratamento mais ricas que o dataset SEER original.

## Objetivo

Prever `Overall Survival Status = Deceased` a partir de atributos clinicos, moleculares e de tratamento, sem usar `Overall Survival (Months)` no modelo principal.

`Overall Survival (Months)`, recidiva e status vital pos-acompanhamento ficam fora do modelo primario. Eles entram apenas em experimento de sensibilidade para demonstrar inflacao por informacao de acompanhamento.

## Artefatos

- `dataset/Breast Cancer METABRIC.csv`: dataset clinico baixado do Kaggle.
- `docs/DATA_DICTIONARY.md`: dicionario de dados e politica de vazamento.
- `reports/tables/metadata_profile.csv`: metadados, nulos, cardinalidade e exemplos.
- `reports/tables/model_comparison_no_leakage.csv`: modelos sem sobrevida como preditor.
- `reports/tables/ensemble_summary.csv`: ensemble ponderado e threshold operacional.
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
```

## Validacao

```bash
PYTHONPATH=projeto_2_neuro_fuzzy_metabric_clinico/src projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy_metabric_clinico/tests -q
projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb --output /tmp/projeto_2_metabric_clinico.executed.ipynb
```

## Resultado principal

Sem usar meses de sobrevida, o melhor modelo individual foi `gradient_boosting`: F2 0.7696, recall 0.7860, precision 0.7101 e PR AUC 0.7590.

O ensemble ponderado com threshold 0.25 chegou a F2 0.8885 e recall 0.9860, reduzindo falsos negativos para 3. Esse ponto aumenta falsos positivos para 121 e deve ser lido como cenario de alta sensibilidade.
