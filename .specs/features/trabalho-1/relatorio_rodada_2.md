# Relatório Técnico: Rodada 2 — Otimização e Refinamento (T1)

## 1. Sumário da Rodada
A Rodada 2 focou em superar o baseline da Random Forest (74.15%) através de arquiteturas de Redes Neurais mais profundas e Engenharia de Atributos. Embora a Rede Neural tenha apresentado uma melhora marginal em relação ao seu próprio baseline, a Random Forest continua sendo o modelo mais robusto para este dataset tabular.

## 2. Implementações Técnicas
- **Engenharia de Atributos:**
  - `stress_work_interaction`: Interação entre nível de estresse e horas trabalhadas.
  - `sleep_efficiency`: Soma das fases REM e Sono Profundo.
  - `age_stress_ratio`: Razão estresse por idade.
- **Arquitetura da Rede Neural (v2):**
  - Estrutura: 128 -> 64 -> 32 -> 16 neurônios.
  - Inclusão de **BatchNormalization** após cada camada densa para estabilizar o gradiente.
  - **Dropout adaptativo** (0.3 e 0.2) para controlar o overfitting em camadas mais largas.
  - **Learning Rate Scheduler:** `ReduceLROnPlateau` para refinar a convergência no final do treino.

## 3. Resultados Comparativos Atualizados

| Modelo | Acurácia | ROC AUC | Evolução (Acc) |
| :--- | :--- | :--- | :--- |
| Random Forest (Rodada 1) | **74.15%** | **0.8218** | Baseline Campeão |
| Rede Neural (Rodada 1) | 73.23% | 0.8142 | - |
| **Rede Neural (Rodada 2)** | **73.36%** | 0.8145 | **+0.13%** |

## 4. Análise Crítica e Dificuldades
- **Limitação de Ganho:** O acréscimo de complexidade na rede (mais camadas e neurônios) resultou em um ganho de apenas **0.13%** na acurácia. Isso sugere que o "teto" de previsibilidade dos dados está sendo alcançado ou que o ruído intrínseco do dataset impede classificações mais precisas.
- **Overfitting:** Notou-se que a acurácia de treino chegou a ~75.4%, enquanto a de validação estagnou em ~73.6%. Mesmo com Dropout e BatchNormalization, a rede maior começou a memorizar padrões do conjunto de treino que não se generalizaram perfeitamente.
- **Discussão para Apresentação:** A superioridade da Random Forest (mesmo que por < 1%) reforça que para dados estruturados com muitas variáveis categóricas, modelos baseados em árvores são extremamente competitivos e muitas vezes preferíveis devido à menor complexidade de tuning.

## 5. Próximos Passos
- Como a entrega é em 8 dias, os modelos atuais são suficientes para um excelente trabalho acadêmico.
- Focar na **Fase 4: Consolidação**, gerando os gráficos comparativos finais e o documento de texto para o relatório.
