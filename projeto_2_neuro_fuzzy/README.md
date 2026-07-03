# Projeto 2: Breast Cancer Survival Risk

Este projeto corrige a trilha do Trabalho 2 para o dataset SEER Breast Cancer.

## Objetivo corrigido

Prever risco de obito (`Status = Dead`) a partir de atributos clinicos disponiveis no diagnostico. O modelo principal nao usa `Survival Months`, porque essa coluna representa acompanhamento posterior e pode contaminar a predicao.

## Artefatos principais

- `docs/DATA_DICTIONARY.md`: dicionario de dados do Projeto 2.
- `reports/tables/metadata_profile.csv`: perfil de metadados do dataset.
- `reports/tables/numeric_relationships.csv`: relacoes numericas com o alvo.
- `reports/tables/categorical_relationships.csv`: relacoes categoricas com o alvo.
- `notebooks/projeto_2_breast_cancer_survival.ipynb`: notebook narrativo do Projeto 2.

## Ordem de execucao

```bash
python projeto_2_neuro_fuzzy/01_validate_data.py
python projeto_2_neuro_fuzzy/02_eda.py
python projeto_2_neuro_fuzzy/03_train_models.py
python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py
python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py
```

Ou:

```bash
python projeto_2_neuro_fuzzy/run_pipeline.py
```

## Validacao do notebook

```bash
jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb
```

