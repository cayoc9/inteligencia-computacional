# Template: Storyboard

> Planeje a estrutura antes de abrir o PowerPoint. Use post-its ou papel.

## Instruções

1. Pegue post-its ou uma folha de papel
2. Para cada slide/seção, escreva **uma ideia por nota**
3. Organize na sequência desejada
4. Reorganize, adicione, remova — é fácil com post-its
5. Só depois de aprovado, vá para o computador

## Formato Sugerido

Cada post-it deve conter:
- **Título** (o que será mostrado)
- **Tipo** (gráfico, texto, tabela, imagem)
- **Mensagem** (o público deve entender isto)
- **Dados** (qual dado/gráfico será usado)

## Exemplo Preenchido (Trabalho 1)

```
┌─────────────────────────────────────────────────┐
│ SLIDE 1: TÍTULO                                  │
│ Tipo: Texto                                      │
│ Mensagem: Comparação RF vs RN em Saúde do Sono   │
│ Dados: Nome do trabalho, autores, disciplina     │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 2: CONTEXTO                                │
│ Tipo: Texto + números em destaque                │
│ Mensagem: Dataset de 100k registros, 32 features │
│ Dados: sleep_health_dataset.csv resumo           │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 3: METODOLOGIA                             │
│ Tipo: Esquema visual                             │
│ Mensagem: Split estratificado, random_state=42   │
│ Dados: Pipeline do pré-processamento             │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 4: RESULTADOS RF                           │
│ Tipo: Gráfico de barras                          │
│ Mensagem: RF: 74.15% accuracy, AUC 82.18%        │
│ Dados: Métricas da RF tuned                      │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 5: RESULTADOS RN                           │
│ Tipo: Gráfico de barras + curva de loss          │
│ Mensagem: RN base 73.23% → otimizada ~74%        │
│ Dados: Curva de treino, métricas                 │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 6: COMPARAÇÃO                              │
│ Tipo: Barras agrupadas                           │
│ Mensagem: RF > RN; HistGB marginalmente melhor   │
│ Dados: 6 métricas × 3 modelos                    │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 7: THRESHOLD TUNING                        │
│ Tipo: Gráfico de linhas                          │
│ Mensagem: Threshold 0.35 maximiza F1 (+6%)       │
│ Dados: F1 × threshold, recall × threshold        │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 8: FEATURE IMPORTANCE                      │
│ Tipo: Barras horizontais                         │
│ Mensagem: 4 features dominam (80% do sinal)      │
│ Dados: Permutation importance                     │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE 9: CONCLUSÃO                               │
│ Tipo: Texto + call-to-action                     │
│ Mensagem: RF > RN em tabular; simplicidade vence │
│ Dados: --                                        │
└─────────────────────────────────────────────────┘
```

## Template em Branco (para imprimir ou copiar)

```
┌─────────────────────────────────────────────────┐
│ SLIDE __: ______________________________________ │
│ Tipo: (Texto/ Gráfico/ Tabela/ Imagem)           │
│ Mensagem: ______________________________________ │
│ Dados: _________________________________________ │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE __: ______________________________________ │
│ Tipo: __________________________________________ │
│ Mensagem: ______________________________________ │
│ Dados: _________________________________________ │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE __: ______________________________________ │
│ Tipo: __________________________________________ │
│ Mensagem: ______________________________________ │
│ Dados: _________________________________________ │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│ SLIDE __: ______________________________________ │
│ Tipo: __________________________________________ │
│ Mensagem: ______________________________________ │
│ Dados: _________________________________________ │
└─────────────────────────────────────────────────┘
```

## Dica

- Máximo **1 slide por post-it** (se uma ideia não cabe em 1 post-it, são 2 slides)
- Se o storyboard tiver mais de 15 slides, corte
- Mostre o storyboard para alguém antes de criar os slides
