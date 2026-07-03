# Relatorio de Execucao: Trabalho 2 Breast Cancer

**Feature**: `.specs/features/trabalho-2-breast-cancer/spec.md`  
**Ultima atualizacao**: 2026-07-03  
**Status**: Executado, validado e documentado

## Escopo executado

O Trabalho 2 foi materializado em duas trilhas:

1. `projeto_2_neuro_fuzzy/`: trilha SEER corrigida, auditavel e alinhada a boas praticas de ciencia de dados.
2. `projeto_2_neuro_fuzzy_metabric_clinico/`: fork clinico para melhoria continua com dataset mais rico.

Este relatorio registra principalmente a execucao efetiva da trilha SEER, que e a base canonica do Projeto 2 no repositorio.

## O que foi feito na trilha SEER

### Fase 1: Contrato de dados e EDA

- Validacao do CSV bruto e saneamento centralizado.
- Mapeamento do alvo `Status` para `Alive=0`, `Dead=1`.
- Tratamento de schema inconsistente e remocao de duplicata.
- Dicionario de dados especifico do projeto.
- EDA com:
  - metadados;
  - relacoes numericas;
  - relacoes categoricas;
  - sumario de qualidade;
  - figuras de apoio.

### Fase 2: Politica de vazamento e modelagem

- Exclusao de `Survival Months` do modelo principal.
- Analise de sensibilidade separada com `Survival Months`.
- Engenharia de features clinicas.
- Suite tabular com:
  - Logistic Regression
  - Random Forest
  - ExtraTrees
  - HistGradientBoosting
  - GradientBoosting
  - AdaBoost
  - SVM calibrado
  - MLP

### Fase 3: Correcao metodologica do ensemble

- Introducao de split `treino / validacao / teste`.
- Pesos do ensemble escolhidos na validacao.
- Threshold do ensemble escolhido na validacao e congelado para o teste.
- Persistencia separada de resultados de validacao e teste.

### Fase 4: Comparativo neuro-fuzzy

- Refatoracao da trilha fuzzy para usar o mesmo contrato de dados.
- Comparacao justa com o pipeline principal.
- Posicionamento explicito como fuzzy manual + MLP, nao ANFIS completo.

### Fase 5: Explicabilidade, calibracao e robustez

- Coeficientes e permutation importance da Logistic Regression.
- Curvas de calibracao e Brier score.
- Analise curta de estabilidade por 5 seeds para:
  - Logistic Regression
  - ensemble ponderado

### Fase 6: Narrativa e documentacao

- Notebook narrativo sincronizado com os scripts.
- Relatorio tecnico atualizado.
- README e docs do projeto atualizados.
- Specs TLC, status executivo e docs de codebase sincronizados.

## Resultados principais da trilha SEER

### Sem vazamento

**Logistic Regression**
- accuracy `0.6807`
- precision `0.2641`
- recall `0.6098`
- F2 `0.4832`
- PR AUC `0.3525`
- falsos negativos `48`

**Ensemble corrigido**
- threshold `0.22`, escolhido na validacao
- accuracy `0.5665`
- precision `0.2271`
- recall `0.7642`
- F2 `0.5188`
- PR AUC `0.3196`
- falsos negativos `29`
- falsos positivos `320`

**Neuro-fuzzy cooperativo**
- accuracy `0.8112`
- precision `0.3505`
- recall `0.2764`
- F2 `0.2886`
- PR AUC `0.3052`
- falsos negativos `89`

### Estabilidade por 5 seeds

**Logistic Regression**
- recall medio `0.6179 +- 0.0752`
- F2 medio `0.4983 +- 0.0560`
- PR AUC media `0.3780 +- 0.0338`
- FN medio `47.0`

**Ensemble**
- recall medio `0.7724 +- 0.0959`
- F2 medio `0.5048 +- 0.0311`
- PR AUC media `0.3422 +- 0.0317`
- FN medio `28.0`
- FP medio `351.8`

## O que foi validado

- `projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy/tests -q`
  - `18 passed`
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy/run_pipeline.py`
  - concluido
- `projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb`
  - concluido
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy/06_explainability.py`
  - concluido
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy/07_stability_analysis.py`
  - concluido

## Artefatos finais relevantes

### Projeto 2 SEER

- `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md`
- `projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md`
- `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`
- `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`
- `projeto_2_neuro_fuzzy/reports/tables/ensemble_test_summary.csv`
- `projeto_2_neuro_fuzzy/reports/tables/calibration_summary.csv`
- `projeto_2_neuro_fuzzy/reports/tables/stability_summary.csv`

### Fork METABRIC

- `projeto_2_neuro_fuzzy_metabric_clinico/docs/DATA_DICTIONARY.md`
- `projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb`
- `projeto_2_neuro_fuzzy_metabric_clinico/reports/relatorio_tecnico_projeto_2_metabric.md`

## Leitura correta da execucao

- O Projeto 2 SEER nao esta mais em estado experimental solto; ele virou pipeline rastreavel.
- O erro metodologico mais grave do ensemble foi corrigido.
- A Logistic Regression continua importante como baseline forte e explicavel.
- O ensemble deve ser lido como ponto operacional de maior sensibilidade.
- O METABRIC continua como trilha de melhoria continua, nao como substituicao silenciosa da trilha SEER.

## Pendencias reais

- consolidar relatorio final/PDF da disciplina;
- fechar narrativa da apresentacao;
- decidir explicitamente se a defesa mostrara apenas SEER ou SEER + METABRIC;
- se houver tempo, ampliar explicabilidade local e robustez com validacao cruzada.
