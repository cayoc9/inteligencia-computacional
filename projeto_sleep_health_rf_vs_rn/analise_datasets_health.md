# Análise Comparativa — Datasets de Saúde para Trabalho 1 (IC — UFPA 2026.1)

> **Objetivo:** Comparar Random Forest vs Redes Neurais em classificação
> **Nicho:** Health / Saúde
> **Entrega:** 15/05/2026
> **Metodologia:** Download via Kaggle CLI + análise local com pandas (dados reais verificados)

---

## Critérios de Avaliação

| Critério | Peso | Justificativa |
|---|---|---|
| **Tamanho (rows únicos)** | Crítico | RN precisa de volume para não overfitar; RF funciona bem com pouco |
| **Target categórico claro** | Crítico | O trabalho pede classificação — precisa de variável alvo binária ou multiclasse |
| **Qualidade / limpeza** | Alto | Dados com nulos/desbalanceados exigem mais pré-processamento |
| **Sem duplicatas** | Alto | Duplicatas artificiais distorcem métricas e validação |
| **Riqueza de features** | Médio | Features mistas (numéricas + categóricas) permitem demonstrar mais técnicas |
| **Relevância clínica** | Médio | Impacto real na saúde = melhor narrativa para o relatório |
| **Popularidade (upvotes)** | Médio | Datasets com baseline na literatura facilitam comparação |

---

## Datasets Analisados via Playwright (dados reais extraídos das páginas do Kaggle)

### 🥇 Sleep Health & Daily Performance Dataset ✅ VERIFICADO

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/mohankrishnathalla/sleep-health-and-daily-performance-dataset` |
| **Autor** | Mohan Krishna Thalla |
| **Rows** | **100.000** ✅ |
| **Cols** | **32** ✅ |
| **Nulos** | **0** ✅ |
| **Duplicatas** | **0** ✅ |
| **Alvos** | 3: `cognitive_performance_score` (contínuo), `sleep_disorder_risk` (categórica: 4 valores), `felt_rested` (binária: 0/1) |
| **Upvotes** | 39 (Silver) |
| **Licença** | CC0 (Domínio Público) |
| **Tamanho** | 14.3 MB CSV (60.6 MB em memória) |

**Targets verificados via pandas:**
- `felt_rested`: 0 = 60.988 (61.0%) | 1 = 39.012 (39.0%) — levemente desbalanceado
- `sleep_disorder_risk`: 4 categorias ('Healthy', 'Mild', 'Moderate', 'Severe') — multiclasse
- `exercise_day`, `sleep_aid_used`, `shift_work` — também binárias mas menos relevantes como target

**Features (7 grupos lógicos):**
- Demográficas: age, gender, occupation, bmi, country (6 cols)
- Arquitetura do sono: sleep_duration, quality, rem%, deep%, latency, wake_episodes (6 cols)
- Lifestyle: caffeine, alcohol, screen_time, exercise, steps, nap (6 cols)
- Psicológicas: stress_score, work_hours, chronotype, mental_health_condition (4 cols)
- Contexto saúde: heart_rate, sleep_aid, shift_work, room_temp, weekend_diff (5 cols)
- Ambientais: season, day_type (2 cols)
- Targets: cognitive_score, disorder_risk, felt_rested (3 cols)

**Correlações médicas (declaradas pelo autor):**
- stress vs quality r=−0.64
- REM% vs cognition r=+0.45
- age vs deep sleep r=−0.45

**Baseline do autor:**
- felt_rested: AUC ≈ 0.78-0.82
- sleep_disorder_risk: F1-macro ≈ 0.72-0.78
- cognitive_performance_score: RMSE ≈ 8-12

**✅ PONTOS FORTES:**
- 100.000 registros REAIS (verificados) — RN terá dados suficientes
- 0 duplicatas, 0 nulos — dataset limpo
- 32 features ricas — material abundante para EDA e feature engineering
- 3 targets — flexibilidade total (binária, multiclasse, regressão)
- 12 ocupações para análise por segmento
- Baseline já fornecida
- Calibrado com fontes reais (CDC, Sleep Foundation, Framingham)

**⚠️ PONTOS DE ATENÇÃO:**
- Dados sintéticos (não reais) — pode ser questionado pelo professor
- `felt_rested` levemente desbalanceado (61/39) — pode exigir class_weight

**NOTA: 9.5/10** ✅

---

### Diabetes Prediction Dataset

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset` |
| **Rows** | ~9.528 |
| **Cols** | 9 (8 preditoras + 1 alvo) |
| **Alvo** | `diabetes` (binária: 0/1) |
| **Features** | age, gender, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level |
| **Nulos** | Nenhum |

**✅ PONTOS FORTES:** Tamanho intermediário, features mistas, relevante clinicamente
**⚠️ PONTOS DE ATENÇÃO:** Menos features que o Sleep Health
**NOTA: 8.5/10**

---

### Stroke Prediction Dataset

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/fedesoriano/stroke-prediction-dataset` |
| **Rows** | ~5.110 |
| **Cols** | 12 |
| **Alvo** | `stroke` (binária) |
| **Nulos** | Sim (requer tratamento) |
| **Balanceamento** | Fortemente desbalanceado (~95% negativos) |

**✅ PONTOS FORTES:** Desafio real de desbalanceamento — permite comparar SMOTE, class weights
**⚠️ PONTOS DE ATENÇÃO:** Desbalanceamento extremo pode dificultar convergência da RN
**NOTA: 8.0/10**

---

### Breast Cancer Wisconsin (Diagnostic)

| Propriedade | Valor |
|---|---|
| **URL** | `archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic` |
| **Rows** | 569 |
| **Cols** | 30 |
| **Alvo** | Diagnosis (benigno/maligno) |
| **Balanceamento** | ~63% benigno, ~37% maligno |

**✅ PONTOS FORTES:** Clássico da literatura, 30 features numéricas reais
**⚠️ PONTOS DE ATENÇÃO:** Apenas 569 registros — RN vai sofrer
**NOTA: 7.5/10**

---

### Heart Disease Dataset (johnsmith88/heart-disease-dataset) ❌ REVISADO COM DADOS REAIS

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/johnsmith88/heart-disease-dataset` |
| **Rows (brutas)** | **1.025** |
| **Rows (únicos)** | **302** ⚠️ |
| **Duplicatas** | **723 (70.5%)** 🔴 |
| **Cols** | **14** |
| **Alvo** | `target` (binária: 0 = sem doença, 1 = com doença) |
| **Nulos** | 0 |
| **Balanceamento (sem duplicatas)** | Classe 1: 164 (54.3%) / Classe 0: 138 (45.7%) — bem balanceado |
| **Features** | age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal |
| **Fonte original** | UCI Cleveland Heart Disease (303 registros originais) |

**O que é:** É o dataset UCI Cleveland Heart Disease **com 70.5% de duplicatas artificiais**. Dos 1.025 registros, apenas 302 são únicos — essencialmente o dataset original de ~303 registros com linhas repetidas para inflar o tamanho.

**✅ PONTOS FORTES:**
- Bem balanceado (54/46)
- Sem valores nulos
- Clássico — dezenas de papers para comparação

**❌ PONTOS FRACOS (CRÍTICOS PARA ESTE TRABALHO):**
1. **70.5% de duplicatas** — Se não detectar e remover, o modelo vai memorizar as duplicatas e as métricas vão ser infladas artificialmente. Se remover, sobram apenas 302 registros
2. **Apenas 302 registros únicos** — Redes Neurais vão overfitar severamente. Mesmo uma MLP simples terá mais parâmetros do que dados suficientes
3. **Dataset mais batido da história** — provavelmente 50+ trabalhos acadêmicos da UFPA já usaram este mesmo dataset
4. **Inflação artificial de tamanho** — Parece ter 1.025 registros mas na prática tem 302. Isso é uma armadilha para quem não faz EDA rigoroso
5. **Sem desafio de pré-processamento** — já vem limpo, sem outliers graves
6. **Features pouco variadas** — tudo numérico ou ordinal categórico

**⚖️ VEREDITO ATUALIZADO:**
> Este dataset é **PIOR do que eu inicialmente estimei**. Não são 303 registros genuínos — são 302 únicos com 723 cópias artificiais (70.5%). Quem não detectar as duplicatas no EDA terá métricas infladas. Quem detectar terá que trabalhar com 302 registros — insuficiente para RN. **Não recomendado.**

**NOTA ATUALIZADA: 3.5/10** (rebaixado de 5.0)

---

### Pima Indians Diabetes Database (UCI Official) ⚠️ COM ALERTA DE ZEROS

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/uciml/pima-indians-diabetes-database` |
| **Autor** | UCI Machine Learning Repository |
| **Rows** | **768** |
| **Cols** | **9** (8 features + 1 target) |
| **Alvo** | `Outcome` (binária: 0/1) — 268 positivos de 768 (34.9%) |
| **Nulos declarados** | 0 |
| **⚠️ Zeros suspeitos (valores faltantes codificados como 0)** | |
| → Insulin | **374 zeros (48.7%)** 🔴 |
| → SkinThickness | **227 zeros (29.6%)** 🟡 |
| → BloodPressure | **35 zeros (4.6%)** |
| → BMI | **11 zeros (1.4%)** |
| → Glucose | **5 zeros (0.7%)** |
| **Upvotes** | **5.021** (Gold Medal 🥇) |
| **Licença** | CC0: Public Domain |
| **Notebooks no Kaggle** | 4.071 |
| **Discussões** | 55 |

**O que é:** O dataset de diabetes mais famoso do mundo. Original do NIDDK. Publicado em 1988 por Smith et al. Todas as pacientes são mulheres de ascendência Pima Indian com 21+ anos.

**✅ PONTOS FORTES:**
- Gold standard — 5.021 upvotes, 4.071 notebooks, é o dataset de saúde mais referenciado do Kaggle
- Baseline abundante — milhares de notebooks públicos para comparar seus resultados
- Paper original citável (Smith et al., 1988, IEEE)
- **Zeros artificiais = desafio real de EDA** — tratar esses zeros (substituir por mediana, KNN imputer, etc.) é uma etapa de pré-processamento legítima e valiosa
- Tamanho intermediário (768) — melhor que 303 para RN, ainda pequeno mas funcional

**⚠️ PONTOS DE ATENÇÃO:**
- 768 registros ainda é limitado para RN profunda (funciona com MLP simples)
- Apenas mulheres Pima Indian — viés demográfico
- Features limitadas (8) — menos material para feature engineering
- **48.7% dos valores de Insulin são zeros artificiais** — se não tratar, a RN vai aprender errado

**NOTA: 7.0/10**

---

### Global Mental Health Crisis Index 2026 ❌ INADEQUADO

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/alitaqishah/global-mental-health-crisis-index-2026` |
| **Rows** | **92** (1 por país) |
| **Cols** | **29** |
| **Alvo** | `mh_crisis_index` (0-100, **contínuo**) |
| **Upvotes** | 45 (Silver) |

**❌ INADEQUADO** — O alvo é contínuo (regressão), não categórico (classificação). Não serve para o Trabalho 1.

**NOTA: 3.0/10**

---

### Sleep & Lifestyle Study ⚠️ SEM TARGET CLARO

| Propriedade | Valor |
|---|---|
| **URL** | `kaggle.com/datasets/ayeshaimran1619/sleep-and-lifestyle-study` |
| **Rows** | **374** |
| **Cols** | **13** |
| **Alvo** | **Nenhum alvo explícito** — dataset exploratório |
| **Upvotes** | 27 (Silver) |

**⚠️ PROBLEMÁTICO** — Não tem variável target definida. Você teria que criar uma artificialmente (ex: binarizar Quality of Sleep), o que enfraquece o trabalho. Apenas 374 registros.

**NOTA: 4.0/10**

---

## Ranking Final Consolidado (verificado com pandas)

| Rank | Dataset | Rows Únicos | Cols | Target | Duplicatas | Nulos | Upvotes | Nota | Veredito |
|:---:|---|---:|---:|---|:---:|:---:|---:|:---:|---|
| 🥇 | **Sleep Health & Daily Performance** | 100.000 | 32 | 3 targets | 0 | 0 | 39 | **9.5** | ✅ MELHOR OPÇÃO |
| 🥈 | **Diabetes Prediction** (iammustafatz) | 9.528 | 9 | Binária | — | 0 | — | **8.5** | Excelente equilíbrio |
| 🥉 | **Pima Indians Diabetes** (UCI Official) | 768 | 8 | Binária | 0 | 0* | 5.021 🥇 | **7.0** | *48.7% zeros em Insulin |
| 4 | Breast Cancer Wisconsin (UCI) | 569 | 30 | Binária | — | 0 | — | **7.5** | Clássico, pequeno |
| 5 | Stroke Prediction (fedesoriano) | ~5.1k | 12 | Binária (desbal.) | — | Sim | — | **8.0** | Desafio desbalanceamento |
| 6 | Sleep & Lifestyle Study | 374 | 13 | Sem target | — | 0 | 27 | **4.0** | Sem alvo definido |
| 7 | **Heart Disease (johnsmith88)** | **302** | 14 | Binária | **723 (70.5%)** | 0 | — | **3.5** | 🔴 70% duplicatas |
| 8 | Global Mental Health Crisis Index | 92 | 29 | Contínuo | — | 0 | 45 | **3.0** | É regressão |

---

## Recomendação Final

### Use o **Sleep Health & Daily Performance Dataset** como dataset principal

**Por que é disparado o melhor:**
1. **100.000 registros** permite demonstrar escalabilidade real — RN converge, RF satura
2. **3 targets** dão flexibilidade: comece com `felt_rested` (binária), expanda para `sleep_disorder_risk` (multiclasse)
3. **32 features em 7 grupos** = material abundante para EDA, feature importance, SHAP
4. **Baseline do autor** (AUC 0.78-0.82) = referência para comparar seus modelos
5. **Ocupações (12 tipos)** = análise por segmento diferencia seu trabalho
6. **Zero limpeza** = máximo tempo para análise e tuning
7. **Dados sintéticos calibrados** com fontes reais (CDC, Sleep Foundation, Framingham)

### Estratégia de uso:
- **Target primário:** `felt_rested` (binária) — mais simples, baseline clara
- **Target secundário (bônus):** `sleep_disorder_risk` (multiclasse) — impressiona na apresentação
- **Modelos:** Random Forest (GridSearchCV) vs MLP/Feed-Forward NN (Keras Tuner)
- **Análise extra:** SHAP feature importance por ocupação

---

## Próximos Passos

1. [ ] Baixar o dataset `mohankrishnathalla/sleep-health-and-daily-performance-dataset`
2. [ ] Formar grupo e preencher planilha (prazo: 10/04)
3. [ ] Iniciar EDA no Jupyter Notebook
4. [ ] Implementar Random Forest + tuning
5. [ ] Implementar Rede Neural + tuning
6. [ ] Avaliar com todas as 6 métricas obrigatórias
7. [ ] Escrever relatório técnico
8. [ ] Preparar apresentação (15 min)

---

*Análise realizada em 09/04/2026 via:*
1. *Playwright CLI (navegação e extração das páginas do Kaggle)*
2. *Kaggle CLI (`kaggle datasets download`) para download real dos CSVs*
3. *Pandas para análise local: dimensões, tipos, nulos, duplicatas, distribuição de targets*

---

## 🔍 Descobertas Críticas (Revisão Pós-Análise)

### ⚠️ johnsmith88/heart-disease tem 70.5% de duplicatas

O dataset que parece ter 1.025 registros na verdade tem apenas **302 registros únicos**. Os outros 723 são cópias exatas. Isso foi verificado com `df.duplicated().sum()`.

**Impacto:** Se não detectar as duplicatas no EDA, o modelo vai ter métricas infladas artificialmente (o mesmo paciente aparece múltiplas vezes em treino e teste). Se detectar, sobram 302 registros — insuficiente para Redes Neurais.

### ⚠️ Pima Indians tem 48.7% de zeros artificiais em Insulin

O dataset não tem `NaN` mas tem **374 zeros em Insulin** e **227 zeros em SkinThickness** — valores fisiológicos impossíveis codificados como 0 para representar "não medido".

**Impacto:** Se não tratar, a RN vai aprender que Insulin=0 é um valor válido, o que distorce completamente o modelo. Tratar esses zeros é uma etapa obrigatória de pré-processamento.

### ✅ Sleep Health & Daily Performance é limpo e completo

100.000 registros, 0 duplicatas, 0 nulos, 32 features. Verificado com pandas. É o dataset mais robusto para este trabalho.
