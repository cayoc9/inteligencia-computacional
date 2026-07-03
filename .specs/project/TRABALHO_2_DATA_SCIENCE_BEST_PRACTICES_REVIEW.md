# Review de Boas Praticas de Ciencia de Dados - Trabalho 2

**Ultima revisao:** 2026-07-03  
**Escopo:** `projeto_2_neuro_fuzzy/` e `projeto_2_neuro_fuzzy_metabric_clinico/`

## Objetivo

Validar se o Trabalho 2 atingiu um patamar metodologico suficiente para servir de base a:

- apresentacao;
- artigo em LaTeX;
- relatorio historico;
- audio de repasse aos integrantes.

## Resumo Executivo

O nucleo de boas praticas de ciencia de dados esta **atendido** nas duas trilhas do Projeto 2.

- **SEER v1 corrigido**: pronto como baseline educacional auditavel.
- **METABRIC v2 canonico**: pronto como trilha principal de melhoria continua.

O que permanece pendente nao esta mais no nucleo de qualidade basica. As pendencias remanescentes sao extensoes de robustez ou aprofundamento analitico.

## Matriz de Validacao

| Pratica | SEER v1 | METABRIC v2 | Evidencia |
|---|---|---|---|
| Objetivo analitico explicitado | Atendido | Atendido | specs, relatorios tecnicos, READMEs |
| Politica de vazamento definida | Atendido | Atendido | exclusao de `survival_months` do modelo principal; cenarios separados |
| Saneamento centralizado | Atendido | Atendido | `data.py`, `01_validate_data.py` |
| Dicionario de dados | Atendido | Atendido | `docs/DATA_DICTIONARY.md` |
| EDA com metadados e relacoes | Atendido | Atendido | `metadata_profile.csv`, `numeric_relationships.csv`, `categorical_relationships.csv` |
| Engenharia de features documentada | Atendido | Atendido | `features.py`, dicionario, relatorios |
| Separacao treino/validacao/teste | Atendido | Atendido | `splits.py`, scripts `03` e `04` |
| Tuning sem contaminar teste | Atendido | Atendido | threshold e pesos escolhidos na validacao |
| Metricas adequadas ao dominio | Atendido | Atendido | recall, F2, PR AUC, FN, FP, Brier |
| Baseline simples comparado | Atendido | Atendido | Logistic Regression, RF e outros tabulares |
| Comparativo do hibrido/neuro-fuzzy | Atendido | Atendido | `05_neuro_fuzzy_comparison.py` |
| Explicabilidade global | Atendido | Atendido | coeficientes e permutation importance |
| Calibracao probabilistica basica | Atendido | Atendido | `calibration_summary.csv`, curvas |
| Robustez minima por seeds | Atendido | Atendido | `stability_summary.csv` |
| Reprodutibilidade via pipeline | Atendido | Atendido | `run_pipeline.py` |
| Reprodutibilidade via notebook | Atendido | Atendido | `nbconvert` executado |
| Testes automatizados | Atendido | Atendido | `18 passed` SEER, `7 passed` METABRIC |
| Documentacao viva | Atendido | Atendido | `.specs`, `STATUS.md`, docs de resumo |

## Pontos Fortes

1. **A trilha deixou de ser ad hoc.**  
   Ha contrato de dados, feature policy e artefatos versionados para cada fase.

2. **O erro metodologico mais grave foi removido.**  
   Ensemble agora faz tuning na validacao, nao no teste.

3. **A qualidade do dataset passou a ser tratada como parte do experimento.**  
   O trabalho nao ficou preso a "melhorar modelo em base ruim"; houve troca fundamentada para uma base clinica mais rica.

4. **A narrativa esta tecnicamente defensavel.**  
   O trabalho consegue explicar objetivo, trade-offs, ganho, perda e limitacoes sem depender de inferencias vagas.

## Pendencias Reais

### Nucleo metodologico

Nenhuma pendencia critica aberta.

### Extensoes desejaveis, mas nao bloqueantes

1. Validacao cruzada estratificada ou repetida para robustez mais forte.
2. Explicabilidade local por instancia, como SHAP ou analise de casos.
3. Analise de custo/beneficio clinico mais formal para threshold.
4. Eventual re-enquadramento futuro para survival analysis, caso o grupo queira explorar horizonte temporal de fato.

## Decisao Final

Do ponto de vista de boas praticas de ciencia de dados, o Trabalho 2 esta **pronto para consolidacao historica**.

Isso significa:

- a base documental ja suporta um relatorio historico unico;
- a apresentacao ja pode ser montada sem lacuna metodologica central;
- o artigo em LaTeX ja pode ser estruturado sobre resultados defensaveis;
- o audio de repasse ja pode se apoiar em fatos consistentes e nao em improviso.
