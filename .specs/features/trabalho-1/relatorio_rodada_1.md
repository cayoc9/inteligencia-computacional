# Relatório Técnico: Rodada 1 — Experimentos Baseline (T1)

## 1. Sumário Executivo
A Rodada 1 estabeleceu os modelos de referência (baselines) para o Trabalho 1. O dataset de Saúde do Sono (100k registros) foi processado e testado em uma Random Forest e uma Rede Neural MLP. A Random Forest superou ligeiramente a Rede Neural em termos de acurácia e poder de discriminação (AUC).

## 2. Metodologia de Dados
- **Dataset:** `Sleep Health and Daily Performance Dataset` (Kaggle).
- **Volume:** 100.000 amostras, 32 colunas.
- **Target:** `felt_rested` (Binário: 0 = Não, 1 = Sim).
- **Divisão:** 80% Treino / 20% Teste (com estratificação).
- **Pré-processamento:** 
  - Variáveis Categóricas: One-Hot Encoding.
  - Variáveis Numéricas: StandardScaler (Z-score normalization).

## 3. Desempenho dos Modelos

| Métrica | Random Forest (Campeã) | Rede Neural (MLP) |
| :--- | :--- | :--- |
| **Acurácia** | **74.15%** | 73.23% |
| **ROC AUC** | **0.8218** | 0.8142 |
| **F1-Score (Classe 1)** | 0.66 | 0.64 |
| **Melhores Hiperparâmetros** | `depth: 20`, `estimators: 200` | Layers: `64-32-16`, Opt: `Adam` |

## 4. Achados da EDA (Insights de Negócio/Saúde)
1. **Qualidade percebida:** A variável `sleep_quality_score` é o preditor isolado mais forte de descanso (corr: 0.48).
2. **Carga de Trabalho:** Existe um limiar crítico em `work_hours_that_day` onde a probabilidade de `felt_rested=1` cai drasticamente.
3. **Estresse:** O `stress_score` apresenta correlação negativa moderada (-0.37).

## 5. Dificuldades Técnicas e Decisões
- **Ambiente Linux:** Erro `externally-managed-environment` resolvido com isolamento em `.venv`.
- **Hardware:** Treinamento da RN limitado à CPU. Tempo de execução aceitável (~1s/época) devido à arquitetura leve.
- **Pipeline:** Uso de `ColumnTransformer` para garantir reprodutibilidade e evitar vazamento de dados.

## 6. Próximos Passos (Rodada 2)
A próxima rodada focará em superar o baseline de 74.15% através de:
1. **Engenharia de Atributos:** Criação de variáveis de interação (ex: `stress * workload`).
2. **Tratamento de Outliers:** Utilizar diretrizes da skill `data-science-expert`.
3. **Ajuste de Arquitetura:** Testar redes mais profundas ou diferentes funções de ativação.
