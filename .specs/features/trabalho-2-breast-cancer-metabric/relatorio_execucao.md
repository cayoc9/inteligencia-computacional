# Relatorio de Execucao: Evolucao Clinica METABRIC do Projeto 2

**Feature**: `.specs/features/trabalho-2-breast-cancer-metabric/spec.md`  
**Ultima atualizacao**: 2026-07-03  
**Status**: Executado, validado e promovido a evolucao canonica da v2

## Escopo executado

A evolucao METABRIC foi promovida de "fork paralelo" para "trilha canonica da v2" do Projeto 2. A logica e simples:

1. o SEER continua como baseline educacional corrigido;
2. o METABRIC passa a ser a trilha principal de melhoria continua;
3. ambos agora compartilham o mesmo padrao minimo de boas praticas.

## O que foi fechado na v2

- saneamento centralizado;
- dicionario de dados;
- EDA com metadados e relacoes;
- engenharia de features;
- suite de modelos tabulares;
- split treino/validacao/teste;
- ensemble com pesos e threshold vindos da validacao;
- comparativo neuro-fuzzy;
- explicabilidade, calibracao e estabilidade por seeds;
- notebook narrativo proprio.

## Correcao tecnica mais importante

O ponto critico corrigido nesta rodada foi o ensemble do METABRIC. A versao antiga ainda escolhia pesos e threshold no teste. A versao atual usa:

- treino para ajuste dos modelos;
- validacao para pesos e threshold;
- teste intocado para reporte final.

## Resultado principal da v2

### Melhor modelo individual sem `survival_months`

**GradientBoosting**
- accuracy `0.7048`
- precision `0.7185`
- recall `0.7953`
- F2 `0.7787`
- PR AUC `0.7600`
- falsos negativos `44`

### Melhor ponto operacional

**Ensemble ponderado corrigido**
- threshold `0.16`, escolhido na validacao
- accuracy `0.6090`
- precision `0.5944`
- recall `0.9953`
- F2 `0.8770`
- PR AUC `0.7586`
- falsos negativos `1`
- falsos positivos `146`

## Leitura correta dos resultados

- O ganho da v2 nao deve ser vendido como "ensemble magico".
- O principal fator de melhoria foi a combinacao entre dataset clinico melhor e pipeline metodologicamente mais limpo.
- O modelo individual forte no METABRIC ja supera com folga a trilha SEER.
- O ensemble corrigido deve ser apresentado como cenario de altissima sensibilidade, nao como melhor ponto universal.

## Validacoes executadas

- `projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy_metabric_clinico/tests -q`
  - `7 passed`
- `projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy_metabric_clinico/run_pipeline.py`
  - concluido
- `projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert --to notebook --execute projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb --output /tmp/projeto_2_metabric_clinico.executed.ipynb`
  - concluido

## Conclusao executiva

A trilha METABRIC agora esta pronta para ser tratada como evolucao canonica do Projeto 2. O que resta para a proxima etapa nao e mais "corrigir metodologia central", e sim consolidar narrativa historica unica para apresentacao, artigo e audio de repasse.
