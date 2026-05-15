# Especificação: Trabalho 1 - Classificação em Saúde

## Problema
Comparar Random Forest e Redes Neurais em uma tarefa de classificação binária usando dados de saúde do sono e desempenho diário.

## Dataset
- **Nome:** Sleep Health and Daily Performance Dataset
- **ID Kaggle:** `mohankrishnathalla/sleep-health-and-daily-performance-dataset`
- **Target Primário:** `felt_rested` (Binário: 0/1)
- **Target Secundário:** `sleep_disorder_risk` (Multiclasse)
- **Tipo de problema oficial:** classificação binária
- **Classes oficiais:** `0` = não se sentiu descansado; `1` = sentiu-se descansado
- **Features excluídas do treino V1:** `person_id`, `felt_rested`, `sleep_disorder_risk`, `cognitive_performance_score`

## Decisão De Escopo V1

A entrega oficial do Trabalho 1 fica congelada com `felt_rested` como target primário. A proposta de alvo composto `sono_restaurador`, combinando `felt_rested` com `cognitive_performance_score`, pertence a uma V2 experimental e não deve ser misturada com as métricas oficiais da V1.

Motivo: `felt_rested` atende diretamente ao enunciado de classificação binária e às métricas obrigatórias; `sono_restaurador` melhora a formulação científica, mas exige nova execução, nova distribuição de classes e nova discussão metodológica.

`felt_rested` foi mantido como alvo oficial porque permite uma comparação binária direta entre Random Forest e Rede Neural com matriz de confusão, precision, recall, F1, curva ROC e AUC sem adaptações multiclasse. Essa escolha também preserva comparabilidade entre modelos, já que RF e RN usam o mesmo split estratificado, o mesmo conjunto de features e a mesma interpretação de erro.

## Limite Metodológico Reconhecido

`felt_rested` é uma medida subjetiva. O diagnóstico da Rodada 3 indica que parte do teto de performance vem dessa subjetividade: perfis parecidos de sono, estresse e rotina podem produzir respostas diferentes.

Esse limite não invalida a V1. Ele deve ser apresentado como aprendizado metodológico e como justificativa para a V2.

## Camada Analítica Adicional

Como a classe positiva representa "sentiu-se descansado", um falso positivo significa classificar alguém como descansado quando a pessoa não está. Na narrativa de saúde ocupacional, esse erro pode mascarar fadiga acumulada.

Por isso, a V1 pode defender a precision da classe 1 como métrica de decisão operacional, sem afirmar diagnóstico clínico de burnout. A formulação recomendada é: "priorizar precision reduz o risco de falsos alarmes de descanso".

`cognitive_performance_score` deve ser usado apenas na discussão como evidência objetiva complementar, não como feature da V1.

## Requisitos de Implementação (ID-REQ)
- **REQ-01:** EDA completo (distribuições, correlações, outliers).
- **REQ-02:** Pré-processamento (One-hot encoding, Normalização/Padronização).
- **REQ-03:** Divisão Treino/Teste (opcional Validação).
- **REQ-04:** Random Forest com Fine-tuning (`n_estimators`, `max_depth`).
- **REQ-05:** Redes Neurais com Fine-tuning de hiperparâmetros.

## Métricas Obrigatórias (ID-MET)
- **MET-01:** Acurácia (Accuracy)
- **MET-02:** Matriz de Confusão
- **MET-03:** Precisão (Precision)
- **MET-04:** Recall (Sensibilidade)
- **MET-05:** F1-Score
- **MET-06:** Curva ROC e AUC

## Resultados Oficiais Da V1

| Modelo | Papel na V1 | Observação |
|---|---|---|
| Random Forest ajustada | Modelo clássico principal | Base direta exigida pelo PDF |
| Rede Neural MLP baseline | Modelo conexionista principal | Comparação direta contra RF |
| Rede Neural MLP otimizada | Variação de otimização | Ganho marginal sobre baseline |
| HistGradientBoosting | Diagnóstico complementar | Usado para investigar teto e threshold, não substitui a comparação RF vs RN |

## Regras De Relatório

- A V1 deve ser narrada como experimento histórico real, sem reescrever o alvo depois dos resultados.
- A discussão deve assumir explicitamente que `felt_rested` é subjetivo.
- A ideia de `sono_restaurador` deve aparecer apenas como trabalho futuro ou V2.
- Tabelas oficiais da V1 não devem incluir métricas de modelos treinados para `sono_restaurador`.
- A narrativa de burnout deve ser descrita como risco operacional, não como prova clínica.
