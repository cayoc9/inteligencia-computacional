# Referência: Gráficos a Evitar

> **"Nunca use 3D."** — Cole Knaflic

## 🚫 GRÁFICO DE PIZZA

### Por que evitar
O olho humano não consegue atribuir valores quantitativos no espaço bidimensional. É difícil comparar ângulos e áreas.

### Problemas específicos
- Difícil comparar fatias de tamanhos parecidos
- Impossível avaliar o quanto uma fatia é maior que outra
- 3D na pizza distorce ainda mais a percepção

### Substitua por
**Barras horizontais ordenadas** (do maior para o menor).

```
Em vez de pizza:            Use barras horizontais:
                            ┌──────────────────────┐
╭────────────────────────╮  │ Fornecedor A (33%) ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
│   ┌───┐                │  │ Fornecedor B (31%) ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
│ ┌─┤ B ├───┐            │  │ Fornecedor C (20%) ▓▓▓▓▓▓▓▓▓▓▓
│ │ └───┘   │            │  │ Fornecedor D (16%) ▓▓▓▓▓▓▓▓▓
│ │   A     │            │  └──────────────────────┘
│ └─────────┘   C        │
│          ┌────┐        │
│          │ D  │        │
│          └────┘        │
╰────────────────────────╯
```

## 🚫 GRÁFICO DE ROSCA

### Por que evitar
Pior que pizza: em vez de ângulos, você está pedindo para o público comparar **comprimentos de arco** — algo que o cérebro humano também não faz bem.

### Substitua por
**Barras horizontais** (mesma recomendação da pizza).

## 🚫 GRÁFICO 3D (QUALQUER TIPO)

### Por que evitar
- Distorce a percepção dos números
- Adiciona elementos desnecessários (painéis laterais, chão)
- No Excel, a altura da barra 3D é determinada por um plano tangente invisível — o que você vê **não é** o valor real

### Exemplo real
Um gráfico com valor 1 para Janeiro e 1 para Fevereiro, em 3D, parecia mostrar 0,8 visualmente.

### Substitua por
**2D simples**. Use cor para destacar, não terceira dimensão.

## 🚫 EIXO Y SECUNDÁRIO

### Por que evitar
- Difícil de ler (qual eixo corresponde a qual dado?)
- Induz a falsas correlações (linhas podem se cruzar por acaso)
- O público precisa decifrar antes de entender

### Substitua por

**Opção 1:** Legendas diretas nos pontos de dados (sem segundo eixo)

**Opção 2:** Dois gráficos separados verticalmente, mesmo eixo X, eixo Y à esquerda em cada um

## 🚫 GRÁFICO DE BARRAS COM LINHA DE BASE DIFERENTE DE ZERO

### Por que evitar
Engana o público. Nossos olhos comparam as pontas das barras. Se a base não é zero, a comparação visual é falsa.

### Exemplo clássico (Fox News)
Um aumento de 35% para 39,6% parecia de **460%** visualmente porque a base do eixo Y começava em 34.

### Regra
**Gráficos de barras SEMPRE começam em zero.**

(Nota: Essa regra NÃO se aplica a gráficos de linhas, onde o foco é a posição relativa no espaço.)

## 🚫 GRÁFICO "ESPAGUETE" (MUITAS LINHAS)

### Por que evitar
Mais de 4-5 linhas no mesmo gráfico e fica impossível distinguir tendências.

### Substitua por
- **Destaque 1 linha por vez** (as outras em cinza)
- **Separe em 2-3 gráficos** por categoria
- **Use uma tabela** com formatação condicional

## 🚫 CLIPART E DECORAÇÃO

### Por que evitar
- Não acrescenta informação
- Aumenta carga cognitiva
- Transmite falta de profissionalismo

### Substitua por
**Dados limpos e bem apresentados** são intrinsecamente bonitos.
