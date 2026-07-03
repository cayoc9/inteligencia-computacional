# Checklist da Segunda Avaliacao - Trabalho 2

**Disciplina:** Inteligencia Computacional - UFPA 2026.1  
**Prazo:** 2026-07-03  
**Fonte primaria:** `materiais_de_aula/Avaliacao2026_1.pdf` e NotebookLM `26a8d20b-97fc-4d83-a513-55f2fa2f89f8`  
**Ultima revisao:** 2026-07-02

## Leitura do Enunciado

O Trabalho 2 pede um **Sistema de Inteligencia Computacional Hibrido ou Ensemble** que combine duas ou mais tecnicas da ementa, com relatorio tecnico e apresentacao. O relatorio deve justificar a arquitetura, explicar como as partes se comunicam, comparar ganho ou perda frente a uma abordagem simples, analisar resultados, desafios e trabalhos futuros.

## Projetos Cobertos

| Projeto | Tema | Tipo | Status |
|---|---|---|---|
| Projeto 1 | Heart Failure - GA-MLP | Genetico-Neural | Implementado, validado e documentado; falta redacao final da discussao |
| Projeto 2 | Breast Cancer Survival Risk | Ensemble + Neuro-Fuzzy comparativo | Pipeline spec-driven executado e documentado; falta redacao final da discussao |

## Aderencia aos Criterios da Avaliacao

| Criterio | Projeto 1 GA-MLP | Projeto 2 Breast Cancer | Status Geral |
|---|---|---|---|
| Problema e dataset publico | Heart Failure Clinical Records, 299 registros | SEER/Kaggle Breast Cancer, 4024 registros brutos | Atendido |
| Sistema hibrido ou ensemble | GA seleciona features/topologia da MLP | Ensemble ponderado e neuro-fuzzy cooperativo comparativo | Atendido |
| Justificativa da arquitetura | Parcialmente documentada em spec/design; falta texto final de relatorio | Documentada em spec/design/relatorio tecnico | Quase atendido |
| Comunicacao entre componentes | Cromossomo -> features/topologia -> MLP -> fitness F1 | Modelos tabulares -> pesos -> ensemble; fuzzy features -> MLP | Atendido |
| Baseline simples | RF e MLP | Logistic Regression, RF, MLP e outros tabulares | Atendido |
| Ganho/perda frente ao baseline | GA-MLP nao supera RF; melhora marginal sobre MLP | Ensemble reduz FN com threshold baixo, mas sacrifica acuracia | Atendido |
| Metricas robustas | Accuracy, precision, recall, F1, ROC AUC, matriz de confusao | Accuracy, balanced accuracy, precision, recall, F1, F2, ROC AUC, PR AUC, FN | Atendido |
| Analise critica | Achado registrado; falta redacao final | Relatorio tecnico existe; revisar narrativa final | Parcial |
| Desafios de implementacao | Overfitting evolutivo e custo computacional | Vazamento por `Survival Months`, desbalanceamento, fuzzy fraco | Atendido |
| Trabalhos futuros | K-fold no fitness, multiplas sementes, interpretabilidade | Validacao clinica, estabilidade, explicabilidade local, calibracao adicional | Parcial |
| Relatorio tecnico | Pendente de redacao final | `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md` | Parcial |
| Apresentacao 15 min | Pendente | Pendente | Pendente |

## Evidencias de Execucao

### Projeto 1

| Evidencia | Local |
|---|---|
| Spec | `.specs/features/projeto-1-genetico-neural/spec.md` |
| Design | `.specs/features/projeto-1-genetico-neural/design.md` |
| Tasks | `.specs/features/projeto-1-genetico-neural/tasks.md` |
| Notebook | `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb` |
| Resultado completo GA-MLP | `projeto_1_genetico_neural/reports/tables/ga_mlp_results.json` |
| Comparacao final | `projeto_1_genetico_neural/reports/tables/model_comparison.csv` |
| Figura evolucao | `projeto_1_genetico_neural/reports/figures/evolucao_genetica.png` |

**Resultado principal:** Random Forest F1 0.7059; MLP F1 0.4848; GA-MLP full F1 0.5000.  
**Interpretacao:** O hibrido e valido como arquitetura, mas nao foi o melhor classificador no dataset pequeno.

### Projeto 2

| Evidencia | Local |
|---|---|
| Spec | `.specs/features/trabalho-2-breast-cancer/spec.md` |
| Design | `.specs/features/trabalho-2-breast-cancer/design.md` |
| Tasks | `.specs/features/trabalho-2-breast-cancer/tasks.md` |
| Dicionario | `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` |
| Notebook | `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb` |
| Relatorio tecnico | `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md` |
| Comparacao sem vazamento | `projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage.csv` |
| Sensibilidade com `Survival Months` | `projeto_2_neuro_fuzzy/reports/tables/model_comparison_with_survival_months.csv` |
| Ensemble | `projeto_2_neuro_fuzzy/reports/tables/ensemble_validation_summary.csv`, `ensemble_test_summary.csv` |
| Neuro-fuzzy | `projeto_2_neuro_fuzzy/reports/tables/neuro_fuzzy_comparison.csv` |
| Explicabilidade/calibracao | `projeto_2_neuro_fuzzy/reports/tables/logistic_regression_top_coefficients.csv`, `logistic_regression_permutation_importance.csv`, `calibration_summary.csv` |
| Estabilidade | `projeto_2_neuro_fuzzy/reports/tables/stability_summary.csv` |

**Resultado principal:** ensemble com threshold 0.22, escolhido na validacao, reduziu falsos negativos para 29 no teste, com recall 0.7642, F2 0.5188 e 320 falsos positivos.  
**Interpretacao:** A escolha e defensavel se o objetivo prioriza sensibilidade para risco de obito, mas deve ser apresentada como trade-off operacional, nao como melhor discriminador global.

## Validacoes Executadas

| Gate | Resultado |
|---|---|
| `py_compile` dos scripts do Projeto 1 | Passou |
| JSONs do Projeto 1 | Passaram |
| Notebook Projeto 1 via `nbconvert` | Passou usando `projeto_2_neuro_fuzzy/.venv` |
| Testes Projeto 2 | 17 passed |
| `python projeto_2_neuro_fuzzy/run_pipeline.py` | Passou |
| Notebook Projeto 2 via `nbconvert` | Passou |

Observacao: o ambiente `projeto_1_genetico_neural/.venv` nao possui Jupyter/kernel registrado; a execucao do notebook do Projeto 1 foi validada com o ambiente do Projeto 2.

## O Que Ainda Pode Ser Feito

### P0 - Essencial para entrega

1. **Redigir relatorio final unificado da segunda avaliacao.**
   - Deve ter uma secao para Projeto 1 e outra para Projeto 2.
   - Deve explicar que nem todo hibrido melhora performance.
   - Deve mostrar tabelas finais dos dois projetos.

2. **Preparar apresentacao de 15 minutos.**
   - 2 min: problema e criterios da avaliacao.
   - 4 min: Projeto 1 GA-MLP.
   - 5 min: Projeto 2 Breast Cancer.
   - 2 min: comparacao critica dos hibridos/ensemble.
   - 2 min: conclusoes e trabalhos futuros.

3. **Gerar PDF final.**
   - Consolidar relatorio tecnico, tabelas e figuras.
   - Garantir que os caminhos de artefatos estejam corretos.

### P1 - Melhora forte se houver tempo

1. **Rodar GA-MLP com 3 sementes.**
   - Objetivo: medir estabilidade do AG.
   - Resultado esperado: media/desvio de F1, recall e ROC AUC.
   - Custo: medio, pois o modo completo levou cerca de 255s por semente.

2. **Adicionar tabela de estabilidade do Projeto 2.**
   - Parcialmente atendido com `stability_summary.csv` em 5 sementes.
   - Melhorar depois com validacao cruzada estratificada.

3. **Aprofundar a interpretabilidade.**
   - Projeto 1: permutation importance das features selecionadas pelo GA.
   - Projeto 2: explicabilidade local por instancia ou SHAP se houver tempo.

### P2 - Trabalhos futuros, nao bloquear entrega

1. K-fold dentro do fitness do GA-MLP.
2. Calibragem fuzzy com especialista clinico.
3. Recalibracao probabilistica e analise de threshold por custo.
4. Validacao externa em outro dataset.

## Riscos de Apresentacao

| Risco | Como responder |
|---|---|
| "Por que o hibrido perdeu para Random Forest?" | Dataset pequeno e tabular favorece arvores; o objetivo era projetar e avaliar criticamente o hibrido, nao forcar superioridade. |
| "Por que usar F1 no GA?" | Classe positiva representa obito e o dataset e desbalanceado; F1 equilibra precision/recall melhor que acuracia. |
| "Por que `Survival Months` foi removido?" | E informacao de acompanhamento posterior; no modelo principal de diagnostico isso e vazamento conceitual. |
| "O neuro-fuzzy e ANFIS?" | Nao. E um modelo cooperativo com fuzzificacao manual + MLP; isso esta documentado para evitar alegacao exagerada. |
| "O ensemble com accuracy baixa e ruim?" | Depende do objetivo. Ele prioriza reduzir falsos negativos; a baixa accuracy vem do aumento de falsos positivos. |
| "O threshold foi escolhido no teste?" | Nao. A versao corrigida usa validacao separada para threshold e pesos, e teste intocado para reporte final. |
| "Qual e o horizonte temporal do alvo?" | O projeto classifica o desfecho observado no registro. Como ha `Survival Months`, uma modelagem de sobrevivencia seria trabalho futuro mais adequado para horizonte temporal. |

## Decisao Final de Qualidade

O trabalho esta **tecnicamente defensavel** para a segunda avaliacao. Os criterios centrais estao cobertos por codigo, notebooks, specs e resultados. A principal lacuna restante saiu do eixo metodologico grave e foi para o eixo de **robustez e comunicacao academica**: estabilidade por sementes, narrativa de trade-off e defesa das limitacoes.

## Nota de Escolha

Como apenas um projeto sera apresentado, a matriz comparativa foi separada em `.specs/project/ESCOLHA_PROJETO_APRESENTACAO.md`. A recomendacao atual e apresentar o **Projeto 2 - Breast Cancer Survival Risk**, por maior completude metodologica, melhor documentacao e narrativa mais forte de ciencia de dados.
