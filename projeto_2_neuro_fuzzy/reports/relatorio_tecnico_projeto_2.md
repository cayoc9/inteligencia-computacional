# Relatorio Tecnico: Projeto 2 Breast Cancer

## Objetivo corrigido

O objetivo corrigido e prever risco de obito (`Status = Dead`) a partir de atributos clinicos disponiveis no diagnostico.

## Objetivo testado antes

O baseline inicial usava `Survival Months` como feature para prever `Status`. Essa configuracao deve ser interpretada como experimento contaminado por informacao posterior ao acompanhamento, nao como predicao em diagnostico.

## Dicionario de dados

O dicionario especifico do Projeto 2 fica em `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` e documenta colunas brutas, nomes sanitizados, tipos, papeis analiticos, risco de vazamento e features derivadas.

## Metadados e relacoes

A EDA gera `metadata_profile.csv`, `numeric_relationships.csv` e `categorical_relationships.csv`. Esses arquivos registram cardinalidade, tipos, exemplos, relacoes com `Status` e alerta de vazamento/follow-up para `Survival Months`.

## Modelagem

O pipeline compara modelos tabulares, aplica threshold tuning e monta ensemble ponderado. A avaliacao prioriza falsos negativos, recall, precision, F2 e PR AUC, em vez de acuracia isolada.

## Neuro-fuzzy

O neuro-fuzzy e mantido como comparativo academico. A implementacao usa funcoes de pertinencia manuais mais MLP, portanto deve ser descrita como neuro-fuzzy cooperativo, nao como ANFIS completo.

