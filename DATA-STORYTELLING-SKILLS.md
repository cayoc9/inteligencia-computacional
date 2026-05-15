# Skills para Data Storytelling

## Busca Realizada

Foi realizada uma busca por skills relacionadas a **data storytelling** e **visualização de dados** no ecossistema open agent skills (skills.sh).

### Resultado
⚠️ **Nenhuma skill específica encontrada** para data storytelling no repositório pesquisado.

O ecossistema de skills é relativamente novo e foca principalmente em:
- Desenvolvimento web (React, Next.js)
- DevOps e deploy
- Code review e boas práticas
- Testes e qualidade de código

---

## Alternativas Disponíveis

### 1. **build-dashboard** (Skill Existente)
**Descrição:** Cria dashboards interativos com charts, filtros e tabelas em HTML auto-contido.

**Quando usar:**
- Criar relatório executivo com KPIs
- Transformar resultados de queries em relatório visual
- Dashboard de monitoramento
- Múltiplos charts com filtros em um arquivo navegável

**Instalação:**
```bash
npx skills add build-dashboard
```

**Aplicação ao seu projeto:**
Pode ser útil para criar visualizações comparativas dos modelos (RF vs RN) em um dashboard interativo.

---

## O Que Fazer Sem uma Skill Específica

### Opção 1: Usar Habilidades Nativas
Posso ajudar com data storytelling diretamente usando:

1. **Estrutura de narrativa:**
   - Contexto → Problema → Análise → Insights → Recomendações
   - Pyramid Principle (Minto)
   - Story arc para apresentações técnicas

2. **Visualizações recomendadas:**
   - Comparação de modelos: barras agrupadas, radar charts
   - Distribuição: histogramas, boxplots, violin plots
   - Relações: scatter plots, heatmaps de correlação
   - Performance: curvas ROC, Precision-Recall

3. **Princípios de design:**
   - Menos é mais (Edward Tufte)
   - Data-ink ratio
   - Pré-atenção e hierarquia visual
   - Acessibilidade (daltonismo, contraste)

### Opção 2: Criar Sua Própria Skill
Se você faz data storytelling frequentemente:

```bash
npx skills init my-data-storytelling
```

Estrutura sugerida para a skill:
```
my-data-storytelling/
├── README.md           # Instruções de uso
├── SKILL.md            # Metadados da skill
├── storytelling.md     # Estruturas de narrativa
├── visualizations.md   # Quando usar cada gráfico
├── accessibility.md    # Guidelines de acessibilidade
└── examples/           # Exemplos de aplicação
```

### Opção 3: Usar Ferramentas Externas

| Ferramenta | Propósito | Link |
|---|---|---|
| **Observable Plot** | Visualização declarativa | observablehq.com/plot |
| **Vega-Lite** | Grammar of graphics | vega.github.io |
| **Charticulator** | Design visual de charts | charticulator.com |
| **Datawrapper** | Charts para publicações | datawrapper.de |
| **Flourish** | Visualização interativa | flourish.studio |

---

## Aplicação ao Trabalho 1 (Seu Projeto Atual)

### Narrativa Sugerida para o Relatório

```
1. CONTEXTUALIZAÇÃO
   - Problema: Classificação em saúde do sono
   - Importância: Impacto na performance diária
   - Dataset: 100k registros, 32 features

2. METODOLOGIA
   - Abordagem: RF vs Redes Neurais
   - Métricas: 6 obrigatórias + análise de threshold
   - Validação: Split estratificado, random_state=42

3. RESULTADOS
   - RF: 74.15% accuracy, 82.18% ROC AUC
   - RN: 73.23% → 74% (otimizada)
   - HistGradientBoosting: 74.25%, 82.58% AUC

4. DISCUSSÃO
   - Por que RF > RN em dados tabulares
   - Teto do alvo (subjetividade)
   - Threshold tuning como oportunidade

5. INSIGHTS
   - 4 features dominam: sleep_quality, sleep_duration, stress, wake_episodes
   - Threshold 0.35 maximiza F1 (ganho de 6%)
   - Balanceamento de classes afeta métricas

6. CONCLUSÃO
   - Modelo recomendado: HistGradientBoosting
   - Limitações: Subjetividade do alvo
   - Trabalhos futuros: Outros targets, boosting
```

### Visualizações Recomendadas

| Seção | Gráfico | Dados |
|---|---|---|
| Resultados | Barras agrupadas | 6 métricas × 3 modelos |
| Performance | Curva ROC | RF vs RN vs HistGB |
| Distribuição | Boxplot | felt_rested por feature |
| Importância | Barras horizontais | Top 10 features |
| Threshold | Linha | F1/Balanced Acc × threshold |
| Correlação | Heatmap | Features × target |

---

## Próximos Passos

1. **Imediato:** Usar habilidades nativas para gerar visualizações do Trabalho 1
2. **Opcional:** Instalar `build-dashboard` para dashboard interativo
3. **Futuro:** Criar skill personalizada se necessidade recorrente

---

*Documento criado em 2026-05-15*
*Busca realizada em: skills.sh, GitHub (vercel-labs/agent-skills)*
