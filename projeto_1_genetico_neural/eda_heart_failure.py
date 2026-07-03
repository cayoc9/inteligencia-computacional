import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    print("="*50)
    print("ANÁLISE EXPLORATÓRIA DOS DADOS (EDA) - Heart Failure")
    print("="*50)

    df = pd.read_csv('dataset/heart_failure_clinical_records_dataset.csv')
    
    print("\n1. Verificando Dados Ausentes:")
    ausentes = df.isnull().sum()
    print(ausentes)
    if ausentes.sum() == 0:
        print("-> Excelente: Dataset não possui dados nulos.")
    
    print("\n2. Distribuição das Features Contínuas vs Target...")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    sns.boxplot(x='DEATH_EVENT', y='age', data=df, ax=axes[0,0])
    sns.boxplot(x='DEATH_EVENT', y='ejection_fraction', data=df, ax=axes[0,1])
    sns.boxplot(x='DEATH_EVENT', y='serum_creatinine', data=df, ax=axes[1,0])
    sns.boxplot(x='DEATH_EVENT', y='time', data=df, ax=axes[1,1])
    plt.tight_layout()
    plt.savefig('eda_distribuicoes.png')
    print("-> Gráfico salvo: 'eda_distribuicoes.png'")

    print("\n3. Matriz de Correlação...")
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Matriz de Correlação - Heart Failure')
    plt.tight_layout()
    plt.savefig('eda_correlacao.png')
    print("-> Gráfico salvo: 'eda_correlacao.png'")
    
    print("\n[INFO] EDA Concluída com Sucesso! Use as imagens geradas no seu relatório.")

if __name__ == "__main__":
    main()
