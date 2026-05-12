import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração de visualização
sns.set_theme(style="whitegrid")

# Carregar dataset
data_path = "./data/sleep_health_dataset.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
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
    print(f"Erro: Arquivo {data_path} não encontrado.")
