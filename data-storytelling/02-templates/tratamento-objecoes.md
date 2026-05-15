# Template: Tratamento de Objeções

> Prepare-se para as perguntas mais difíceis antes de apresentar.

## Método

1. Antes da apresentação, liste as **3 perguntas mais difíceis** que podem surgir
2. Para cada pergunta, prepare uma resposta baseada em dados
3. Inclua slides de apoio no apêndice, se necessário
4. Durante a apresentação, responda com confiança — ou diga "não sei, mas vou verificar"

## Template

### Pergunta Difícil 1

**Pergunta:** _________________________________________________

**Intenção por trás da pergunta (o que eles realmente querem saber):**
_________________________________________________

**Resposta preparada:**
_________________________________________________
_________________________________________________

**Dado de suporte:**
_________________________________________________

**Slide de apêndice (se aplicável):** Slide ___

### Pergunta Difícil 2

**Pergunta:** _________________________________________________

**Intenção por trás da pergunta:**
_________________________________________________

**Resposta preparada:**
_________________________________________________
_________________________________________________

**Dado de suporte:**
_________________________________________________

**Slide de apêndice (se aplicável):** Slide ___

### Pergunta Difícil 3

**Pergunta:** _________________________________________________

**Intenção por trás da pergunta:**
_________________________________________________

**Resposta preparada:**
_________________________________________________
_________________________________________________

**Dado de suporte:**
_________________________________________________

**Slide de apêndice (se aplicável):** Slide ___

## Exemplo Preenchido (Trabalho 1)

### Pergunta 1: "Por que a Rede Neural foi pior? Você fez tuning suficiente?"

**Intenção:** O avaliador quer saber se o tuning foi rigoroso ou superficial.

**Resposta:**
> "Fizemos tuning em três níveis: primeiro uma MLP base com 2 camadas densas, depois uma versão otimizada com batch normalization, dropout em duas camadas e ReduceLROnPlateau. Também testamos variações de learning rate e número de neurônios. O que observamos é que o ganho foi marginal — de 73,23% para cerca de 74%. Isso não é limitação do tuning, mas sim característica do problema: em dados tabulares com ~100k registros, modelos baseados em árvore tendem a saturar antes."

**Slide de apêndice:** Slide 10 (tabela com todas as arquiteturas testadas)

### Pergunta 2: "74% de acurácia não é baixo? O que garante que isso não é sorte?"

**Intenção:** O avaliador questiona a validade geral do resultado.

**Resposta:**
> "Usamos split estratificado com random_state=42 para garantir que a distribuição do alvo fosse preservada. Comparamos com um baseline ingênuo (classe majoritária: 61%) e com outros modelos como Logistic Regression e Extra Trees. O melhor modelo, HistGradientBoosting, teve 74,25%. Além disso, o diagnóstico de Rodada 3 mostrou que o teto de ~74% é consistente com múltiplos modelos — não é sorte de um modelo específico. A subjetividade do alvo felt_rested impõe um limite prático."

**Slide de apêndice:** Slide 11 (tabela comparativa com baseline e 5 modelos)

### Pergunta 3: "E se você tivesse usado XGBoost/LightGBM?"

**Intenção:** O avaliador quer saber se você conhece outras alternativas.

**Resposta:**
> "Testamos o HistGradientBoosting do scikit-learn, que é conceitualmente similar ao XGBoost e LightGBM. O resultado foi 74,25% — marginalmente melhor que a RF. A literatura mostra que para datasets desse porte (~100k), as diferenças entre implementações de gradient boosting são pequenas. Não testamos XGBoost ou LightGBM por restrições de dependências, mas o diagnóstico sugere que o ganho seria marginal, dado que o gargalo principal é o alvo, não o algoritmo."

**Slide de apêndice:** Slide 12 (gráfico comparando resultados por modelo)

## Dicas para Responder

| Situação | Resposta |
|---|---|
| Você sabe a resposta | Responda direto, com dado de suporte |
| Você sabe parcialmente | Responda o que sabe + "posso detalhar depois" |
| Você não sabe | "Não tenho essa informação agora, mas posso verificar e retornar" |
| Pergunta fora do escopo | "Essa é uma boa pergunta, mas está fora do escopo deste trabalho" |
| Pergunta agressiva | Mantenha calma, agradeça, responda com dados |
