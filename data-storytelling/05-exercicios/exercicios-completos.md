# Exercícios Práticos

> Pratique cada princípio com exercícios baseados em situações reais.

## Exercício 1: Contexto

**Cenário:** Você precisa apresentar os resultados do Trabalho 1 para dois públicos diferentes:
1. **Público A:** Professor da disciplina (especialista em ML)
2. **Público B:** Um colega de outra área que nunca viu ML

**Tarefa:**
- Escreva a Grande Ideia para cada público
- Escreva a História de 3 Minutos para cada público
- Liste as diferenças na abordagem (o que muda? o que mantém?)

**Gabarito (reflexão):**
- Para o professor: foque em métricas, arquitetura dos modelos, insights técnicos
- Para o colega: foque no problema, no resultado principal, evite jargão
- O que mantém: a conclusão (RF > RN)
- O que muda: profundidade técnica, vocabulário, ênfase

## Exercício 2: Visual Eficaz

**Cenário:** Você tem os seguintes dados para comunicar:

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---|---|---|---|---|
| RF | 0,7415 | 0,6528 | 0,6999 | 0,6756 | 0,8218 |
| RN Base | 0,7323 | — | — | — | — |
| RN Otimizada | ~0,74 | — | — | — | — |
| HistGB | 0,7425 | 0,6787 | 0,6453 | 0,6616 | 0,8258 |

**Tarefa:**
- Desenhe (conceitualmente) 3 opções de gráfico diferentes para esses dados
- Para cada opção, anote: vantagem, desvantagem, qual mensagem ela comunica primeiro
- Escolha a melhor opção e justifique

**Opções a considerar:**
1. Barras agrupadas (6 métricas × 4 modelos)
2. Barras horizontais (1 métrica por gráfico, vários gráficos)
3. Tabela com mapa de calor
4. Barras empilhadas 100%

## Exercício 3: Saturação

**Cenário:** O gráfico abaixo (descrito textualmente) precisa ser simplificado.

```
Gráfico atual:
- Moldura preta grossa ao redor
- Linhas de grade horizontais e verticais (escuras)
- Fundo cinza com gradiente
- 12 cores diferentes (uma para cada barra)
- Borda 3D em cada barra
- Eixo Y com marcações a cada 0,5
- Título "Gráfico 1: Comparação"
- Legenda grande no canto inferior direito
- Logo grande no canto superior direito
- Nota de rodapé com fonte em 8pt
```

**Tarefa:**
- Liste cada elemento e classifique como: **Sinal** (informa) ou **Ruído** (saturação)
- Para cada elemento classificado como ruído, decida: remover ou suavizar?
- Descreva a versão final simplificada

**Gabarito (parcial):**
- Moldura grossa → remover
- Linhas de grade verticais → remover; horizontais → cinza claro
- Fundo gradiente → branco sólido
- 12 cores → 1 cor neutra + 1 destaque
- Borda 3D → remover
- Eixo Y → menos marcações, em cinza
- Título → "RF lidera em 4 das 6 métricas"
- Legenda → direto nas barras ou remover se auto-explicativo
- Logo → pequeno e discreto ou no slide de abertura
- Nota de rodapé → fonte maior (10-12pt) ou mover para apêndice

## Exercício 4: Foco

**Cenário:** Você tem um gráfico de barras com 3 modelos (RF, RN, HistGB) e 6 métricas. O ponto principal é: "RF e HistGB têm performance similar, RN fica atrás."

**Tarefa:**
- Descreva como você usaria cor para guiar a atenção
- Descreva onde colocaria anotações
- Escreva o título do gráfico
- Como você ordenaria as barras?

**Reflexão:**
- RF e HistGB em tons similares (ex: azul médio e azul escuro)
- RN em cinza
- Anotação: seta + "RF: melhor equilíbrio" sobre as barras de RF
- Título: "RF e HistGB lideram; RN fica ~1% atrás"
- Ordenação: HistGB, RF, RN (do melhor para o pior)

## Exercício 5: Design

**Cenário:** Você está criando a apresentação do Trabalho 1. O template do slide está todo em azul claro com texto branco.

**Tarefa:**
- Identifique problemas de contraste
- Sugira uma paleta de cores alternativa
- Verifique se a paleta funciona para daltônicos
- Proponha 3 regras de consistência para toda a apresentação

**Gabarito parcial:**
- Problema: texto branco em azul claro tem contraste insuficiente
- Paleta alternativa: fundo branco, texto #333333, destaque #2166AC
- Daltonismo: evite vermelho+verde; use azul+laranja
- Regras: mesma fonte (sem serifa), mesma paleta, gráficos sempre 2D

## Exercício 6: Storytelling

**Cenário:** Usando os resultados do Trabalho 1, crie uma apresentação completa em 3 atos.

**Tarefa:**
- Escreva a Grande Ideia
- Crie um storyboard de 9 slides
- Escreva a História de 3 Minutos
- Liste as 3 perguntas mais difíceis e prepare respostas
- Pratique em voz alta e cronometre

**Entregáveis esperados:**
1. Grande Ideia em 1 frase
2. Storyboard com 9 post-its
3. Texto de 3 minutos (~450 palavras)
4. 3 perguntas + respostas preparadas
