# Analise do audio sobre estrategia para o dataset Breast Cancer

**Audio:** `/home/cayo/Downloads/WhatsApp Ptt 2026-07-01 at 17.42.19.ogg`  
**Duracao:** 185,46s  
**Transcricao:** Faster-Whisper `small`, idioma `pt`, probabilidade `1.0`  
**Dataset citado:** `dataset/Breast_Cancer.csv`  

## Transcricao revisada

> "Cara, ta. E um dataset bom. Depende, mas tem que fazer o EDA para ver qual tipo de ferramenta voce vai aplicar. Como sao dados tabulares, nao te recomendo usar redes convolucionais, porque isso tem desempenho muito fraco para dados tabulares.
>
> Tem que usar aprendizado normal, pode ser SVM, XGBoost, LSTM, o proprio Random Forest, como o proprio dataset indica. E tu faz ensembles de deteccao com classificacao. Vai testando diversos, escolhe uns 5 para fazer o ensemble, os melhores, os que tem melhores resultados.
>
> Cuidado com overfit. Outra coisa: como e um caso de ensemble, tu tem que fazer um balanceamento dos teus resultados, do teu ensemble. Basicamente o ensemble e composto por varias ferramentas; no teu caso de classificacao, elas vao te dar o resultado, e a classificacao mais votada e a classificacao que teu ensemble vai dar.
>
> So que tu tem que fazer uma distribuicao de pesos para dar pontuacao para esse ensemble. Por exemplo, tua ferramenta mais assertiva provavelmente vai ser o LSTM ou XGBoost, entao a pontuacao dele vai ter que ser maior que os outros. Tudo depende do teu resultado.
>
> Como teu dataset e da area medica, tu tem que esquecer a acuracia. Tu tem que avaliar recall e precision. Tu tem que ver quais valores dao menos falsos negativos. Dataset e bom, faz aplicacao, nao testa so 5, testa mais, nao vai pela CNN, que nao vai ter resultado bom."

Observacao: a transcricao automatica confundiu alguns termos. Pela coerencia do contexto, "EIDA" foi interpretado como EDA, "CVM" como SVM, "CIGAS BUST/Stigibust" como XGBoost, "render florist" como Random Forest e "assemble" como ensemble.

## Metodo e estrategia sugeridos no audio

1. Fazer EDA antes de escolher o modelo.
2. Tratar o problema como classificacao tabular, nao como imagem/sequencia.
3. Evitar CNN para esse dataset, porque dados tabulares tendem a ter baixo ganho com convolucionais.
4. Testar varios modelos candidatos, nao apenas cinco.
5. Usar modelos adequados para tabular, especialmente Random Forest, SVM e XGBoost; o audio tambem cita LSTM, embora LSTM nao seja a escolha mais natural para esse CSV sem estrutura temporal.
6. Construir ensemble com os melhores modelos.
7. Usar votacao e, idealmente, votacao ponderada: modelos mais assertivos recebem maior peso.
8. Controlar overfitting.
9. Como e area medica, nao otimizar pela acuracia. Priorizar precision, recall e reducao de falsos negativos.

## O que foi feito no projeto

Arquivos avaliados:

- `baseline.py`
- `hybrid_neuro_fuzzy.py`
- `dataset/Breast_Cancer.csv`

### Baseline atual

O `baseline.py`:

- carrega o CSV com 4024 linhas e 16 colunas;
- usa `Status` como alvo, mapeando `Alive = 0` e `Dead = 1`;
- detecta forte desbalanceamento: `Alive = 84,69%`, `Dead = 15,31%`;
- aplica `StandardScaler` nas numericas e `OneHotEncoder` nas categoricas;
- treina Random Forest com `class_weight='balanced'`;
- treina MLP;
- usa `GridSearchCV` com `scoring='f1'`.

Resultados executados:

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC | Falsos negativos |
|---|---:|---:|---:|---:|---:|---:|
| Random Forest | 0,8907 | 0,7059 | 0,4878 | 0,5769 | 0,8418 | 63 |
| MLP | 0,8671 | 0,5800 | 0,4715 | 0,5202 | 0,7871 | 65 |

### Hibrido neuro-fuzzy atual

O `hybrid_neuro_fuzzy.py`:

- fuzzifica manualmente `Age`, `Tumor Size` e `Reginol Node Positive`;
- cria 9 features fuzzy;
- aplica one-hot encoding nas variaveis categoricas;
- concatena features fuzzy + categoricas, chegando a 43 atributos;
- treina uma MLP como motor de inferencia.

Resultado executado:

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC | Falsos negativos |
|---|---:|---:|---:|---:|---:|---:|
| Neuro-fuzzy cooperativo | 0,7913 | 0,2816 | 0,2358 | 0,2566 | 0,6142 | 94 |

## Comparacao com o que o audio recomendou

| Recomendacao do audio | Status no projeto | Comentario |
|---|---|---|
| Fazer EDA | Parcial | O projeto carrega e modela o CSV, mas nao ha EDA especifica versionada para o `projeto_2_neuro_fuzzy`. |
| Evitar CNN | Cumprido | Nao ha CNN nos scripts atuais. |
| Testar varios modelos tabulares | Parcial | Foram testados Random Forest e MLP. Faltam SVM, XGBoost/HistGradientBoosting, Logistic Regression, ExtraTrees etc. |
| Fazer ensemble | Nao cumprido | Nao existe ensemble implementado no projeto 2. |
| Usar votacao ponderada | Nao cumprido | Nao ha `VotingClassifier`, `StackingClassifier` ou regra de pesos. |
| Cuidar de overfit | Parcial | Existe CV no baseline, mas o hibrido usa split simples e MLP sem busca/validacao cruzada. |
| Priorizar precision/recall e falsos negativos | Parcial | As metricas sao exibidas, mas a selecao do modelo ainda nao otimiza diretamente recall ou falso negativo. |
| Nao usar acuracia como criterio principal | Parcial | O baseline usa F1 no grid search, mas a apresentacao ainda destaca acuracia. O hibrido parece fraco quando visto por recall/FN. |

## Diagnostico

A direcao atual do projeto nao segue a estrategia principal do audio. O baseline esta mais alinhado do que o neuro-fuzzy: usa modelo tabular forte, trata desbalanceamento no Random Forest e avalia metricas corretas. O hibrido neuro-fuzzy, apesar de estar coerente com o tema da disciplina, tem desempenho inferior nos criterios clinicos indicados no audio.

O ponto mais critico e falso negativo. Para `Dead = 1`, falso negativo significa prever `Alive` quando o registro real e `Dead`. O audio pede minimizar exatamente isso. Nesse criterio:

- Random Forest: 63 falsos negativos;
- MLP: 65 falsos negativos;
- Neuro-fuzzy: 94 falsos negativos.

Logo, o modelo hibrido atual piora o risco clinico em relacao aos baselines.

## Proximo caminho recomendado

1. Criar uma EDA especifica do `Breast_Cancer.csv`, documentando desbalanceamento, correlacoes, distribuicoes e variaveis clinicas mais relevantes.
2. Ampliar o baseline com modelos tabulares:
   - Random Forest;
   - ExtraTrees;
   - HistGradientBoosting;
   - XGBoost, se dependencia externa for permitida;
   - SVM calibrado;
   - Logistic Regression balanceada.
3. Usar metricas orientadas a risco:
   - recall da classe `Dead`;
   - precision da classe `Dead`;
   - F1/F2;
   - PR AUC;
   - matriz de confusao;
   - quantidade de falsos negativos.
4. Fazer ajuste de threshold para reduzir falsos negativos, em vez de aceitar threshold 0.5.
5. Montar ensemble com os melhores modelos:
   - primeiro `VotingClassifier` soft;
   - depois votacao ponderada com pesos proporcionais a validacao;
   - opcionalmente `StackingClassifier`.
6. Manter o neuro-fuzzy como comparativo academico, nao como modelo principal, a menos que ele seja refeito para otimizar recall/threshold e validacao.

