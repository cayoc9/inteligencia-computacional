from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de visualização
sns.set_theme(style="whitegrid")

# Caminhos robustos (funcionam independentemente do diretório atual)
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sleep_health_dataset.csv"

# Carregar dataset
if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)
    
    print("### Informações Básicas ###")
    print(df.info())
    
    print("\n### Estatísticas Descritivas ###")
    print(df.describe())
    
    print("\n### Valores Nulos ###")
    print(df.isnull().sum())
    
    print("\n### Duplicatas ###")
    print(f"Total de duplicatas: {df.duplicated().sum()}")
    
    # Target: felt_rested
    print("\n### Distribuição do Target (felt_rested) ###")
    print(df['felt_rested'].value_counts(normalize=True))
else:
    print(f"Erro: Arquivo {DATA_PATH} não encontrado.")
