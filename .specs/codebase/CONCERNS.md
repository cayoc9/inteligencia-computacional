# Preocupações Técnicas

## Reprodutibilidade ✅ Resolvido
- **Status:** `requirements.txt` criado em 2026-05-14
- **Comando único:** `pip install -r requirements.txt`
- **Validação:** `python scripts/smoke_test.py`
- **Pipeline:** Scripts numerados permitem reexecução completa

## Organização DS ✅ Resolvido
- **Scripts:** Pipeline auditável (`01_` a `05_`)
- **Notebook:** Narrativa central em consolidação
- **Sincronização:** Notebook deve refletir resultados dos scripts (mesmo random_state=42)

## Risco de Entrega 🟡 Atenção
- **Prazo:** 15/05/2026 (urgente)
- **Pendências:** Gráficos comparativos finais + relatório técnico (5-7 páginas)
- **Mitigação:** Focar em consolidar resultados existentes, não em novos experimentos

## Performance dos Modelos ✅ Compreendido
- **Teto identificado:** ~74% accuracy para `felt_rested`
- **Causa raiz:** Subjetividade do alvo (resposta individual varia mesmo com features similares)
- **Features dominantes:** `sleep_quality`, `sleep_duration`, `stress`, `wake_episodes` (80% do sinal)
- **Conclusão:** RF > RN em dataset tabular — consistente com literatura

## Threshold de Decisão ⚠️ Não Ótimo
- **Padrão:** 0.5 não é ideal para este problema desbalanceado
- **Otimizado:** 0.35 maximiza F1, 0.39 maximiza balanced accuracy
- **Ação:** Incorporar análise de threshold no relatório final

## Métricas de Avaliação ⚠️ Incompleto
- **Obrigatórias:** 6 métricas (acurácia, matriz confusão, precisão, recall, F1, ROC AUC) ✅
- **Recomendadas:** PR Curve, balanced_accuracy, análise por segmentos ⏳ Pendente

## Interpretabilidade 🟡 Parcial
- **Feature importance:** Permutation importance calculada no diagnóstico
- **SHAP:** Não implementado (opcional, tempo limitado)
- **Recomendação:** Usar permutation importance no relatório (já disponível)

## Recomendação Prioritária
1. **Imediato:** Gerar gráficos das 6 métricas obrigatórias + PR Curve
2. **Imediato:** Redigir relatório técnico com resultados consolidados
3. **Opcional:** Adicionar análise de erro por ocupação/segmento se sobrar tempo
