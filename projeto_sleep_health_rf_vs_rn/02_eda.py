from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de visualização
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [12, 8]

# Caminhos robustos
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sleep_health_dataset.csv"
OUTPUT_DIR = ROOT / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("--- Iniciando EDA Completa ---")

# 1. Correlação de variáveis numéricas
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()

plt.figure(figsize=(15, 10))
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f")
plt.title("Mapa de Calor de Correlação (Variáveis Numéricas)")
plt.savefig(f"{OUTPUT_DIR}/correlation_heatmap.png")
print(f"- Mapa de calor salvo em {OUTPUT_DIR}/correlation_heatmap.png")

# 2. Top correlações com o target 'felt_rested'
target_corr = corr['felt_rested'].sort_values(ascending=False)
print("\nTop 5 correlações positivas com 'felt_rested':")
print(target_corr.head(6))
print("\nTop 5 correlações negativas com 'felt_rested':")
print(target_corr.tail(5))

# 3. Distribuição de Idade por Qualidade de Sono
plt.figure()
sns.histplot(data=df, x='age', hue='felt_rested', multiple='stack', kde=True)
plt.title("Distribuição de Idade por Sensação de Descanso")
plt.savefig(f"{OUTPUT_DIR}/age_distribution_target.png")

# 4. Ocupação vs Descanso (Variável Categórica importante)
plt.figure()
occ_rested = pd.crosstab(df['occupation'], df['felt_rested'], normalize='index') * 100
occ_rested.plot(kind='barh', stacked=True)
plt.title("Porcentagem de Descanso por Ocupação")
plt.xlabel("Porcentagem (%)")
plt.legend(title="Sentiu-se Descansado?", labels=["Não", "Sim"])
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/occupation_vs_target.png")

# 5. Análise de variáveis de sono
sleep_vars = ['sleep_duration_hrs', 'sleep_quality_score', 'rem_percentage', 'deep_sleep_percentage']
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.flatten()

for i, var in enumerate(sleep_vars):
    sns.boxplot(data=df, x='felt_rested', y=var, ax=axes[i])
    axes[i].set_title(f"{var} vs felt_rested")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/sleep_features_boxplot.png")

print("\n--- EDA Concluída com Sucesso ---")
