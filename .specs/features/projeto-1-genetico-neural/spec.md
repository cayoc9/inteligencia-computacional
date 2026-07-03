# Spec: Projeto 1 - Sistema Genetico-Neural GA-MLP

## Status

**Estado atual:** implementado e validado localmente; falta transformar os resultados em texto final de relatorio/apresentacao.

**Contexto:** segunda avaliacao da disciplina Inteligencia Computacional - UFPA 2026.1.

**Fontes de requisito:**
- `materiais_de_aula/Avaliacao2026_1.pdf`
- NotebookLM `26a8d20b-97fc-4d83-a513-55f2fa2f89f8` com as aulas da disciplina
- Scripts em `projeto_1_genetico_neural/`

## Problema

Construir, justificar e avaliar um sistema hibrido de Inteligencia Computacional para classificacao em saude, combinando Algoritmo Genetico e Rede Neural MLP no dataset `heart_failure_clinical_records_dataset.csv`.

O alvo e `DEATH_EVENT`, com classe positiva representando obito. Por ser um problema medico e desbalanceado, a leitura de qualidade nao deve depender apenas de acuracia; F1, recall, precision, matriz de confusao e comparacao contra baseline sao obrigatorios.

## Alinhamento com a Segunda Avaliacao

O PDF da avaliacao exige que o Trabalho 2 desenvolva um sistema hibrido ou ensemble, combinando duas ou mais tecnicas da ementa. Para sistemas hibridos, o proprio enunciado cita como exemplo o uso de Algoritmo Genetico para otimizar pesos ou topologia de uma Rede Neural.

Critérios derivados da avaliacao:

| ID | Criterio | Status atual |
|---|---|---|
| P1-GN-R01 | Escolher problema e dataset publico adequado | Feito |
| P1-GN-R02 | Justificar por que a combinacao GA + MLP e promissora | Parcial |
| P1-GN-R03 | Explicar como os componentes se comunicam | Feito no codigo e arquitetura, precisa aparecer no relatorio final |
| P1-GN-R04 | Comparar ganho ou perda contra baseline simples | Feito |
| P1-GN-R05 | Avaliar com metricas robustas no conjunto de teste | Feito |
| P1-GN-R06 | Discutir desafios de implementacao e trabalhos futuros | Parcial |
| P1-GN-R07 | Preparar relato tecnico e apresentacao de 15 minutos | Pendente |

## Alinhamento com os Materiais das Aulas

Consulta ao NotebookLM indicou que a justificativa metodologica do GA-MLP deve cobrir:

- MLP como modelo conexionista sujeito a ajuste de topologia, hiperparametros, minimo local e overfitting.
- Algoritmo Genetico como mecanismo de busca populacional para explorar combinacoes de features e topologia.
- Cromossomo como codificacao da solucao candidata.
- Fitness como criterio numerico de aptidao.
- Selecao, crossover, mutacao e elitismo como operadores evolutivos.
- Comparacao obrigatoria com abordagem simples, especialmente MLP treinada por backpropagation convencional.

## Escopo Funcional

### Incluido

- Carregar dataset Heart Failure Clinical Records.
- Executar EDA com verificacao de dados ausentes, distribuicoes e correlacao.
- Treinar baseline com Random Forest e MLP.
- Implementar GA do zero em Python/NumPy, sem DEAP/PyGAD.
- Codificar cromossomo com:
  - bits de selecao de features;
  - bits de topologia para numero de neuronios ocultos.
- Usar F1-Score em validacao como fitness.
- Treinar MLP final com configuracao escolhida pelo AG e avaliar no teste cego.
- Comparar GA-MLP contra baseline.

### Fora do escopo principal

- K-fold dentro do fitness, por custo computacional e prazo.
- SMOTE ou geracao sintetica de dados.
- Otimizacao de pesos completos da MLP por GA, que elevaria muito a dimensionalidade.
- Deploy de modelo.

## Criterios de Aceite

| ID | Aceite | Verificacao |
|---|---|---|
| P1-GN-A01 | EDA executa sem erro e gera figuras | `python eda_heart_failure.py` |
| P1-GN-A02 | Baseline RF e MLP executa e imprime metricas | `python baseline.py` |
| P1-GN-A03 | GA-MLP executa ate o fim em tempo controlado | `python hybrid_ga_mlp.py` ou modo parametrizado |
| P1-GN-A04 | Resultado do GA-MLP fica salvo em arquivo reprodutivel | JSON/CSV em `projeto_1_genetico_neural/reports/` |
| P1-GN-A05 | Comparacao final inclui baseline vs hibrido | Tabela no relatorio/spec |
| P1-GN-A06 | Relatorio explica ganho ou perda de performance | Secao critica do relatorio |
| P1-GN-A07 | Trabalhos futuros incluem K-fold no fitness e estabilidade por sementes | Secao final do relatorio |

## Revisao de Qualidade Atual

### Pontos fortes

- Tema esta aderente a segunda avaliacao: Genetico-Neural e um hibrido aceito explicitamente.
- A comunicacao entre componentes e clara: GA seleciona features e topologia; MLP mede fitness e depois e treinada com a solucao escolhida.
- A escolha de F1 como fitness e tecnicamente adequada para target desbalanceado.
- O baseline existe e foi validado localmente em 2026-07-02:
  - Random Forest: accuracy 0.8333, F1 0.7059, ROC AUC 0.9101.
  - MLP: accuracy 0.7167, F1 0.4848, ROC AUC 0.7754.
- O GA-MLP agora tem modo auditavel por CLI e salvou resultado rapido em `projeto_1_genetico_neural/reports/tables/ga_mlp_results_quick.json`:
  - GA-MLP quick: accuracy 0.7833, F1 0.6061, ROC AUC 0.8472.
- O GA-MLP completo foi validado localmente e salvou `projeto_1_genetico_neural/reports/tables/ga_mlp_results.json`:
  - GA-MLP full: accuracy 0.7667, precision 0.7778, recall 0.3684, F1 0.5000, ROC AUC 0.7766.
- A comparacao consolidada foi registrada em `projeto_1_genetico_neural/reports/tables/model_comparison.csv`.
- A EDA executa e gera `eda_distribuicoes.png` e `eda_correlacao.png`.
- Existe notebook unico em `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb`.

### Fragilidades

- Dataset tem apenas 299 linhas; isso torna o AG vulneravel a overfitting no conjunto de validacao.
- O notebook foi validado como JSON, mas nao foi executado por `nbconvert` porque o ambiente nao possui kernel Jupyter registrado.
- O GA-MLP completo melhorou muito pouco sobre a MLP em F1 e nao superou a Random Forest; isso precisa aparecer como achado critico, nao como fracasso do projeto.
- A documentacao anterior marcava o Projeto 1 como concluido, mas sem spec propria nem evidencia textual da execucao final do hibrido.

## Decisao de Qualidade

O Projeto 1 e **bom como proposta academica de sistema hibrido** e esta alinhado ao enunciado da segunda avaliacao. Como projeto de ciencia de dados, agora possui execucao auditavel, notebook unico e comparacao baseline vs hibrido. A conclusao tecnica deve ser critica: o GA-MLP demonstrou a arquitetura hibrida, mas nao superou a Random Forest no teste cego.

Classificacao atual:

| Dimensao | Nota qualitativa | Justificativa |
|---|---|---|
| Aderencia ao tema | Alta | GA + MLP atende diretamente o exemplo do enunciado |
| Clareza de arquitetura | Boa | Fluxo esta no codigo e em `.specs/codebase/ARCHITECTURE.md` |
| Rigor de ciencia de dados | Medio-alto | Execucao completa e comparacao existem; falta estabilidade por multiplas sementes |
| Reprodutibilidade | Media-alta | Scripts, JSON e CSV existem; falta kernel Jupyter registrado |
| Narrativa para defesa | Alta | Notebook unico e tabela final existem; falta redacao final do relatorio |
