# Estado do Projeto: Trabalho 1 - Classificação em Saúde

**Status:** ✅ **100% Concluído — Entregue em 15/05/2026**

---

## 📌 Visão Geral
Comparação entre Random Forest e Redes Neurais para prever o estado de descanso (`felt_rested`) utilizando o Sleep Health Dataset.

## Fronteira de Escopo: V1 Oficial e V2 Experimental

- **V1 oficial:** permanece congelada com `felt_rested` como target primário. Esta é a narrativa histórica da entrega do Trabalho 1.
- **V2 experimental:** fica reservada para o alvo composto `sono_restaurador`, combinando `felt_rested` com `cognitive_performance_score`.
- **Regra de separação:** a análise de `cognitive_performance_score` pode justificar a V2 e enriquecer a discussão da V1, mas métricas da V2 não devem aparecer como resultado oficial da V1.

## 🚀 Aprendizados e Descobertas (Lições Aprendidas)

### 1. O Teto de Performance (The 74% Ceiling)
- **Descoberta:** Identificamos um limite de acurácia em torno de **73.4% - 74.5%** para todos os modelos testados (RF, NN, Gradient Boosting).
- **Causa:** O diagnóstico de ambiguidade revelou que existem perfis de usuários muito semelhantes (sono, estresse e rotina parecidos) que resultam em labels diferentes. Isso indica que o dataset possui ruído intrínseco ou falta de variáveis (ex: dieta, genética) para uma separação perfeita.
- **Ação:** No relatório final, a narrativa deve focar não na busca por 100% de acurácia, mas na aceitação deste limite como o patamar prático observado para este dado.

### 2. Contexto de Saúde: O Perigo dos Falsos Positivos
- **Decisão Crítica:** Optamos por priorizar a **Precisão para a classe 1 (Descansado)**.
- **Justificativa:** Um Falso Positivo (dizer que a pessoa está bem quando não está) pode ser mais sensível que um Falso Negativo, pois pode mascarar fadiga acumulada associada a risco ocupacional, incluindo **Burnout**.
- **Métrica Chave:** Precision (evitar falsos alarmes de descanso) e análise do `cognitive_performance_score`.
- **Cuidado de redação:** esta é uma interpretação de risco operacional, não uma validação clínica de burnout. O relatório deve dizer que a priorização de precision reduz o risco de classificar incorretamente pessoas cansadas como descansadas.

### 3. Engenharia de Atributos Avançada
- **O que tentamos:** Criamos `social_jetlag_factor`, `resilience_index`, `deep_sleep_ratio`, `sleep_efficiency` e `stress_work_interaction`.
- **Resultado:** Embora logicamente coerentes, essas variáveis não romperam o teto de 74%, reforçando a tese de que a ambiguidade está na percepção subjetiva do target (`felt_rested`).

### 4. Papel do `cognitive_performance_score`
- **Na V1:** foi removido das features para evitar vazamento conceitual, pois representa um desfecho pós-descanso.
- **Na análise:** serve como variável objetiva complementar para explicar por que `felt_rested` é subjetivo e por que uma V2 com `sono_restaurador` é metodologicamente interessante.
- **Na V2:** pode compor o target composto, desde que continue fora do conjunto de features.

## 🛠️ Decisões Técnicas (ADR-like)
- **Arquitetura RN:** Optamos por uma rede profunda (128-64-32-16) com BatchNormalization para estabilidade, dado o volume de 100k registros.
- **Modelo Campeão:** `HistGradientBoosting` (74.2%) superou ligeiramente a RN (73.4%) e a RF (73.7%), sugerindo que o tratamento nativo de features do GBDT é eficiente para este dataset.

## 📋 Próximos Passos (To-Do)
- [x] Integrar a narrativa final da V1 em relatório técnico e notebook consolidado.
- [x] Gerar gráficos comparativos finais da Fase 4.
- [x] Manter V1 e V2 separadas: V1 como entrega oficial; V2 como evolução metodológica.
- [ ] Decidir se a próxima execução será o Experimento V2 (`sono_restaurador`) ou o Trabalho 2.
- [ ] Para V2, executar `V2-1` a `V2-9` em `.specs/features/experimento-v2-sono-restaurador/tasks.md`.
- [ ] Para Trabalho 2, criar spec própria antes de implementar.
