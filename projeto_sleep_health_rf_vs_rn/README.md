# Projeto Sleep Health: RF vs RN

Este diretorio concentra o projeto de classificacao em saude do sono que antes estava espalhado na raiz do repositorio.

## Escopo

- comparacao entre Random Forest e Redes Neurais para `felt_rested`;
- EDA e diagnostico avancado do teto de performance;
- notebook consolidado do Trabalho 1 original;
- relatorio tecnico, figuras e diagnosticos do experimento.

## Estrutura

- `01_check_data.py`: inspecao inicial dos dados
- `02_eda.py`: analise exploratoria
- `03_random_forest.py`: baseline com Random Forest
- `04_neural_network.py`: rede neural base
- `05_neural_network_optimized.py`: rede neural otimizada
- `scripts/diagnose_model_limits.py`: diagnostico avancado
- `scripts/generate_final_graphs.py`: gera as figuras finais do projeto
- `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`: notebook principal
- `reports/`: figuras, diagnosticos e fragmentos
- `docs/DATA_DICTIONARY.md`: dicionario do dataset

## Dados

O dataset principal fica em `data/sleep_health_dataset.csv`.

## Ambiente

As dependencias continuam centralizadas no `requirements.txt` da raiz do repositorio.

No diretorio raiz:

```bash
pip install -r requirements.txt
```

## Execucao

No diretorio raiz do repositorio:

```bash
python projeto_sleep_health_rf_vs_rn/01_check_data.py
python projeto_sleep_health_rf_vs_rn/02_eda.py
python projeto_sleep_health_rf_vs_rn/03_random_forest.py
python projeto_sleep_health_rf_vs_rn/04_neural_network.py
python projeto_sleep_health_rf_vs_rn/05_neural_network_optimized.py
python projeto_sleep_health_rf_vs_rn/scripts/diagnose_model_limits.py
python projeto_sleep_health_rf_vs_rn/scripts/generate_final_graphs.py
```

## Artefatos principais

- figuras finais: `projeto_sleep_health_rf_vs_rn/reports/figures/`
- diagnosticos: `projeto_sleep_health_rf_vs_rn/reports/diagnostics/`
- modelos derivados: `projeto_sleep_health_rf_vs_rn/models/`
- relatorio tecnico: `projeto_sleep_health_rf_vs_rn/relatorio-tecnico.md`
