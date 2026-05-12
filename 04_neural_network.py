import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
import joblib
import os

# Configurações
output_dir = "./models"
os.makedirs(output_dir, exist_ok=True)
data_path = "./data/sleep_health_dataset.csv"

# 1. Carregar Dados e Preparar (Mesma lógica do T1-RF)
df = pd.read_csv(data_path)
X = df.drop(columns=['person_id', 'felt_rested', 'sleep_disorder_risk', 'cognitive_performance_score'])
y = df['felt_rested']

categorical_features = X.select_dtypes(include=['object', 'str']).columns.tolist()
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ])

# Garantir o MESMO split (random_state=42)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Aplicar pré-processamento
X_train = preprocessor.fit_transform(X_train_raw)
X_test = preprocessor.transform(X_test_raw)

print(f"Shape de entrada: {X_train.shape}")

# 2. Definir Arquitetura da Rede Neural (MLP)
def create_model(input_dim):
    model = Sequential([
        Input(shape=(input_dim,)),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dropout(0.1),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.AUC(name='auc')])
    return model

model = create_model(X_train.shape[1])

# 3. Treinamento com Early Stopping
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

print("\n--- Iniciando Treinamento da Rede Neural ---")
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=128,
    callbacks=[early_stop],
    verbose=1
)

# 4. Avaliação (Métricas Obrigatórias)
y_proba = model.predict(X_test).flatten()
y_pred = (y_proba > 0.5).astype(int)

print("\n### Resultados Rede Neural (MLP) ###")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"ROC AUC: {roc_auc_score(y_test, y_proba):.4f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 5. Salvar Modelo e Histórico
model.save(f"{output_dir}/neural_network_model.h5")
joblib.dump(history.history, f"{output_dir}/nn_history.pkl")

print(f"\nModelo salvo em {output_dir}/neural_network_model.h5")
