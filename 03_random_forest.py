import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
import joblib
import os

# Configurações
output_dir = "./models"
os.makedirs(output_dir, exist_ok=True)
data_path = "./data/sleep_health_dataset.csv"

# 1. Carregar Dados
df = pd.read_csv(data_path)

# Remover person_id (não agrega informação) e targets secundários
# Vamos focar no felt_rested conforme plano
X = df.drop(columns=['person_id', 'felt_rested', 'sleep_disorder_risk', 'cognitive_performance_score'])
y = df['felt_rested']

# 2. Identificar colunas
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns.tolist()

print(f"Features Categóricas: {categorical_features}")
print(f"Features Numéricas: {numeric_features}")

# 3. Pipeline de Pré-processamento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# 4. Split Treino/Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\nShape Treino: {X_train.shape}")
print(f"Shape Teste: {X_test.shape}")

# 5. Modelagem Random Forest com Pipeline
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 6. Hyperparameter Tuning (Requisito REQ-04)
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5]
}

print("\n--- Iniciando Tuning da Random Forest (GridSearchCV) ---")
grid_search = GridSearchCV(rf_pipeline, param_grid, cv=3, scoring='f1', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

best_rf = grid_search.best_estimator_
print(f"Melhores parâmetros: {grid_search.best_params_}")

# 7. Avaliação (Métricas Obrigatórias)
y_pred = best_rf.predict(X_test)
y_proba = best_rf.predict_proba(X_test)[:, 1]

print("\n### Resultados Random Forest ###")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"ROC AUC: {roc_auc_score(y_test, y_proba):.4f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Salvar Modelo e Dados de Teste para Comparação posterior
joblib.dump(best_rf, f"{output_dir}/random_forest_model.pkl")
# Salvar dados de teste para garantir que a RN use o MESMO split
test_data = {'X_test': X_test, 'y_test': y_test}
joblib.dump(test_data, f"./data/test_split.pkl")

print(f"\nModelo salvo em {output_dir}/random_forest_model.pkl")
