# Prompt NotebookLM - Audio Unico Padrao 15 Minutos

Gere um unico audio em portugues do Brasil com duracao alvo de aproximadamente 15 minutos.

Nao gere um resumo curto de 5 a 7 minutos.
Nao gere um deep dive longo de 30 minutos.
O alvo e uma explicacao intermediaria, entre 14 e 16 minutos, para ensaio da apresentacao.

## Objetivo

Explicar a apresentacao do Trabalho 2 de forma didatica para integrantes do grupo que nao desenvolveram ativamente o projeto.

O audio deve funcionar como uma narrativa oral do que dizer na apresentacao, nao como leitura de slides.

## Roteiro compacto

1. Abra com a tese: o projeto evoluiu de SEER corrigido para METABRIC canonico.
2. Explique o problema: classificacao de obito observado em cancer de mama.
3. Explique por que acuracia nao basta e por que recall, F2, PR AUC e falsos negativos importam.
4. Explique o erro metodologico original: `Survival Months` causava vazamento conceitual.
5. Explique a correcao: remover vazamento e separar treino, validacao e teste.
6. Explique o SEER como baseline corrigido com 4.023 registros analiticos.
7. Explique o METABRIC como trilha canonica com 1.876 registros analiticos e mais sinais clinicos: tratamento, ER, PR, HER2, PAM50, NPI e mutation count.
8. Explique os modelos: Logistic Regression, arvores/boosting, MLP, SVM calibrado, ensemble ponderado e neuro-fuzzy cooperativo.
9. Explique que o neuro-fuzzy e fuzzificacao manual + MLP, nao ANFIS.
10. Compare os resultados individuais:
   - SEER Logistic Regression: F2 0.4832, recall 0.6098, PR AUC 0.3525, 48 falsos negativos.
   - METABRIC GradientBoosting: F2 0.7787, recall 0.7953, PR AUC 0.7600, 44 falsos negativos.
11. Compare os ensembles:
   - SEER ensemble: threshold 0.22, recall 0.7642, F2 0.5188, 29 falsos negativos, 320 falsos positivos.
   - METABRIC ensemble: threshold 0.16, recall 0.9953, F2 0.8770, 1 falso negativo, 146 falsos positivos.
12. Explique a interpretacao: dados melhores elevaram o teto; threshold e ensemble moveram o ponto operacional.
13. Explique o trade-off: alta sensibilidade reduz falsos negativos, mas aumenta falsos positivos.
14. Assuma as limitacoes: dataset publico, sem validacao clinica externa, classificacao binaria e nao survival analysis formal.
15. Feche com a mensagem: bons dados e boa validacao foram mais importantes que complexidade isolada.

## Regras obrigatorias

- Nao incluir Projeto 1.
- Nao dizer que houve validacao clinica externa.
- Nao chamar neuro-fuzzy de ANFIS.
- Nao dizer que o ensemble e sempre melhor.
- Sempre que falar de alto recall, falar tambem de falsos positivos.
- Explicar como se estivesse preparando colegas para apresentar.
- Usar tom natural, didatico e objetivo.
