# Outline do Artigo LaTeX - Trabalho 2

## 1. Introducao

- contexto de sistemas hibridos e ensemble em saude;
- problema de risco de obito em cancer de mama;
- objetivo do trabalho;
- contribuicoes: correcao metodologica do baseline e evolucao para dataset clinico melhor.

## 2. Materiais e Metodos

### 2.1 Datasets
- SEER corrigido como baseline educacional;
- METABRIC como evolucao canonica.

### 2.2 Politica de dados
- sanitizacao;
- dicionario de dados;
- EDA e metadados;
- exclusao de `Survival Months` do modelo principal.

### 2.3 Modelagem
- modelos tabulares;
- ensemble ponderado com validacao;
- comparativo neuro-fuzzy.

### 2.4 Avaliacao
- recall, F2, PR AUC, FN, FP;
- explicabilidade, calibracao e estabilidade.

## 3. Resultados

### 3.1 Resultados no SEER

### 3.2 Resultados no METABRIC

### 3.3 Comparacao entre trilhas

## 4. Discussao

- impacto da correcao metodologica;
- impacto da qualidade do dataset;
- trade-offs do ensemble;
- papel academico do neuro-fuzzy.

## 5. Limitacoes

- dataset publico;
- ausencia de validacao externa;
- ausencia de survival analysis formal;
- comparacao entre bases heterogeneas.

## 6. Conclusao

- sintese final da evolucao do projeto;
- por que o METABRIC se tornou a trilha canonica;
- direcoes futuras.

## Mapeamento de fonte

- `relatorio_historico.md` fornece a narrativa principal;
- `qa_professor_checkpoints.md` fornece a secao de objecoes e respostas;
- `SOURCE_MAP.md` fornece rastreabilidade de processo.
