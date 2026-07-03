# Fragmento do Relatorio - Diagnostico de Performance e Otimizacao

## O resultado esta ruim?

Nao no sentido tecnico. A classe majoritaria representa 60,99% do dataset, entao um baseline ingenuo que sempre prediz classe 0 ja teria aproximadamente 61% de acuracia, mas `F1=0`, `balanced_accuracy=0,50` e `ROC AUC=0,50`. Os modelos treinados chegam a aproximadamente 74% de acuracia e AUC em torno de 0,82, portanto aprendem sinal relevante.

O ponto critico e que a acuracia sozinha esconde parte do problema. Como `felt_rested=1` e a classe minoritaria, faz mais sentido olhar tambem F1, recall, balanced accuracy e ROC AUC.

## Por que nao passou muito de 74%?

O diagnostico indica que o gargalo esta menos na arquitetura e mais no proprio problema:

- O target `felt_rested` e subjetivo e provavelmente ruidoso.
- Poucas variaveis concentram quase todo o sinal preditivo: `sleep_duration_hrs`, `sleep_quality_score`, `wake_episodes_per_night` e `stress_score`.
- Modelos adicionais, como `HistGradientBoosting`, melhoraram pouco em relacao a Random Forest.
- Perfis parecidos de sono/estresse ainda misturam pessoas que se sentiram e nao se sentiram descansadas.

## Fez tudo que poderia?

Nao. Foi feito o suficiente para uma comparacao academica inicial, mas nao uma otimizacao exaustiva. Faltaram principalmente:

- Ajuste formal do threshold de decisao.
- Validação cruzada sistematica para todos os modelos.
- Curva Precision-Recall e PR AUC.
- Busca mais ampla de hiperparametros.
- Teste de LightGBM, XGBoost ou CatBoost.
- Analise de erro por segmentos.
- Interpretabilidade com SHAP ou permutation importance.
- Redes neurais com embeddings para categoricas.

## Principal oportunidade imediata

O melhor ganho sem mudar o dataset vem de ajustar o threshold. Com `HistGradientBoosting`, o threshold padrao 0,5 gerou F1 de 0,6616. Reduzindo o threshold para 0,35, o F1 sobe para 0,7017 e o recall da classe positiva sobe para 0,8491, embora a acuracia caia para 0,7184. Isso deve ser apresentado como trade-off: mais acertos globais ou maior sensibilidade para identificar quem se sentiu descansado.
