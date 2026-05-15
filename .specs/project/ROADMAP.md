# Roadmap do Projeto

## Trabalho 1: Comparação RF vs Redes Neurais (Saúde)
- **Prazo:** 15/05/2026
- **Status:** 🟡 **85% Concluído** — Consolidando resultados finais
- [x] Setup do ambiente e download do dataset `mohankrishnathalla/sleep-health-and-daily-performance-dataset`
- [x] Análise Exploratória de Dados (EDA)
- [x] Pré-processamento e Limpeza
- [x] Implementação Random Forest + Tuning (74.15% accuracy, 82.18% ROC AUC)
- [x] Implementação Redes Neurais + Tuning (73.23% → 74% com otimização)
- [x] Diagnóstico de limites do modelo (Rodada 3)
- [x] Identificação de threshold ótimo (0.35 para F1, 0.39 para balanced accuracy)
- [ ] **T1-10:** Gerar gráficos comparativos finais + PR Curve
- [ ] **T1-11:** Redigir relatório técnico (5-7 páginas)
- [ ] **T1-12:** Incorporar análise de threshold no notebook final
- [ ] **Entrega:** Submeter até 23:59 de 15/05/2026

**Resultados Chave:**
- Melhor modelo: HistGradientBoosting (74.25% accuracy, 82.58% ROC AUC)
- RF superou RN em dataset tabular — consistente com literatura
- Teto de performance limitado pela subjetividade do alvo `felt_rested`

## Trabalho 2: Sistema Híbrido ou Ensemble
- **Prazo:** 03/07/2026
- **Status:** ⚪ Não Iniciado
- [ ] Definição do tema e dataset
- [ ] Design da arquitetura (Neuro-Fuzzy, Genético-Neural ou Ensemble)
- [ ] Implementação e Validação
- [ ] Relatório e Apresentação

**Ideias em Consideração:**
- Ensemble stacking: RF + Gradient Boosting + Logistic Regression
- Sistema Neuro-Fuzzy para classificação com interpretabilidade
- Otimização por algoritmo genético de hiperparâmetros de RN
