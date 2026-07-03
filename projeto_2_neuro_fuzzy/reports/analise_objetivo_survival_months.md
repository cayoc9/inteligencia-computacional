# Analise: Objetivo do Dataset e Uso de Survival Months

## Por que excluir `Survival Months`

`Survival Months` deve ser excluido do modelo principal porque representa uma informacao de acompanhamento posterior ao diagnostico. Se a pergunta do projeto e prever risco de obito usando dados clinicos disponiveis no diagnostico, essa coluna nao estaria disponivel no momento da decisao.

Usar `Survival Months` para prever `Status` cria vazamento conceitual: saber que uma paciente sobreviveu poucos meses depois do diagnostico ajuda muito a prever `Dead`, mas isso ja carrega parte da resposta que o modelo deveria estimar.

Por isso, `Survival Months` fica permitido apenas em analise exploratoria e analise de sensibilidade, nao como feature do modelo principal.

## Dado principal do dataset

O alvo principal do projeto e:

- `Status`
  - `Alive = 0`
  - `Dead = 1`

As features principais sao dados demograficos e clinicos:

- idade;
- raca;
- estado civil;
- estagio tumoral (`T Stage`, `N Stage`, `6th Stage`);
- grau e diferenciacao do tumor;
- tamanho do tumor;
- status hormonal;
- linfonodos examinados;
- linfonodos positivos.

## Pergunta que o projeto tenta responder

A pergunta corrigida do Projeto 2 e:

> A partir dos dados clinicos disponiveis no diagnostico, conseguimos identificar pacientes com maior risco de obito, minimizando falsos negativos?

O erro mais sensivel nesse contexto e o falso negativo: prever `Alive` quando o registro real e `Dead`.

## Como os dados estao respondendo ate agora

Sem `Survival Months`, o problema fica mais dificil e mais realista. A classe `Dead` e minoritaria, com aproximadamente 15% dos registros, entao modelos com alta acuracia podem ainda perder muitos casos de obito.

Resultados principais sem `Survival Months`:

- Logistic Regression teve melhor recall entre os modelos simples: recall aproximado de 0,62 e 47 falsos negativos.
- Random Forest teve acuracia maior que Logistic Regression, mas recall menor para `Dead`.
- Modelos como HistGradientBoosting e SVM calibrado ficaram com acuracia alta, mas muitos falsos negativos.
- O ensemble ponderado com threshold 0,21 reduziu falsos negativos para 16 e elevou recall para aproximadamente 0,87, mas aumentou bastante os falsos positivos.
- O neuro-fuzzy cooperativo ficou fraco para o objetivo clinico: recall aproximado de 0,27 e 90 falsos negativos.

Quando `Survival Months` entra no experimento de sensibilidade, as metricas sobem bastante. Isso confirma que a coluna tem forte relacao com `Status`, mas tambem reforca o risco de vazamento se ela for usada como feature principal.

## Leitura metodologica

O dataset tem sinal preditivo, mas prever obito apenas com dados de diagnostico nao e trivial. A abordagem mais defensavel e tratar o problema como classificacao medica desbalanceada, priorizando recall, F2, PR AUC e reducao de falsos negativos, em vez de escolher o modelo por acuracia isolada.

