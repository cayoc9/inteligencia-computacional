# Escolha do Projeto para Apresentacao

**Contexto:** segunda avaliacao de Inteligencia Computacional - UFPA 2026.1  
**Decisao a tomar:** apresentar apenas um projeto entre:

- Projeto 1: Heart Failure - Sistema Genetico-Neural GA-MLP
- Projeto 2: Breast Cancer Survival Risk - Ensemble ponderado + Neuro-Fuzzy comparativo

## Criterios da Avaliacao

O enunciado da avaliacao pede:

1. Sistema hibrido ou ensemble que combine duas ou mais tecnicas.
2. Justificativa da arquitetura escolhida.
3. Explicacao de como as partes do sistema se comunicam.
4. Comparacao com baseline simples.
5. Analise de ganho ou perda de performance.
6. Metricas robustas.
7. Analise aprofundada dos resultados.
8. Desafios de implementacao.
9. Trabalhos futuros.
10. Relatorio tecnico e apresentacao clara.

## Comparacao Executiva

| Dimensao | Projeto 1 - GA-MLP | Projeto 2 - Breast Cancer | Melhor |
|---|---|---|---|
| Aderencia direta ao tema hibrido | Muito alta: Genetico-Neural explicito | Alta: ensemble + neuro-fuzzy comparativo | Projeto 1 |
| Complexidade tecnica | Media: GA + MLP | Alta: saneamento, EDA, multiplos modelos, ensemble, neuro-fuzzy | Projeto 2 |
| Completude documental | Boa: spec, design, tasks, notebook, resultados | Muito boa: spec, design, tasks, dicionario, EDA, notebook, relatorio | Projeto 2 |
| Qualidade de ciencia de dados | Media-alta: dataset pequeno, validacao simples | Alta: dataset maior, vazamento tratado, metricas clinicas | Projeto 2 |
| Resultado frente ao baseline | Fraco: GA-MLP nao supera RF; melhora marginal sobre MLP | Defensavel: ensemble melhora recall/FN sob trade-off | Projeto 2 |
| Explicabilidade | Boa: cromossomo e features selecionadas sao claros | Muito boa: dicionario, EDA, leakage, threshold, FN/FP | Projeto 2 |
| Facilidade de explicar em 15 min | Alta: narrativa simples | Media: narrativa mais rica, exige controle do tempo | Projeto 1 |
| Risco de pergunta dificil | Medio: "por que perdeu da RF?" | Medio-alto: "por que accuracy baixa?", "isso e clinicamente util?" | Empate |
| Impressao academica | Boa | Mais madura e metodologicamente robusta | Projeto 2 |

## Matriz de Pontuacao

Escala: 1 a 5.

| Criterio | Peso | Projeto 1 | Pontos P1 | Projeto 2 | Pontos P2 |
|---|---:|---:|---:|---:|---:|
| Aderencia ao enunciado | 5 | 5 | 25 | 5 | 25 |
| Justificativa da arquitetura | 4 | 4 | 16 | 5 | 20 |
| Comunicacao entre componentes | 4 | 5 | 20 | 4 | 16 |
| Comparacao com baseline | 5 | 4 | 20 | 5 | 25 |
| Qualidade das metricas | 5 | 3 | 15 | 5 | 25 |
| Analise critica | 5 | 3 | 15 | 5 | 25 |
| Explicabilidade | 4 | 3 | 12 | 5 | 20 |
| Reprodutibilidade | 4 | 4 | 16 | 5 | 20 |
| Forca da narrativa | 4 | 4 | 16 | 5 | 20 |
| Baixo risco de defesa | 3 | 4 | 12 | 3 | 9 |
| **Total** |  |  | **167** |  | **205** |

## Projeto 1 - Diagnostico de Apresentabilidade

### Pontos fortes

- E o exemplo mais direto do enunciado: Algoritmo Genetico otimizando topologia/seleção para Rede Neural.
- A comunicacao entre componentes e simples de explicar:
  - cromossomo escolhe features e neuronios;
  - MLP calcula fitness;
  - AG evolui solucoes;
  - melhor individuo e testado.
- Tem uma historia didatica boa sobre hibridizacao.
- Apresentacao cabe facilmente em 15 minutos.

### Pontos fracos

- Dataset pequeno: 299 registros.
- Resultado principal nao e forte:
  - Random Forest F1: 0.7059
  - MLP F1: 0.4848
  - GA-MLP F1: 0.5000
- O hibrido melhora pouco sobre a MLP e perde claramente para Random Forest.
- Explicabilidade e limitada a features selecionadas e curva evolutiva.
- Falta relatorio tecnico final redigido.

### Como defender se escolher o Projeto 1

Mensagem central:

> O objetivo nao era provar que o hibrido sempre vence, mas projetar, implementar e avaliar criticamente um sistema Genetico-Neural. O resultado mostra que, em dataset tabular pequeno, Random Forest generalizou melhor, enquanto o GA-MLP demonstrou o mecanismo hibrido e expôs risco de overfitting evolutivo.

## Projeto 2 - Diagnostico de Apresentabilidade

### Pontos fortes

- Mais completo como ciencia de dados:
  - dicionario de dados;
  - saneamento de schema;
  - EDA de metadados e relacoes;
  - politica explicita contra vazamento;
  - varios modelos tabulares;
  - ensemble;
  - threshold tuning;
  - neuro-fuzzy comparativo.
- Dataset maior e mais robusto: 4024 registros brutos.
- Métricas sao mais maduras:
  - balanced accuracy;
  - precision;
  - recall;
  - F1;
  - F2;
  - ROC AUC;
  - PR AUC;
  - falsos negativos.
- Tem uma decisao metodologica forte: remover `Survival Months` por risco de vazamento/follow-up.
- Melhor para demonstrar maturidade tecnica e pensamento critico.

### Pontos fracos

- O componente neuro-fuzzy nao e o campeao e precisa ser apresentado como comparativo academico.
- O ensemble escolhido tem accuracy baixa:
  - accuracy 0.4857;
  - recall 0.8699;
  - falsos negativos 16;
  - falsos positivos 398.
- Exige explicar bem o trade-off entre sensibilidade e falsos positivos.
- A narrativa e mais densa para 15 minutos.

### Como defender se escolher o Projeto 2

Mensagem central:

> Em um problema medico desbalanceado, a escolha do sistema depende do custo do erro. O ensemble com threshold ajustado explorou um ponto de alta sensibilidade, reduzindo falsos negativos de forma agressiva, mas aceitando muitos falsos positivos. O neuro-fuzzy foi mantido como comparativo de sistema hibrido, mas os resultados mostram que regras fuzzy manuais sem calibragem especialista podem piorar o desempenho clinico.

Ponto critico historico: na versao anterior, pesos e threshold do ensemble foram escolhidos no mesmo conjunto reservado usado para reporte. Esse problema foi corrigido na trilha final com separacao treino/validacao/teste; portanto, a defesa atual deve enfatizar que pesos e threshold sao escolhidos na validacao e o teste fica reservado para reporte final.

## Recomendacao

**Recomendacao principal: apresentar o Projeto 2.**

Motivo: ele e mais completo, mais bem documentado, tem dataset maior, metrica mais alinhada a risco clinico, trata vazamento de dados e mostra maturidade de ciencia de dados. Mesmo com trade-offs, ele oferece uma narrativa mais forte para avaliacao: problema real, baseline, correção metodologica, modelos, ensemble, neuro-fuzzy comparativo e decisao critica.

**Quando escolher o Projeto 1:** se a prioridade for uma apresentacao mais simples e diretamente aderente ao exemplo Genetico-Neural do enunciado, aceitando que os resultados de desempenho sao mais fracos.

## Escolha Recomendada para Entrega

Apresentar:

**Projeto 2 - Breast Cancer Survival Risk: Ensemble ponderado com comparativo Neuro-Fuzzy**

Estrutura sugerida da apresentacao:

1. Problema e risco clinico: prever `Dead` sem usar informacao posterior.
2. Dataset e EDA: classe minoritaria, metadados, vazamento por `Survival Months`.
3. Baselines: mostrar que acuracia engana.
4. Ensemble: explicar pesos, threshold e reducao de falsos negativos.
5. Neuro-fuzzy: mostrar como comparativo academico e por que nao venceu.
6. Conclusao: sistemas hibridos/ensemble exigem trade-off e validacao critica.

## O Que Falta Para Fechar o Projeto Escolhido

Se escolher Projeto 2:

1. Revisar `relatorio_tecnico_projeto_2.md` para virar relatorio final.
2. Criar slides de 15 minutos.
3. Inserir 3 figuras principais:
   - distribuicao do alvo;
   - impacto de `Survival Months`;
   - tabela/curva de threshold do ensemble.
4. Preparar resposta para a pergunta: "por que aceitar tantos falsos positivos?"
5. Explicar claramente que o neuro-fuzzy nao e ANFIS completo.

Se escolher Projeto 1:

1. Redigir relatorio tecnico final do GA-MLP.
2. Rodar estabilidade com mais sementes, se houver tempo.
3. Explicar por que RF venceu.
4. Mostrar cromossomo, curva evolutiva e features selecionadas.
