# Referência: Árvore de Decisão de Gráficos

> Qual gráfico usar? Siga esta árvore.

```
                  ┌───────────────────────┐
                  │ QUAIS SÃO SEUS DADOS? │
                  └───────────────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
  1-2 números          Vários números       Dados contínuos
       │                    │                    │
       ▼                    ▼                    ▼
  TEXTO SIMPLES        Série temporal?        Série temporal?
       │                    │                    │
       │           ┌───────┴───────┐       ┌───────┴───────┐
       │           ▼               ▼       ▼               ▼
       │          SIM              NÃO     SIM              NÃO
       │           │                │       │                │
       │           ▼                ▼       ▼                ▼
       │         LINHAS    2 pontos     LINHAS          BARRAS
       │                    no tempo?                      │
       │                    │     │                  ┌─────┴─────┐
       │                    ▼     ▼                  ▼           ▼
       │                 INCLI-  BARRAS        Nomes longos?  Nomes curtos?
       │                 NAÇÃO                  │     │        │     │
       │                                   ┌────┘     └────┐  └──┐  └──┐
       │                                   ▼                ▼     ▼     ▼
       │                             HORIZONTAIS    VERTICAIS    │   VERTICAIS
       │                                                        │
       │                                      ┌─────────────────┤
       │                                      ▼                 ▼
       │                                 Comparar totais    Decompor total
       │                                   + partes?         em partes?
       │                                      │                 │
       │                             ┌────────┴────────┐       ▼
       │                             ▼                 ▼    CASCATA
       │                        BARRAS EMPILHADAS  BARRAS EMPILHADAS
       │                        (ABSOLUTO)         (100%)
       │
       ▼
  Relação entre 2 variáveis?
       │
  ┌────┴────┐
  ▼         ▼
 SIM        NÃO
  │          │
  ▼          ▼
DISPERSÃO  Magnitudes muito
           diferentes?
               │
          ┌────┴────┐
          ▼         ▼
         SIM        NÃO
          │          │
          ▼          ▼
     ÁREA        TABELA /
     QUADRADA    MAPA DE CALOR

```

## Tabela de Referência Rápida

| Situação | Gráfico Recomendado |
|---|---|
| 1-2 números para comunicar | Texto simples (sem gráfico) |
| Dados tabulares, várias linhas | Tabela ou Mapa de Calor |
| Série temporal (1+ séries) | Gráfico de Linhas |
| 2 pontos no tempo, várias categorias | Gráfico de Inclinação |
| Categorias, nomes curtos | Barras Verticais |
| Categorias, nomes longos | Barras Horizontais |
| Categorias, séries múltiplas | Barras Agrupadas |
| Total + partes | Barras Empilhadas (absoluto ou 100%) |
| Decompor início → mudanças → fim | Cascata |
| Relação entre 2 variáveis | Dispersão |
| Magnitudes muito diferentes | Área Quadrada |
| Escala Likert | Barras Horizontais Empilhadas 100% |

## O que NÃO usar

| Gráfico | Substitua por |
|---|---|
| Pizza | Barras Horizontais (ordenadas) |
| Rosca | Barras Horizontais |
| 3D (qualquer tipo) | 2D simples |
| Eixo Y secundário | Legendas diretas ou 2 gráficos separados |
| Radar | Barras Horizontais |
| Bolhas | Dispersão (sem terceira dimensão desnecessária) |
| Gráfico "espaguete" (muitas linhas) | Separe em 2-3 visuais ou destaque 1 por vez |
