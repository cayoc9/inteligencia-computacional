# Relatorio Consolidado V1 - Comparacao RF vs RN

## Contexto

Este relatorio consolida a primeira versao oficial do experimento do Trabalho 1 de Inteligencia Computacional. A V1 compara modelos baseados em arvores e redes neurais para classificacao binaria usando o dataset Sleep Health and Daily Performance.

A V1 deve ser preservada como registro historico do experimento executado. A proposta de alvo composto `sono_restaurador` pertence a V2 e nao altera os resultados apresentados aqui.

## Problema E Dataset

O objetivo foi prever se uma pessoa se sentiu descansada apos o sono, usando informacoes demograficas, habitos, arquitetura do sono, estresse, rotina de trabalho e contexto ambiental.

- **Dataset:** Sleep Health and Daily Performance Dataset
- **Registros:** 100.000
- **Colunas nativas:** 32
- **Target oficial:** `felt_rested`
- **Distribuicao do target:** 60,99% classe 0 e 39,01% classe 1
- **Qualidade dos dados:** 0 nulos e 0 duplicatas

## Metodologia

Foram removidas as colunas `person_id`, `felt_rested`, `sleep_disorder_risk` e `cognitive_performance_score` do conjunto de features. A remocao de `person_id` evita usar identificador sem significado preditivo. A remocao dos demais targets evita misturar desfechos alternativos com preditores.

O pre-processamento combinou padronizacao de variaveis numericas e one-hot encoding de variaveis categoricas. A divisao treino/teste foi estratificada, usando `random_state=42`, para preservar a proporcao das classes e permitir comparacao justa entre modelos.

## Modelos Avaliados

- Random Forest com ajuste de hiperparametros.
- Rede Neural MLP baseline.
- Rede Neural MLP otimizada com regularizacao e engenharia de atributos.
- Modelos diagnosticos adicionais para investigar limites do problema, incluindo HistGradientBoosting.

## Resultados Principais

| Modelo | Acuracia | ROC AUC | Observacao |
|---|---:|---:|---|
| Random Forest | 74,15% | 0,8218 | Melhor modelo dentro da comparacao principal RF vs RN |
| Rede Neural MLP baseline | 73,23% | 0,8142 | Competitiva, mas abaixo da RF |
| Rede Neural MLP otimizada | 73,36% | 0,8145 | Pequeno ganho sobre a MLP baseline |
| HistGradientBoosting | 74,25% | 0,8258 | Modelo diagnostico complementar |

Na comparacao exigida pelo trabalho, a Random Forest apresentou o melhor equilibrio entre desempenho, simplicidade e interpretabilidade. A Rede Neural nao falhou, mas exigiu mais ajuste para ficar ligeiramente abaixo do modelo de arvores.

## Discussao Critica

A diferenca entre Random Forest e Rede Neural foi pequena, mas consistente. Em dados tabulares com variaveis mistas, modelos baseados em arvores tendem a capturar interacoes nao lineares sem exigir arquitetura manual complexa. A Rede Neural MLP continuou competitiva, mas a versao otimizada trouxe ganho marginal diante do aumento de complexidade.

O diagnostico posterior mostrou que o teto de desempenho esta ligado ao proprio alvo `felt_rested`. Trata-se de uma medida subjetiva: duas pessoas com perfis parecidos de sono, estresse e rotina podem responder de forma diferente sobre terem se sentido descansadas.

O ajuste de threshold tambem mostrou que o limiar padrao 0,5 nao e necessariamente o melhor. Para o melhor modelo diagnostico, reduzir o threshold para 0,35 aumentou o F1, com trade-off em acuracia.

## Camada Analitica: Precision, Fadiga E Burnout

Na V1, a classe positiva (`felt_rested = 1`) significa que a pessoa se sentiu descansada. Portanto, um falso positivo indica que o modelo classificou uma pessoa como descansada quando ela nao estava. Em um contexto de saude ocupacional, esse erro e sensivel porque pode mascarar fadiga acumulada.

Por esse motivo, alem de acuracia e ROC AUC, a precision da classe positiva deve ser destacada como metrica operacional: quanto maior a precision, menor o risco de falsos alarmes de descanso. Essa leitura nao deve ser apresentada como diagnostico clinico de burnout, mas como uma interpretacao pratica do custo dos erros.

O `cognitive_performance_score` reforca a discussao porque representa um desfecho objetivo associado ao funcionamento cognitivo apos o sono. Ele nao foi usado como feature na V1 para evitar vazamento conceitual, mas serve como base para a proposta da V2 com `sono_restaurador`.

## Limitacoes

- O dataset e sintetico-calibrado, entao a generalizacao para populacoes reais deve ser tratada com cautela.
- O alvo oficial `felt_rested` e subjetivo.
- A V1 usa classificacao binaria simples; alvos clinicamente mais ricos exigiriam nova formulacao.
- A otimizacao da Rede Neural foi suficiente para comparacao academica, mas nao exaustiva.
- A narrativa de burnout e uma interpretacao de risco operacional, nao uma inferencia clinica validada pelo dataset.

## Trabalho Futuro: V2

A principal evolucao proposta e criar o alvo composto `sono_restaurador`, combinando:

- `felt_rested == 1`, dimensao subjetiva do descanso;
- `cognitive_performance_score` acima de um limiar, dimensao objetiva de desempenho cognitivo.

Essa V2 deve ser executada separadamente, com novos resultados e novo relatorio, para nao reescrever a narrativa historica da V1.
