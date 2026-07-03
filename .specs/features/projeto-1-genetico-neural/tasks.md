# Tasks: Projeto 1 - Sistema Genetico-Neural GA-MLP

## Estado

Ultima revisao: 2026-07-02.

Legenda:
- `[x]` concluido e verificado
- `[~]` implementado, mas precisa evidencia melhor
- `[ ]` pendente

## Tarefas

| ID | Status | Tarefa | Evidencia/Gate |
|---|---|---|---|
| P1-GN-T001 | [x] | Confirmar requisito da segunda avaliacao | `materiais_de_aula/Avaliacao2026_1.pdf`; NotebookLM `26a8d20b-97fc-4d83-a513-55f2fa2f89f8` |
| P1-GN-T002 | [x] | Definir problema e dataset | `projeto_1_genetico_neural/dataset/heart_failure_clinical_records_dataset.csv` |
| P1-GN-T003 | [x] | Implementar EDA | `projeto_1_genetico_neural/eda_heart_failure.py` |
| P1-GN-T004 | [x] | Validar EDA localmente | `python eda_heart_failure.py` gera `eda_distribuicoes.png` e `eda_correlacao.png` |
| P1-GN-T005 | [x] | Implementar baseline RF e MLP | `projeto_1_genetico_neural/baseline.py` |
| P1-GN-T006 | [x] | Validar baseline localmente | RF F1 0.7059; MLP F1 0.4848 em 2026-07-02 |
| P1-GN-T007 | [x] | Implementar GA para feature selection | `hybrid_ga_mlp.py` bits de features |
| P1-GN-T008 | [x] | Expandir GA para topologia da MLP | `hybrid_ga_mlp.py` bits de neuronios ocultos |
| P1-GN-T009 | [x] | Validar execucao completa do GA-MLP | `reports/tables/ga_mlp_results.json` |
| P1-GN-T010 | [x] | Parametrizar GA-MLP para execucao auditavel | CLI com `--quick`, `--generations`, `--pop-size`, `--seed` |
| P1-GN-T011 | [x] | Salvar metricas completas do hibrido | `reports/tables/ga_mlp_results_quick.json` |
| P1-GN-T012 | [x] | Consolidar comparacao baseline vs GA-MLP | `reports/tables/model_comparison.csv` |
| P1-GN-T013 | [ ] | Adicionar analise critica de perda/ganho | Relatorio explica se hibrido melhorou ou piorou e por que |
| P1-GN-T014 | [ ] | Registrar trabalhos futuros | K-fold no fitness, multiplas sementes, SHAP/permutation importance |
| P1-GN-T015 | [ ] | Preparar roteiro de apresentacao | 15 minutos, com arquitetura, resultados, limitacoes e defesa metodologica |
| P1-GN-T016 | [x] | Criar notebook unico do processo | `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb` |
| P1-GN-T017 | [x] | Executar notebook por nbconvert | Validado com `projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert` |

## Sequencia Recomendada

1. **P1-GN-T013/P1-GN-T014**: fechar discussao critica.
2. **P1-GN-T015**: preparar apresentacao.
3. Opcional: registrar kernel Jupyter no `.venv` local do Projeto 1.

## Criterio de Fechamento

O Projeto 1 so deve voltar a aparecer como **concluido** no roadmap quando:

- `hybrid_ga_mlp.py` executou ate o fim em modo completo;
- os resultados foram salvos em artefato versionavel;
- a comparacao com RF e MLP foi registrada;
- a discussao explicar claramente ganho ou perda do hibrido contra baseline.
