# Arquitetura Atual

## Fluxo de Dados
1. Leitura do CSV em `data/sleep_health_dataset.csv`.
2. Inspeção e EDA em scripts separados.
3. Preparação de features com `ColumnTransformer`.
4. Treinamento de modelos comparáveis com split estratificado.
5. Persistência de modelos, histórico de treino, split de teste e figuras.

## Decisões Observadas
- Uso de scripts sequenciais numerados para deixar execução e auditoria mais previsíveis.
- Uso de `Pipeline`/`ColumnTransformer` no Random Forest para reduzir risco de data leakage.
- Uso do mesmo `random_state=42` e estratificação para comparação entre modelos.
- Foco em relatório acadêmico comparativo, não em produto interativo.

## Papel Possível de Notebook
O notebook principal passa a servir como camada de exploração, narrativa e apresentação intermediária. A camada de scripts continua útil para reexecução controlada e auditoria dos resultados.
