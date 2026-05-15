# Exemplo: Gráficos Antes/Depois (Trabalho 1)

> Exemplos de como aplicar os princípios de visualização aos dados do projeto.

## Exemplo 1: Comparação de Modelos

### Antes (tabela densa em apresentação ao vivo)

```
                    RF         RN Base    RN V2      HistGB
Accuracy         0.7415      0.7323     ~0.74      0.7425
Balanced Acc     0.7309      ~0.72      ~0.73      0.7250
Precision        0.6528      ~0.64      ~0.65      0.6787
Recall           0.6999      ~0.68      ~0.69      0.6453
F1-Score         0.6756      ~0.66      ~0.67      0.6616
ROC AUC          0.8218      ~0.81      ~0.82      0.8258
```

**Problemas:** Difícil de ler em tempo real, público precisa comparar linha por linha, sem hierarquia visual.

### Depois (barras agrupadas)

```
             ┌─────────────────────────────────────────────┐
             │  RF e HistGB lideram em todas as métricas   │
             └─────────────────────────────────────────────┘
                      ╔════╗  ╔════╗  ╔════╗
Accuracy      0.74    ║ RF ║  ║ H  ║  ║ RN ║
             ──────────────────────────────────────
             ┌──────────────────────────────────────┐
Precision     │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
Recall        │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
F1            │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
ROC AUC       │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
             └──────────────────────────────────────┘
  [azul]   = RF e HistGB (melhores)
  [cinza]  = RN (atrás)
  [destaque seta] → "RF: melhor custo-benefício entre performance e complexidade"
```

## Exemplo 2: Threshold Tuning

### Antes (tabela com vários thresholds)

```
Threshold    Accuracy     F1         Recall     Prec
0.30         0.7120      0.6945      0.8712     0.5780
0.35         0.7184      0.7017      0.8491     0.5980  ← Melhor F1
0.39         0.7215      0.6981      0.8026     0.6180  ← Melhor Bal Acc
0.45         0.7260      0.6800      0.7300     0.6360
0.50         0.7415      0.6616      0.6453     0.6787  ← Padrão
```

### Depois (gráfico de linhas)

```
       F1 × Threshold
       ┌────────────────────────────────────────────────┐
       │                                                │
       │                                    ┌─────┐      │
       │  Recall ────╮                     │     │      │
       │             │                     │ F1  │      │
F1     │             ▼                     │     │      │
 0.70  │                          ★━━━━━━━━┘     │      │
       │                        ╱│                 │      │
 0.68  │                      ╱ │                 │      │
       │ ───────────────────────────────────────────│      │
 0.66  │ │  Threshold 0.50   │                     │      │
       │ │  F1 = 0.66        │                     │      │
 0.64  │ └──────────────────────────────────────────┘      │
       │                                                    │
       └────────────────────────────────────────────────┘
         0.30   0.35   0.40   0.45   0.50
                  ↑
           [destaque] Threshold 0.35:
           F1 = 0.7017 (ganho de 6%)
```

## Exemplo 3: Feature Importance

### Antes (lista numerada)

```
1. sleep_quality_score       → 0.7849
2. sleep_duration_hrs        → 0.7738
3. stress_score              → 0.7125
4. work_hours_that_day       → 0.6454
5. wake_episodes_per_night   → 0.6352
6. ... (demais 27 features)
```

### Depois (barras horizontais)

```
     Feature Importance (AUC isolado ajustado)
     ┌────────────────────────────────────────────┐
     │  80% do sinal está em apenas 4 features    │
     └────────────────────────────────────────────┘

sleep_quality      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  0.78
sleep_duration     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   0.77
stress_score       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        0.71
work_hours         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               0.65
wake_episodes      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               0.64

  [azul escuro] = features dominantes
  [cinza]       = demais features (27)
  [linha vertical] = marca de 0.70 (referência)
```

## Exemplo 4: Curvas ROC

### Antes (apenas o valor de AUC)

```
RF AUC: 0.8218
RN AUC: 0.8100
HistGB AUC: 0.8258
```

### Depois (curvas ROC sobrepostas)

```
     1.0 ──────────────────────────────────────────────
          ╱                                          
         ╱            ╱╱╱╱╱                          
        ╱           ╱    ╱╱╱     ─── RF (0.8218)
       ╱          ╱        ╱╱    ─── RN (0.8100)
TPR   ╱         ╱           ╱╱   ─── HistGB (0.8258)
      ╱        ╱              ╱╱
     ╱       ╱                 ╱╱
    ╱      ╱                    ╱╱
   ╱     ╱                       ╱╱
  ╱    ╱                          ╱╱
 ╱   ╱                             ╱╱
0.0 ──────────────────────────────────────────────
     0.0                                       1.0
                         FPR

  [destaque] Área sob a curva: todos os modelos próximos
  [seta] "Diferença marginal — o gargalo é o alvo, não o modelo"
```
