## Status Atual
- **Rodada 1 (Baseline):** ✅ Concluída e Documentada em `relatorio_rodada_1.md`.
- **Rodada 2 (Otimização):** 🕒 Iniciando. Foco em Feature Engineering e diretrizes `data-science-expert`.

## Decisões Atuais
- **Dataset (T1):** Sleep Health & Daily Performance Dataset (100k rows, 32 cols). Escolhido pela robustez para Redes Neurais.
- **Tecnologias:** Python, Scikit-Learn (RF), TensorFlow/Keras (RN), Pandas (EDA).
- **Ambiente:** Virtual Environment isolado (`.venv`).
- **Baseline:** RF (74.15%) venceu a RN (73.23%) na configuração inicial.
- **Jupyter:** Passa a existir como artefato central de análise em `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`, reunindo EDA, modelagem e comparação final. Os scripts numerados continuam como pipeline auditável/reexecutável.
- **Relatório:** Fragmentar apenas a seção de resultados em `reports/fragmentos/`, mantendo o restante concentrado no notebook e nos relatórios vivos da feature.

## Bloqueios
- Limitação de GPU local (Treino de RN em CPU), mas sem impacto crítico no cronograma atual.
