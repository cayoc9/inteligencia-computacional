# Roadmap do Projeto

## Trabalho 1: Comparação RF vs Redes Neurais (Saúde)
- **Prazo:** 15/05/2026
- **Status:** ✅ **100% Concluído — Entregue**
- [x] Setup do ambiente e download do dataset
- [x] Análise Exploratória de Dados (EDA)
- [x] Pré-processamento e Limpeza
- [x] Implementação Random Forest + Tuning (74.15% accuracy, 82.18% ROC AUC)
- [x] Implementação Redes Neurais + Tuning (73.23% → 74% com otimização)
- [x] Diagnóstico de limites do modelo (Rodada 3)
- [x] Identificação de threshold ótimo (0.35 para F1, 0.39 para balanced accuracy)
- [x] **T1-10:** Gráficos comparativos finais (7 figuras: barras, ROC, PR, threshold, importance, confusion, feature AUC)
- [x] **T1-11:** Relatório técnico (~7 páginas em `relatorio-tecnico.md`)
- [x] **T1-12:** Notebook consolidado (37 células, Seção 9 com diagnóstico avançado)
- [x] **Entrega:** ✅ 15/05/2026

**Resultados Chave:**
- Melhor modelo: HistGradientBoosting (74.25% accuracy, 82.58% ROC AUC)
- RF superou RN em dataset tabular — consistente com literatura
- Teto de performance limitado pela subjetividade do alvo `felt_rested`
- V1 oficial congelada com `felt_rested`; alvo composto `sono_restaurador` fica reservado para V2
- Revisão estrutural registrada em `.specs/project/REPO_CLEANUP_REVIEW.md`

## Experimento V2: Sono Restaurador
- **Prazo:** Pós-entrega do Trabalho 1
- **Status:** 📝 Especificado, não executado
- [x] Registrar hipótese do alvo composto `sono_restaurador`
- [x] Separar V2 da narrativa oficial da V1
- [ ] Criar script/notebook derivando o novo target
- [ ] Reexecutar RF e RN com o mesmo protocolo da V1
- [ ] Comparar limiar mediano vs percentil 60 de `cognitive_performance_score`
- [ ] Escrever relatório V2 separado

**Decisão:** V2 é uma evolução metodológica, não uma correção retroativa da V1.

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
