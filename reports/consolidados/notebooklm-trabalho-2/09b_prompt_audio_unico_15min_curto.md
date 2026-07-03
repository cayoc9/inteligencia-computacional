# Prompt NotebookLM - Audio Unico Curto 12-16 Minutos

Gere um unico resumo em audio, em portugues do Brasil, com duracao alvo entre 12 e 16 minutos.

Importante: nao faca um Deep Dive longo. O audio precisa ser compacto, didatico e direto, para preparar os integrantes do grupo para explicar a apresentacao oralmente.

## Objetivo do audio

Criar uma explicacao narrativa da apresentacao do Trabalho 2, como se fosse um ensaio guiado para colegas que nao participaram ativamente do desenvolvimento.

O audio deve responder:

- qual era o problema;
- por que a metodologia inicial precisava ser corrigida;
- por que `Survival Months` foi removido;
- por que o SEER ficou como baseline corrigido;
- por que o METABRIC virou a trilha canonica;
- quais modelos foram avaliados;
- qual foi o papel do ensemble;
- qual foi o papel do neuro-fuzzy;
- quais resultados realmente importam;
- quais trade-offs e limites precisam ser assumidos.

## Estrutura obrigatoria

1. Abertura: explique que o trabalho evoluiu de SEER corrigido para METABRIC canonico.
2. Problema: classificacao supervisionada de obito observado em cancer de mama.
3. Metrica: acuracia nao basta; recall, F2, PR AUC e falsos negativos sao mais importantes.
4. Correcao metodologica: remover `Survival Months`, separar treino, validacao e teste.
5. SEER: 4.023 registros analiticos; baseline corrigido; resultado individual e ensemble.
6. METABRIC: 1.876 registros analiticos; mais sinais clinicos; virou trilha canonica.
7. Modelos: baseline explicavel, arvores/boosting, MLP/SVM, ensemble, neuro-fuzzy cooperativo.
8. Resultados: explicar os numeros principais sem ler tabela inteira.
9. Trade-off: reduzir falso negativo aumenta falso positivo.
10. Limitacoes: sem validacao clinica externa, nao survival analysis formal, neuro-fuzzy nao e ANFIS.
11. Fechamento: bons dados e boa validacao foram mais importantes que complexidade isolada.

## Numeros obrigatorios

- SEER Logistic Regression: accuracy 0.6807, recall 0.6098, F2 0.4832, PR AUC 0.3525, 48 falsos negativos.
- SEER ensemble: threshold 0.22, recall 0.7642, F2 0.5188, 29 falsos negativos, 320 falsos positivos.
- METABRIC GradientBoosting: accuracy 0.7048, recall 0.7953, F2 0.7787, PR AUC 0.7600, 44 falsos negativos.
- METABRIC ensemble: threshold 0.16, recall 0.9953, F2 0.8770, 1 falso negativo, 146 falsos positivos.
- Neuro-fuzzy SEER: F2 0.2886, recall 0.2764.
- Neuro-fuzzy METABRIC: F2 0.6548, recall 0.6512.

## Regras de linguagem

- Seja didatico e natural.
- Nao leia como artigo.
- Nao repita os mesmos pontos.
- Nao inclua Projeto 1.
- Nao diga que houve validacao clinica externa.
- Nao chame o neuro-fuzzy de ANFIS.
- Nao diga que o ensemble e sempre melhor.
- Sempre que citar alto recall, cite tambem falsos positivos.

## Fechamento desejado

Finalize dizendo que a defesa deve ser honesta: o projeto e forte como exercicio academico de metodologia, validacao e comparacao de modelos, mas ainda nao deve ser vendido como sistema clinico pronto.
