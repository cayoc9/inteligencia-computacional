# Exemplo: Storytelling Aplicado ao Trabalho 1

> Este documento mostra como aplicar os **6 princípios de storytelling com dados** ao seu projeto de classificação RF vs RN.

## 1. Contexto (Princípio 1)

### Público
**Professor da disciplina IC + banca avaliadora**

- Nível técnico: Alto (especialistas em Machine Learning)
- Contexto: Sabem que é um trabalho de comparação RF vs RN
- Atitude: Avaliadores — buscam profundidade técnica + clareza na comunicação
- O que está em jogo: Nota do trabalho, demonstração de domínio do conteúdo

### Ação Desejada
> "Reconhecer que a Random Forest superou a Rede Neural em dados tabulares de saúde do sono, e aprovar a entrega como trabalho final da disciplina."

### Mecanismo
Apresentação ao vivo (15 min) + relatório escrito

### Tom
Informativo-técnico, com momentos de insight para engajar

## 2. Visual Eficaz (Princípio 2)

### Gráficos Escolhidos

| Dado | Gráfico | Justificativa |
|---|---|---|
| 6 métricas × 3 modelos | Barras agrupadas | Comparação direta entre modelos |
| Curvas ROC | Linhas (3 séries) | Mostrar trade-off TP × FP |
| Feature importance | Barras horizontais | Nomes longos, ranking claro |
| Threshold tuning | Linhas (F1 × threshold) | Mostrar ponto ótimo |
| Matriz de confusão | Mapa de calor | Destacar acertos/erros |
| Distribuição do target | Barras verticais | Mostrar desbalanceamento |

## 3. Eliminação de Saturação (Princípio 3)

**Antes:** Tabela densa com todas as 6 métricas, desvios padrão, p-values, notas de rodapé, linhas de grade, bordas, 6 cores diferentes.

**Depois:** Barras agrupadas limpas, 1 cor de destaque (azul para o melhor), cinza para os demais, sem bordas, título descritivo.

**O que foi removido:**
- Linhas de grade → apenas 3 horizontais sutis
- Bordas das barras → sem borda
- Cores múltiplas → 1 destaque + 2 neutras
- Eixo Y redundante → legendas nos dados
- Moldura do gráfico → removida
- Notas de rodapé → apêndice

## 4. Foco da Atenção (Princípio 4)

**Hierarquia visual da apresentação:**

```
Nível 1: Título do slide → 36pt, negrito, cor escura
Nível 2: Mensagem principal → 28pt, destaque azul
Nível 3: Números relevantes → 20pt, no gráfico
Nível 4: Rótulos de eixos → 12pt, cinza
Nível 5: Notas e fontes → 10pt, cinza claro
```

**Uso de cor:**
- **Azul escuro (#2166AC):** Melhor modelo em cada métrica
- **Cinza claro (#B3B3B3):** Demais modelos (contexto)
- **Vermelho (#B2182B):** Threshold problemático (0.5) — para contraste
- **Verde (#1B9E77):** Threshold otimizado (0.35) — para sucesso

## 5. Design (Princípio 5)

### Paleta
``` 
Fundo: branco
Texto principal: #333333
Destaque: #2166AC
Secundário: #B3B3B3
Alerta: #B2182B
Sucesso: #1B9E77
```

### Regras de Consistência
1. Todos os gráficos em 2D (sem 3D em hipótese alguma)
2. Barras sempre com linha de base zero
3. Fonte sem serifa (Arial/Helvetica) em toda a apresentação
4. Mesmo formato de número: 4 casas decimais para métricas (ex: 0.7415)

## 6. Storytelling (Princípio 6)

### Grande Ideia
> "A Random Forest superou as Redes Neurais na classificação de saúde do sono com performance similar e complexidade muito menor, confirmando que para dados tabulares a simplicidade vence — e o verdadeiro gargalo é a subjetividade do alvo, não o modelo."

### Estrutura Narrativa (3 Atos)

```
Ato 1 (25%): Contexto
  - Problema: Classificar felt_rested com dados de saúde do sono
  - Dataset: 100k registros, 32 features, 0 nulos
  - Objetivo: Comparar RF vs RN

Ato 2 (50%): Descobertas
  - RF: 74.15% accuracy, GridSearchCV
  - RN: 73.23% base → 74% otimizada
  - HistGB: 74.25% (melhor, ganho marginal)
  - Threshold: 0.35 maximiza F1 (ganho de 6%)
  - Apenas 4 features carregam 80% do sinal

Ato 3 (25%): Conclusão
  - RF > RN para dados tabulares
  - Teto do alvo: felt_rested é subjetivo
  - Recomendação: para problemas tabulares, comece com RF
```
