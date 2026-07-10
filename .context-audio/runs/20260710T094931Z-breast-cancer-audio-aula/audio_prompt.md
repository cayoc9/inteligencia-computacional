# Audio Prompt NotebookLM

Gere um audio em portugues do Brasil, com duracao alvo de 14 a 16 minutos, ensinando o assunto que o grupo vai apresentar no Trabalho 2.

O publico sao integrantes do grupo que precisam entender e conseguir apresentar o projeto, mesmo que nao tenham participado de toda a implementacao. O tom deve ser didatico, natural e objetivo. Nao leia slides. Explique como uma aula preparatoria para defesa.

## Arco narrativo obrigatorio

1. Abra com a tese: o projeto evoluiu de SEER corrigido para METABRIC canonico.
2. Explique o problema: classificacao de obito observado em cancer de mama a partir de dados tabulares.
3. Explique por que acuracia nao basta em saude e por que recall, F2, PR AUC e falsos negativos importam.
4. Explique o erro original: `Survival Months` era vazamento conceitual porque trazia informacao de acompanhamento posterior.
5. Explique o protocolo: treino ajusta modelos; validacao escolhe pesos e threshold; teste apenas reporta.
6. Ensine o papel do SEER: baseline corrigido, 4.023 registros analiticos, menor profundidade clinica.
7. Ensine o papel do METABRIC: trilha canonica, 1.876 registros analiticos, tratamento, ER, PR, HER2, PAM50, NPI e mutation count.
8. Explique os modelos: Logistic Regression, arvores/boosting, MLP, SVM, ensemble ponderado e neuro-fuzzy cooperativo.
9. Diga explicitamente que o neuro-fuzzy nao e ANFIS completo.
10. Compare resultados individuais e depois ensembles, sempre pareando ganho de recall com custo em falsos positivos.
11. Feche com limitacoes e proximos passos: sem validacao clinica externa, classificacao binaria, survival analysis formal como futuro, explicabilidade local e analise de custo.

## Numeros que devem aparecer

- SEER Logistic Regression: F2 0.4832, recall 0.6098, PR AUC 0.3525, 48 falsos negativos.
- SEER ensemble threshold 0.22: recall 0.7642, F2 0.5188, 29 falsos negativos, 320 falsos positivos.
- METABRIC GradientBoosting: F2 0.7787, recall 0.7953, PR AUC 0.7600, 44 falsos negativos.
- METABRIC ensemble threshold 0.16: recall 0.9953, F2 0.8770, 1 falso negativo, 146 falsos positivos.

## Regras negativas

- Nao incluir Projeto 1.
- Nao dizer que e modelo clinico pronto.
- Nao dizer que houve validacao clinica externa.
- Nao chamar o neuro-fuzzy de ANFIS.
- Nao dizer que o ensemble e sempre melhor.
- Nao falar de alto recall sem mencionar falsos positivos.
- Nao vender SEER vs METABRIC como benchmark clinico estrito entre bases identicas.

## Frases que devem aparecer, com naturalidade

- "Validacao escolhe, teste reporta."
- "O SEER nao foi apagado; ele ficou como baseline corrigido."
- "O METABRIC virou a trilha canonica porque traz sinais clinicos mais ricos."
- "O ensemble e um ponto operacional experimental de alta sensibilidade."
- "O modelo nao decide tratamento; ele cria um ponto de alerta que exigiria validacao externa."
