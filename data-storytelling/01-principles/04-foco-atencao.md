# Princípio 4: Foque a Atenção do Seu Público

> **"Onde você quer que seu público olhe primeiro? E depois? E depois?"** — Cole Knaflic

## O Conceito

Seu público não processa tudo em um gráfico ao mesmo tempo. Os olhos são atraídos por estímulos específicos. Você pode — e deve — controlar essa atenção.

## Por Que Isso Importa

### Atributos Pré-Atentivos

O cérebro processa certos atributos visuais **antes mesmo da atenção consciente**. Em menos de 250 milissegundos, seu público já identificou:

| Atributo | O que comunica |
|---|---|
| **Cor** (destaque) | "Isto é importante" |
| **Tamanho** (maior) | "Isto tem mais magnitude" |
| **Posição** (topo/esquerda) | "Comece por aqui" |
| **Intensidade** (mais escuro) | "Isto tem mais peso" |
| **Orientação** (diferente) | "Isto é diferente" |

### Como Funciona na Prática

1. O público olha para o slide
2. Em <0.25s, os atributos pré-atentivos guiam o olhar
3. Se tudo tem o mesmo destaque, **nada tem destaque**
4. Se você não controla a atenção, o público se perde

## Como Aplicar

### 4.1 Use cor com estratégia

**Regra de ouro:** Apenas **1-2 elementos** devem ter cor. O resto fica em cinza.

**Exemplo (Trabalho 1):**
Em um gráfico de barras comparando RF, RN e HistGradientBoosting:
- RF em cinza claro
- RN em cinza claro
- **HistGradientBoosting em azul escuro** (destaque)
- Título: "HistGradientBoosting: melhor AUC (82.58%)"

**Resultado:** O olhar vai imediatamente para a barra azul.

### 4.2 Crie hierarquia visual

Nem toda informação tem a mesma importância. Crie níveis:

```
Nível 1 (Título/Mensagem principal) → Maior, negrito, cor forte
Nível 2 (Dados principais) → Tamanho normal, destaque sutil
Nível 3 (Contexto/Dados secundários) → Cinza, menor, sem destaque
Nível 4 (Eixos/Bordas/Fonte) → Cinza claro, mínimo
```

**Nunca** use o mesmo peso visual para tudo.

### 4.3 Posicione estrategicamente

**Padrão de leitura:** O público começa no canto superior esquerdo e faz "Z" com os olhos.

- Coloque a mensagem principal no **topo ou início**
- Elementos mais importantes no **canto superior esquerdo**
- Informações de suporte na **sequência natural de leitura**

### 4.4 Use tamanho para mostrar magnitude

O maior elemento visual = a informação mais importante.

**Exemplo:**
- Título do slide: 36pt
- Mensagem principal: 28pt  
- Números de destaque: 24pt
- Eixos e fontes: 10-12pt

### 4.5 Dê e tire ênfase

**Para dar ênfase:**
- Cor vibrante (em meio a cinza)
- Fonte maior ou mais pesada (bold)
- Posição de destaque (canto superior esquerdo ou centro)
- Anotação/destaque direto

**Para tirar ênfase:**
- Cinza claro
- Fonte menor
- Posição periférica
- Opacidade reduzida

### 4.6 Use anotações para guiar

**Bom:** "Aqui está o ponto principal"
**Melhor:** Seta + "AUC subiu 6% com threshold 0.35"
**Excelente:** Marcação direta no gráfico + texto explicativo + seta apontando

## Exemplo Antes/Depois (Trabalho 1)

**Antes (sem foco):**
Gráfico de barras com 3 modelos, todas as barras na mesma cor azul, mesmo peso visual, sem destaque para o melhor.

**Depois (com foco):**
- Cinza para RF e RN
- Azul escuro para HistGradientBoosting
- Rótulo "Melhor AUC (82.58%)" sobre a barra destacada
- Título: "HistGradientBoosting lidera em ROC AUC"
- Seta sutil apontando para a barra

**Resultado:** Em 0.25s o público sabe qual modelo é o melhor e por quê.

## Checklist

- [ ] 1-2 elementos têm cor; o resto está em cinza/neutro
- [ ] Há hierarquia visual clara (título > dados > contexto > bordas)
- [ ] Posição do elemento mais importante segue padrão de leitura
- [ ] Tamanhos refletem importância (maior = mais importante)
- [ ] Anotações guiam o olhar (setas, rótulos, destaques)
- [ ] Se eu remover a cor, a mensagem ainda fica clara? (apenas com cinza)
- [ ] Testei com alguém: para onde ela olhou primeiro?

## Erros Comuns

| Erro | Correção |
|---|---|
| Arco-íris de cores sem propósito | 1 cor de destaque, resto cinza |
| "Deixei tudo colorido para chamar atenção" | Nada chama atenção se tudo chama |
| Fonte 8pt em tudo "para caber" | Hierarquia: grande para importante, pequeno para detalhe |
| Destaque no lugar errado | Pergunte: o que é mais importante? |
| Sem anotações no gráfico | Coloque setas + texto nos pontos-chave |
