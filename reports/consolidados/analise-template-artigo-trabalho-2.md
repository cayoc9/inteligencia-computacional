# Analise do Template do Artigo - Trabalho 2

## Objetivo da Analise

Esta analise complementa a etapa do artigo do Projeto 2 a partir do template `docs/template/Sleep_Health/`. O objetivo nao e copiar a estrutura de outro tema, mas extrair o padrao editorial que ja funciona e reencaixar esse padrao no trabalho de cancer de mama.

## O que o template base ensina

O template `Sleep_Health` tem uma estrutura IEEE direta e util:

1. resumo curto e objetivo;
2. introducao com problema e contribuicoes;
3. metodologia em blocos pequenos;
4. resultados com tabelas;
5. discussao com leitura critica;
6. limitacoes assumidas sem maquiagem;
7. conclusao com tese final;
8. referencias enxutas.

Esse desenho e adequado ao Trabalho 2 porque o projeto tambem depende de comparacao de modelos, narrativa metodologica e leitura critica de trade-offs.

## O que deve ser mantido

1. Formato `IEEEtran` em conferencia.
2. Estrutura curta, com secoes objetivas.
3. Uso de figuras e tabelas como prova material dos resultados.
4. Tom tecnico e descritivo, sem linguagem promocional.
5. Discussao separada da conclusao.

## O que deve ser trocado

1. Todo o tema de sono, ocupacao e estado de descanso.
2. As figuras do template de `Sleep_Health`.
3. O target binario do exemplo.
4. Os metadados e as correlacoes especificas daquele dataset.
5. As referencias do dominio de sono.

## Estrutura recomendada para o artigo do Trabalho 2

### Titulo

Deve explicitar tres coisas:

1. cancer de mama;
2. correcao metodologica do SEER;
3. evolucao canonica para METABRIC.

### Abstract

Precisa responder em poucas linhas:

1. qual era a tarefa;
2. qual era o problema metodologico;
3. o que o SEER corrigido mostrou;
4. por que o METABRIC virou a trilha canonica;
5. qual foi o papel do ensemble e do neuro-fuzzy.

### Introducao

Deve conter:

1. contexto de IA em saude;
2. problema de risco de obito;
3. justificativa do trabalho;
4. contribuicoes reais;
5. aviso de que a melhoria veio tanto de metodo quanto de dataset.

### Materiais e Metodos

Deve separar:

1. datasets;
2. politica de dados;
3. EDA e dicionario de dados;
4. engenharia de features;
5. modelos tabulares;
6. ensemble;
7. neuro-fuzzy;
8. avaliacao.

### Resultados

Deve mostrar:

1. baseline corrigido do SEER;
2. ensemble do SEER com threshold escolhido na validacao;
3. baseline forte do METABRIC;
4. ensemble do METABRIC com threshold escolhido na validacao;
5. comparacao clara de trade-offs.

### Discussao

Deve responder:

1. o que a correcao metodologica realmente mudou;
2. o que veio do dataset melhor;
3. por que o ensemble vale como ponto operacional;
4. por que o neuro-fuzzy e comparativo, nao campeao.

### Limitacoes

Deve deixar explicito:

1. nao ha validacao clinica externa;
2. nao ha survival analysis formal;
3. as bases sao heterogeneas;
4. o sistema nao e pronto para uso clinico.

### Conclusao

Deve fechar com uma tese unica:

1. corrigir o pipeline aumentou a credibilidade;
2. trocar o dataset elevou o teto do projeto;
3. o METABRIC ficou como evolucao canonica;
4. o SEER permanece como baseline historico.

## Ponto critico do template do artigo

O template do artigo nao pode virar apenas um espelho do relatorio tecnico final. Ele precisa ser mais seletivo:

1. menos narrativa de processo;
2. mais prova de resultado;
3. mais densidade nas tabelas e figuras;
4. menos repeticao entre introducao, discussao e conclusao.

## Figuras e tabelas que fazem falta

Para fechar o artigo com o padrao do template, ainda faltam:

1. tabela resumindo SEER vs METABRIC;
2. tabela de metricas principais por trilha;
3. figura ou tabela do trade-off recall x FP para o ensemble;
4. figura de explicabilidade da Logistic Regression ou importance ranking;
5. figura de calibracao;
6. tabela resumindo as features derivadas principais.

## Lacunas ainda abertas

1. preencher autores reais;
2. fechar bibliografia final;
3. decidir quais figuras entram no corpo principal;
4. compilar e revisar o PDF no Overleaf;
5. alinhar a redação final com a fala da apresentacao.

## Conclusao da analise

O template `Sleep_Health` e bom como ossatura editorial, mas o conteudo do Projeto 2 precisa ser mais rigoroso em justificativa metodologica e mais seletivo na exposicao dos resultados. A adaptacao correta nao e trocar nomes; e reorganizar a narrativa para que o artigo prove, com evidencias, por que o SEER foi corrigido e por que o METABRIC virou a trilha canonica.
