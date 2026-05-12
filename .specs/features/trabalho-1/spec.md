# Especificação: Trabalho 1 - Classificação em Saúde

## Problema
Classificar o estado de saúde do sono e performance diária utilizando modelos de aprendizado de máquina, comparando uma abordagem baseada em árvores (Random Forest) com uma conexão (Redes Neurais).

## Dataset
- **Nome:** Sleep Health and Daily Performance Dataset
- **ID Kaggle:** `mohankrishnathalla/sleep-health-and-daily-performance-dataset`
- **Target Primário:** `felt_rested` (Binário: 0/1)
- **Target Secundário:** `sleep_disorder_risk` (Multiclasse)

## Requisitos de Implementação (ID-REQ)
- **REQ-01:** EDA completo (distribuições, correlações, outliers).
- **REQ-02:** Pré-processamento (One-hot encoding, Normalização/Padronização).
- **REQ-03:** Divisão Treino/Teste (opcional Validação).
- **REQ-04:** Random Forest com Fine-tuning (`n_estimators`, `max_depth`).
- **REQ-05:** Redes Neurais com Fine-tuning de hiperparâmetros.

## Métricas Obrigatórias (ID-MET)
- **MET-01:** Acurácia (Accuracy)
- **MET-02:** Matriz de Confusão
- **MET-03:** Precisão (Precision)
- **MET-04:** Recall (Sensibilidade)
- **MET-05:** F1-Score
- **MET-06:** Curva ROC e AUC
