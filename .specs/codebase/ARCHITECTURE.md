# Arquitetura do Projeto

## Visão Geral

```
┌─────────────────────────────────────────────────────────────────┐
│                     PIPELINE DE DADOS                           │
├─────────────────────────────────────────────────────────────────┤
│  01_check_data.py → 02_eda.py → 03_rf.py → 04_nn.py → 05_nn_v2 │
│       ↓              ↓            ↓           ↓           ↓     │
│    Shape/       Figuras      Modelo       Modelo     Modelo    │
│    Nulos        (.png)       .pkl         .h5        .keras    │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                    DIAGNÓSTICO (Rodada 3)                       │
├─────────────────────────────────────────────────────────────────┤
│  diagnose_model_limits.py: compara 5 modelos + threshold tuning │
│  → HistGradientBoosting, Extra Trees, Logistic Regression       │
│  → Permutation importance, threshold optimization, baseline     │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│              NARRATIVA (Notebook + Relatórios)                  │
├─────────────────────────────────────────────────────────────────┤
│  notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb        │
│  reports/fragmentos/01-resultados-comparativos.md               │
│  reports/fragmentos/02-discussao-e-limitacoes.md                │
└─────────────────────────────────────────────────────────────────┘
```

## Fluxo de Dados

### Pipeline Principal (Scripts)
1. **Leitura:** `data/sleep_health_dataset.csv` (100k rows, 32 cols)
2. **Inspeção:** `01_check_data.py` — shape, tipos, nulos, duplicatas
3. **EDA:** `02_eda.py` — distribuições, correlações, outliers → `reports/figures/`
4. **Split:** Estratificado (70/30), `random_state=42`, preservado em `data/test_split.pkl`
5. **Pré-processamento:** `ColumnTransformer` (one-hot para categóricas, padronização para numéricas)
6. **Modelagem:**
   - `03_random_forest.py`: GridSearchCV → `models/random_forest_model.pkl`
   - `04_neural_network.py`: MLP base → `models/neural_network_model.h5`
   - `05_neural_network_optimized.py`: MLP v2 → `models/v2/neural_network_v2_optimized.keras`
7. **Diagnóstico:** `scripts/diagnose_model_limits.py` — compara modelos + threshold tuning

### Arquitetura de Modelos

#### Random Forest
```
ColumnTransformer → Pipeline → RandomForestClassifier → GridSearchCV
  - OneHotEncoding     - n_estimators: [100, 200]
  - StandardScaler     - max_depth: [10, 20, None]
                         - min_samples_split: [2, 5]
```

#### Rede Neural (MLP)
```
ColumnTransformer → Dense(64, ReLU) → BatchNorm → Dropout(0.3)
                  → Dense(32, ReLU) → BatchNorm → Dropout(0.2)
                  → Dense(1, Sigmoid)
  - Optimizer: Adam
  - Loss: binary_crossentropy
  - Callbacks: ReduceLROnPlateau, EarlyStopping
```

#### HistGradientBoosting (Diagnóstico)
```
ColumnTransformer → HistGradientBoostingClassifier
  - Nativo do scikit-learn para dados tabulares
  - Performance: 74.25% accuracy, 82.58% ROC AUC
```

## Decisões Arquiteturais

### Scripts Numerados vs Notebook
| Critério | Scripts | Notebook |
|---|---|---|
| Reprodutibilidade | ✅ Alta (execução determinística) | ⚠️ Média (células podem ser puladas) |
| Auditoria | ✅ Rastreável (cada passo isolado) | ✅ Narrativo (contexto + código) |
| Apresentação | ⚠️ Técnico (console) | ✅ Visual (markdown + gráficos) |
| Manutenção | ✅ Modular (cada script independente) | ⚠️ Monolítico (notebook único) |

**Decisão:** Manter ambos — scripts para execução, notebook para narrativa.

### Pré-processamento com ColumnTransformer
**Por que:** Evita data leakage ao aplicar one-hot/scaling apenas nos dados de treino.
**Como:** `ColumnTransformer` dentro de `Pipeline` do scikit-learn.

### Split Preservado
**Por que:** Garantir comparação justa entre modelos.
**Como:** `joblib.dump(X_test, 'data/test_split.pkl')` e reuso nos scripts subsequentes.

### Random Seed Único
**Por que:** Reprodutibilidade e comparação isolando apenas o modelo.
**Como:** `random_state=42` em todos os scripts + `tf.keras.utils.set_random_seed(42)`.

## Integração com Diagnóstico

O script `diagnose_model_limits.py` foi adicionado na Rodada 3 para responder:
1. O resultado está realmente ruim?
2. A modelagem fez tudo que poderia?
3. O que faltou para otimização exaustiva?

**Saídas:**
- Comparação de 5 modelos (RF, Extra Trees, HistGradientBoosting, Logistic Regression, MLP)
- Threshold tuning (encontra melhor ponto de corte por métrica)
- Permutation importance (rankeia features por poder preditivo)
- Baseline ingênuo (classe majoritária)
- Análise de ambiguidade do alvo (grupos com respostas mistas)

## Camadas de Persistência

| Camada | Artefatos | Localização |
|---|---|---|
| Dados brutos | `sleep_health_dataset.csv` | `data/` |
| Dados processados | `test_split.pkl` | `data/` |
| Modelos treinados | `.pkl`, `.h5`, `.keras` | `models/`, `models/v2/` |
| Histórico de treino | `.pkl` (histórico de epochs) | `models/`, `models/v2/` |
| Visualizações | `.png` (EDA, métricas) | `reports/figures/` |
| Diagnósticos | `.csv`, `.json` | `reports/diagnostics/` |
| Narrativa | `.ipynb`, `.md` | `notebooks/`, `reports/fragmentos/` |
| Especificação | `.md` | `.specs/` |
