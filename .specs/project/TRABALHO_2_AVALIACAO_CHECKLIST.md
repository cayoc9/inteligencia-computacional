# Checklist da Segunda Avaliacao - Trabalho 2

**Disciplina:** Inteligencia Computacional - UFPA 2026.1  
**Prazo:** 2026-07-03  
**Fonte primaria:** `materiais_de_aula/Avaliacao2026_1.pdf` e NotebookLM `26a8d20b-97fc-4d83-a513-55f2fa2f89f8`  
**Ultima revisao:** 2026-07-09

## Leitura do Enunciado

O Trabalho 2 pede um **Sistema de Inteligencia Computacional Hibrido ou Ensemble** que combine duas ou mais tecnicas da ementa, com relatorio tecnico e apresentacao. O relatorio deve justificar a arquitetura, explicar como as partes se comunicam, comparar ganho ou perda frente a uma abordagem simples, analisar resultados, desafios e trabalhos futuros.

## Projetos Cobertos

| Projeto | Tema | Tipo | Status |
|---|---|---|---|
| Projeto 1 | Heart Failure - GA-MLP | Genetico-Neural | Implementado, validado e documentado; permanece como apoio comparativo |
| Projeto 2 | Breast Cancer Survival Risk | Ensemble + Neuro-Fuzzy comparativo | Trilha escolhida; SEER corrigido + METABRIC canonico executados, documentados e materializados para defesa |

## Aderencia aos Criterios da Avaliacao

| Criterio | Projeto 1 GA-MLP | Projeto 2 Breast Cancer | Status Geral |
|---|---|---|---|
| Problema e dataset publico | Heart Failure Clinical Records, 299 registros | SEER/Kaggle Breast Cancer, 4024 registros brutos | Atendido |
| Sistema hibrido ou ensemble | GA seleciona features/topologia da MLP | Ensemble ponderado e neuro-fuzzy cooperativo comparativo | Atendido |
| Justificativa da arquitetura | Documentada em spec/design e resultados; nao e a trilha escolhida para apresentacao | Documentada em spec/design/relatorio tecnico/relatorio consolidado | Atendido |
| Comunicacao entre componentes | Cromossomo -> features/topologia -> MLP -> fitness F1 | Modelos tabulares -> pesos -> ensemble; fuzzy features -> MLP | Atendido |
| Baseline simples | RF e MLP | Logistic Regression, RF, MLP e outros tabulares | Atendido |
| Ganho/perda frente ao baseline | GA-MLP nao supera RF; melhora marginal sobre MLP | Ensemble reduz FN com threshold baixo, mas sacrifica acuracia | Atendido |
| Metricas robustas | Accuracy, precision, recall, F1, ROC AUC, matriz de confusao | Accuracy, balanced accuracy, precision, recall, F1, F2, ROC AUC, PR AUC, FN | Atendido |
| Analise critica | Achado registrado: GA-MLP valido, mas inferior a Random Forest no teste | Consolidada em relatorio final, roteiro, QA professorial e plano de slides | Atendido |
| Desafios de implementacao | Overfitting evolutivo e custo computacional | Vazamento por `Survival Months`, desbalanceamento, fuzzy fraco | Atendido |
| Trabalhos futuros | K-fold no fitness, multiplas sementes, interpretabilidade | Validacao clinica externa, survival analysis formal, explicabilidade local e custo clinico | Atendido |
| Relatorio tecnico | Evidencias e resultados existem; nao e o pacote principal de apresentacao | `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md` | Atendido |
| Apresentacao 15 min | Apoio comparativo se perguntarem | Roteiro, plano, HTML, PPTX e capturas de revisao materializados | Atendido com curadoria final pendente |

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

### Projeto 2 v2 - METABRIC canonico

| Evidencia | Local |
|---|---|
| Spec/design/tasks | `.specs/features/trabalho-2-breast-cancer-metabric/` |
| Notebook | `projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb` |
| Relatorio tecnico | `projeto_2_neuro_fuzzy_metabric_clinico/reports/relatorio_tecnico_projeto_2_metabric.md` |
| Comparacao sem vazamento | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/model_comparison_no_leakage.csv` |
| Ensemble | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/ensemble_validation_summary.csv`, `ensemble_test_summary.csv` |
| Figuras finais | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/` |

**Resultado principal:** GradientBoosting individual com F2 0.7787, recall 0.7953 e PR AUC 0.7600; ensemble com threshold 0.16, escolhido na validacao, atingiu F2 0.8770, recall 0.9953 e 1 falso negativo no teste, com 146 falsos positivos.

## Validacoes Executadas

| Gate | Resultado |
|---|---|
| `py_compile` dos scripts do Projeto 1 | Passou |
| JSONs do Projeto 1 | Passaram |
| Notebook Projeto 1 via `nbconvert` | Passou usando `projeto_2_neuro_fuzzy/.venv` |
| Testes Projeto 2 SEER | 20 passed com `projeto_2_neuro_fuzzy/.venv/bin/python -m pytest tests projeto_2_neuro_fuzzy/tests -q` |
| Testes Projeto 2 METABRIC | 7 passed com `PYTHONPATH=projeto_2_neuro_fuzzy_metabric_clinico/src projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy_metabric_clinico/tests -q` |
| `python projeto_2_neuro_fuzzy/run_pipeline.py` | Passou |
| Notebook Projeto 2 via `nbconvert` | Passou |
| Slides/defesa | HTML, PPTX, PDFs/capturas de revisao existem em `reports/consolidados/slides-trabalho-2/` |
| Artigo revisado | PDF existe em `docs/template/Breast_Cancer/main.pdf`; copia de revisao em `reports/consolidados/finalizacao-defesa-2026-07-09/artigo_prism_revisao_editorial_local.pdf` |

Observacao: o ambiente `projeto_1_genetico_neural/.venv` nao possui Jupyter/kernel registrado; a execucao do notebook do Projeto 1 foi validada com o ambiente do Projeto 2.

Observacao tecnica: nao usar a suite SEER + METABRIC no mesmo processo como gate unico. As duas trilhas possuem pacote Python com o mesmo nome (`breast_cancer_survival`), entao a ordem de import pode contaminar a suite combinada. O gate confiavel e executar as trilhas separadamente, como acima.

## O Que Ainda Pode Ser Feito

### P0 - Essencial para defesa

1. **Curadoria final dos slides/PPTX.**
   - Confirmar se a versao usada sera HTML, PPTX NotebookLM ou uma versao revisada manualmente.
   - Garantir que os slides mostrem tanto falsos negativos quanto falsos positivos.

2. **Revisao editorial do artigo no Overleaf.**
   - Conferir autores, emails, referencias, limite de paginas e figuras/tabelas finais.
   - Usar o PDF local revisado em `docs/template/Breast_Cancer/main.pdf` como base validada, nao como garantia de submissao final.

3. **Ensaio de fala do grupo.**
   - Distribuir tempo por integrante.
   - Manter a narrativa: SEER corrigido como baseline; METABRIC como evolucao canonica; ensemble como ponto operacional de alta sensibilidade.

### P1 - Melhora forte se houver tempo

1. **Rodar GA-MLP com 3 sementes.**
   - Objetivo: medir estabilidade do AG.
   - Resultado esperado: media/desvio de F1, recall e ROC AUC.
   - Custo: medio, pois o modo completo levou cerca de 255s por semente.

2. **Aprofundar estabilidade do Projeto 2.**
   - Ja existe `stability_summary.csv` em 5 sementes.
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

O trabalho esta **tecnicamente defensavel** para a segunda avaliacao. Os criterios centrais estao cobertos por codigo, notebooks, specs, resultados, relatorio consolidado, artigo-base e material de apresentacao. A principal lacuna restante saiu do eixo metodologico e ficou no eixo de **curadoria final de defesa**: revisao visual/editorial, ensaio de fala e conferencia qualitativa dos audios.

## Nota de Escolha

Como apenas um projeto sera apresentado, a matriz comparativa foi separada em `.specs/project/ESCOLHA_PROJETO_APRESENTACAO.md`. A recomendacao atual e apresentar o **Projeto 2 - Breast Cancer Survival Risk**, por maior completude metodologica, melhor documentacao e narrativa mais forte de ciencia de dados.
