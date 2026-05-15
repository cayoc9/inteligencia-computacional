# Stack do Projeto

## Linguagem e Ambiente
- **Python:** 3.12.3 em ambiente virtual local `.venv`
- **Gerenciador de Dependências:** pip com `requirements.txt` (criado em 2026-05-14)
- **Git:** Repositório funcional (`.git/` presente)

## Bibliotecas Principais

### Dados e EDA
| Biblioteca | Versão | Uso |
|---|---|---|
| pandas | ≥2.2.0 | Manipulação de DataFrames |
| numpy | ≥1.26.0 | Operações numéricas |
| matplotlib | ≥3.9.0 | Visualização 2D |
| seaborn | ≥0.13.0 | Visualização estatística |

### Machine Learning Clássico
| Biblioteca | Versão | Uso |
|---|---|---|
| scikit-learn | ≥1.6.0 | RF, Gradient Boosting, pré-processamento |
| joblib | ≥1.4.0 | Serialização de modelos (.pkl) |

### Redes Neurais
| Biblioteca | Versão | Uso |
|---|---|---|
| tensorflow | ≥2.18.0 | MLP, callbacks, saving .h5/.keras |
| keras | (bundled) | API de alto nível para RN |

### Ambiente Interativo
| Biblioteca | Versão | Uso |
|---|---|---|
| notebook | ≥7.0.0 | Jupyter Notebook UI |
| jupyter | ≥1.0.0 | Kernel e ferramentas |

## Artefatos

### Dados
- **Principal:** `data/sleep_health_dataset.csv` (100.000 rows, 32 cols, 14.3 MB)
- **Split de teste:** `data/test_split.pkl` (preservado para comparação)

### Modelos
| Modelo | Arquivo | Status |
|---|---|---|
| Random Forest Tuned | `models/random_forest_model.pkl` | ✅ Gerado |
| Neural Network Base | `models/neural_network_model.h5` | ✅ Gerado |
| Neural Network V2 Otimizada | `models/v2/neural_network_v2_optimized.keras` | ✅ Gerado |

### Visualizações
- **EDA:** `reports/figures/eda_*.png` (distribuições, correlações, boxplots)
- **Performance:** `reports/figures/comparison_*.png` (métricas, curvas ROC)

### Scripts de Pipeline
| Script | Propósito | Status |
|---|---|---|
| `01_check_data.py` | Inspeção inicial | ✅ Funcional |
| `02_eda.py` | Análise exploratória | ✅ Funcional |
| `03_random_forest.py` | Treinamento RF + GridSearchCV | ✅ Funcional |
| `04_neural_network.py` | MLP base | ✅ Funcional |
| `05_neural_network_optimized.py` | MLP com regularization | ✅ Funcional |
| `scripts/diagnose_model_limits.py` | Diagnóstico comparativo | ✅ Funcional |
| `scripts/smoke_test.py` | Validação de ambiente | ✅ Funcional |

### Notebooks
- `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` — Narrativa principal (em consolidação)

## Reprodutibilidade

### Dependências Congeladas
- `requirements.txt` presente com versões mínimas e máximas
- Compatibilidade verificada: TensorFlow requer numpy<2.1.0

### Random Seed
- Todos os scripts usam `random_state=42`
- TensorFlow: `tf.keras.utils.set_random_seed(42)`
- NumPy: `np.random.seed(42)`

### Comandos de Reprodução
```bash
# Ambiente
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Validação
python scripts/smoke_test.py

# Pipeline completo
python 01_check_data.py && python 02_eda.py && python 03_random_forest.py && python 04_neural_network.py && python 05_neural_network_optimized.py
```
