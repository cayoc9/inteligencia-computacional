# Princípio 2: Escolha um Visual Eficaz

> **"Existem muitos tipos de gráficos, mas alguns poucos funcionarão para a maioria das suas necessidades."** — Cole Knaflic

## O Conceito

O tipo de gráfico certo reduz o esforço mental do público para entender os dados. O gráfico errado — por mais bonito que seja — destrói a comunicação.

## Por Que Isso Importa

- **Tabelas** interagem com o sistema **verbal** (lemos, processamos devagar)
- **Gráficos** interagem com o sistema **visual** (vemos, processamos rápido)

Um gráfico bem projetado comunica mais rápido que uma tabela bem projetada.

## Os Tipos que Você Precisa Conhecer

### Texto Simples

**Quando usar:** Apenas 1 ou 2 números para comunicar.

**Exemplo:** "20% dos filhos tinham mães que ficavam em casa em 2012, contra 41% em 1970."

**Não faça:** Colocar 2 números em um gráfico cheio de eixos e legendas. Use o número direto.

### Tabela

**Quando usar:** Público misto, cada um procura sua linha de interesse, múltiplas unidades de medida.

**Regras:**
- Bordas claras ou espaçamento, nunca linhas grossas
- Dados em primeiro plano, bordas em segundo
- Em apresentações ao vivo: **evite tabelas**. O público lê e para de te ouvir.

**Exemplo (Trabalho 1):**

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---|---|---|---|---|
| Random Forest | 0.7415 | 0.6528 | 0.6999 | 0.6756 | 0.8218 |
| Rede Neural | 0.7323 | 0.6400 | 0.6800 | 0.6600 | 0.8100 |
| HistGradientBoosting | **0.7425** | **0.6787** | 0.6453 | 0.6616 | **0.8258** |

### Mapa de Calor

**Quando usar:** Muitos números em formato tabular, quer destacar magnitudes.

**Como fazer:** Use saturação de cor para guiar os olhos. Mais escuro = maior valor.

**Regra:** Sempre inclua legenda.

### Gráfico de Linhas

**Quando usar:** Dados contínuos, especialmente **séries temporais**.

**Regra de ouro:** Intervalos consistentes no eixo X. Não misture décadas com anos no mesmo gráfico.

**Variações:**
- **Linha simples:** 1 série de dados ao longo do tempo
- **Múltiplas linhas:** Comparação entre séries (cuidado com o "gráfico espaguete")
- **Linha + intervalo:** Mostrar média + faixa (mín/máx, desvio padrão)

**Exemplo (Trabalho 1):** Curvas ROC dos modelos — linha para RF, RN e HistGradientBoosting no mesmo gráfico.

### Gráfico de Inclinação

**Quando usar:** Comparar **2 pontos no tempo** para várias categorias. Mostra aumento/diminuição relativa.

**Vantagem:** Transmite direção e magnitude da mudança em um único visual compacto.

**Cuidado:** Se muitas linhas se sobrepõem, destaque 1 série por vez.

### Gráfico de Barras Verticais

**Quando usar:** Dados categóricos, comparar magnitudes entre categorias.

**Regra ABSOLUTA:** Linha de base **SEMPRE em zero**. (Eixo Y começa em 0. Não engane seu público.)

**Variações:**
- **Simples:** 1 série
- **Agrupadas:** 2+ séries (máximo 3-4 séries, depois fica confuso)
- **Empilhadas:** Mostrar total + partes (só a série inferior é facilmente comparável)

**Exemplo (Trabalho 1):** Barras agrupadas com as 6 métricas para RF, RN e HistGradientBoosting — 3 cores, 6 grupos de barras.

### Gráfico de Cascata

**Quando usar:** Decompor um total em suas partes. Mostrar ponto inicial + acréscimos + reduções = ponto final.

**Exemplo:** Nº de funcionários: início do ano → contratações → transferências de entrada → saídas → perda de pessoal = final do ano.

**No Excel:** Use barras empilhadas com uma série invisível (força bruta).

### Gráfico de Barras Horizontais

**Quando usar:** Categorias com nomes longos, comparação de rankings.

**Por que é o melhor:** A leitura natural (esquerda→direita, cima→baixo) faz com que os nomes das categorias sejam lidos antes dos dados. Mais fácil que barras verticais.

**Ordenação:** Sempre ordene (maior para menor ou vice-versa), a menos que haja ordem natural.

**Exemplo (Trabalho 1):** Feature importance — barras horizontais ordenadas da feature mais importante para a menos importante.

### Gráfico de Barras Horizontais Empilhadas 100%

**Quando usar:** Partes de um todo, especialmente escalas Likert (discordo totalmente → concordo totalmente).

**Vantagem:** Linha de base coerente nas duas extremidades.

### Gráfico de Dispersão

**Quando usar:** Mostrar relação entre 2 variáveis (X e Y).

**Exemplo (Trabalho 1):** Dispersão entre sleep_quality e felt_rested, destacando os pontos onde o modelo errou.

### Gráfico de Área Quadrada

**Quando usar:** Comparar magnitudes muito diferentes (ex: 1 milhão vs 10 bilhões).

**Como funciona:** Usa altura + largura (2 dimensões) para caber números de ordens muito diferentes.

## O que EVITAR (Sempre)

| Visual | Problema |
|---|---|
| **Gráfico de Pizza** | Olho humano não compara ângulos/áreas bem. Use barras horizontais. |
| **Gráfico de Rosca** | Olho humano não compara arcos. Pior que pizza. |
| **3D** | Distorce a percepção. A altura da barra não é mais confiável. |
| **Eixo Y secundário** | Difícil de ler, induz a falsas correlações. Legende diretamente ou separe em 2 gráficos. |

## Árvore de Decisão Rápida

```
1-2 números?                    → TEXTO SIMPLES
Dados tabulares, várias linhas? → TABELA ou MAPA DE CALOR
Série temporal?                 → LINHAS (ou INCLINAÇÃO se só 2 pontos)
Comparar categorias?            → BARRAS HORIZONTAIS (ordenadas)
Comparar ao longo do tempo?     → BARRAS VERTICAIS
Decompor um total?              → CASCATA
Partes de um todo?              → BARRAS EMPILHADAS 100%
Relação entre 2 variáveis?      → DISPERSÃO
Magnitudes muito diferentes?    → ÁREA QUADRADA
```

## Exemplo Antes/Depois (Trabalho 1)

**Antes (tabela densa em slide ao vivo):**
Tabela com 6 métricas × 3 modelos + desvios padrão + p-values + notas de rodapé

**Depois (gráfico de barras agrupadas):**
Barras agrupadas com 6 grupos (uma por métrica), 3 cores por grupo, destaque para RF nas métricas principais.

**Por que funciona:** O público vê imediatamente que RF e HistGradientBoosting estão próximos, e ambos superam a RN base. A mensagem é clara sem ler números.

## Checklist

- [ ] Tipo de gráfico adequado aos dados (não apenas ao gosto pessoal)
- [ ] Linha de base zero em gráficos de barras
- [ ] 3D, pizza, rosca, eixo Y secundário — nenhum deles presente
- [ ] Cores usadas com intenção (não apenas decorativas)
- [ ] Categorias ordenadas logicamente (valor, ordem natural)
- [ ] Gráfico legível em preto e branco (impressão)
- [ ] Testei com um colega: ele entendeu a mensagem em <5 segundos?

## Erros Comuns

| Erro | Correção |
|---|---|
| Pizza "para variar" | Barras horizontais |
| 3D "para ficar bonito" | 2D simples, cores estratégicas |
| Tabela em apresentação ao vivo | Gráfico ou texto simples |
| Muitas séries no mesmo gráfico | Separe em 2-3 gráficos focados |
| Eixo Y truncado para "enfatizar" | Mantenha zero, use texto para destacar |
