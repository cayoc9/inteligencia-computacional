# Relatório Técnico

## Comparação entre Random Forest e Redes Neurais na Classificação de Saúde do Sono

**Disciplina:** Inteligência Computacional — PPGEE/UFPA 2026.1  
**Grupo:** Alunos da disciplina  
**Data:** 15 de maio de 2026

---

## 1. Introdução

### 1.1 Contexto

A classificação de dados tabulares é um dos problemas mais frequentes em Machine Learning aplicado à saúde. A escolha entre modelos baseados em árvore (Random Forest, Gradient Boosting) e Redes Neurais Artificiais (RNA) depende de características do dataset como volume de dados, dimensionalidade, natureza das features e presença de ruído no alvo.

Este trabalho compara sistematicamente Random Forest (RF) e Redes Neurais MLP na tarefa de classificar a sensação de descanso ao acordar (`felt_rested`) a partir de dados de saúde do sono, estilo de vida e indicadores fisiológicos.

### 1.2 Objetivos

1. Implementar pipeline reprodutível de pré-processamento e modelagem
2. Comparar RF e RNA nas 6 métricas obrigatórias (acurácia, matriz de confusão, precisão, recall, F1, ROC AUC)
3. Investigar o limite prático de performance do alvo (`felt_rested`)
4. Otimizar threshold de decisão para maximizar F1-Score
5. Identificar features mais relevantes para a classificação
6. Propor recomendações baseadas nos resultados

---

## 2. Dataset

### 2.1 Origem e Descrição

O **Sleep Health and Daily Performance Dataset** (Kaggle, CC0) contém 100.000 registros com 32 features abrangendo:

- **Sono:** Duração, qualidade, latência, estágios (REM, profundo), episódios de acordar
- **Estilo de vida:** Horas de trabalho, exercício, tempo de tela, cafeína, álcool
- **Saúde:** Estresse, frequência cardíaca, IMC, condição de saúde mental
- **Demografia:** Idade, gênero, ocupação, país

O dataset é limpo: **0 valores nulos, 0 duplicatas**.

### 2.2 Target: `felt_rested`

Variável binária indicando se a pessoa se sentiu descansada ao acordar:

| Classe | Contagem | Proporção |
|---|---|---|
| 0 (Não descansado) | 60.988 | 61,0% |
| 1 (Descansado) | 39.012 | 39,0% |

**Observação:** Leve desbalanceamento (61%/39%). A classe majoritária como baseline atinge 61,0% de acurácia, mas F1=0 e ROC AUC=0,5 — não aprende nada.

### 2.3 Feature `cognitive_performance_score`

Esta feature representa um **desfecho pós-descanso** (score de performance cognitiva após acordar). Por isso, foi **removida do conjunto de features** na modelagem V1 oficial para evitar vazamento conceitual. Seu alto AUC individual (0,771) sugere que um target composto (`sono_restaurador` = `felt_rested` + `cognitive_performance_score`) pode ser interessante como trabalho futuro (V2 experimental).

---

## 3. Metodologia

### 3.1 Pipeline de Pré-processamento

```python
ColumnTransformer([
    ('cat', OneHotEncoder(), categorical_features),
    ('num', StandardScaler(), numerical_features),
])
```

- **Categóricas:** One-hot encoding (gênero, ocupação, país, etc.)
- **Numéricas:** Padronização (média 0, desvio 1)
- **Split:** Estratificado 70/30, random_state=42 (preservado para comparação justa)

### 3.2 Modelos

| Modelo | Hiperparâmetros | Biblioteca |
|---|---|---|
| **Random Forest** | n_estimators: [100, 200], max_depth: [10, 20, None], min_samples_split: [2, 5] — GridSearchCV, cv=3, scoring=f1 | scikit-learn |
| **MLP Base** | Dense(64)→Dense(32)→Dense(16), Dropout(0.2/0.1), Adam, EarlyStopping | TensorFlow/Keras |
| **MLP Otimizada (V2)** | Dense(128)→Dense(64)→Dense(32)→Dense(16), BatchNorm, Dropout(0.3/0.2), ReduceLROnPlateau | TensorFlow/Keras |
| **HistGradientBoosting** | Default (diagnóstico de rodada 3) | scikit-learn |
| **Logistic Regression** | max_iter=1000, solver=lbfgs | scikit-learn |
| **Extra Trees** | default | scikit-learn |

### 3.3 Métricas de Avaliação

As 6 métricas obrigatórias foram calculadas sobre o conjunto de teste (30.000 registros):

1. **Acurácia (Accuracy):** Proporção de acertos totais
2. **Matriz de Confusão:** VP, FP, FN, VN
3. **Precisão (Precision):** VP / (VP + FP)
4. **Recall (Sensibilidade):** VP / (VP + FN)
5. **F1-Score:** Média harmônica entre precisão e recall
6. **ROC AUC:** Área sob a curva ROC

Adicionalmente, foram computadas *Balanced Accuracy* e *Precision-Recall AUC* para lidar com o desbalanceamento.

---

## 4. Resultados

### 4.1 Comparação de Modelos

| Modelo | Acurácia | Balanced Acc | Precisão | Recall | F1 | ROC AUC |
|---|---|---|---:|---:|---:|---:|---:|
| **HistGradientBoosting** | **0,7425** | 0,7250 | **0,6787** | 0,6453 | 0,6616 | **0,8258** |
| Random Forest | 0,7415 | **0,7309** | 0,6528 | **0,6999** | **0,6756** | 0,8218 |
| Logistic Regression | 0,7315 | 0,7332 | 0,6332 | 0,7410 | 0,6828 | 0,8126 |
| Extra Trees | 0,7321 | 0,7211 | 0,6521 | 0,6711 | 0,6615 | 0,8110 |
| MLP Base | 0,7323 | ~0,72 | ~0,64 | ~0,68 | ~0,66 | ~0,81 |
| MLP Otimizada (V2) | ~0,74 | ~0,73 | ~0,65 | ~0,69 | ~0,67 | ~0,82 |
| Baseline (classe maj.) | 0,6099 | 0,5000 | 0,0000 | 0,0000 | 0,0000 | 0,5000 |

**Principais observações:**

- A diferença entre o melhor modelo (HistGradientBoosting, 74,25%) e a Random Forest (74,15%) é de **apenas 0,1 ponto percentual** — essencialmente empate técnico.
- A Rede Neural MLP base (73,23%) ficou ~1 pp abaixo da RF. A versão otimizada (V2) chegou a ~74%, ainda marginalmente abaixo.
- Todos os modelos convergem para o mesmo teto de ~74-74,5%, sugerindo um **limite prático do alvo**, não do modelo.

### 4.2 Matriz de Confusão (HistGradientBoosting)

```
              Previsto 0    Previsto 1
Real 0          9.814         2.384
Real 1          2.767         5.035
```

- **Falsos Positivos (2.384):** Pessoas classificadas como descansadas quando não estavam — risco ocupacional (Burnout)
- **Falsos Negativos (2.767):** Pessoas classificadas como não descansadas quando estavam — oportunidade perdida de bem-estar

### 4.3 Análise de Threshold

O threshold padrão de 0,5 não é o ideal para este problema desbalanceado:

| Threshold | Acurácia | Balanced Acc | Precisão | Recall | F1 |
|---|---:|---:|---:|---:|---:|
| **0,35** (ótimo F1) | 0,7184 | 0,7420 | 0,5979 | **0,8491** | **0,7017** |
| **0,39** (ótimo Bal Acc) | 0,7292 | **0,7424** | 0,6177 | 0,8026 | 0,6981 |
| 0,50 (padrão) | **0,7425** | 0,7250 | **0,6787** | 0,6453 | 0,6616 |

**Ganho:** Ajustando o threshold de 0,50 para **0,35**, o F1-Score sobe de **0,66 para 0,70 (+6,1%)** sem retreinar o modelo — apenas ajustando o ponto de corte.

### 4.4 Curvas ROC e Precision-Recall

As curvas ROC (Figura 1) mostram AUCs entre 0,81 e 0,83 para todos os modelos — indicando que todos aprendem padrões relevantes, com diferenças marginais. A curva Precision-Recall (Figura 2) reforça que o modelo ranqueia bem as instâncias positivas, com F1 máximo de 0,70 após ajuste de threshold.

### 4.5 Importância de Features

Apenas **4 features** concentram aproximadamente 80% do poder preditivo:

| Feature | Queda no AUC (permutação) | AUC individual |
|---|---|---|
| **Duração do sono (hrs)** | 0,1165 | 0,774 |
| **Qualidade do sono** | 0,0420 | 0,785 |
| **Episódios de acordar** | 0,0211 | 0,635 |
| **Nível de estresse** | 0,0172 | 0,712 (invertido) |

As demais 28 features contribuem marginalmente. Isso explica por que modelos mais complexos (RN profunda) não superam modelos baseados em árvore — **não há sinal adicional suficiente nas features restantes**.

---

## 5. Discussão

### 5.1 Por que a Random Forest superou a Rede Neural?

Resultado consistente com a literatura (Fernández-Delgado et al., 2014; Grinsztajn et al., 2022): **para dados tabulares de porte médio (~100k registros), modelos baseados em árvore tendem a superar redes neurais**. As razões:

1. **Não-linearidades locais:** RF captura interações complexas sem necessidade de arquitetura profunda
2. **Robustez a escalas:** Árvores são invariantes à escala das features (diferente de RN que requer padronização)
3. **Menos hiperparâmetros:** RF converge com tuning mínimo; RN requer ajuste fino de arquitetura, learning rate, regularização

### 5.2 O Teto de 74%

Todos os modelos — de uma regressão logística simples a uma MLP com 4 camadas — convergem para o mesmo patamar de ~74-74,5% de acurácia. Isso indica que **o gargalo não é o modelo, é o alvo**.

O diagnóstico de ambiguidade do target (Rodada 3) revelou que existem grupos de pessoas com perfil de sono semelhante (sono, estresse, rotina) que respondem de forma diferente para `felt_rested`. Isso sugere:

- **Ruído intrínseco:** A percepção subjetiva de descanso varia entre indivíduos
- **Features ausentes:** Variáveis como dieta, genética ou condições psicológicas não capturadas no dataset poderiam melhorar a separação
- **Target composto:** Combinar `felt_rested` com `cognitive_performance_score` (AUC individual = 0,771) pode gerar um alvo mais objetivo

### 5.3 Risco de Falsos Positivos no Contexto de Saúde

Em saúde ocupacional, classificar incorretamente uma pessoa cansada como descansada (Falso Positivo) pode mascarar **fadiga acumulada associada a risco de Burnout**. Por isso, a **Precisão** para a classe positiva merece atenção especial.

Com threshold 0,50, a precisão é 0,6787 e o recall 0,6453. Com threshold 0,35 (otimizado para F1), o recall sobe para 0,8491, mas a precisão cai para 0,5979 — mais falsos alarmes. A escolha do threshold deve considerar o contexto de aplicação:

- **Triagem populacional:** Threshold baixo (0,35) — prioriza não perder pessoas cansadas
- **Diagnóstico individual:** Threshold alto (0,50+) — prioriza não alarmar pessoas saudáveis

### 5.4 Engenharia de Atributos

Foram criadas features derivadas (`sleep_efficiency`, `stress_work_interaction`, `resilience_index`, etc.) na versão V2, mas nenhuma delas rompeu o teto de 74%. Isso reforça a conclusão de que a ambiguidade está no target subjetivo, não na falta de features.

### 5.5 Limitações

1. **Dataset sintético-calibrado:** O dataset, embora realista, pode não refletir toda a complexidade de dados clínicos reais
2. **Treino em CPU:** Redes Neurais foram treinadas em CPU (sem GPU), limitando o escopo de tuning arquitetural
3. **Validação cruzada:** Realizada apenas no diagnóstico de Rodada 3 (5 folds para HistGB); RF e RN usaram holdout único
4. **SHAP não implementado:** A interpretabilidade via SHAP poderia complementar a análise de permutation importance

---

## 6. Conclusão

### 6.1 Síntese dos Resultados

1. **Random Forest é a melhor escolha** para classificação em dados tabulares de saúde do sono — performance competitiva (74,15% acc, 82,18% AUC) com complexidade muito menor que Redes Neurais
2. **Rede Neural não fracassou** — ela encontrou o mesmo teto de performance com maior custo computacional
3. **O gargalo é o alvo, não o modelo** — o teto de ~74% é consistente em todos os modelos testados e reflete a subjetividade de `felt_rested`
4. **Threshold tuning entrega ganho real** — ajustar de 0,50 para 0,35 melhora o F1 em 6,1% sem retreinar
5. **4 features dominam** — duração do sono, qualidade do sono, estresse e episódios de acordar concentram ~80% do sinal

### 6.2 Recomendações

- **Para problemas tabulares similares:** Comece com Random Forest ou Gradient Boosting antes de investir em Redes Neurais
- **Para produção:** Ajuste o threshold de decisão conforme o contexto (triagem vs diagnóstico)
- **Para trabalhos futuros (V2):** Considere um target composto (`sono_restaurador`) combinando `felt_rested` com `cognitive_performance_score` para reduzir a subjetividade do alvo

### 6.3 Trabalhos Futuros (V2)

- **Alvo composto:** `sono_restaurador` = `felt_rested` + `cognitive_performance_score` (binário)
- **Stacking ensemble:** Combinar RF, HistGB e Logistic Regression como meta-estimador
- **Sistema Neuro-Fuzzy:** Para maior interpretabilidade das regras de decisão
- **Otimização genética:** Busca de hiperparâmetros para RN com algoritmos evolutivos

---

## Referências

- Fernández-Delgado, M. et al. (2014). "Do we need hundreds of classifiers to solve real world classification problems?" *Journal of Machine Learning Research*
- Grinsztajn, L. et al. (2022). "Why do tree-based models still outperform deep learning on tabular data?" *NeurIPS 2022*
- Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
- scikit-learn: Pedregosa et al. (2011). *Journal of Machine Learning Research*
- TensorFlow: Abadi et al. (2016). *OSDI*

---

*Anexos: Gráficos comparativos disponíveis em `reports/figures/`. Código fonte em `scripts/`. Notebook consolidado em `notebooks/`.*
