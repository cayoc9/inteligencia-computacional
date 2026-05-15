# Estrutura do Projeto

## Visão Geral

```
.
├── 01_check_data.py              # Inspeção: shape, nulos, duplicatas
├── 02_eda.py                     # EDA: distribuições, correlações, figuras
├── 03_random_forest.py           # RF + GridSearchCV → modelo .pkl
├── 04_neural_network.py          # MLP base → modelo .h5
├── 05_neural_network_optimized.py # MLP v2 + regularization → .keras
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação principal
│
├── data/
│   ├── sleep_health_dataset.csv  # Dataset (100k rows, 32 cols)
│   └── test_split.pkl            # Split preservado para comparação
│
├── models/
│   ├── random_forest_model.pkl          # RF tuned (74.15%)
│   ├── neural_network_model.h5          # MLP base
│   ├── nn_history.pkl                   # Histórico de treino
│   └── v2/
│       ├── neural_network_v2_optimized.keras  # MLP otimizada
│       └── nn_history_v2.pkl                  # Histórico v2
│
├── reports/
│   ├── figures/                    # Visualizações (.png)
│   │   ├── eda_*.png               # EDA: distribuições, correlações
│   │   └── comparison_*.png        # Métricas comparativas
│   ├── fragmentos/                 # Trechos de relatório
│   │   ├── 01-resultados-comparativos.md
│   │   └── 02-discussao-e-limitacoes.md
│   └── diagnostics/                # Diagnóstico (Rodada 3)
│       ├── *.csv                   # Métricas por modelo
│       └── diagnostics_summary.json
│
├── notebooks/
│   └── trabalho_1_classificacao_saude_rf_vs_rn.ipynb  # Narrativa principal
│
├── scripts/
│   ├── smoke_test.py             # Validação de ambiente
│   └── diagnose_model_limits.py  # Diagnóstico comparativo
│
└── .specs/
    ├── project/
    │   ├── PROJECT.md            # Visão e objetivos
    │   ├── ROADMAP.md            # Cronograma e milestones
    │   └── STATE.md              # Decisões, bloqueios, lições
    ├── codebase/
    │   ├── STACK.md              # Tecnologias e versões
    │   ├── ARCHITECTURE.md       # Fluxo e decisões arquiteturais
    │   ├── STRUCTURE.md          # Este arquivo
    │   ├── CONVENTIONS.md        # Padrões de código
    │   ├── TESTING.md            # Validação e gates
    │   ├── CONCERNS.md           # Riscos e preocupações
    │   └── INTEGRATIONS.md       # Integrações externas
    └── features/
        └── trabalho-1/
            ├── spec.md                       # Requisitos do Trabalho 1
            ├── tasks.md                      # Tarefas e status
            ├── log_execucao.md               # Log de execução
            ├── relatorio_rodada_1.md         # Baseline RF vs RN
            ├── relatorio_rodada_2.md         # Otimização RN v2
            └── relatorio_rodada_3_diagnostico.md  # Diagnóstico de limites
```

## Scripts Principais

| Script | Propósito | Artefatos Gerados | Status |
|---|---|---|---|
| `01_check_data.py` | Inspeção básica | Console (shape, tipos, nulos) | ✅ Funcional |
| `02_eda.py` | EDA completo | `reports/figures/*.png` | ✅ Funcional |
| `03_random_forest.py` | RF + tuning | `models/random_forest_model.pkl`, `data/test_split.pkl` | ✅ Funcional |
| `04_neural_network.py` | MLP base | `models/neural_network_model.h5` | ✅ Funcional |
| `05_neural_network_optimized.py` | MLP v2 | `models/v2/neural_network_v2_optimized.keras` | ✅ Funcional |
| `scripts/smoke_test.py` | Validação ambiente | Console (dependências OK) | ✅ Funcional |
| `scripts/diagnose_model_limits.py` | Diagnóstico | `reports/diagnostics/*.csv`, `.json` | ✅ Funcional |

## Notebook Principal

**`notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`**

Reúne em narrativa única:
- Contexto e objetivo do Trabalho 1
- EDA com visualizações
- Preparação dos dados (split, pré-processamento)
- Random Forest + GridSearchCV
- MLP baseline
- MLP otimizada (v2)
- Comparação final (6 métricas obrigatórias)
- Discussão e limitações
- Síntese para relatório

**Status:** Em consolidação (agrega resultados dos scripts)

## Documentação Viva

### Projeto (`.specs/project/`)
| Arquivo | Conteúdo | Atualização |
|---|---|---|
| `PROJECT.md` | Visão, objetivos, equipe | Estático |
| `ROADMAP.md` | Cronograma, tarefas, status | Atualizado por sessão |
| `STATE.md` | Decisões, bloqueios, lições, preferências | Atualizado por sessão |

### Codebase (`.specs/codebase/`)
| Arquivo | Conteúdo | Atualização |
|---|---|---|
| `STACK.md` | Tecnologias, versões, comandos | Após setup/mudança |
| `ARCHITECTURE.md` | Fluxo, decisões, diagramas | Após mudanças arquiteturais |
| `STRUCTURE.md` | Estrutura de arquivos | Após nova estrutura |
| `CONVENTIONS.md` | Padrões de código | Após convenções novas |
| `TESTING.md` | Validação, gates, resultados | Após nova validação |
| `CONCERNS.md` | Riscos, preocupações | Após identificação |
| `INTEGRATIONS.md` | APIs, integrações externas | Após integração |

### Feature: Trabalho 1 (`.specs/features/trabalho-1/`)
| Arquivo | Conteúdo | Status |
|---|---|---|
| `spec.md` | Requisitos (REQ-01 a REQ-05, MET-01 a MET-06) | ✅ Completo |
| `tasks.md` | Tarefas T1-1 a T1-12 | 🟡 85% completo |
| `log_execucao.md` | Log de execução | ✅ Documentado |
| `relatorio_rodada_1.md` | Baseline: RF 74.15% vs RN 73.23% | ✅ Concluído |
| `relatorio_rodada_2.md` | Otimização RN v2 | ✅ Concluído |
| `relatorio_rodada_3_diagnostico.md` | Diagnóstico de limites | ✅ Concluído |

## Fragmentos de Relatório

### `reports/fragmentos/01-resultados-comparativos.md`
Tabela comparativa das 6 métricas obrigatórias entre RF e RN (todas as rodadas).

### `reports/fragmentos/02-discussao-e-limitacoes.md`
Discussão crítica:
- Por que RF superou RN em dataset tabular
- Limitações do alvo `felt_rested` (subjetividade)
- Impacto do desbalanceamento (61%/39%)
- Threshold tuning como oportunidade

## Observação

A estrutura combina:
1. **Pipeline executável** (scripts numerados) para reprodutibilidade
2. **Notebook narrativo** para apresentação e exploração
3. **Documentação viva** (`.specs/`) para decisões e contexto
4. **Fragmentos** para compor relatório final
