from pathlib import Path

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
import joblib

# Reprodutibilidade
np.random.seed(42)
tf.keras.utils.set_random_seed(42)

# Configurações
ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "models" / "v2"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_PATH = ROOT / "data" / "sleep_health_dataset.csv"

# 1. Carregar Dados
df = pd.read_csv(DATA_PATH)

# --- ENGENHARIA DE ATRIBUTOS (Diretrizes Data Science Expert) ---
# Criando interações que fazem sentido clínico/lifestyle
df['stress_work_interaction'] = df['stress_score'] * df['work_hours_that_day']
df['sleep_efficiency'] = (df['rem_percentage'] + df['deep_sleep_percentage']) / 100
df['age_stress_ratio'] = df['stress_score'] / (df['age'] + 1)

print("Novas features criadas: stress_work_interaction, sleep_efficiency, age_stress_ratio")

# Preparar X e y
X = df.drop(columns=['person_id', 'felt_rested', 'sleep_disorder_risk', 'cognitive_performance_score'])
y = df['felt_rested']

# Identificar colunas atualizadas
categorical_features = X.select_dtypes(include=['object', 'str']).columns.tolist()
numeric_features = X.select_dtypes(include=['float64', 'int64']).columns.tolist()

# 2. Pipeline de Pré-processamento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ])

# Garantir o MESMO split inicial (random_state=42) para comparação honesta
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Aplicar pré-processamento
X_train = preprocessor.fit_transform(X_train_raw)
X_test = preprocessor.transform(X_test_raw)

print(f"Novo shape de entrada (v2): {X_train.shape}")

# 3. Definir Arquitetura Aprofundada da Rede Neural (v2)
def create_deeper_model(input_dim):
    model = Sequential([
        Input(shape=(input_dim,)),
        
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.2),
        
        Dense(32, activation='relu'),
        BatchNormalization(),
        
        Dense(16, activation='relu'),
        
        Dense(1, activation='sigmoid')
    ])
    
    # Optimizer com learning rate inicial ligeiramente menor para estabilidade
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    
    model.compile(optimizer=opt, 
                  loss='binary_crossentropy', 
                  metrics=['accuracy', tf.keras.metrics.AUC(name='auc')])
    return model

model = create_deeper_model(X_train.shape[1])

# 4. Callbacks Avançados
early_stop = EarlyStopping(monitor='val_loss', patience=12, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-5)

print("\n--- Iniciando Treinamento da Rede Neural Otimizada (v2) ---")
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100, # Aumentado para permitir convergência da rede maior
    batch_size=64, # Batch size menor para melhor generalização
    callbacks=[early_stop, reduce_lr],
    verbose=1
)

# 5. Avaliação (Métricas Obrigatórias)
y_proba = model.predict(X_test).flatten()
y_pred = (y_proba > 0.5).astype(int)

print("\n### Resultados Rede Neural Otimizada (v2) ###")
acc = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)
print(f"Accuracy: {acc:.4f}")
print(f"ROC AUC: {auc:.4f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 6. Salvar Modelo e Histórico
model.save(OUTPUT_DIR / "neural_network_v2_optimized.keras")
joblib.dump(history.history, OUTPUT_DIR / "nn_history_v2.pkl")

print(f"\nModelo otimizado salvo em {OUTPUT_DIR}/neural_network_v2_optimized.keras")

# Comparação rápida no console
# Baseline da rede neural simples (04_neural_network.py) - valor de referência
# Para comparação exata, execute ambos os scripts e compare os resultados
print(f"\nAccuracy atual: {acc:.4f}")
print("Execute 04_neural_network.py para comparação direta com a baseline")
