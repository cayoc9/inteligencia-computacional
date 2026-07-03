# Preocupações Técnicas

## Reprodutibilidade ✅ Resolvido
- **Status:** `requirements.txt` criado em 2026-05-14
- **Comando único:** `pip install -r requirements.txt`
- **Validação:** `python scripts/smoke_test.py`
- **Pipeline:** Scripts numerados permitem reexecução completa

## Organização DS ✅ Resolvido
- **Scripts:** Pipeline auditável (`01_` a `05_`)
- **Notebook:** Narrativa central consolidada para a V1
- **Sincronização:** Notebook deve refletir resultados dos scripts (mesmo random_state=42)

## Risco de Entrega ✅ Resolvido
- **Prazo:** 15/05/2026
- **Resultado:** Trabalho 1 concluído e entregue.
- **Registro:** Manter as decisões e limitações como histórico da V1; não misturar com V2.

## Performance dos Modelos ✅ Compreendido
- **Teto identificado:** ~74% accuracy para `felt_rested`
- **Causa raiz:** Subjetividade do alvo (resposta individual varia mesmo com features similares)
- **Features dominantes:** `sleep_quality`, `sleep_duration`, `stress`, `wake_episodes` (80% do sinal)
- **Conclusão:** RF > RN em dataset tabular — consistente com literatura

## Threshold de Decisão ✅ Incorporado
- **Padrão:** 0.5 não é ideal para este problema desbalanceado
- **Otimizado:** 0.35 maximiza F1, 0.39 maximiza balanced accuracy
- **Ação:** Análise incorporada ao fechamento da V1 e mantida como referência para V2.

## Métricas de Avaliação ✅ Fechadas Para V1
- **Obrigatórias:** 6 métricas (acurácia, matriz confusão, precisão, recall, F1, ROC AUC) ✅
- **Adicionais usadas:** PR Curve, balanced_accuracy e threshold tuning.
- **Aberto para trabalho futuro:** análise por segmentos, validação cruzada sistemática e SHAP.

## Interpretabilidade 🟡 Parcial
- **Feature importance:** Permutation importance calculada no diagnóstico
- **SHAP:** Não implementado (opcional, tempo limitado)
- **Recomendação:** Usar permutation importance no relatório (já disponível)

## Recomendação Prioritária
1. **Próxima decisão:** escolher entre executar V2 `sono_restaurador` ou iniciar Trabalho 2.
2. **Se V2:** seguir `.specs/features/experimento-v2-sono-restaurador/tasks.md`.
3. **Se Trabalho 2:** criar spec separada antes de selecionar arquitetura/dataset.
