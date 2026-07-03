# Integrações

## Fontes de Dados

### Kaggle (Origem)
- **Dataset:** `mohankrishnathalla/sleep-health-and-daily-performance-dataset`
- **URL:** https://kaggle.com/datasets/mohankrishnathalla/sleep-health-and-daily-performance-dataset
- **Download:** Via Kaggle CLI (`kaggle datasets download`) ou interface web
- **Licença:** CC0 (Domínio Público)
- **Status:** ✅ Baixado e disponível em `projeto_sleep_health_rf_vs_rn/data/sleep_health_dataset.csv`

### UCI Machine Learning Repository (Referência)
- **Dataset original:** Pima Indians Diabetes, Breast Cancer Wisconsin, Heart Disease Cleveland
- **Uso:** Comparação e benchmark na literatura
- **Status:** ⚪ Não utilizado neste projeto (apenas referência)

## Ferramentas Locais

### Ambiente Virtual
- **Gerenciador:** Python `venv` em `.venv/`
- **Ativação:** `source .venv/bin/activate` (Linux/macOS) ou `.venv\Scripts\Activate.ps1` (Windows)
- **Dependências:** `requirements.txt` com versões mínimas e máximas

### JupyterLab/Notebook
- **Instalação:** `notebook>=7.0.0`, `jupyter>=1.0.0`
- **Notebook principal:** `projeto_sleep_health_rf_vs_rn/notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`
- **Execução:** `jupyter notebook` ou `jupyter nbconvert --execute`

### Git (Versionamento)
- **Status:** ✅ Repositório funcional
- **Uso:** Versionamento de código, documentação e dataset
- **Ignorados:** `models/*.pkl`, `models/*.h5`, `models/*.keras`, `reports/figures/*.png`, `.venv/`

## Bibliotecas e Frameworks

### Scikit-Learn
- **Versão:** >=1.6.0
- **Uso:** Random Forest, Gradient Boosting, pré-processamento, métricas
- **Integração:** Pipeline + ColumnTransformer para evitar data leakage

### TensorFlow/Keras
- **Versão:** >=2.18.0
- **Uso:** Redes Neurais MLP
- **Integração:** `tf.keras.utils.set_random_seed(42)` para reprodutibilidade

### Pandas/NumPy
- **Versão:** pandas>=2.2.0, numpy>=1.26.0
- **Uso:** Manipulação de dados, operações numéricas
- **Integração:** Compatibilidade verificada com TensorFlow (numpy<2.1.0)

### Matplotlib/Seaborn
- **Versão:** matplotlib>=3.9.0, seaborn>=0.13.0
- **Uso:** Visualização de dados
- **Integração:** Figuras salvas em `projeto_sleep_health_rf_vs_rn/reports/figures/`

### Joblib
- **Versão:** >=1.4.0
- **Uso:** Serialização de modelos (.pkl) e splits
- **Integração:** `joblib.dump()` e `joblib.load()`

## Serviços Externos (Não Integrados em Runtime)

### Kaggle API
- **Uso:** Download inicial do dataset
- **Status:** ✅ Usado uma vez (dataset versionado localmente)

### GitHub/GitLab
- **Uso:** Hospedagem do repositório (opcional)
- **Status:** ⚪ Não configurado

### Google Colab / Kaggle Notebooks
- **Uso:** Treino com GPU (opcional, se necessário)
- **Status:** ⚪ Não utilizado (treino local em CPU funcional)

## Observação

Não há integração com serviços externos em runtime. O projeto é **local, acadêmico e baseado em arquivos**. Todas as dependências são bibliotecas Python instaláveis via pip.

## Dependências de Versão Críticas

| Biblioteca | Versão Mínima | Versão Máxima | Motivo |
|---|---|---|---|
| numpy | 1.26.0 | 2.1.0 | TensorFlow requer numpy<2.1.0 |
| pandas | 2.2.0 | 3.0.0 | Compatibilidade com scikit-learn |
| scikit-learn | 1.6.0 | 2.0.0 | API estável |
| tensorflow | 2.18.0 | 3.0.0 | Keras integrado, suporte Python 3.12 |
