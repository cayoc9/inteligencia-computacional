# Outline de Apresentacao - Trabalho 2

## Bloco 1: Problema e motivacao

- Tema: classificacao supervisionada de risco de obito em cancer de mama.
- Problema inicial: dataset e pipeline original tinham limitacoes metodologicas.
- Tese: melhorar a metodologia e depois melhorar o dataset elevou a qualidade real do trabalho.

## Bloco 2: Fase SEER corrigida

- saneamento e contrato de dados;
- EDA com metadados e relacoes;
- exclusao de `Survival Months`;
- ensemble com validacao separada;
- resultado principal: ensemble com recall `0.7642`, F2 `0.5188`, `29` falsos negativos.

## Bloco 3: Limites do SEER

- base clinicamente mais rasa;
- ganho operacional com muitos falsos positivos;
- baseline corrigido, mas teto limitado.

## Bloco 4: Evolucao METABRIC

- justificativa da troca;
- novas variaveis clinicas e moleculares;
- mesma disciplina metodologica;
- melhor baseline individual: GradientBoosting com F2 `0.7787`;
- melhor ponto operacional: ensemble com recall `0.9953`, F2 `0.8770`, `1` falso negativo.

## Bloco 5: Conclusao critica

- o principal salto veio de metodologia + qualidade do dataset;
- o ensemble nao e melhor em tudo, mas e forte para sensibilidade;
- o neuro-fuzzy teve valor academico, nao lideranca empirica;
- trabalhos futuros: survival analysis, explicabilidade local e robustez adicional.
