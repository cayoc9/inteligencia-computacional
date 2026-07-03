import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
import warnings

from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# ==========================================
# MÓDULO 1: FUNÇÕES DE PERTINÊNCIA FUZZY
# ==========================================
def trimf(x, abc):
    """
    Função de Pertinência Triangular (Triangular Membership Function).
    Mapeia um valor numérico crisp 'x' para um grau de pertinência Fuzzy [0, 1]
    baseado nos vértices do triângulo [a, b, c].
    """
    a, b, c = abc
    y = np.zeros_like(x, dtype=float)
    
    # Rampa de subida
    idx1 = (x > a) & (x < b)
    if b > a:
        y[idx1] = (x[idx1] - a) / (b - a)
        
    # Rampa de descida
    idx2 = (x >= b) & (x < c)
    if c > b:
        y[idx2] = (c - x[idx2]) / (c - b)
        
    # Topo (100% de pertinência)
    y[x == b] = 1.0
    
    return y

def main():
    print("="*60)
    print("SISTEMA HÍBRIDO: NEURO-FUZZY COOPERATIVO")
    print("Objetivo: Fuzzificar variáveis clínicas e inferir com RNA")
    print("="*60)

    # Carregando Dados
    file_path = 'dataset/Breast_Cancer.csv'
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return
        
    df = pd.read_csv(file_path)
    
    # Target (Alive -> 0, Dead -> 1)
    df['Status'] = df['Status'].map({'Alive': 0, 'Dead': 1})
    y = df['Status'].values

    print("[FUZZY] Etapa 1: Aplicando Funções de Pertinência nas variáveis contínuas...")
    
    # Extração de variáveis contínuas
    age = df['Age'].values
    tumor_size = df['Tumor Size'].values
    nodes = df['Reginol Node Positive'].values

    # 1.1 Fuzzificando Idade (Análise Semântica)
    # Valores baseados na distribuição médica da doença
    age_young = trimf(age, [20, 30, 45])
    age_mid = trimf(age, [35, 50, 65])
    age_old = trimf(age, [55, 70, 95])

    # 1.2 Fuzzificando Tamanho do Tumor
    tumor_small = trimf(tumor_size, [0, 10, 25])
    tumor_medium = trimf(tumor_size, [15, 35, 55])
    tumor_large = trimf(tumor_size, [45, 80, 150]) # Pode passar de 150, mas a pertinência decai

    # 1.3 Fuzzificando Nódulos Regionais Positivos
    nodes_few = trimf(nodes, [0, 0, 4])
    nodes_some = trimf(nodes, [2, 6, 12])
    nodes_many = trimf(nodes, [8, 20, 50])

    # Matriz Fuzzy (Cada paciente agora tem um "grau" de pertinência em 9 regras semânticas)
    fuzzy_features = np.column_stack([
        age_young, age_mid, age_old,
        tumor_small, tumor_medium, tumor_large,
        nodes_few, nodes_some, nodes_many
    ])

    print("[FUZZY] Matriz Fuzzificada gerada! (9 colunas de pertinência)")

    print("\n[PREPROCESS] Etapa 2: One-Hot Encoding das variáveis categóricas...")
    # O restante dos dados são categóricos, a rede precisa deles codificados
    cat_cols = df.select_dtypes(include=['object', 'string']).columns
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    cat_features = encoder.fit_transform(df[cat_cols])

    # Unindo o mundo Fuzzy com as características categóricas
    X_hybrid = np.hstack([fuzzy_features, cat_features])
    print(f"Dimensão final do dataset Híbrido: {X_hybrid.shape}")

    # ==========================================
    # MÓDULO 2: REDE NEURAL COMO MOTOR DE INFERÊNCIA
    # ==========================================
    print("\n[NEURAL] Etapa 3: Treinando a Rede Neural para inferência...")
    
    X_train, X_test, y_train, y_test = train_test_split(X_hybrid, y, test_size=0.2, random_state=42, stratify=y)
    
    # A Rede Neural agora atua no lugar de uma base de regras manual gigante (Mamdani/Sugeno)
    # Ela "descobre" qual o peso de pertencer ao grupo 'Age_Young' E 'Tumor_Large'
    mlp = MLPClassifier(
        hidden_layer_sizes=(100, 50), 
        activation='relu', 
        solver='adam',
        max_iter=1000, 
        random_state=42
    )
    
    mlp.fit(X_train, y_train)
    preds = mlp.predict(X_test)
    probs = mlp.predict_proba(X_test)[:, 1]

    print("\n" + "="*60)
    print(" RESULTADOS FINAIS: SISTEMA HÍBRIDO NEURO-FUZZY")
    print("="*60)
    
    print(f"Acurácia:  {accuracy_score(y_test, preds):.4f}")
    print(f"Precisão:  {precision_score(y_test, preds):.4f}")
    print(f"Recall:    {recall_score(y_test, preds):.4f}")
    print(f"F1-Score:  {f1_score(y_test, preds):.4f}")
    print(f"ROC AUC:   {roc_auc_score(y_test, probs):.4f}")
    
    cm = confusion_matrix(y_test, preds)
    print("\nMatriz de Confusão (0 = Sobreviveu, 1 = Óbito):")
    print(cm)
    
    print("\n[INFO] O modelo Neuro-Fuzzy aprendeu os pesos sinápticos associados aos graus de pertinência fuzzy!")

if __name__ == "__main__":
    main()
