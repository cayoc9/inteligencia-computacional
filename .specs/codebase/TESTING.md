# Validação e Testes

## Validação Existente
- Validação manual por execução dos scripts.
- Métricas obrigatórias no console: acurácia, matriz de confusão, precision, recall, F1 e ROC AUC.
- Relatórios de rodada em `.specs/features/trabalho-1/`.

## Gates Recomendados
- `python 01_check_data.py`
- `python 02_eda.py`
- `python 03_random_forest.py`
- `python 04_neural_network.py`
- `python 05_neural_network_optimized.py`
- `python scripts/diagnose_model_limits.py`
- `jupyter nbconvert --to notebook --execute notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`

## Lacunas
- Não há testes automatizados.
- Não há script único de reprodução ponta a ponta.
- Não há manifesto de dependências congelado para outro membro do grupo reproduzir o ambiente.
