# Relatorio Tecnico: Projeto 2 Breast Cancer

## Objetivo corrigido

O objetivo corrigido e prever risco de obito (`Status = Dead`) a partir de atributos clinicos disponiveis no diagnostico.

## Objetivo testado antes

O baseline inicial usava `Survival Months` como feature para prever `Status`. Essa configuracao deve ser interpretada como experimento contaminado por informacao posterior ao acompanhamento, nao como predicao em diagnostico.

## Dicionario de dados

O dicionario especifico do Projeto 2 fica em `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` e documenta colunas brutas, nomes sanitizados, tipos, papeis analiticos, risco de vazamento e features derivadas.

## Metadados e relacoes

A EDA gera `metadata_profile.csv`, `numeric_relationships.csv` e `categorical_relationships.csv`. Esses arquivos registram cardinalidade, tipos, exemplos, relacoes com `Status` e alerta de vazamento/follow-up para `Survival Months`.

## Modelagem

O pipeline compara modelos tabulares, aplica threshold tuning e monta ensemble ponderado. A avaliacao prioriza falsos negativos, recall, precision, F2 e PR AUC, em vez de acuracia isolada.

### Resultados sem `Survival Months`

| Modelo | Accuracy | Precision | Recall | F2 | PR AUC | Falsos negativos |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.6919 | 0.2744 | 0.6179 | 0.4941 | 0.3686 | 47 |
| Random Forest | 0.7814 | 0.3037 | 0.3333 | 0.3270 | 0.2826 | 82 |
| ExtraTrees | 0.7863 | 0.2906 | 0.2764 | 0.2791 | 0.2772 | 89 |
| MLP | 0.8087 | 0.3038 | 0.1951 | 0.2102 | 0.2657 | 99 |
| HistGradientBoosting | 0.8360 | 0.4000 | 0.1463 | 0.1676 | 0.3124 | 105 |
| SVM calibrado | 0.8534 | 0.6471 | 0.0894 | 0.1081 | 0.3664 | 112 |

### Ensemble ponderado

O ensemble ponderado escolheu threshold 0.21 para maximizar F2/recall. Esse ponto reduziu falsos negativos para 16 e obteve recall 0.8699, mas aumentou falsos positivos para 398. A leitura correta e trade-off de sensibilidade, nao ganho universal.

## Neuro-fuzzy

O neuro-fuzzy e mantido como comparativo academico. A implementacao usa funcoes de pertinencia manuais mais MLP, portanto deve ser descrita como neuro-fuzzy cooperativo, nao como ANFIS completo.

Resultado do neuro-fuzzy cooperativo: accuracy 0.7764, precision 0.2683, recall 0.2683, F2 0.2683, PR AUC 0.2365 e 90 falsos negativos. Portanto, ele nao superou os baselines tabulares no criterio clinico principal.
