## Status Atual (Atualizado: 2026-05-15)

### Trabalho 1 - Classificação em Saúde

| Rodada | Status | Descrição |
|---|---|---|
| **Rodada 1 (Baseline)** | ✅ Concluída | RF 74.15% vs RN 73.23% — RF venceu |
| **Rodada 2 (Otimização)** | ✅ Concluída | RN v2 com feature engineering + regularization — ganho marginal |
| **Rodada 3 (Diagnóstico)** | ✅ Concluída | Script `diagnose_model_limits.py` identificou teto do alvo `felt_rested` |

**Status Geral:** 🟢 **85% Concluído** — Pendente: gráficos comparativos finais + relatório técnico

## Decisões Atuais

### Dataset e Modelagem
- **Dataset:** Sleep Health & Daily Performance (100k rows, 32 cols, 0 nulos, 0 duplicatas)
- **Target Primário:** `felt_rested` (binária: 61%/39% — levemente desbalanceada)
- **Melhor Modelo:** HistGradientBoosting (accuracy 74.25%, ROC AUC 82.58%)
- **Threshold Otimizado:** 0.35 maximiza F1 (0.7017), 0.39 maximiza balanced accuracy (0.7424)

### Stack Tecnológico
- **Linguagem:** Python 3.12.3 (`.venv`)
- **ML Clássico:** scikit-learn (Random Forest, HistGradientBoosting, Logistic Regression)
- **Redes Neurais:** TensorFlow 2.18+ / Keras (MLP com BatchNorm + Dropout)
- **EDA/Visualização:** pandas, matplotlib, seaborn
- **Ambiente Interativo:** Jupyter Notebook

### Arquitetura e Organização
- **Pipeline:** Scripts numerados (`01_` a `05_`) para reprodutibilidade
- **Notebook Central:** `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` (narrativa + apresentação)
- **Artefatos:** `data/` (dataset), `models/` (modelos .pkl/.keras), `reports/figures/` (visualizações)
- **Especificação:** `.specs/features/trabalho-1/` (spec.md, tasks.md, relatórios de rodada)

## Lições Aprendidas

### O Que Funcionou
1. **Scripts numerados** facilitaram reexecução e auditoria
2. **Mesmo random_state=42** permitiu comparação justa entre modelos
3. **Diagnóstico de Rodada 3** revelou que o gargalo é o alvo, não o modelo
4. **Threshold tuning** entregou ganho real sem retreinar modelo

### O Que Não Funcionou
1. **Rede Neural Profunda** em dataset tabular não superou Random Forest
2. **Feature Engineering** adicionou complexidade sem ganho proporcional
3. **Acurácia como métrica principal** mascarou desempenho real (desbalanceamento)

### Surpresas
1. **Teto do alvo:** `felt_rested` parece subjetivo — 2 pessoas com sono similar respondem diferente
2. **Poucas features importam:** `sleep_quality`, `sleep_duration`, `stress`, `wake_episodes` carregam 80% do sinal
3. **Threshold 0.5 é arbitrário:** Ajustar para 0.35 melhorou F1 de 0.66 para 0.70

## Bloqueios e Restrições

| Bloqueio | Impacto | Mitigação |
|---|---|---|
| GPU local limitada | Treino de RN em CPU é lento | Modelo já convergiu; otimização adicional tem retorno decrescente |
| Subjetividade do alvo | Teto de ~74% accuracy | Justificar no relatório como limitação do dataset, não do modelo |
| Prazo: 15/05/2026 | Tempo curto para otimização exaustiva | Focar em consolidar resultados existentes, não em novos experimentos |

## Próximos Passos (Pendentes)

- [ ] **T1-10:** Gerar gráficos comparativos das 6 métricas obrigatórias + PR Curve
- [ ] **T1-11:** Redigir relatório técnico (5-7 páginas) conforme PDF de avaliação
- [ ] **T1-12:** Incorporar análise de threshold e diagnóstico no notebook final
- [ ] **Entrega:** Submeter relatório + notebook + scripts até 23:59 de 15/05/2026

## Preferências de Execução

- **Modelos mais rápidos:** Para tarefas de validação/estado, modelos mais rápidos são suficientes
- **Sub-agentes:** Usar para implementação de tarefas; orquestrador mantém contexto de planejamento
- **Diagramas:** Preferir `mermaid-studio` skill se instalado
