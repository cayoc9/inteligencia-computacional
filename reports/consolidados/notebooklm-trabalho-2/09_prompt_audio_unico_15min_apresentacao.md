# Prompt NotebookLM - Audio Unico de 15 Minutos

Use este prompt para gerar um audio unico, didatico e narrativo, que explique toda a apresentacao do Trabalho 2 para integrantes do grupo que nao participaram ativamente do desenvolvimento.

## Prompt

Gere um resumo em audio, em portugues do Brasil, com aproximadamente 15 minutos.

O objetivo nao e apenas resumir os slides. O objetivo e criar uma explicacao narrativa, didatica e oral, para que qualquer integrante do grupo consiga entender o projeto, explicar a apresentacao e responder perguntas basicas da banca.

Tema: sistema de Inteligencia Computacional para risco de obito em cancer de mama, com SEER corrigido como baseline e METABRIC como evolucao canonica.

## Tom e formato

- Tom de explicacao academica clara, como uma conversa de preparacao para apresentacao.
- Linguagem acessivel, mas tecnicamente correta.
- Nao soar como propaganda.
- Nao exagerar resultados.
- Sempre diferenciar: o que foi implementado, o que foi validado, o que e limite e o que e trabalho futuro.
- Explicar os conceitos antes de citar numeros.
- Usar transicoes narrativas entre blocos.
- Evitar frases muito longas.

## Estrutura narrativa obrigatoria

### 1. Abertura e tese central

Explique que o trabalho evoluiu de uma primeira trilha com SEER para uma versao canonica com METABRIC.

Tese central:

- a melhoria nao veio apenas de trocar algoritmo;
- veio de corrigir metodologia;
- remover vazamento;
- separar treino, validacao e teste;
- melhorar a qualidade do dataset;
- assumir explicitamente o trade-off entre falsos negativos e falsos positivos.

### 2. Problema do trabalho

Explique a tarefa:

- classificar risco ou desfecho de obito observado em cancer de mama;
- no SEER, classe positiva relacionada a `Status = Dead`;
- no METABRIC, classe positiva relacionada a `Overall Survival Status = Deceased`;
- o problema e de classificacao supervisionada tabular.

Explique por que isso exige cuidado:

- em saude, falso negativo pode ser mais grave;
- acuracia pode enganar;
- recall, F2, PR AUC e falsos negativos sao mais importantes para a leitura principal.

### 3. Erro metodologico original e correcao

Explique com calma por que `Survival Months` foi removido do modelo principal.

Mensagem obrigatoria:

- `Survival Months` e informacao posterior de acompanhamento;
- usar essa variavel para prever obito observado introduz vazamento conceitual;
- por isso ela foi retirada do modelo principal;
- o teste foi preservado para reporte final;
- pesos e threshold do ensemble foram escolhidos na validacao, nao no teste.

### 4. Dataset SEER corrigido

Explique o papel do SEER:

- SEER ficou como baseline corrigido;
- 4.023 registros analiticos;
- serviu para corrigir pipeline, EDA, dicionario, politica de vazamento e validacao;
- mas tinha menor profundidade clinica.

Resultados principais do SEER:

- melhor modelo individual: Logistic Regression;
- accuracy 0.6807;
- recall 0.6098;
- F2 0.4832;
- PR AUC 0.3525;
- 48 falsos negativos.

Ensemble SEER:

- threshold 0.22;
- recall 0.7642;
- F2 0.5188;
- 29 falsos negativos;
- 320 falsos positivos.

Leitura obrigatoria:

- o ensemble reduziu falsos negativos;
- mas gerou muitos falsos positivos;
- portanto e um ponto operacional de alta sensibilidade, nao melhor modelo universal.

### 5. Por que migrar para METABRIC

Explique que a troca de dataset nao foi para esconder o SEER, mas para melhorar a qualidade do problema.

METABRIC:

- 1.876 registros analiticos;
- inclui sinais clinicos e biologicos mais ricos;
- tratamento;
- ER, PR, HER2;
- subtipo molecular PAM50;
- Nottingham Prognostic Index;
- mutation count.

Mensagem obrigatoria:

- SEER tinha mais registros;
- METABRIC tinha menos registros, mas mais qualidade de sinal;
- por isso METABRIC virou a trilha canonica.

### 6. Metodologia aplicada nas duas trilhas

Explique as fases:

- sanitizacao;
- dicionario de dados;
- analise exploratoria com metadados;
- engenharia de features;
- modelos individuais;
- ensemble ponderado;
- neuro-fuzzy cooperativo;
- explicabilidade;
- calibracao;
- estabilidade por seeds.

Explique que SEER e METABRIC passaram pelas mesmas fases essenciais.

### 7. Modelos avaliados

Explique brevemente:

- Logistic Regression como baseline explicavel;
- modelos de arvores e boosting;
- MLP e SVM calibrado;
- ensemble ponderado por soft voting;
- neuro-fuzzy cooperativo com fuzzificacao manual + MLP.

Mensagem obrigatoria:

- nao chamar o neuro-fuzzy de ANFIS;
- explicar que ele foi comparativo academico coerente com a disciplina;
- ele nao foi o melhor modelo.

Resultados neuro-fuzzy:

- SEER: F2 0.2886, recall 0.2764;
- METABRIC: F2 0.6548, recall 0.6512.

### 8. Resultados METABRIC

Explique primeiro o melhor modelo individual:

- GradientBoosting;
- accuracy 0.7048;
- recall 0.7953;
- F2 0.7787;
- PR AUC 0.7600;
- 44 falsos negativos.

Explique por que isso importa:

- METABRIC melhorou antes mesmo do ensemble;
- isso reforca que o ganho veio da qualidade dos dados, nao so do modelo combinado.

Depois explique o ensemble METABRIC:

- threshold 0.16;
- recall 0.9953;
- F2 0.8770;
- 1 falso negativo;
- 146 falsos positivos.

Mensagem obrigatoria:

- esse resultado e forte para alta sensibilidade;
- mas ainda tem custo operacional por falsos positivos;
- nao e validacao clinica externa;
- nao e sistema clinico pronto.

### 9. Comparacao geral

Explique a progressao de F2:

- SEER individual: 0.4832;
- SEER ensemble: 0.5188;
- METABRIC individual: 0.7787;
- METABRIC ensemble: 0.8770.

Interprete:

- dados melhores elevaram o teto;
- threshold e ensemble moveram o ponto operacional;
- complexidade sozinha nao compensaria um dataset fraco.

### 10. Trade-off e leitura critica

Explique:

- em saude, pode fazer sentido priorizar recall;
- mas falsos positivos aumentam custo operacional;
- o melhor resultado deve ser defendido como ponto operacional;
- a banca pode perguntar por que aceitar falsos positivos;
- a resposta e que isso depende do objetivo: triagem sensivel versus confirmacao diagnostica.

### 11. Limitacoes

Assuma claramente:

- datasets publicos;
- ausencia de validacao clinica externa;
- classificacao binaria, nao survival analysis formal;
- comparacao SEER vs METABRIC nao e benchmark perfeitamente controlado;
- neuro-fuzzy nao e ANFIS completo;
- falsos positivos precisam de analise de custo.

### 12. Trabalhos futuros

Explique:

- survival analysis formal;
- validacao externa;
- validacao cruzada/repetida mais ampla;
- explicabilidade local;
- analise de custo clinico;
- calibragem fuzzy com especialista.

### 13. Fechamento

Feche com uma mensagem simples:

- SEER ficou como baseline corrigido;
- METABRIC virou a trilha canonica;
- bons dados e boa validacao foram mais importantes que complexidade isolada;
- o ensemble foi util quando interpretado como ponto de alta sensibilidade;
- o trabalho e forte como exercicio academico e metodologico, mas ainda nao como sistema clinico pronto.

## Perguntas que o audio deve preparar a pessoa para responder

Inclua respostas curtas, em tom natural, para:

- Por que nao usar acuracia como metrica principal?
- Por que remover `Survival Months`?
- O teste foi usado para escolher threshold?
- O neuro-fuzzy e ANFIS?
- Por que METABRIC e melhor que SEER?
- Como justificar falsos positivos?
- O resultado pode ser usado clinicamente?

## Regras negativas

- Nao incluir Projeto 1.
- Nao dizer que houve validacao clinica externa.
- Nao dizer que o ensemble e sempre melhor.
- Nao dizer que METABRIC e comparacao perfeitamente controlada contra SEER.
- Nao chamar neuro-fuzzy de ANFIS.
- Nao transformar o audio em leitura seca de slide.

## Resultado esperado

Um audio unico, de aproximadamente 15 minutos, com narrativa continua, didatica e util para ensaio da apresentacao.
