# Baseline Oficial da Trilha Metodologica do Trabalho 2

## Objetivo

Este documento fixa a versao factual minima da historia metodologica do Trabalho 2 antes de novos ajustes narrativos de apresentacao, artigo ou audio.

Ele responde quatro perguntas:

1. quais dados realmente entraram no projeto;
2. como esses dados foram saneados e enquadrados;
3. por que a trilha saiu do SEER e avancou para o METABRIC;
4. qual e a leitura oficial, hoje, da sequencia metodologica completa.

## Regra de Leitura

- os artefatos do repositorio continuam sendo a fonte final sobre implementacao e resultados;
- as fontes externas abaixo servem para contextualizar a origem e a natureza dos datasets;
- a narrativa oficial nao pode contradizer os contratos de dados, notebooks, CSVs e relatorios tecnicos locais.

## 1. Inventario Oficial dos Dados Trabalhados

### 1.1 SEER derivado usado na trilha inicial

**Arquivo local:** `projeto_2_neuro_fuzzy/dataset/Breast_Cancer.csv`

**Estado bruto observado no repositorio**

- `4024` linhas e `16` colunas;
- `1` duplicata bruta;
- `0` valores ausentes no CSV bruto;
- alvo bruto `Status`: `3408` `Alive` e `616` `Dead`.

**Estado apos saneamento do pipeline**

- `4023` linhas e `16` colunas;
- duplicata removida;
- `0` valores ausentes;
- alvo saneado: `3407` classe `0` e `616` classe `1`;
- taxa positiva aproximada: `15,31%`.

**Leitura metodologica**

O arquivo local e um recorte tabular pequeno e altamente estruturado, com variaveis demograficas, estadiamento, tamanho tumoral, receptores hormonais e dois campos de desfecho/seguimento: `Survival Months` e `Status`.

Isso tornou o dataset util para:

- montar rapidamente uma trilha completa de classificacao supervisionada;
- exercitar limpeza, EDA, engenharia de features e comparacao de modelos;
- demonstrar com clareza o risco de vazamento quando uma coluna de seguimento aparece junto do alvo final.

Ao mesmo tempo, isso limitou a profundidade clinica da trilha:

- poucas variaveis de tratamento;
- pouca informacao molecular;
- desbalanceamento forte da classe positiva;
- presenca explicita de uma variavel de acompanhamento posterior (`Survival Months`) que podia inflar modelos se usada ingenuamente.

**Contexto externo minimo**

- O programa SEER e uma fonte oficial de estatisticas populacionais de cancer mantida pelo NCI e cobre diagnostico, tratamento e desfechos.
- A documentacao oficial do SEER organiza as variaveis em grupos como demografia, caracteristicas do tumor, tratamento e follow-up/datas.
- O calculo de tempo de sobrevida no SEER deriva de datas de acompanhamento e contato, logo e semanticamente uma informacao de seguimento, nao uma feature de diagnostico basal.

## 1.2 METABRIC clinico usado na evolucao v2

**Arquivo local:** `projeto_2_neuro_fuzzy_metabric_clinico/dataset/Breast Cancer METABRIC.csv`

**Estado bruto observado no repositorio**

- `2509` linhas e `34` colunas;
- `0` duplicatas brutas;
- alvo bruto `Overall Survival Status`: `1144` `Deceased`, `837` `Living` e `528` ausentes;
- ausencias relevantes em varias colunas clinicas e moleculares, incluindo cirurgia, cellularity, HER2, PAM50 e estagio.

**Estado apos saneamento do pipeline**

- `1876` linhas e `34` colunas;
- `633` linhas removidas por ausencia em campos nucleares do contrato atual;
- alvo saneado: `801` classe `0` e `1075` classe `1`;
- taxa positiva aproximada: `57,30%`;
- ainda restam `1081` celulas ausentes distribuidas em colunas nao nucleares.

**Observacao importante sobre a perda de linhas**

O saneamento atual exige presenca simultanea de:

- `status`;
- `survival_months`;
- `age`;
- `tumor_size`;
- `grade`.

No bruto, os `528` faltantes de `status` coincidem exatamente com os `528` faltantes de `survival_months`. As demais perdas vieram principalmente de `tumor_size`, `grade` e `age`.

**Leitura metodologica**

O METABRIC local e uma base muito mais rica para a pergunta de risco em cancer de mama porque adiciona:

- informacao de tratamento;
- subtipo molecular (`PAM50`);
- marcadores como `HER2`, `ER`, `PR`;
- `Nottingham prognostic index`;
- `mutation_count`;
- variaveis de recidiva e status vital pos-acompanhamento.

Isso elevou o teto analitico do projeto, mas introduziu um custo metodologico real:

- missingness relevante;
- maior necessidade de politica explicita de leakage;
- necessidade de separar o que e feature basal do que e desfecho ou acompanhamento.

**Contexto externo minimo**

- O artigo original do METABRIC descreve integracao genomica e transcriptomica em `2.000` tumores primarios de mama com acompanhamento clinico de longo prazo.
- O ecossistema METABRIC expandido em cBioPortal e descrito com `2509` tumores primarios e `548` normais pareados em extensoes posteriores de sequenciamento.
- A pagina do dataset Kaggle usada no projeto apresenta o arquivo como perfis clinicos de `2509` pacientes com cancer de mama.

## 2. Trilha Metodologica Oficial, em Ordem

### Fase 0: escolha do tema

O trabalho foi deliberadamente enquadrado em oncologia, com foco em risco de obito em cancer de mama, por tres motivos:

1. o tema permite discutir custo de falso negativo com seriedade;
2. os datasets publicos disponiveis oferecem um caminho claro para classificacao supervisionada;
3. a disciplina pedia justificativa de arquitetura, baseline e leitura critica dos trade-offs.

### Fase 1: escolha da primeira base publica

A primeira base efetivamente adotada foi o recorte tabular derivado do SEER.

Razoes praticas da escolha:

- acesso simples;
- schema pequeno o suficiente para evoluir rapido;
- presenca de atributos clinico-patologicos classicos;
- aderencia imediata a uma trilha de classificacao.

### Fase 2: sanitizacao e contrato de dados

Na trilha SEER, a primeira consolidacao metodologica fez:

- padronizacao de nomes de colunas;
- limpeza de strings;
- mapeamento do alvo `Alive=0`, `Dead=1`;
- normalizacao do campo `grade`;
- remocao de duplicata;
- formalizacao de dicionario de dados e contrato do dataset.

Na trilha METABRIC, o mesmo principio foi reaplicado, com maior complexidade:

- renomeacao de colunas clinicas e moleculares para um schema consistente;
- mapeamento do alvo `Living=0`, `Deceased=1`;
- coercao numerica controlada em campos clinicos;
- exclusao de linhas sem desfecho ou sem campos nucleares definidos pelo contrato;
- formalizacao da politica de leakage para `survival_months`, recidiva e status pos-acompanhamento.

### Fase 3: EDA e leitura estrutural do problema

Nos dois datasets a EDA deixou de ser ornamental e passou a cumprir funcao metodologica:

- perfil de metadados;
- relacoes numericas e categoricas com o alvo;
- qualidade do dado;
- distribuicao de classe;
- exposicao explicita dos campos de seguimento.

Foi nessa fase que a trilha SEER mostrou seu principal alerta conceitual: `Survival Months` parecia fortemente informativa, mas representava acompanhamento posterior e nao deveria compor o modelo principal de risco basal.

### Fase 4: feature engineering e primeira rodada de modelos

A primeira rodada completa, ainda no SEER corrigido, incluiu:

- engenharia de features clinicas tabulares;
- baselines explicaveis;
- arvores e boosting;
- MLP;
- ensemble ponderado;
- trilha neuro-fuzzy comparativa.

O ponto oficial aqui nao e "qual modelo ganhou" isoladamente, e sim:

- o pipeline deixou de ser um conjunto de scripts soltos;
- o ensemble deixou de escolher threshold no teste;
- o modelo principal passou a ser lido com foco em recall, F2, PR AUC e falsos negativos, nao so accuracy.

### Fase 5: descoberta dos limites do SEER

Os limites do SEER nao foram apenas numericos; foram estruturais.

Os principais sinais foram:

1. dependencia forte de trade-off de threshold para reduzir falsos negativos;
2. profundidade clinica restrita para sustentar uma narrativa mais rica de risco oncologico;
3. presenca de coluna de seguimento que exigia vigilancia metodologica permanente;
4. neuro-fuzzy fraco como classificador, o que enfraquecia qualquer tentativa de vender sofisticacao pela sofisticacao.

Isso levou a uma conclusao importante: insistir apenas em ajustes de modelo sobre a mesma base teria retorno metodologico menor do que melhorar a qualidade do dado.

### Fase 6: troca orientada de dataset

A ida ao METABRIC nao foi uma substituicao oportunista para buscar metrica melhor. A leitura correta e outra:

- o SEER foi mantido como baseline corrigido e auditavel;
- a troca foi justificada por limite estrutural da base anterior;
- a mesma disciplina metodologica foi reaplicada no novo dataset;
- o objetivo passou a ser testar o mesmo problema em uma base com mais sinal clinico e molecular.

Essa e a virada central da narrativa oficial do projeto.

### Fase 7: rerun completo com base mais rica

No METABRIC, o projeto refez a trilha completa:

- saneamento;
- EDA;
- engenharia de features;
- suite tabular;
- ensemble com validacao separada;
- comparativo neuro-fuzzy;
- explicabilidade;
- calibracao;
- estabilidade por seeds;
- notebook unico.

Ou seja, o projeto nao apenas "copiou scripts" para outra base. Ele reaplicou o mesmo contrato metodologico para testar se o teto do projeto mudava quando o dado melhorava.

### Fase 8: leitura oficial atual

Hoje, a leitura correta e:

- `projeto_2_neuro_fuzzy/` = baseline SEER corrigido, historicamente valioso e metodologicamente defensavel;
- `projeto_2_neuro_fuzzy_metabric_clinico/` = evolucao canonica v2, com base mais rica e maior poder explicativo para a apresentacao principal.

## 3. Evidencias Operacionais que Sustentam a Narrativa

### SEER

- contrato e saneamento: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/data.py`
- feature engineering: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py`
- EDA e metadados: `projeto_2_neuro_fuzzy/reports/tables/metadata_profile.csv`
- resumo executivo: `projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md`
- execucao final: `.specs/features/trabalho-2-breast-cancer/relatorio_execucao.md`

**Split oficial atual**

- treino: `2413`
- validacao: `805`
- teste: `805`
- positivos em validacao: `123`
- positivos em teste: `123`

### METABRIC

- contrato e saneamento: `projeto_2_neuro_fuzzy_metabric_clinico/src/breast_cancer_survival/data.py`
- feature engineering: `projeto_2_neuro_fuzzy_metabric_clinico/src/breast_cancer_survival/features.py`
- EDA e metadados: `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/metadata_profile.csv`
- resumo executivo: `projeto_2_neuro_fuzzy_metabric_clinico/docs/PROJECT_EXECUTION_SUMMARY.md`
- execucao final: `.specs/features/trabalho-2-breast-cancer-metabric/relatorio_execucao.md`

**Split oficial atual**

- treino: `1125`
- validacao: `375`
- teste: `376`
- positivos em validacao: `215`
- positivos em teste: `215`

## 4. O Que Esta Fechado como Fato

| Afirmacao | Status | Evidencia principal |
|---|---|---|
| O tema oficial passou a ser cancer de mama com foco em risco de obito | Fechado | `.specs/features/trabalho-2-breast-cancer/introducao_relatorio.md` |
| A primeira trilha completa foi feita sobre o recorte SEER | Fechado | `projeto_2_neuro_fuzzy/` e `.specs/features/trabalho-2-breast-cancer/relatorio_execucao.md` |
| `Survival Months` foi tratado como leakage/follow-up no modelo principal | Fechado | `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md`, `features.py`, `reports/analise_objetivo_survival_months.md` |
| O SEER continuou como baseline corrigido, nao foi apagado | Fechado | `.specs/features/trabalho-2-relatorio-historico/relatorio_historico.md` |
| A migracao para METABRIC veio de limite estrutural do SEER | Fechado | `introducao_relatorio.md`, `relatorio_historico.md`, diferenca objetiva de riqueza de variaveis entre as bases |
| O METABRIC virou a leitura canonica v2 | Fechado | `.specs/features/trabalho-2-breast-cancer-metabric/relatorio_execucao.md` |

## 5. Baseline Narrativo Recomendado

Se a equipe quiser uma formulacao curta e fiel aos fatos, a narrativa-base e esta:

1. escolhemos o tema de cancer de mama por relevancia e pela necessidade de discutir erro clinico;
2. comecamos com um recorte publico derivado do SEER porque ele permitia montar rapidamente a trilha completa;
3. saneamos, fizemos EDA, engenharia de features e uma primeira rodada de baselines, ensemble e neuro-fuzzy;
4. essa rodada serviu para duas coisas: produzir resultados e revelar limites reais da base, sobretudo leakage por seguimento e baixa riqueza clinica;
5. em vez de apenas insistir em ajuste fino, migramos para o METABRIC, mantendo a mesma disciplina metodologica;
6. refizemos toda a trilha em uma base clinica e molecularmente mais rica;
7. o resultado final nao e so um modelo melhor, mas uma historia metodologica melhor: correcao de pipeline mais melhora de qualidade de dado.

## 6. Pontos Abertos so de Narrativa, nao de Fato

Os seguintes pontos ainda podem ser ajustados depois sem ferir a base factual:

1. dizer "troca de dataset" ou "evolucao para uma base mais rica";
2. decidir se a apresentacao mostrara o SEER como primeira metade forte da historia ou apenas como baseline curto;
3. calibrar o peso da palavra "canonico" conforme o publico;
4. decidir se as referencias externas vao citar Kaggle, artigo original do METABRIC ou ambos na fala oral.

## 7. Fontes Externas de Contexto dos Dados

### SEER

- https://seer.cancer.gov/
- https://seer.cancer.gov/news/SEER-Overview-Variables.pdf
- https://seer.cancer.gov/survivaltime/

### METABRIC

- https://www.nature.com/articles/nature10983
- https://www.cbioportal.org/study?id=brca_metabric
- https://www.kaggle.com/datasets/gunesevitan/breast-cancer-metabric
