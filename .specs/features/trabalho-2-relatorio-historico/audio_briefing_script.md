# Roteiro de Audio - Repasse ao Grupo

## Objetivo do audio

Explicar para quem nao desenvolveu ativamente:

- o que era o Projeto 2;
- o que estava errado no inicio;
- o que foi corrigido;
- por que o dataset mudou;
- qual resultado vale de verdade;
- como defender o projeto sem inventar nada.

## Roteiro base

### Parte 1: O que o projeto queria fazer

O Projeto 2 buscou prever risco de obito em cancer de mama com modelos tabulares, ensemble e um comparativo neuro-fuzzy, dentro da disciplina de Inteligencia Computacional.

### Parte 2: O que descobrimos que estava errado

O pipeline inicial tinha dois problemas centrais:

1. a pergunta principal estava contaminada pelo uso de `Survival Months`;
2. o ensemble ainda tinha risco metodologico por ajustar decisao no teste.

### Parte 3: O que foi corrigido

- saneamento centralizado;
- dicionario de dados;
- EDA com metadados e relacoes;
- exclusao de `Survival Months` do principal;
- split treino/validacao/teste;
- ensemble com tuning so na validacao;
- explicabilidade, calibracao e estabilidade.

### Parte 4: O que o SEER mostrou

O SEER corrigido virou um baseline defensavel, mas ainda limitado. O ensemble melhorou sensibilidade, porem com muito falso positivo.

### Parte 5: Por que migramos para o METABRIC

Migramos porque o METABRIC e mais rico clinicamente. Ele tem tratamento, biomarcadores e subtipo molecular, o que melhora a capacidade de aprendizagem e de interpretacao do projeto.

### Parte 6: Qual resultado final importa

- SEER: baseline corrigido;
- METABRIC: evolucao canonica;
- melhor ponto operacional final: ensemble METABRIC com recall `0.9953`, F2 `0.8770` e `1` falso negativo.

### Parte 7: Como responder perguntas

- nao chamar neuro-fuzzy de ANFIS;
- nao vender `Survival Months` como parte do modelo principal;
- nao usar acuracia como criterio principal;
- explicar que o ensemble e forte para sensibilidade, nao necessariamente o melhor modelo universal.

## Relacao com outros artefatos

- narrativa principal: `relatorio_historico.md`
- perguntas de banca: `qa_professor_checkpoints.md`
- estrutura de apresentacao: `presentation_outline.md`
