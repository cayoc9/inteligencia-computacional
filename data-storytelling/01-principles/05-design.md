# Princípio 5: Pense Como um Designer

> **"A forma segue a função."** — Louis Sullivan (arquiteto)

## O Conceito

Design não é sobre "deixar bonito". Design é sobre **funcionar bem**. No contexto de dados:

- **Função:** O que você quer que seu público **faça** com a informação
- **Forma:** A aparência que permite que isso aconteça **com facilidade**

## Por Que Isso Importa

### Affordances (Reconhecimento de Funcionalidades)

Um bom design comunica como deve ser usado sem precisar de instruções. Um botão parece clicável. Uma barra parece comparável.

**Aplicação em gráficos:**
- Barras parecem comparáveis (linha de base zero)
- Linhas parecem contínuas (dados temporais)
- Cores contrastam quando devem se destacar

### Acessibilidade

Seu público inclui pessoas com diferentes capacidades. Design inclusivo não é opcional.

**Mínimo:**
- Contraste suficiente (preto/branco, não amarelo claro/branco)
- Legível em preto e branco (impressão, fotocópia)
- Sem dependência exclusiva de cor para transmitir informação
- Tamanho de fonte adequado (12pt+ para corpo, 18pt+ para slides)

### Estética Funcional

Gráficos limpos e organizados transmitem **confiança**. Gráficos bagunçados transmitem **desleixo**, mesmo que os dados estejam corretos.

## Como Aplicar

### 5.1 Forma segue função

Antes de criar, pergunte:

1. Qual é **a única coisa** que quero que meu público tire deste gráfico?
2. Que tipo de gráfico comunica isso mais rapidamente?
3. Que elementos visuais reforçam (ou atrapalham) essa comunicação?

**Exemplo (Trabalho 1):**
> **Função:** Mostrar que a RF e o HistGradientBoosting têm performance similar, e ambos superam a RN.
> **Forma:** Barras agrupadas com RF e HistGB em cores similares (tons de azul) e a RN em cinza — indicando visualmente que RF e HistGB estão no mesmo grupo.

### 5.2 Acessibilidade

**Contraste:**
- Texto escuro sobre fundo claro (ou vice-versa)
- Nunca texto claro sobre fundo claro
- Ferramenta: WebAIM Contrast Checker

**Daltonismo:**
- 8% dos homens têm daltonismo (vermelho-verde)
- Use texturas ou padrões além de cor
- Paletas seguras: ColorBrewer, viridis, cividis

**Fonte:**
- Mínimo 12pt para corpo de texto
- Mínimo 18pt para slides
- Fontes sem serifa (Arial, Helvetica, Open Sans) para telas
- Fontes com serifa (Georgia, Times) para impressão

### 5.3 Equilíbrio e Proporção

- Centralize o elemento principal ou posicione seguindo a regra dos terços
- Distribua o peso visual: não concentre tudo em um canto
- Espaço em branco faz parte do design (não é "espaço vazio")

### 5.4 Consistência

- Mesma paleta de cores em toda a apresentação
- Mesmo estilo de gráfico (barras sempre do mesmo jeito)
- Mesma fonte para elementos similares
- Mesmo formato de número (2 casas decimais ou inteiro, não misture)

### 5.5 Obtenha Aceitação (Feedback)

**Estratégia para receber feedback útil:**

1. Mostre para um colega
2. Peça: "O que você entendeu deste gráfico?"
3. **Não** pergunte: "Está bonito?"
4. Observe: para onde ele olha primeiro? O que ele pergunta?

**Se ele entendeu a mensagem:** o design funcionou.  
**Se ele se confundiu:** revise o design antes dos dados.

## Checklist

- [ ] Função claramente definida antes de criar a forma
- [ ] Contraste suficiente entre texto e fundo
- [ ] Funciona em preto e branco (impressão)
- [ ] Não depende só de cor (uso de texto ou padrões)
- [ ] Consistência visual em toda a apresentação
- [ ] Espaço em branco está presente e equilibrado
- [ ] Testei com 1 colega: ele entendeu a mensagem?
- [ ] Fonte legível no formato final (tela, projetor, papel)

## Erros Comuns

| Erro | Correção |
|---|---|
| "Design é só estética" | Design é função primeiro, estética depois |
| Ignorar daltonismo | Use paletas seguras + texturas |
| Fonte 8pt "para caber tudo" | Priorize. Se não cabe, não é importante. |
| Estilos diferentes em cada slide | Crie um template/guia de estilo |
| Mudar cor sem motivo | Cor sempre tem propósito |
