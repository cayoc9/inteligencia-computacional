# Outline do Artigo LaTeX - Trabalho 2

## 1. Introducao

- contexto de sistemas hibridos e ensemble em saude;
- problema de risco de obito em cancer de mama;
- objetivo do trabalho;
- contribuicoes: correcao metodologica do baseline e evolucao para dataset clinico melhor.
- o artigo deve ser enxuto e provar, nao narrar tudo o que aconteceu;
- o relatorio historico fica como fonte de contexto, nao como copia integral no paper.

## 2. Materiais e Metodos

### 2.1 Datasets
- SEER corrigido como baseline educacional;
- METABRIC como evolucao canonica.
- inserir tabela comparativa resumida com numero de registros, target, variaveis clinicas e papel de cada trilha.

### 2.2 Politica de dados
- sanitizacao;
- dicionario de dados;
- EDA e metadados;
- exclusao de `Survival Months` do modelo principal.
- destacar explicitamente que `Survival Months` fica fora do modelo principal e pode aparecer apenas como sensibilidade.

### 2.3 Modelagem
- modelos tabulares;
- ensemble ponderado com validacao;
- comparativo neuro-fuzzy.
- explicitar que o ensemble e um ponto operacional de alta sensibilidade, nao campeao universal.

### 2.4 Avaliacao
- recall, F2, PR AUC, FN, FP;
- explicabilidade, calibracao e estabilidade.
- incluir tabela de metricas e, se possivel, figura de calibracao/importance.

## 3. Resultados

### 3.1 Resultados no SEER
- baseline individual e ponto operacional do ensemble;
- trade-off entre recall e falsos positivos;
- leitura correta: baseline corrigido, nao modelo final canonico.

### 3.2 Resultados no METABRIC
- baseline individual forte e ensemble final;
- destaque do quase zero de falsos negativos;
- custo pago em falsos positivos.

### 3.3 Comparacao entre trilhas
- separar ganho por dataset de ganho por pipeline;
- deixar claro que o METABRIC sobe o teto de aprendizagem.

## 4. Discussao

- impacto da correcao metodologica;
- impacto da qualidade do dataset;
- trade-offs do ensemble;
- papel academico do neuro-fuzzy.
- discutir por que o trabalho melhora mais pela base e pela metodologia do que por troca isolada de algoritmo.

## 5. Limitacoes

- dataset publico;
- ausencia de validacao externa;
- ausencia de survival analysis formal;
- comparacao entre bases heterogeneas.
- evitar qualquer leitura de uso clinico direto.

## 6. Conclusao

- sintese final da evolucao do projeto;
- por que o METABRIC se tornou a trilha canonica;
- direcoes futuras.
- reforcar que o SEER continua valioso como baseline corrigido.

## Mapeamento de fonte

- `relatorio_historico.md` fornece a narrativa principal;
- `qa_professor_checkpoints.md` fornece a secao de objecoes e respostas;
- `SOURCE_MAP.md` fornece rastreabilidade de processo.
- [analise-template-artigo-trabalho-2.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/reports/consolidados/analise-template-artigo-trabalho-2.md) complementa a escrita com o que adaptar do template `Sleep_Health`.
