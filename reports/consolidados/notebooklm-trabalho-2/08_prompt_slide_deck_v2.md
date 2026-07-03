# Prompt NotebookLM - Slide Deck v2

Use este prompt para gerar uma nova versao do slide deck no NotebookLM.

## Prompt

Crie uma apresentacao em portugues do Brasil para defesa academica do Trabalho 2 de Inteligencia Computacional.

Tema: sistema de Inteligencia Computacional para risco de obito em cancer de mama, com SEER corrigido como baseline e METABRIC como evolucao canonica.

## Regra estrutural principal

Mantenha os blocos obrigatorios da avaliacao:

1. Introducao
2. Desenvolvimento da solucao
3. Avaliacao experimental
4. Conclusao

Mas nao mantenha obrigatoriamente 20 slides.

Voce pode:

- fundir slides redundantes ou fracos;
- dar mais espaco aos slides que realmente defendem o trabalho;
- colocar perguntas provaveis em slides extras depois da tela de encerramento;
- manter a narrativa principal mais curta e mais forte.

## Faixa recomendada

- Narrativa principal: 14 a 16 slides.
- Slides extras apos encerramento: 1 a 3 slides.

## Estrutura recomendada da narrativa principal

1. Capa
2. Roteiro curto
3. Problema e custo do erro
4. Objetivo corrigido e vazamento
5. Dataset e mudanca SEER -> METABRIC
6. Arquitetura + pipeline de treino/validacao/teste
7. Pre-processamento + EDA + papel dos modelos
8. Metodologia experimental + metricas
9. Resultados dos modelos individuais
10. Resultados do sistema hibrido
11. Comparacao geral
12. Trade-off e leitura critica
13. Principais conclusoes
14. Limitacoes + trabalhos futuros
15. Encerramento

Depois disso, crie slides extras de perguntas provaveis.

## Regra narrativa principal

Cada slide deve defender uma afirmacao, nao listar um topico.

Use titulos como frases-claim, por exemplo:

- Em saude, acuracia alta pode esconder erro grave
- Survival Months foi removido para evitar vazamento
- METABRIC adiciona sinais clinicos que o SEER nao tinha
- Validacao escolhe; teste reporta
- METABRIC melhora antes mesmo do ensemble
- O ensemble reduz FN, mas precisa assumir FP
- O melhor resultado e um ponto operacional, nao verdade clinica

## Prioridade de espaco

Dedique mais densidade visual e mais espaco para estes quatro momentos:

1. problema;
2. dataset;
3. resultados;
4. trade-off.

Slides de arquitetura, metodologia e modelos podem ser mais compactos, desde que continuem claros.

## Numeros obrigatorios

Mantenha estes numeros exatamente:

- SEER corrigido: 4.023 registros analiticos.
- METABRIC canonico: 1.876 registros analiticos.
- SEER melhor modelo individual: Logistic Regression.
- SEER Logistic Regression: accuracy 0.6807, recall 0.6098, F2 0.4832, PR AUC 0.3525, falsos negativos 48.
- SEER ensemble: threshold 0.22, recall 0.7642, F2 0.5188, falsos negativos 29, falsos positivos 320.
- METABRIC melhor modelo individual: GradientBoosting.
- METABRIC GradientBoosting: accuracy 0.7048, recall 0.7953, F2 0.7787, PR AUC 0.7600, falsos negativos 44.
- METABRIC ensemble: threshold 0.16, recall 0.9953, F2 0.8770, falsos negativos 1, falsos positivos 146.
- Neuro-fuzzy SEER: F2 0.2886, recall 0.2764.
- Neuro-fuzzy METABRIC: F2 0.6548, recall 0.6512.

## Regras metodologicas obrigatorias

- Nao inclua Projeto 1.
- Nao diga que ha validacao clinica externa.
- Nao chame o neuro-fuzzy de ANFIS.
- Descreva o neuro-fuzzy como fuzzificacao manual + MLP.
- Explique que Survival Months foi removido do modelo principal por risco de vazamento.
- Explique que pesos e threshold do ensemble foram escolhidos na validacao.
- Explique que o teste foi preservado para reporte final.
- Sempre que mencionar alto recall, mencione tambem falsos positivos.

## Regras de estilo visual

Evite aparencia de template automatico.

Use:

- visual academico, clinico e analitico;
- fundo claro;
- texto escuro;
- azul escuro para metodologia;
- cinza para SEER/contexto;
- teal ou verde contido para METABRIC/evolucao;
- vermelho contido apenas para risco, vazamento, falso negativo ou falso positivo;
- pouco texto por slide;
- no maximo 25 a 35 palavras por slide, exceto tabelas de resultado;
- sem paragrafos longos;
- sem quatro cards iguais em grade;
- sem rodape pesado;
- sem bordas grossas;
- sem tabela grande quando uma comparacao de dois lados resolver.

## Composicoes desejadas

Use variedade de layouts:

- capa editorial com fluxo SEER corrigido -> METABRIC canonico;
- comparacao lado a lado para SEER vs METABRIC;
- pipeline horizontal ou comparativo compacto para treino/validacao/teste;
- numero hero nos slides de resultado;
- trade-off visual entre falsos negativos e falsos positivos;
- barra ou comparacao curta para progressao de F2;
- matriz simples para analise de resultado;
- conclusao em tres ou quatro aprendizados curtos.

## Foco dos slides de resultado

### Modelos individuais

Mostrar que METABRIC melhora antes do ensemble.

Use comparacao de duas colunas:

- SEER Logistic Regression: F2 0.4832, recall 0.6098, PR AUC 0.3525, FN 48.
- METABRIC GradientBoosting: F2 0.7787, recall 0.7953, PR AUC 0.7600, FN 44.

### Sistema hibrido

Mostrar o ensemble como ponto operacional de alta sensibilidade.

O foco visual deve ser:

- METABRIC: 1 falso negativo.
- Mas mostrar claramente: 146 falsos positivos.

Tambem mostrar:

- SEER: 29 falsos negativos e 320 falsos positivos.

### Comparacao geral

Mostrar progressao de F2:

- SEER individual: 0.4832.
- SEER ensemble: 0.5188.
- METABRIC individual: 0.7787.
- METABRIC ensemble: 0.8770.

Mensagem: dados melhores elevaram o teto; threshold/ensemble moveram o ponto operacional.

### Trade-off

Nao vender o modelo como verdade clinica.

Mensagem: o melhor resultado e um ponto operacional de alta sensibilidade, ainda limitado por falsos positivos e ausencia de validacao externa.

## Slide de encerramento

A tela de encerramento deve fechar a narrativa principal com esta ideia:

- SEER fica como baseline corrigido;
- METABRIC vira a trilha canonica;
- bons dados e boa validacao foram mais importantes que complexidade isolada.

Depois do encerramento, crie slides extras de perguntas provaveis.

## Slides extras de perguntas provaveis

Inclua perguntas como:

- Por que nao usar acuracia?
- Por que remover Survival Months?
- O ensemble foi ajustado no teste?
- O neuro-fuzzy e ANFIS?
- Por que METABRIC e melhor que SEER?
- Como justificar falsos positivos?

## Resultado esperado

Gere um slide deck em formato presenter, com visual limpo, humano, pouco verboso e pronto para ajustes finos em PowerPoint.
