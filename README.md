# Inteligência Computacional

Repositório com scripts e análises de data science para o estudo do dataset de saúde do sono.

## Estrutura

- `01_check_data.py`: inspeção inicial dos dados
- `02_eda.py`: análise exploratória (gera figuras em `reports/figures/`)
- `03_random_forest.py`: treinamento com random forest (modelo em `models/`)
- `04_neural_network.py`: rede neural base (modelo em `models/`)
- `05_neural_network_optimized.py`: rede neural otimizada (modelo em `models/v2/`)
- `scripts/diagnose_model_limits.py`: diagnóstico avançado de limites do modelo
- `scripts/smoke_test.py`: teste rápido de validação do ambiente
- `notebooks/`: notebooks de análise e experimentos
- `reports/`: figuras e fragmentos do relatório
- `analise_datasets_health.md`: observações e análise do conjunto de dados

## Dados

O dataset principal (`data/sleep_health_dataset.csv`) **está versionado** neste repositório.

Artefatos gerados (`.pkl`, `.h5`, `.keras`) ficam fora do versionamento e devem ser regenerados localmente.

## Setup

### 1. Criar ambiente virtual

```bash
# Linux/macOS
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate.bat
```

### 2. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Verificação rápida

Execute o smoke test para validar o ambiente:

```bash
python scripts/smoke_test.py
```

Se tudo estiver correto, você verá mensagens de sucesso para cada dependência.

## Executando os Scripts

Execute na ordem abaixo para reproduzir toda a pipeline:

```bash
# 1. Inspeção dos dados
python 01_check_data.py

# 2. Análise exploratória (gera figuras em reports/figures/)
python 02_eda.py

# 3. Random Forest (gera modelo e salva split de teste)
python 03_random_forest.py

# 4. Rede Neural Base (usa o mesmo split do passo 3)
python 04_neural_network.py

# 5. Rede Neural Otimizada
python 05_neural_network_optimized.py

# 6. Diagnóstico avançado (opcional)
python scripts/diagnose_model_limits.py
```

## Onde os artefatos são gerados

| Script | Artefatos gerados |
|--------|-------------------|
| `02_eda.py` | `reports/figures/*.png` |
| `03_random_forest.py` | `models/random_forest_model.pkl`, `data/test_split.pkl` |
| `04_neural_network.py` | `models/neural_network_model.h5`, `models/nn_history.pkl` |
| `05_neural_network_optimized.py` | `models/v2/neural_network_v2_optimized.keras`, `models/v2/nn_history_v2.pkl` |
| `scripts/diagnose_model_limits.py` | `reports/diagnostics/*.csv`, `reports/diagnostics/diagnostics_summary.json` |

## Reprodutibilidade

Todos os scripts usam `random_state=42` para garantir resultados reproduzíveis:

- scikit-learn: `random_state=42`
- numpy: `np.random.seed(42)`
- TensorFlow: `tf.keras.utils.set_random_seed(42)`

Os splits de treino/teste são preservados entre scripts para comparação justa de modelos.

## Resultados de Referência

Executados em 2026-05-14 com as versões especificadas em `requirements.txt`:

| Modelo | Accuracy | ROC AUC |
|--------|----------|---------|
| Random Forest (tuned) | 0.7415 | 0.8218 |
| HistGradientBoosting (diagnóstico) | 0.74 | ~0.82 |

Valores exatos podem variar levemente devido a diferenças de plataforma, mas devem estar dentro de ±0.01.

## Observação

Os diretórios `models/` e artefatos `.pkl`/`.keras`/`.h5` ficam fora do controle de versão por conterem arquivos derivados e pesados. Execute os scripts para regenerá-los localmente.
