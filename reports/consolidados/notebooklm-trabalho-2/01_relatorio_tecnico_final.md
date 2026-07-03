# Relatorio Tecnico Final - Trabalho 2

## Sistema de Inteligencia Computacional para Risco de Obito em Cancer de Mama

**Disciplina:** Inteligencia Computacional - UFPA 2026.1  
**Projeto escolhido para apresentacao:** Projeto 2  
**Tema:** Ensemble tabular com comparativo neuro-fuzzy em cancer de mama  
**Versao final:** 2026-07-03

---

## 1. Introducao

O Trabalho 2 da disciplina exige um sistema de Inteligencia Computacional hibrido ou ensemble, com justificativa metodologica, comparacao com baseline simples, analise critica dos resultados e discussao de limitacoes. Dentro desse escopo, o projeto selecionado foi o problema de classificacao supervisionada de risco de obito em cancer de mama a partir de dados tabulares clinicos.

Ao longo da execucao, o projeto se desdobrou em duas trilhas:

1. `projeto_2_neuro_fuzzy/`: trilha SEER corrigida metodologicamente;
2. `projeto_2_neuro_fuzzy_metabric_clinico/`: evolucao canonica v2 com dataset clinico mais rico.

A contribuicao principal do trabalho nao foi apenas treinar modelos. O projeto mostrou que:

- corrigir politica de dados e validacao muda a credibilidade do experimento;
- melhorar a qualidade do dataset pode elevar mais o teto do projeto do que insistir em modelos mais sofisticados sobre uma base limitada.

---

## 2. Problema e objetivo

O objetivo final do trabalho foi classificar o desfecho de obito observado no dataset a partir de variaveis clinicas, patologicas e, na trilha v2, tambem moleculares e de tratamento.

### 2.1 Objetivo corrigido

Prever a classe positiva de obito observado:

- no SEER: `Status = Dead`
- no METABRIC: `Overall Survival Status = Deceased`

sem usar a variavel de tempo de sobrevida como feature principal.

### 2.2 Erro metodologico original

A versao inicial do projeto usava `Survival Months` como feature para prever `Status`. Isso contaminava a pergunta principal com informacao de acompanhamento posterior ao evento clinico observado.

Outra fragilidade relevante era o uso do teste para orientar parte da decisao de ensemble. Esse problema foi eliminado com a introducao explicita de `treino / validacao / teste`.

---

## 3. Datasets

## 3.1 Trilha SEER corrigida

- Base: Kaggle Breast Cancer / SEER
- Tamanho bruto: 4.024 registros
- Tamanho analitico: 4.023 registros
- Classe positiva: `Dead`
- Papel no trabalho: baseline educacional corrigido

Essa base permitiu corrigir o projeto original, estruturar o pipeline e demonstrar o trade-off entre sensibilidade e falsos positivos. No entanto, ela e mais limitada em profundidade clinica.

## 3.2 Trilha METABRIC canonica

- Base: Kaggle `gunesevitan/breast-cancer-metabric`
- Tamanho bruto: 2.509 registros
- Tamanho analitico: 1.876 registros
- Classe positiva: `Deceased`
- Papel no trabalho: evolucao canonica v2

O METABRIC foi adotado porque inclui:

- quimioterapia, hormonioterapia e radioterapia;
- ER, PR e HER2;
- subtipo molecular PAM50;
- Nottingham Prognostic Index;
- mutation count;
- variaveis clinicas mais ricas para engenharia de atributos.

---

## 4. Metodologia

## 4.1 Politica de dados

As duas trilhas passaram a seguir a mesma disciplina metodologica:

1. sanitizacao centralizada;
2. dicionario de dados;
3. EDA com metadados e relacoes;
4. exclusao de variaveis de vazamento do modelo principal;
5. pipeline unico com `treino / validacao / teste`;
6. relatorios, tabelas e notebook executavel.

## 4.2 Engenharia de features

No SEER, foram criadas features clinicas derivadas como:

- `node_positive_ratio`
- `advanced_stage_flag`
- `hormone_receptor_negative`
- `tumor_node_burden`

No METABRIC, a engenharia foi ampliada para incluir:

- carga tumoral e nodal;
- burden por stage e grade;
- exposicao a tratamento;
- perfis moleculares;
- discretizacoes clinicas;
- atributos fuzzy para comparativo neuro-fuzzy.

## 4.3 Modelos avaliados

Nas duas trilhas, o pipeline comparou modelos tabulares e um comparativo neuro-fuzzy:

- Logistic Regression
- Random Forest
- ExtraTrees
- GradientBoosting
- HistGradientBoosting
- SVM calibrado
- AdaBoost
- MLP
- ensemble ponderado
- neuro-fuzzy cooperativo

## 4.4 Metricas

Como o problema e desbalanceado e o custo de falso negativo e relevante, a leitura principal priorizou:

- recall
- F2-score
- PR AUC
- falsos negativos

Acuracia foi mantida como metrica secundaria, nunca como criterio isolado de escolha.

---

## 5. Resultados

## 5.1 Resultados do SEER corrigido

### Melhor baseline individual

**Logistic Regression**

- accuracy: `0.6807`
- precision: `0.2641`
- recall: `0.6098`
- F2: `0.4832`
- PR AUC: `0.3525`
- falsos negativos: `48`

### Melhor ponto operacional

**Ensemble ponderado com threshold `0.22` escolhido na validacao**

- accuracy: `0.5665`
- precision: `0.2271`
- recall: `0.7642`
- F2: `0.5188`
- PR AUC: `0.3196`
- falsos negativos: `29`
- falsos positivos: `320`

### Leitura correta

O ensemble no SEER nao foi o melhor discriminador global. Ele foi um ponto operacional agressivo de sensibilidade: reduz falsos negativos, mas paga caro em falsos positivos.

## 5.2 Resultados do METABRIC canonico

### Melhor baseline individual

**GradientBoosting**

- accuracy: `0.7048`
- precision: `0.7185`
- recall: `0.7953`
- F2: `0.7787`
- PR AUC: `0.7600`
- falsos negativos: `44`

### Melhor ponto operacional

**Ensemble ponderado com threshold `0.16` escolhido na validacao**

- accuracy: `0.6090`
- precision: `0.5944`
- recall: `0.9953`
- F2: `0.8770`
- PR AUC: `0.7586`
- falsos negativos: `1`
- falsos positivos: `146`

### Leitura correta

No METABRIC, o ensemble tambem e um ponto operacional de alta sensibilidade, mas sobre uma base muito mais forte. O resultado final e substancialmente superior ao SEER tanto em baseline individual quanto em ponto operacional.

## 5.3 Neuro-fuzzy

O neuro-fuzzy foi mantido como comparativo academico coerente com a disciplina, mas nao foi o melhor modelo em nenhuma das trilhas.

- SEER neuro-fuzzy: F2 `0.2886`, recall `0.2764`
- METABRIC neuro-fuzzy: F2 `0.6548`, recall `0.6512`

Ele deve ser descrito como **neuro-fuzzy cooperativo com fuzzificacao manual + MLP**, e nao como ANFIS completo.

---

## 6. Discussao

## 6.1 O que o projeto demonstrou

O trabalho demonstrou tres pontos centrais:

1. **corrigir metodologia importa**: retirar vazamento e impedir tuning no teste aumenta a validade da defesa;
2. **dataset importa tanto quanto modelo**: o salto do METABRIC nao pode ser atribuido apenas ao ensemble;
3. **nem todo hibrido melhora performance**: o valor academico tambem esta em mostrar, com honestidade, quando o modelo hibrido nao lidera empiricamente.

## 6.2 Por que o METABRIC passou a ser a trilha canonica

O METABRIC virou a v2 canonica porque:

- preserva o mesmo rigor metodologico da trilha SEER;
- oferece melhor profundidade clinica;
- melhora a capacidade de engenharia de atributos e explicabilidade;
- produz desempenho muito superior sem depender de `survival_months`.

## 6.3 Trade-offs

Os resultados nao devem ser lidos como “o ensemble sempre vence”.

- No SEER, o ganho de recall foi comprado com muitos falsos positivos.
- No METABRIC, o ensemble final quase elimina falsos negativos, mas ainda aumenta falsos positivos.

Portanto, o ensemble deve ser defendido como **ponto operacional para alta sensibilidade**, nao como melhor modelo universal em todos os criterios.

---

## 7. Explicabilidade, calibracao e robustez

O projeto adicionou uma camada de defesa cientifica que faltava na versao inicial:

- coeficientes da Logistic Regression;
- permutation importance;
- curvas de calibracao;
- Brier score;
- estabilidade por 5 seeds.

Esses artefatos ajudam a responder objecoes de banca sobre interpretabilidade, qualidade probabilistica e dependencia de um unico split favoravel.

---

## 8. Limitacoes

As limitacoes que precisam ser assumidas sem exagero:

1. o projeto usa datasets publicos, nao validacao clinica externa;
2. a tarefa permanece enquadrada como classificacao supervisionada, nao survival analysis formal;
3. o neuro-fuzzy implementado nao e ANFIS completo;
4. a comparacao entre SEER e METABRIC e metodologicamente justa, mas nao e benchmark perfeito entre bases identicas.

---

## 9. Conclusao

O Projeto 2 esta tecnicamente defensavel para a disciplina e foi o mais forte para apresentacao porque reuniu:

- problema relevante em saude;
- pipeline corrigido e auditavel;
- ensemble justificavel;
- comparativo neuro-fuzzy coerente com a ementa;
- explicabilidade, calibracao e estabilidade;
- evolucao natural para um dataset clinico melhor.

A leitura final mais correta e:

- **SEER**: baseline corrigido e historicamente importante;
- **METABRIC**: evolucao canonica e melhor base para defesa final.

Os proximos passos naturais, se o trabalho continuar, sao:

- survival analysis formal;
- explicabilidade local;
- validacao cruzada repetida;
- analise de decisao por custo clinico.

---

## 10. Artefatos principais

- [Relatorio historico canonico](../../.specs/features/trabalho-2-relatorio-historico/relatorio_historico.md)
- [Checkpoint professorial](../../.specs/features/trabalho-2-relatorio-historico/qa_professor_checkpoints.md)
- [Resumo de execucao SEER](../../projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md)
- [Resumo de execucao METABRIC](../../projeto_2_neuro_fuzzy_metabric_clinico/docs/PROJECT_EXECUTION_SUMMARY.md)
- [Relatorio tecnico SEER](../../projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md)
- [Relatorio tecnico METABRIC](../../projeto_2_neuro_fuzzy_metabric_clinico/reports/relatorio_tecnico_projeto_2_metabric.md)
