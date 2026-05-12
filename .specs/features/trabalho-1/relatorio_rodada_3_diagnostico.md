# Relatório Técnico: Rodada 3 — Diagnóstico de Performance e Plano de Otimização

## 1. Pergunta da Rodada

O objetivo desta rodada foi responder três perguntas:

1. O resultado está realmente ruim?
2. A modelagem atual fez tudo que poderia com os dados?
3. O que faltou para uma otimização mais rigorosa?

Para isso, foi criado o script `scripts/diagnose_model_limits.py`, que compara modelos adicionais, mede baseline ingênuo, avalia ajuste de limiar, valida um modelo forte com validação cruzada e analisa importância/ambiguidade das features.

## 2. Resultado Não É Ruim, Mas Tem Teto Claro

O baseline de classe majoritária acerta **60,99%**, mas tem `balanced_accuracy=0,50`, `F1=0,00` e `ROC AUC=0,50`, pois simplesmente prevê sempre a classe 0. Portanto, a Random Forest com ~74% de acurácia e AUC ~0,82 não é fraca em relação ao ponto de partida.

O melhor modelo testado nesta rodada foi `HistGradientBoosting`:

| Modelo | Accuracy | Balanced Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|
| HistGradientBoosting | 0,7425 | 0,7250 | 0,6787 | 0,6453 | 0,6616 | 0,8258 |
| Random Forest tuned-like | 0,7378 | 0,7309 | 0,6528 | 0,6999 | 0,6756 | 0,8216 |
| Logistic Regression | 0,7315 | 0,7332 | 0,6332 | 0,7410 | 0,6828 | 0,8126 |
| Extra Trees | 0,7321 | 0,7211 | 0,6521 | 0,6711 | 0,6615 | 0,8110 |

Leitura: trocar de família de modelo melhora pouco. O ganho máximo observado sobre a Random Forest anterior foi marginal em AUC. Isso sugere que o gargalo principal não é apenas arquitetura.

## 3. Por Que Parece Ruim?

### 3.1 Acurácia é uma métrica limitada aqui

O target é desbalanceado:

- Classe 0: **60.988 registros** (**60,99%**)
- Classe 1: **39.012 registros** (**39,01%**)

Um modelo ingênuo já atinge ~61% de acurácia sem aprender nada sobre a classe positiva. Por isso, o resultado deve ser julgado por `ROC AUC`, `balanced_accuracy`, `recall` e `F1`, não apenas por acurácia.

### 3.2 O limiar 0,5 não é necessariamente o melhor

Com o melhor modelo (`HistGradientBoosting`), o limiar padrão 0,5 gerou F1 de **0,6616**. Ajustando o limiar:

- Melhor F1 em threshold **0,35**: `F1=0,7017`, `recall=0,8491`, `accuracy=0,7184`
- Melhor balanced accuracy em threshold **0,39**: `balanced_accuracy=0,7424`, `F1=0,6981`, `recall=0,8026`

Isso mostra que o modelo ranqueia relativamente bem, mas o ponto de corte padrão sacrifica recall da classe 1.

### 3.3 O alvo `felt_rested` parece subjetivo/ruidoso

As variáveis mais fortes são poucas:

| Feature | AUC isolado ajustado |
|---|---:|
| `sleep_quality_score` | 0,7849 |
| `sleep_duration_hrs` | 0,7738 |
| `stress_score` | 0,7125 |
| `work_hours_that_day` | 0,6454 |
| `wake_episodes_per_night` | 0,6352 |

Pela permutation importance do melhor modelo, praticamente todo o sinal relevante ficou concentrado em:

1. `sleep_duration_hrs`
2. `sleep_quality_score`
3. `wake_episodes_per_night`
4. `stress_score`

As demais variáveis adicionam pouco sinal incremental. Isso reduz a margem de ganho para modelos mais complexos.

### 3.4 Há ambiguidade dentro de grupos parecidos

Agrupando combinações de qualidade do sono, estresse, horas trabalhadas e duração do sono, a taxa média da classe minoritária dentro dos grupos foi **18,8%**, com percentil 90 em **39,6%**. Em termos práticos: mesmo entre pessoas com perfis parecidos nas principais variáveis, ainda há mistura relevante de `felt_rested=0` e `felt_rested=1`.

Isso é compatível com um alvo subjetivo: duas pessoas com sono parecido podem responder diferente sobre terem se sentido descansadas.

## 4. Fez Tudo Que Poderia?

Não. O projeto fez o suficiente para uma comparação acadêmica inicial bem defendável, mas ainda não fez uma otimização exaustiva.

O que já foi feito:

- EDA básica e correlações.
- Pré-processamento com `ColumnTransformer`.
- Split estratificado.
- Random Forest com `GridSearchCV`.
- MLP baseline.
- MLP otimizada com feature engineering, BatchNormalization, Dropout e ReduceLROnPlateau.
- Comparação com métricas obrigatórias.

O que faltou para dizer que “otimizamos seriamente”:

- Validação cruzada sistemática para todos os modelos, não apenas holdout.
- Otimização de limiar de decisão conforme objetivo do problema.
- Métricas adicionais: `balanced_accuracy`, PR AUC e curva Precision-Recall.
- Busca mais ampla de hiperparâmetros por `RandomizedSearchCV`, Optuna ou equivalente.
- Testar gradient boosting dedicado para tabular, como LightGBM, XGBoost ou CatBoost.
- Testar `class_weight`, focal loss ou estratégia de custo para a classe 1.
- Comparar redes neurais com embeddings para variáveis categóricas, não apenas one-hot.
- Fazer análise de erro: quais perfis são mais confundidos?
- Fazer SHAP/permutation importance formal para discussão interpretável.
- Avaliar outro alvo (`sleep_disorder_risk`) como experimento complementar.

## 5. Melhor Próximo Plano

Para maximizar ganho sem perder prazo:

1. **Ajustar threshold do melhor modelo** e reportar dois cenários: maior acurácia vs maior F1/recall.
2. **Rodar um modelo gradient boosting tabular forte** (`HistGradientBoosting` já testado; idealmente LightGBM/CatBoost se puder instalar).
3. **Adicionar análise de erro por grupos**: por qualidade do sono, estresse, duração e ocupação.
4. **Adicionar curva Precision-Recall** para avaliar melhor a classe positiva.
5. **Usar interpretabilidade**: permutation importance ou SHAP para explicar por que o modelo acerta/erra.

## 6. Conclusão Técnica

O desempenho atual não é simplesmente “ruim”; ele parece estar perto do teto prático para `felt_rested` usando as features disponíveis sem vazamento de alvo. A melhoria real mais promissora não é aprofundar ainda mais a rede neural, mas ajustar a formulação: métrica, threshold, análise de erro, modelos gradient boosting e talvez escolha de target.

Para apresentação, a conclusão forte é: a Random Forest venceu porque o problema é tabular, o alvo é parcialmente subjetivo e o sinal útil está concentrado em poucas variáveis. A rede neural não fracassou; ela encontrou praticamente o mesmo limite com maior complexidade.
