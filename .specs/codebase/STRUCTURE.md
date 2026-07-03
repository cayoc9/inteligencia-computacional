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
