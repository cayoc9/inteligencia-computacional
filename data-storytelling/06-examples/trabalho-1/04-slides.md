# Exemplo: Estrutura de Slides (Trabalho 1)

> Estrutura pronta para criar os slides da apresentação. Cada linha = 1 slide.

## Estrutura (10 slides, ~12 minutos)

| # | Título | Tipo | Tempo | Dica |
|---|---|---|---|---|
| 1 | **Comparação RF vs RN em Saúde do Sono** | Texto | 30s | Título, autores, disciplina |
| 2 | **O Problema e os Dados** | Números destaque | 60s | 100k registros, 32 features, target felt_rested |
| 3 | **Metodologia** | Esquema visual | 45s | Mostre a pipeline como imagem, não texto |
| 4 | **Random Forest** | Barras verticais | 60s | 74.15% acc, 82.18% AUC |
| 5 | **Rede Neural** | Barras + curva loss | 60s | Base 73.23% → otimizada ~74% |
| 6 | **Comparação** | Barras agrupadas | 90s | 6 métricas × 3 modelos + HistGB |
| 7 | **Threshold Tuning** | Linhas F1 × thresh | 60s | 0.35 → F1 0.7017 (+6%) |
| 8 | **Feature Importance** | Barras horizontais | 60s | 4 features = 80% do sinal |
| 9 | **Conclusão** | Texto + 3 bullets | 60s | RF vence, teto do alvo, threshold importa |
| 10 | **Obrigado e Perguntas** | Texto + contato | 30s | Call-to-action claro |

## Modelo de Slide (PowerPoint / Google Slides / Keynote)

### Slide 6 — Comparação (o mais importante)

**Título (36pt):** `RF e HistGB lideram em todas as métricas`

**Gráfico (esquerda, 60% do slide):**
```
┌──────────────────────────────────────────────────────┐
│                                                       │
│ Accuracy  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓░░  │
│ Precision ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓░░▓░░  │
│ Recall    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓░░  │
│ F1        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓░░  │
│ ROC AUC   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  │
│                                                       │
│ [azul escuro = RF]  [azul médio = HistGB]  [cinza = RN]│
└──────────────────────────────────────────────────────┘
```

**Texto à direita (30% do slide, 24pt):**
```
• RF: 74.15% acc, 82.18% AUC
• RN: 73.23% base → ~74% otimizada
• HistGB: 74.25% acc, 82.58% AUC
• Diferença RF vs HistGB: 0.1 pp
```

**Anotação no gráfico:**
```
★ "RF — melhor custo-benefício"
```

## Template para Criar Seus Slides

### Regras de Estilo

| Elemento | Especificação |
|---|---|
| Fonte título | Arial/Helvetica 36pt, negrito |
| Fonte corpo | Arial/Helvetica 24-28pt |
| Fonte eixos | Arial 12-14pt, cinza |
| Cor destaque | #2166AC (azul escuro) |
| Cor secundária | #B3B3B3 (cinza) |
| Cor alerta | #B2182B (vermelho) |
| Fundo | Branco |
| Largura máxima gráfico | 80% do slide |
| Número máximo bullets | 3 por slide |
| Número máximo slides | 12 para 15 min |

### CheckList por Slide

Antes de finalizar cada slide:

- [ ] Uma única mensagem principal
- [ ] Título descritivo (conta a história)
- [ ] Gráfico ou visual, não texto corrido
- [ ] Destaque visual para o ponto principal
- [ ] Fonte legível no projetor (teste em 50% de zoom)
- [ ] Sem bordas desnecessárias
- [ ] Cores com propósito (não decorativas)
