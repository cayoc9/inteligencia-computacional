# Referência: Paleta de Cores

> Cores têm função: guiar a atenção. Use com estratégia.

## Paleta Base (Neutra + 1 Destaque)

Use para 80% dos gráficos: 1 cor neutra para o contexto + 1 cor de destaque.

``` 
Contexto:    #B3B3B3 (cinza claro) — dados secundários
Destaque:   #2166AC (azul escuro) — dados principais
Fundo:      #FFFFFF (branco) — slide/fundo
Texto:      #333333 (cinza escuro) — legível, não preto puro
Sutil:      #969696 (cinza médio) — eixos, bordas, fontes secundárias
```

## Paleta de Contraste (2+ Destaques)

Para gráficos comparativos (ex: RF vs RN).

### Opção 1: Monocromática (recomendada)

``` 
Mais claro:  #67A9CF (azul claro)  → categoria A
Médio:       #3690C0 (azul médio)  → categoria B
Mais escuro: #2166AC (azul escuro) → categoria C (destaque)
```

### Opção 2: Complementar (2 grupos)

``` 
Grupo 1:     #2166AC (azul)        → Modelos baseados em árvore
Grupo 2:     #B2182B (vermelho)    → Redes neurais
```

### Opção 3: Segura para daltônicos (ColorBrewer)

``` 
#1B9E77 (verde escuro)
#D95F02 (laranja)
#7570B3 (roxo)
#E7298A (rosa)
#66A61E (verde claro)
#E6AB02 (amarelo)
```

## Paletas por Contexto

| Contexto | Paleta Sugerida |
|---|---|
| **Apresentação formal** (banca, diretoria) | Azuis escuros + cinza + um destaque |
| **Resultado positivo** | Verde escuro + cinza |
| **Alerta/Problema** | Vermelho + cinza |
| **Comparação binária** | Azul vs Vermelho (ou Verde vs Laranja para daltônicos) |
| **Multicategoria** (3-6) | ColorBrewer qualitativo |
| **Gradiente** (mapa de calor) | Azul → Branco → Vermelho (divergente) ou Branco → Azul (sequencial) |

## Cores para Mapas de Calor

```
Sequencial (baixo → alto):
#F7FBFF → #DEEBF7 → #C6DBEF → #9ECAE1 → #6BAED6 → #4292C6 → #2171B5 → #084594
(branco → azul escuro)

Divergente (negativo → neutro → positivo):
#B2182B → #D6604D → #F4A582 → #FDDBC7 → #F7F7F7 → #D1E5F0 → #92C5DE → #4393C3 → #2166AC
(vermelho → branco → azul)
```

## Regras de Ouro

| Regra | Por quê |
|---|---|
| **1 destaque por gráfico** | Mais que isso = nada é destacado |
| **Resto em cinza** | Neutro permite contraste sem competir |
| **Evite arco-íris** | Cores demais = informação demais = confusão |
| **Teste em preto e branco** | Impressão pode ser sem cor |
| **Teste para daltonismo** | 8% dos homens têm daltonismo vermelho-verde |
| **Consistência** | Mesma cor = mesma categoria em toda a apresentação |
| **Contraste** | Texto escuro em fundo claro (ou vice-versa) |

## Ferramentas Recomendadas

| Ferramenta | Para quê | Link |
|---|---|---|
| **ColorBrewer** | Paletas seguras para mapas | colorbrewer2.org |
| **Coolors** | Gerar paletas rápidas | coolors.co |
| **WebAIM Contrast** | Verificar contraste | webaim.org/resources/contrastchecker |
| **Viz Palette** | Verificar como daltônicos veem | projects.susielu.com/viz-palette |
| **Adobe Color** | Paletas baseadas em harmonia | color.adobe.com |
