# Fragmento do Relatorio - Resultados Comparativos

## Resultados

Foram avaliados tres cenarios principais: Random Forest com ajuste de hiperparametros, Rede Neural MLP baseline e Rede Neural MLP otimizada com engenharia de atributos. A Random Forest apresentou o melhor desempenho geral, com acuracia de 74,15% e ROC AUC de 0,8218. A Rede Neural baseline obteve acuracia de 73,23% e ROC AUC de 0,8142. A versao otimizada da Rede Neural apresentou melhora marginal, chegando a 73,36% de acuracia e ROC AUC de 0,8145.

| Modelo | Acuracia | ROC AUC | Observacao |
|---|---:|---:|---|
| Random Forest | 74,15% | 0,8218 | Melhor desempenho geral |
| Rede Neural MLP baseline | 73,23% | 0,8142 | Competitiva, mas abaixo da RF |
| Rede Neural MLP otimizada | 73,36% | 0,8145 | Pequeno ganho sobre a MLP baseline |

## Leitura dos Resultados

O ganho obtido pela rede otimizada foi pequeno em relacao ao aumento de complexidade. Isso sugere que o conjunto de dados possui um limite pratico de previsibilidade para o target `felt_rested`, ou que as relacoes relevantes ja foram capturadas de forma eficiente pela Random Forest. Para dados tabulares com variaveis mistas, a Random Forest tende a ser uma abordagem forte por capturar interacoes nao lineares sem exigir uma arquitetura manual complexa.
