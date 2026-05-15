# Tarefas: Experimento V2 - `sono_restaurador`

## Fase 1: Especificacao Do Alvo

- [ ] **V2-1:** Criar coluna derivada `sono_restaurador` com limiar mediano (`cognitive_performance_score >= 60.4`).
  - Done when: distribuicao do target salva e documentada.
- [ ] **V2-2:** Criar variante de sensibilidade com percentil 60 (`cognitive_performance_score >= 66.4`).
  - Done when: comparacao de distribuicao entre os dois limiares estiver registrada.
- [ ] **V2-3:** Confirmar lista final de features sem vazamento.
  - Done when: `felt_rested`, `cognitive_performance_score`, `sleep_disorder_risk` e `person_id` estiverem fora de `X`.

## Fase 2: Modelagem Comparavel A V1

- [ ] **V2-4:** Reexecutar Random Forest com o mesmo protocolo da V1.
  - Done when: metricas e matriz de confusao forem salvas.
- [ ] **V2-5:** Reexecutar Rede Neural MLP com o mesmo protocolo da V1.
  - Done when: historico de treino e metricas forem salvos.
- [ ] **V2-6:** Avaliar threshold tuning para o novo target.
  - Done when: melhor threshold por F1 e balanced accuracy estiver documentado.

## Fase 3: Analise E Relatorio

- [ ] **V2-7:** Comparar V1 vs V2 sem misturar tabelas oficiais.
  - Done when: houver uma secao clara de "evolucao metodologica".
- [ ] **V2-8:** Escrever relatorio V2 separado.
  - Done when: resultados V2 estiverem em documento proprio.
- [ ] **V2-9:** Atualizar roadmap com decisao de continuidade.
  - Done when: V2 estiver marcada como continuar, pausar ou descartar.

