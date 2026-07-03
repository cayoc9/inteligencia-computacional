import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, roc_auc_score, confusion_matrix, classification_report)

def main():
    print("="*50)
    print("BASELINE - PROJETO 2: NEURO-FUZZY (ANFIS)")
    print("Dataset: SEER Breast Cancer")
    print("="*50)

    file_path = 'dataset/Breast_Cancer.csv'
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return

    df = pd.read_csv(file_path)
    print(f"\n[INFO] Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
    # Target: Status (Mapeando Alive -> 0, Dead -> 1)
    # A classe "Dead" é a minoria, então será a nossa classe positiva (1)
    df['Status'] = df['Status'].map({'Alive': 0, 'Dead': 1})
    
    X = df.drop(columns=['Status'])
    y = df['Status']

    print(f"\n[INFO] Distribuição da classe alvo (Status = 1 significa 'Dead'):")
    print(y.value_counts(normalize=True) * 100)

    # 2. Divisão Treino/Teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 3. Pré-processamento (Numéricas e Categóricas)
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object', 'string']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
        ])

    def evaluate_model(name, model, X_test, y_test):
        preds = model.predict(X_test)
        probs = model.predict_proba(X_test)[:, 1]
        
        print(f"\n--- Resultados: {name} ---")
        print(f"Acurácia:  {accuracy_score(y_test, preds):.4f}")
        print(f"Precisão:  {precision_score(y_test, preds):.4f}")
        print(f"Recall:    {recall_score(y_test, preds):.4f}")
        print(f"F1-Score:  {f1_score(y_test, preds):.4f}")
        print(f"ROC AUC:   {roc_auc_score(y_test, probs):.4f}")
        
        cm = confusion_matrix(y_test, preds)
        print("Matriz de Confusão (0=Alive, 1=Dead):")
        print(cm)
        return model

    # 4. Baseline 1: Random Forest
    print("\n[INFO] Treinando Random Forest (com Pipeline de pré-processamento)...")
    
    rf_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42, class_weight='balanced'))
    ])
    
    # Tuning de Hiperparâmetros
    rf_params = {
        'classifier__n_estimators': [100, 200],
        'classifier__max_depth': [None, 10, 20],
        'classifier__min_samples_split': [5, 10]
    }
    
    rf_grid = GridSearchCV(rf_pipeline, rf_params, cv=3, scoring='f1', n_jobs=-1)
    rf_grid.fit(X_train, y_train)
    print(f"Melhores parâmetros RF: {rf_grid.best_params_}")
    
    evaluate_model("Random Forest", rf_grid.best_estimator_, X_test, y_test)

    # 5. Baseline 2: Rede Neural Simples (MLP)
    print("\n[INFO] Treinando Rede Neural / MLP (com Pipeline de pré-processamento)...")
    
    mlp_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', MLPClassifier(max_iter=1000, random_state=42))
    ])
    
    mlp_params = {
        'classifier__hidden_layer_sizes': [(50,), (100,), (50, 50)],
        'classifier__activation': ['relu', 'tanh'],
        'classifier__alpha': [0.001, 0.01]
    }
    
    mlp_grid = GridSearchCV(mlp_pipeline, mlp_params, cv=3, scoring='f1', n_jobs=-1)
    mlp_grid.fit(X_train, y_train)
    print(f"Melhores parâmetros MLP: {mlp_grid.best_params_}")

    evaluate_model("Rede Neural (MLP)", mlp_grid.best_estimator_, X_test, y_test)

    print("\n[INFO] Fim do Baseline. Guarde esses resultados para comparar com a abordagem Neuro-Fuzzy (ANFIS) no seu relatório!")

if __name__ == "__main__":
    main()
