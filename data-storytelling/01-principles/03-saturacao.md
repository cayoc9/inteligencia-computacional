# Princípio 3: Elimine a Saturação

> **"Cada elemento adicionado a uma página ou tela absorve carga cognitiva do seu público."** — Cole Knaflic

## O Conceito

Imagine uma página em branco. Cada elemento que você adiciona — uma linha, uma cor, um rótulo, uma borda — consome poder de processamento mental do seu público.

**Saturação** é tudo que ocupa espaço mas não acrescenta informação. Seu trabalho: identificar e remover.

## Por Que Isso Importa

### Carga Cognitiva

O cérebro humano tem **poder de processamento finito**. Sempre que seu público precisa decifrar um elemento visual confuso, ele gasta recursos mentais que deveriam ser usados para entender sua mensagem.

### Data-Ink Ratio (Edward Tufte)

```
data-ink ratio = tinta dedicada aos dados ÷ tinta total do gráfico
```

**Quanto maior, melhor.** Maximize a proporção de tinta que realmente informa.

### Relação Sinal-Ruído (Nancy Duarte)

- **Sinal:** A informação que você quer comunicar
- **Ruído:** Elementos que atrapalham ou distraem

Maximize o sinal. Minimize o ruído.

## Como Aplicar

### 3.1 Remova bordas e linhas desnecessárias

**Antes:**
Tabela com bordas grossas em todas as células, linhas de grade escuras, moldura grossa ao redor do gráfico.

**Depois:**
Remova bordas ou torne-as cinza claro. Use espaçamento. Remova moldura do gráfico.

**Regra:** Se uma borda não ajuda a legibilidade, remova.

### 3.2 Remova efeitos decorativos

**Remova sempre:**
- Sombras
- Gradientes
- Relevo 3D
- Brilhos/reflexos
- Clip-art
- Logos grandes e repetitivos

**Regra:** Se não informa, é ruído.

### 3.3 Remova redundância

Eixo Y + legenda de dados no mesmo gráfico geralmente é redundante.

**Decisão:**
- Se o **valor exato** importa → mostre a legenda, remova o eixo
- Se a **tendência** importa → mantenha o eixo (em cinza), remova legendas

### 3.4 Simplifique cores

**Regra:** Se a cor não tem função, remova. Cores devem sempre ter um propósito.

**Exemplo:** Em vez de 6 cores diferentes para 6 barras, use 1 cor neutra para todas + 1 cor de destaque para a barra mais importante.

### 3.5 Use espaço em branco estrategicamente

Espaço em branco não é "espaço vazio" — é **espaço de respiro**. Use para:
- Separar seções
- Agrupar elementos relacionados
- Guiar o olhar do público

### 3.6 Aplique os Princípios da Gestalt

| Princípio | O que significa | Aplicação em gráficos |
|---|---|---|
| **Proximidade** | Elementos próximos parecem relacionados | Coloque rótulos perto dos dados |
| **Similaridade** | Elementos similares parecem do mesmo grupo | Mesma cor = mesma categoria |
| **Fechamento** | Tendemos a completar formas | Use espaço para criar grupos implícitos |
| **Figura-Fundo** | Separamos elementos em primeiro e segundo plano | Dados em destaque, bordas em segundo plano |

## Exemplo Antes/Depois

**Antes (gráfico saturado):**
- Moldura preta grossa
- Linhas de grade em todas as direções
- 6 cores diferentes (arco-íris)
- Fundo cinza com gradiente
- Borda 3D nas barras
- Eixo Y com muitas marcações
- Título em negrito sublinhado
- Logo grande no canto

**Depois (gráfico limpo):**
- Sem moldura
- Linhas de grade sutis (cinza, só horizontais)
- 1 cor neutra + 1 destaque
- Fundo branco
- Barras 2D simples
- Eixo Y em cinza, marcações mínimas
- Título direto, sem formatação excessiva
- Logo pequeno ou ausente

**Resultado:** O público vê os dados em <3 segundos, não os elementos decorativos.

## Checklist

- [ ] Todas as bordas e linhas têm função ou podem ser removidas/clairificadas?
- [ ] Não há efeitos decorativos (sombra, 3D, gradiente, brilho)?
- [ ] Cores são usadas com propósito (não decorativas)?
- [ ] Eixo e legendas de dados não são redundantes?
- [ ] Espaço em branco está presente e é usado para organizar?
- [ ] Princípios da Gestalt aplicados (proximidade, similaridade, fechamento)?
- [ ] Se eu remover este elemento, a informação se perde ou melhora?
- [ ] Meu gráfico é compreensível em <5 segundos?

## Erros Comuns

| Erro | Correção |
|---|---|
| "Mais informações = mais profissional" | Menos é mais. Cada elemento extra reduz o foco. |
| Borda preta grossa no gráfico | Remova ou torne cinza claro |
| "Precisa ser bonito" (com decoração) | Dados limpos são intrinsecamente bonitos |
| Manter linhas de grade padrão da ferramenta | Questione cada linha: ela ajuda? |
| Mesma ênfase para tudo | Nem tudo é importante. Hierarquize. |

> **Teste prático:** Pegue seu gráfico e remova um elemento. A informação ainda está clara? Então mantenha removido. Repita até que remover algo piore a comunicação.
