# Relatorio Tecnico: Projeto 2 METABRIC Clinico

## Objetivo

Este fork avalia o mesmo tema do Projeto 2, cancer de mama e risco de obito, usando o dataset clinico METABRIC do Kaggle. O objetivo principal e prever `Overall Survival Status = Deceased` sem usar `Overall Survival (Months)` como feature.

## Por que este fork existe

O dataset SEER usado no Projeto 2 original e adequado para demonstracao tabular, mas tem poucas variaveis sobre tratamento, biomarcadores e subtipo molecular. O METABRIC clinico melhora essa base de aprendizado porque inclui quimioterapia, hormonioterapia, radioterapia, ER/PR/HER2, subtipo PAM50, tamanho tumoral, estagio, grau, linfonodos, mutation count e Nottingham Prognostic Index.

## Contrato de dados

- Dataset bruto: 2509 linhas e 34 colunas.
- Dataset analitico: 1876 linhas apos remover registros sem alvo/tempo/variaveis centrais.
- Classe positiva: `Deceased = 1`.
- Distribuicao analitica: 801 vivos e 1075 obitos.
- Nulos remanescentes: 1081, tratados por imputacao no preprocessor.

## Politica de vazamento

Ficam fora do modelo principal:

- `survival_months`
- `relapse_free_status_months`
- `relapse_free_status`
- `patient_s_vital_status`
- `patient_id`

`survival_months` so entra no experimento de sensibilidade para mostrar o efeito de acompanhamento posterior nas metricas.

## Engenharia de features

O fork adiciona features especificas do METABRIC:

- carga tumoral: `tumor_grade_burden`, `tumor_stage_burden`, `node_stage_burden`;
- risco prognostico: `nottingham_grade_burden`, `mutation_density`;
- tratamento: `chemotherapy_flag`, `hormone_therapy_flag`, `radio_therapy_flag`, `treatment_count`;
- perfil molecular: `triple_negative_like`, `hr_positive_her2_negative`, `receptor_profile`, `pam50_risk_group`;
- discretizacoes: `tumor_size_band`, `age_band`;
- fuzzy: idade, tamanho tumoral, linfonodos e NPI.

## Resultados sem meses de sobrevida

| Modelo | Accuracy | Precision | Recall | F2 | PR AUC | Falsos negativos |
|---|---:|---:|---:|---:|---:|---:|
| GradientBoosting | 0.7048 | 0.7185 | 0.7953 | 0.7787 | 0.7600 | 44 |
| AdaBoost | 0.6649 | 0.6831 | 0.7721 | 0.7525 | 0.7301 | 49 |
| SVM calibrado | 0.6755 | 0.7031 | 0.7488 | 0.7392 | 0.7253 | 54 |
| HistGradientBoosting | 0.6755 | 0.7048 | 0.7442 | 0.7360 | 0.7679 | 55 |
| ExtraTrees | 0.6729 | 0.7150 | 0.7116 | 0.7123 | 0.7581 | 62 |
| Random Forest | 0.6622 | 0.7157 | 0.6791 | 0.6861 | 0.7516 | 69 |
| MLP | 0.6250 | 0.6637 | 0.6977 | 0.6906 | 0.7037 | 65 |
| Logistic Regression | 0.6383 | 0.7182 | 0.6047 | 0.6244 | 0.7243 | 85 |

## Ensemble e threshold

O ensemble do fork foi corrigido para usar `treino / validacao / teste`, com pesos e threshold definidos na validacao e metricas finais reportadas no teste intocado.

O ensemble ponderado escolheu threshold 0.16 na validacao:

- accuracy: 0.6090
- precision: 0.5944
- recall: 0.9953
- F2: 0.8770
- PR AUC: 0.7586
- falsos negativos: 1
- falsos positivos: 146

Esse e um ponto operacional de alta sensibilidade. Ele e util para discutir trade-off clinico, mas nao deve ser vendido como melhoria universal porque aumenta falsos positivos.

## Explicabilidade, calibracao e robustez

O fork agora tambem produz:

- coeficientes e ranking da Logistic Regression;
- permutation importance do baseline linear;
- curvas de calibracao e Brier score;
- analise curta de estabilidade por 5 seeds para Logistic Regression e ensemble.

Esses artefatos colocam o METABRIC no mesmo patamar metodologico do SEER corrigido, com a diferenca de usar um dataset clinico mais forte.

## Neuro-fuzzy

O neuro-fuzzy cooperativo usa funcoes de pertinencia manuais para idade, tamanho tumoral, linfonodos e NPI, combinadas com MLP. Resultado:

- accuracy: 0.6170
- precision: 0.6699
- recall: 0.6512
- F2: 0.6548
- PR AUC: 0.7012
- falsos negativos: 75

Ele e melhor que o neuro-fuzzy no SEER, mas ainda fica abaixo dos melhores modelos tabulares do METABRIC.

## Conclusao

O METABRIC clinico e melhor para a meta pessoal de melhoria continua porque permite engenharia de features clinicamente mais rica, tem biomarcadores e tratamentos, e gerou desempenho substancialmente superior sem depender de `survival_months`. O proximo passo metodologico e transformar o problema em analise de sobrevivencia formal ou em classificacao por horizonte temporal, por exemplo obito em ate 60 meses, com tratamento correto de censura.
