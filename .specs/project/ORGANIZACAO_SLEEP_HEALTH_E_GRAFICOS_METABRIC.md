# Organizacao do Sleep Health e Mapa de Graficos para o METABRIC

## Executive Summary

O projeto `sleep_health` foi isolado em `projeto_sleep_health_rf_vs_rn/`, retirando da raiz os scripts, dados, notebook, modelos, figuras e diagnosticos operacionais do experimento de sono [1][2][3]. Em paralelo, foi criada uma suite de graficos equivalentes para o METABRIC em `projeto_2_neuro_fuzzy_metabric_clinico/08_generate_sleep_health_equivalent_graphs.py`, cobrindo EDA, comparacao de modelos, curvas de discriminacao, threshold, importancia de features e matriz de confusao [4][5].

## Key Findings

- **Separacao fisica do projeto de sono**: os artefatos operacionais do `sleep_health` sairam da raiz e passaram a viver em um diretorio proprio [1][3].
- **Suite oficial de graficos do sono identificada**: o projeto de sono tinha um conjunto claro de figuras de EDA e um conjunto complementar de figuras finais/diagnosticas [1][2][3].
- **METABRIC agora tem grade comparavel**: foram gerados 11 graficos equivalentes ou semanticamente analogos para o Projeto 2 METABRIC [4][5].
- **Nem toda equivalencia e literal**: como os domínios mudam, `occupation_vs_target` no sono virou `pam50_vs_target` no METABRIC, e o boxplot de variaveis do sono virou boxplot de variaveis clinicas-chave [1][4][5].

## Detailed Analysis

### 1. O que foi separado do projeto de sono

Os seguintes blocos foram isolados em `projeto_sleep_health_rf_vs_rn/`:

- pipeline principal `01` a `05`;
- `data/`, `models/`, `notebooks/` e `scripts/`;
- `docs/DATA_DICTIONARY.md`;
- `reports/diagnostics/`, `reports/figures/`, `reports/fragmentos/`;
- relatorios consolidados da V1;
- template `Sleep_Health` usado historicamente como base editorial do artigo [1][3].

### 2. Suite de graficos identificada no Sleep Health

#### 2.1 Graficos de EDA

| Grafico | Arquivo | Origem | Papel |
|---|---|---|---|
| Heatmap de correlacao | `correlation_heatmap.png` | `02_eda.py` | relacoes numericas globais |
| Distribuicao de idade por target | `age_distribution_target.png` | `02_eda.py` | distribuicao demografica por classe |
| Ocupacao vs target | `occupation_vs_target.png` | `02_eda.py` | principal leitura categorica |
| Boxplots das variaveis de sono | `sleep_features_boxplot.png` | `02_eda.py` | contraste direto das variaveis centrais por classe |

#### 2.2 Graficos finais e diagnosticos

| Grafico | Arquivo | Origem | Papel |
|---|---|---|---|
| Comparacao de metricas | `comparacao_metricas.png` | `scripts/generate_final_graphs.py` | comparacao de modelos |
| Curvas ROC | `curvas_roc.png` | `scripts/generate_final_graphs.py` | discriminacao por threshold |
| Curvas PR | `curvas_pr.png` | `scripts/generate_final_graphs.py` | leitura mais sensivel ao desbalanceamento |
| Threshold optimization | `threshold_otimizacao.png` | `scripts/generate_final_graphs.py` | escolha do ponto de corte |
| Feature importance | `feature_importance.png` | `scripts/generate_final_graphs.py` | interpretabilidade do melhor modelo |
| Matriz de confusao | `confusion_matrix_histgb.png` | `scripts/generate_final_graphs.py` | leitura operacional do melhor modelo |
| AUC por feature isolada | `feature_auc_individual.png` | `scripts/generate_final_graphs.py` | sinal individual das features |

### 3. Graficos gerados para o METABRIC

| Sleep Health | METABRIC | Tipo de equivalencia | Observacao |
|---|---|---|---|
| `correlation_heatmap.png` | `correlation_heatmap.png` | direta | ambos mostram correlacao numerica global |
| `age_distribution_target.png` | `age_distribution_target.png` | direta | mesma logica de distribuicao etaria por classe |
| `occupation_vs_target.png` | `pam50_vs_target.png` | semantica | troca de variavel categorica-chave do dominio |
| `sleep_features_boxplot.png` | `metabric_features_boxplot.png` | semantica | troca de variaveis de sono por idade, tumor size, NPI e linfonodos |
| `comparacao_metricas.png` | `comparacao_metricas.png` | direta | comparacao de modelos no teste |
| `curvas_roc.png` | `curvas_roc.png` | direta | curvas ROC com probabilidades reais |
| `curvas_pr.png` | `curvas_pr.png` | direta | curvas PR com baseline explicito |
| `threshold_otimizacao.png` | `threshold_otimizacao.png` | direta | threshold do ensemble escolhido na validacao |
| `feature_importance.png` | `feature_importance.png` | semantica | agora usando GradientBoosting no METABRIC |
| `confusion_matrix_histgb.png` | `confusion_matrix_ensemble.png` | semantica | matriz do modelo final operacional do projeto |
| `feature_auc_individual.png` | `feature_auc_individual.png` | direta | AUC individual das features numericas sem leakage |

### 4. Arquivos principais do METABRIC usados para isso

- EDA estrutural: `projeto_2_neuro_fuzzy_metabric_clinico/src/breast_cancer_survival/eda.py`
- tabelas de modelos e ensemble: `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/`
- gerador novo de figuras equivalentes: `projeto_2_neuro_fuzzy_metabric_clinico/08_generate_sleep_health_equivalent_graphs.py` [4][5]

## Areas of Consensus

- O `sleep_health` ja tinha uma suite visual bem definida e reaproveitavel como grade metodologica [1][2][3].
- O METABRIC precisava de uma camada visual adicional para ficar comparavel ao nivel de acabamento do projeto de sono [4][5].
- As equivalencias mais honestas sao por funcao analitica, nao por nome literal da variavel [1][4][5].

## Areas of Debate

- **Variavel categorica equivalente**: `occupation` no sono nao tem correspondente literal no METABRIC. A escolha por `pam50_subtype` foi interpretativa, mas tecnicamente defensavel por relevancia clinica [4][5].
- **Matriz de confusao do METABRIC**: foi priorizado o ensemble final, nao o melhor modelo individual. Isso favorece coerencia com a narrativa do Projeto 2, mas nao e uma copia literal da escolha do `sleep_health` [2][5].
- **Feature importance**: no sono a leitura final estava centrada no melhor classificador tabular do diagnostico; no METABRIC a versao equivalente foi ancorada em `gradient_boosting`, enquanto a escolha final de operacao continua sendo o ensemble [2][5].

## Sources

[1] `projeto_sleep_health_rf_vs_rn/02_eda.py` e `projeto_sleep_health_rf_vs_rn/README.md`. Fonte primaria do pipeline de EDA e da organizacao atual do projeto de sono. Credibilidade: artefato canonico do repositorio.

[2] `projeto_sleep_health_rf_vs_rn/scripts/generate_final_graphs.py`. Fonte primaria da suite final de visualizacoes do projeto de sono. Credibilidade: artefato canonico do repositorio.

[3] `projeto_sleep_health_rf_vs_rn/reports/figures/` e `projeto_sleep_health_rf_vs_rn/reports/diagnostics/`. Evidencia material dos graficos e diagnosticos gerados. Credibilidade: artefatos persistidos do experimento.

[4] `projeto_2_neuro_fuzzy_metabric_clinico/src/breast_cancer_survival/eda.py` e `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/`. Base estrutural dos artefatos do Projeto 2 METABRIC. Credibilidade: artefatos canonicos do repositorio.

[5] `projeto_2_neuro_fuzzy_metabric_clinico/08_generate_sleep_health_equivalent_graphs.py`. Fonte primaria da nova suite de figuras comparaveis geradas para o METABRIC. Credibilidade: script implementado e executado no repositorio.

## Gaps and Further Research

- Atualizar mais documentos historicos secundarios que ainda mencionam o layout antigo da raiz.
- Decidir se a suite do METABRIC deve substituir visualmente parte dos graficos antigos nas apresentacoes do Trabalho 2.
- Se houver interesse em simetria total, gerar tambem para o SEER a mesma grade expandida que agora existe no METABRIC.
