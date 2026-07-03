import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, roc_auc_score, confusion_matrix, classification_report)
import os

def main():
    print("="*50)
    print("BASELINE - PROJETO 1: GENÉTICO + NEURAL")
    print("Dataset: Heart Failure Clinical Records")
    print("="*50)

    # 1. Carregamento dos dados
    file_path = 'dataset/heart_failure_clinical_records_dataset.csv'
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return

    df = pd.read_csv(file_path)
    print(f"\n[INFO] Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
    # Target: DEATH_EVENT (0 = Sobreviveu, 1 = Faleceu)
    X = df.drop(columns=['DEATH_EVENT'])
    y = df['DEATH_EVENT']

    print(f"\n[INFO] Distribuição da classe alvo (DEATH_EVENT):")
    print(y.value_counts(normalize=True) * 100)

    # 2. Divisão Treino/Teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 3. Pré-processamento (Apenas Padronização, pois todas as features numéricas)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Função auxiliar para avaliar e imprimir métricas
    def evaluate_model(name, model, X_t, y_t):
        preds = model.predict(X_t)
        probs = model.predict_proba(X_t)[:, 1]
        
        print(f"\n--- Resultados: {name} ---")
        print(f"Acurácia:  {accuracy_score(y_t, preds):.4f}")
        print(f"Precisão:  {precision_score(y_t, preds):.4f}")
        print(f"Recall:    {recall_score(y_t, preds):.4f}")
        print(f"F1-Score:  {f1_score(y_t, preds):.4f}")
        print(f"ROC AUC:   {roc_auc_score(y_t, probs):.4f}")
        
        cm = confusion_matrix(y_t, preds)
        print("Matriz de Confusão:")
        print(cm)
        return model

    # 4. Baseline 1: Random Forest com Tuning
    print("\n[INFO] Treinando Random Forest (Tuning hiperparâmetros)...")
    rf = RandomForestClassifier(random_state=42)
    rf_params = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 5, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    rf_grid = GridSearchCV(rf, rf_params, cv=5, scoring='f1', n_jobs=-1)
    rf_grid.fit(X_train_scaled, y_train)
    print(f"Melhores parâmetros RF: {rf_grid.best_params_}")
    
    evaluate_model("Random Forest", rf_grid.best_estimator_, X_test_scaled, y_test)

    # 5. Baseline 2: Rede Neural Simples (MLP) com Tuning
    print("\n[INFO] Treinando Rede Neural / MLP (Tuning hiperparâmetros)...")
    mlp = MLPClassifier(max_iter=1000, random_state=42)
    mlp_params = {
        'hidden_layer_sizes': [(50,), (100,), (50, 50)],
        'activation': ['relu', 'tanh'],
        'alpha': [0.0001, 0.001, 0.01]
    }
    mlp_grid = GridSearchCV(mlp, mlp_params, cv=5, scoring='f1', n_jobs=-1)
    mlp_grid.fit(X_train_scaled, y_train)
    print(f"Melhores parâmetros MLP: {mlp_grid.best_params_}")

    evaluate_model("Rede Neural (MLP)", mlp_grid.best_estimator_, X_test_scaled, y_test)

    print("\n[INFO] Fim do Baseline. Esses resultados devem ser usados no relatório para comparar com o Algoritmo Genético + Neural!")

if __name__ == "__main__":
    main()
