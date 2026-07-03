# Relatorio Tecnico: Projeto 2 Breast Cancer

## Objetivo corrigido

O objetivo corrigido e classificar risco de obito observado (`Status = Dead`) a partir de variaveis clinico-patologicas registradas no dataset, excluindo informacao de acompanhamento posterior.

Esta formulacao e mais segura do que dizer "predicao no diagnostico", pois algumas variaveis do dataset, como nodos positivos e estadiamento, podem depender de avaliacao clinico-patologica posterior ao primeiro contato diagnostico. O projeto nao modela tempo ate evento nem censura; portanto, deve ser lido como classificacao tabular educacional, nao como modelo clinico de sobrevivencia.

## Objetivo testado antes

O baseline inicial usava `Survival Months` como feature para prever `Status`. Essa configuracao deve ser interpretada como experimento contaminado por informacao posterior ao acompanhamento, nao como predicao em diagnostico.

## Dicionario de dados

O dicionario especifico do Projeto 2 fica em `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` e documenta colunas brutas, nomes sanitizados, tipos, papeis analiticos, risco de vazamento e features derivadas.

## Metadados e relacoes

A EDA gera `metadata_profile.csv`, `numeric_relationships.csv` e `categorical_relationships.csv`. Esses arquivos registram cardinalidade, tipos, exemplos, relacoes com `Status` e alerta de vazamento/follow-up para `Survival Months`.

## Modelagem

O pipeline compara modelos tabulares, aplica threshold tuning e monta ensemble ponderado. A avaliacao prioriza falsos negativos, recall, precision, F2 e PR AUC, em vez de acuracia isolada.

Correcao metodologica aplicada: o projeto agora usa `treino / validacao / teste`. Os modelos base sao ajustados em treino, pesos do ensemble e threshold sao escolhidos exclusivamente na validacao, e as metricas finais do ensemble sao reportadas no teste intocado.

### Resultados sem `Survival Months` apos otimizacoes

| Modelo | Accuracy | Precision | Recall | F2 | PR AUC | Falsos negativos |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.6807 | 0.2641 | 0.6098 | 0.4832 | 0.3525 | 48 |
| Random Forest | 0.7801 | 0.3151 | 0.3740 | 0.3605 | 0.2905 | 77 |
| ExtraTrees | 0.7963 | 0.3153 | 0.2846 | 0.2902 | 0.2840 | 88 |
| MLP | 0.7975 | 0.3214 | 0.2927 | 0.2980 | 0.3020 | 87 |
| GradientBoosting | 0.8484 | 0.5152 | 0.1382 | 0.1619 | 0.3503 | 106 |
| HistGradientBoosting | 0.8224 | 0.3214 | 0.1463 | 0.1642 | 0.2896 | 105 |
| SVM calibrado | 0.8522 | 0.6429 | 0.0732 | 0.0889 | 0.3439 | 114 |
| AdaBoost | 0.8460 | 0.0000 | 0.0000 | 0.0000 | 0.3293 | 123 |

### Ensemble ponderado

Na validacao, o ensemble ponderado escolheu threshold 0.22 para maximizar F2/recall, com recall 0.7561, F2 0.5099 e PR AUC 0.3360. Esse threshold foi entao congelado e aplicado no teste intocado.

No teste, o ensemble com threshold escolhido na validacao obteve accuracy 0.5665, precision 0.2271, recall 0.7642, F2 0.5188, PR AUC 0.3196, 29 falsos negativos e 320 falsos positivos. A leitura correta continua sendo trade-off de sensibilidade, nao ganho universal.

Tambem e importante notar que a PR AUC do ensemble (0.3196) ficou abaixo de Logistic Regression (0.3525), GradientBoosting (0.3503) e SVM calibrado (0.3439). Assim, o ensemble nao deve ser apresentado como melhor discriminador global; ele representa um ponto operacional agressivo para capturar mais casos `Dead`.

## Neuro-fuzzy

O neuro-fuzzy e mantido como comparativo academico. A implementacao usa funcoes de pertinencia manuais mais MLP, portanto deve ser descrita como neuro-fuzzy cooperativo, nao como ANFIS completo.

Resultado do neuro-fuzzy cooperativo: accuracy 0.8112, precision 0.3505, recall 0.2764, F2 0.2886, PR AUC 0.3052 e 89 falsos negativos. Portanto, ele nao superou os baselines tabulares no criterio clinico principal.

## Explicabilidade e calibracao

Foram adicionados artefatos de explicabilidade pos-modelo para a Logistic Regression e de calibracao para os modelos que mais importam na defesa oral:

- `logistic_regression_top_coefficients.csv`: os maiores coeficientes absolutos destacam `node_positive_band_high`, `node_positive_ratio`, `n_stage_ord`, `grade` e `tumor_grade_burden` como sinais relevantes.
- `logistic_regression_permutation_importance.csv`: por PR AUC, `node_positive_ratio`, `n_stage_ord`, `tumor_grade_burden`, `regional_node_positive` e `grade` aparecem como variaveis mais influentes.
- `calibration_summary.csv`: a Logistic Regression teve Brier score 0.2055, o SVM calibrado 0.1179 e o ensemble 0.1414. Isso nao autoriza falar em risco clinico calibrado, mas melhora a defesa quando a banca cobrar qualidade probabilistica.

## Estabilidade por sementes

Foi adicionada uma analise curta de robustez em 5 sementes (`stability_summary.csv`) comparando o baseline forte e o ensemble corrigido:

- Logistic Regression: recall medio 0.6179 +- 0.0752, F2 medio 0.4983 +- 0.0560, PR AUC media 0.3780 +- 0.0338 e 47 falsos negativos em media.
- Ensemble ponderado: recall medio 0.7724 +- 0.0959, F2 medio 0.5048 +- 0.0311, PR AUC media 0.3422 +- 0.0317 e 28 falsos negativos em media.

Isso reforca a leitura principal do projeto: o ensemble tende a capturar mais casos `Dead`, mas paga esse ganho com mais falsos positivos e variabilidade operacional maior que a regressao logistica.

## Fork METABRIC clinico

Foi criado um fork em `projeto_2_neuro_fuzzy_metabric_clinico/` para aprendizado continuo com dataset clinico melhor. O METABRIC traz tratamento, biomarcadores e subtipo molecular, permitindo features mais ricas que o SEER atual.

No METABRIC, sem usar meses de sobrevida, o melhor modelo individual foi `gradient_boosting`: accuracy 0.7048, precision 0.7185, recall 0.7953, F2 0.7787, PR AUC 0.7600 e 44 falsos negativos. O ensemble corrigido, com threshold 0.16 escolhido na validacao, chegou a recall 0.9953, F2 0.8770 e 1 falso negativo, com 146 falsos positivos no teste. Esse resultado confirma que o novo dataset e mais adequado para experimentacao de melhoria continua e agora segue o mesmo padrao metodologico do SEER corrigido.

## Limites e trabalhos futuros

- Definir horizonte temporal explicito para o alvo ou migrar para analise de sobrevivencia.
- Confirmar disponibilidade temporal das variaveis clinico-patologicas usadas como features.
- Ampliar a estabilidade por validacao cruzada estratificada, e nao apenas repeticao curta por seeds.
- Ampliar calibracao probabilistica com analise por faixas de decisao e custo.
- Adicionar explicabilidade local por instancia, caso a apresentacao exija justificativa individual.
