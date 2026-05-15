# Template: Estrutura Narrativa

> Toda história tem início, meio e fim. Sua apresentação de dados também.

## Arco de 3 Atos

```
Ato 1                Ato 2                 Ato 3
Contexto      →      Dados         →       Ação
[Por quê?]          [O quê?]              [E daí?]
```

## Ato 1: Contexto (25% do tempo)

| Elemento | Pergunta a responder | Exemplo (Trabalho 1) |
|---|---|---|
| **Problema** | O que motivou este trabalho? | Classificar saúde do sono com ML |
| **Importância** | Por que o público deve se importar? | Comparação RF vs RN para dados tabulares |
| **O que está em jogo** | O que ganha/perde? | Escolha do modelo certo para o problema |
| **Prévia** | O que vamos ver? | Vou mostrar que RF superou RN |

## Ato 2: Dados (50% do tempo)

| Cena | O que mostrar | Como mostrar |
|---|---|---|
| **Metodologia** | Como foi feita a análise | Esquema visual (não slides de texto) |
| **Descoberta 1** | RF: 74.15% accuracy | Gráfico de barras |
| **Descoberta 2** | RN: 73.23% → 74% | Gráfico de barras + curva de loss |
| **Descoberta 3** | Threshold tuning: 0.35 | Gráfico de linhas |
| **Insight** | Por que RF > RN? | Feature importance (barras horizontais) |

**Regra:** Cada descoberta é 1 slide. Não coloque múltiplas descobertas no mesmo slide.

## Ato 3: Ação (25% do tempo)

| Elemento | Pergunta a responder | Exemplo (Trabalho 1) |
|---|---|---|
| **Síntese** | O que os dados significam? | RF > RN para dados tabulares |
| **Recomendação** | O que fazer com isso? | Escolha RF para problemas similares |
| **Call-to-action** | O que o público deve fazer? | Aprovar relatório / Considerar RF em projetos futuros |
| **Próximos passos** | O que vem depois? | Trabalho 2: Ensemble / Híbrido |

## Técnicas de Transição

| De | Para | Frase de transição |
|---|---|---|
| Contexto | Metodologia | "Para responder essa pergunta, fizemos..." |
| Metodologia | Descobertas | "E o que encontramos foi surpreendente..." |
| Descoberta 1 | Descoberta 2 | "Mas não paramos por aí..." |
| Descobertas | Análise | "O que isso significa na prática?" |
| Análise | Ação | "Com base nisso, recomendamos..." |

## Exemplo de Fluxo Completo (Trabalho 1)

```
[Ato 1] Problema: Comparar RF vs RN em dados de saúde do sono
      → Importância: 100k registros, 32 features, alvo binário
      → Prévia: "Vou mostrar que a RF venceu"

[Ato 2] Metodologia: Split estratificado, random_state=42
      → RF: 74.15% accuracy, GridSearchCV → gráfico de barras
      → RN: 73.23% base → 74% otimizada → curva de loss
      → Comparação: 6 métricas × 3 modelos → barras agrupadas
      → Threshold: 0.35 maximiza F1 → gráfico de linhas
      → Feature importance: 4 features dominam → barras horizontais

[Ato 3] Síntese: RF > RN em dados tabulares (consistente com literatura)
      → Recomendação: Para problemas similares, comece com RF
      → Call-to-action: Relatório aprovado para entrega
      → Próximos passos: Trabalho 2 com ensemble
```

## Verificação Final

- [ ] Ato 1 responde "por que eu deveria me importar?"
- [ ] Ato 2 tem 1 descoberta principal por slide
- [ ] Ato 3 termina com call-to-action claro
- [ ] Transições conectam os atos suavemente
- [ ] Tempo dividido ~25% / 50% / 25%
- [ ] Mensagem principal aparece em todos os 3 atos
