# Relatorio Historico Canonico do Trabalho 2

## Escopo e Regra de Leitura

Este documento consolida a historia tecnica do Trabalho 2 a partir de duas trilhas:

1. `projeto_2_neuro_fuzzy/` como baseline SEER corrigido;
2. `projeto_2_neuro_fuzzy_metabric_clinico/` como evolucao canonica v2.

Regra central:

- artefatos do repositorio definem a verdade final sobre implementacao e resultados;
- sessoes de agentes servem para reconstruir processo, racional e bifurcacoes;
- em caso de conflito, o repositorio prevalece.

## Linha do Tempo Consolidada

### 2026-07-01: gatilho inicial de revisao metodologica

- O processo foi reaberto a partir da analise de um audio sobre o dataset SEER e sobre a estrategia recomendada para o projeto.
- Nessa fase, a direcao pedida foi revisar saneamento, EDA, engenharia de features e o proprio objetivo testado com o dataset.
- Fonte de processo: sessao Codex `019f2525-5a79-7723-b4eb-8759cc32ce9f`.

### 2026-07-02: consolidacao spec-driven da correcao do SEER

- A trilha do Projeto 2 passou a ser documentada em TLC.
- Foram formalizados:
  - notebook proprio do projeto;
  - dicionario de dados;
  - EDA com metadados e relacoes;
  - exclusao de `Survival Months` do modelo principal;
  - suite tabular sem vazamento;
  - ensemble com validacao separada;
  - neuro-fuzzy mantido como comparativo academico.
- Nessa fase o projeto deixa de ser um conjunto de scripts soltos e vira pipeline rastreavel.
- Fontes canonicas: [.specs/features/trabalho-2-breast-cancer/spec.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/.specs/features/trabalho-2-breast-cancer/spec.md) e [projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md).

### 2026-07-02 a 2026-07-03: entrada do METABRIC como resposta a limite estrutural do dataset

- A partir da avaliacao critica da qualidade do SEER, foi feita pesquisa de datasets melhores e reais para o mesmo tema.
- O usuario escolheu seguir com o dataset clinico METABRIC em pasta-clone separada.
- O fork `projeto_2_neuro_fuzzy_metabric_clinico/` foi elevado ao mesmo padrao metodologico do SEER corrigido.
- Fontes de processo:
  - Codex `019f2525-5a79-7723-b4eb-8759cc32ce9f`
  - Antigravity `cd405d9c-1645-4090-8ada-150e8f2aea59`
- Fonte canonica: [projeto_2_neuro_fuzzy_metabric_clinico/docs/PROJECT_EXECUTION_SUMMARY.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy_metabric_clinico/docs/PROJECT_EXECUTION_SUMMARY.md)

### 2026-07-03: formalizacao da v2 canonica

- O METABRIC deixou de ser apenas um fork paralelo e passou a ser registrado como evolucao canonica v2 do Projeto 2.
- Foi aberta a feature TLC dedicada a essa evolucao.
- Foi produzida auditoria explicita de boas praticas de ciencia de dados.
- Fonte canonica:
  - [.specs/features/trabalho-2-breast-cancer-metabric/spec.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/.specs/features/trabalho-2-breast-cancer-metabric/spec.md)
  - [.specs/project/TRABALHO_2_DATA_SCIENCE_BEST_PRACTICES_REVIEW.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/.specs/project/TRABALHO_2_DATA_SCIENCE_BEST_PRACTICES_REVIEW.md)

## O que cada trilha representa

### SEER v1 corrigido

- representa a correcao metodologica do projeto original;
- serve como baseline educacional rastreavel;
- preserva a historia do erro e da correcao;
- nao deve mais ser vendido como trilha principal de melhoria continua.

### METABRIC v2 canonico

- representa a evolucao natural apos a constatacao de que o dataset anterior era limitado;
- mantem o mesmo rigor metodologico do SEER corrigido;
- vira a melhor base para defesa de melhoria continua e comparacao clinicamente mais rica.

## Resultados historicamente validos

### SEER corrigido

- Logistic Regression sem vazamento:
  - recall `0.6098`
  - F2 `0.4832`
- Ensemble corrigido:
  - threshold `0.22` escolhido na validacao
  - recall `0.7642`
  - F2 `0.5188`
  - falsos negativos `29`

### METABRIC canonico

- Melhor modelo individual sem vazamento:
  - `gradient_boosting`
  - recall `0.7953`
  - F2 `0.7787`
- Ensemble corrigido:
  - threshold `0.16` escolhido na validacao
  - recall `0.9953`
  - F2 `0.8770`
  - falsos negativos `1`

## O que nao pode ser confundido

1. Analise de sensibilidade com `Survival Months` nao e resultado principal.
2. Sessoes de agentes nao substituem artefatos canonicos do repositorio.
3. O METABRIC nao apaga o SEER; ele o sucede como evolucao canonica.
4. Melhora de metrica no METABRIC nao deve ser atribuida apenas ao ensemble; a qualidade do dataset mudou materialmente.

## Comparacao SEER vs METABRIC

### Tabela comparativa

| Eixo | SEER v1 corrigido | METABRIC v2 canonico | Leitura correta |
|---|---|---|---|
| Papel historico | baseline corrigido | evolucao canonica | SEER mostra correcao; METABRIC mostra maturacao |
| Profundidade clinica | clinico-patologica limitada | clinica + tratamento + biomarcadores + subtipo molecular | METABRIC oferece mais sinal util |
| Variaveis criticas extras | nao possui PAM50, HER2 estruturado, NPI, mutation count | possui PAM50, HER2, NPI, mutation count, terapias | o teto de aprendizagem sobe com a base |
| Politica de vazamento | `Survival Months` excluido do principal | `survival_months` excluido do principal | mesma regra metodologica |
| Melhor baseline individual | Logistic Regression, F2 `0.4832`, recall `0.6098` | GradientBoosting, F2 `0.7787`, recall `0.7953` | a melhora nao veio so do algoritmo; a base mudou materialmente |
| Melhor ponto operacional | Ensemble threshold `0.22`, recall `0.7642`, `29` FN | Ensemble threshold `0.16`, recall `0.9953`, `1` FN | ambos sao cenarios de alta sensibilidade, mas com escalas muito diferentes |
| Trade-off dominante | muitos FP para reduzir FN | ainda ha trade-off, mas com discriminacao muito superior | METABRIC melhora o compromisso global |
| Papel do neuro-fuzzy | comparativo academico | comparativo academico | nao e o modelo campeao em nenhuma trilha |

### Comparacao justa

- A comparacao e justa **metodologicamente** porque as duas trilhas usam o mesmo padrao minimo de boas praticas.
- A comparacao **nao pode** ser tratada como duelo puro de metricas, porque os datasets nao oferecem a mesma riqueza informacional.
- O ganho do METABRIC veio de dois fatores combinados:
  1. pipeline metodologicamente corrigido;
  2. dataset clinico muito mais informativo.

### Por que isso nao e cherry-picking

- O SEER nao foi apagado nem escondido; ele foi mantido e documentado como baseline corrigido.
- O METABRIC foi adotado depois de uma critica explicita ao limite do dataset anterior.
- A mesma politica de avaliacao foi mantida.
- O relatorio mostra tanto ganho quanto trade-off, inclusive o custo de falsos positivos do ensemble.

## Narrativa de defesa

### Tese principal

O Trabalho 2 mostrou duas coisas ao mesmo tempo:

1. corrigir metodologia muda a credibilidade do experimento;
2. melhorar o dataset pode mudar mais o teto do projeto do que insistir em tecnicas mais sofisticadas sobre uma base limitada.

### Narrativa oral em 5 a 10 minutos

1. O projeto comecou com um dataset de cancer de mama e uma trilha ainda fragil metodologicamente.
2. A primeira entrega real foi consertar a pergunta analitica: tirar `Survival Months` do modelo principal, fazer EDA adequada e impedir tuning no teste.
3. Com isso, o SEER virou um baseline corrigido e defensavel, mas ainda limitado em riqueza clinica.
4. A etapa seguinte foi trocar para o METABRIC, mantendo a mesma disciplina metodologica.
5. O METABRIC elevou substancialmente os resultados porque oferece tratamento, biomarcadores e subtipo molecular.
6. O ensemble final deve ser defendido como ponto operacional de alta sensibilidade, nao como melhor modelo universal.
7. O neuro-fuzzy foi mantido por valor academico, mas os resultados mostraram que ele nao foi o melhor classificador.

### Trade-offs que precisam ser ditos sem maquiagem

- No SEER, reduzir falsos negativos exigiu aceitar muitos falsos positivos.
- No METABRIC, o ensemble tambem tem trade-off, mas o ponto operacional ficou muito mais forte.
- Nem todo hibrido melhora desempenho; o valor academico tambem esta em demonstrar isso com honestidade.

### Limitacoes e trabalhos futuros

- ainda nao ha survival analysis formal;
- explicabilidade local por instancia ainda nao foi adicionada;
- robustez mais forte com validacao cruzada repetida continua como extensao;
- a defesa nao deve vender generalizacao clinica real alem do escopo do dataset publico.

## Status ao fim da Fase 2

- comparacao SEER vs METABRIC consolidada;
- tese principal escrita;
- trade-offs e limitacoes explicitados;
- pronto para desdobrar em apresentacao, artigo e audio.
