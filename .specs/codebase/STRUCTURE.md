# Estrutura do Repositório (Projeto IC)

```text
.
├── materiais_de_aula/               # 10 PDFs oficiais da disciplina.
├── podcasts/                        # Arquivos de áudio (Revisão da teoria gerada via NotebookLM).
├── guia_de_acao_ic.md               # Roteiro metodológico e teoria da disciplina condensada.
├── relatorio_projeto1_genetico_neural.md # Esboço do relatório acadêmico para o Prof. (na pasta oculta de artefatos).
│
├── projeto_1_genetico_neural/       # PROJETO 1
│   ├── dataset/
│   │   └── heart_failure_clinical_records_dataset.csv
│   ├── .venv/                       # Ambiente virtual (Bibliotecas isoladas).
│   ├── eda_heart_failure.py         # Script de Análise Exploratória.
│   ├── baseline.py                  # Script de Treinamento Base (RF vs MLP).
│   ├── hybrid_ga_mlp.py             # Script do Algoritmo Genético + Rede Neural.
│   ├── notebooks/
│   │   └── projeto_1_genetico_neural_ga_mlp.ipynb
│   ├── reports/
│   │   ├── figures/
│   │   │   └── evolucao_genetica.png
│   │   └── tables/
│   │       ├── ga_mlp_results_quick.json
│   │       ├── ga_mlp_results.json
│   │       └── model_comparison.csv
│   ├── eda_correlacao.png           # Artefato visual.
│   ├── eda_distribuicoes.png        # Artefato visual.
│   └── evolucao_genetica_v2.png     # Gráfico gerado da curva evolutiva do F1-Score.
│
├── projeto_2_neuro_fuzzy/           # PROJETO 2
│   ├── dataset/
│   │   └── Breast_Cancer.csv
│   ├── .venv/                       # Ambiente virtual.
│   ├── baseline.py                  # Script de Treinamento Base.
│   └── hybrid_neuro_fuzzy.py        # Script do Modelo Fuzzy + Rede Neural.
│
└── .specs/                          # Documentação Técnica TLC.
    ├── project/
    │   ├── PROJECT.md
    │   ├── ROADMAP.md
    │   └── STATE.md
    └── codebase/
        ├── ARCHITECTURE.md
        └── STRUCTURE.md
```

### Specs do Projeto 1

| Artefato | Localizacao |
|---|---|
| Spec | `.specs/features/projeto-1-genetico-neural/spec.md` |
| Design | `.specs/features/projeto-1-genetico-neural/design.md` |
| Tasks | `.specs/features/projeto-1-genetico-neural/tasks.md` |

Status revisado: Projeto 1 esta implementado e alinhado ao tema Genetico-Neural da segunda avaliacao. A validacao do GA-MLP e a comparacao contra baseline foram persistidas; resta transformar os resultados em relatorio/apresentacao final.

## Atualizacao: Projeto 2 Breast Cancer Survival Risk

O Projeto 2 foi expandido para uma trilha spec-driven completa, mantendo o historico neuro-fuzzy e adicionando dicionario de dados, EDA de metadados/relacoes, notebook proprio, suite de modelos tabulares e ensemble ponderado.

```text
projeto_2_neuro_fuzzy/
├── 01_validate_data.py                 # contrato, sanitizacao e dicionario
├── 02_eda.py                           # EDA com metadados e relacoes
├── 03_train_models.py                  # modelos tabulares sem vazamento + sensibilidade
├── 04_threshold_and_ensemble.py         # threshold tuning e ensemble ponderado
├── 05_neuro_fuzzy_comparison.py         # neuro-fuzzy comparativo
├── run_pipeline.py                      # executa a trilha completa
├── baseline.py                          # baseline historico
├── hybrid_neuro_fuzzy.py                # wrapper de compatibilidade
├── dataset/Breast_Cancer.csv
├── docs/DATA_DICTIONARY.md
├── notebooks/projeto_2_breast_cancer_survival.ipynb
├── reports/
│   ├── figures/
│   ├── tables/
│   │   ├── metadata_profile.csv
│   │   ├── numeric_relationships.csv
│   │   ├── categorical_relationships.csv
│   │   ├── model_comparison_no_leakage.csv
│   │   ├── model_comparison_with_survival_months.csv
│   │   ├── ensemble_summary.csv
│   │   └── neuro_fuzzy_comparison.csv
│   └── relatorio_tecnico_projeto_2.md
├── src/breast_cancer_survival/
│   ├── data.py
│   ├── dictionary.py
│   ├── eda.py
│   ├── features.py
│   ├── preprocessing.py
│   ├── evaluation.py
│   ├── models.py
│   ├── ensemble.py
│   └── fuzzy.py
└── tests/test_*.py
```

### Specs do Projeto 2

| Artefato | Localizacao |
|---|---|
| Spec | `.specs/features/trabalho-2-breast-cancer/spec.md` |
| Design | `.specs/features/trabalho-2-breast-cancer/design.md` |
| Tasks | `.specs/features/trabalho-2-breast-cancer/tasks.md` |
