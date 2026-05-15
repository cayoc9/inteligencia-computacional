# Princípio 1: Entenda o Contexto

> **"O sucesso na visualização de dados não começa com a visualização de dados."** — Cole Knaflic

## O Conceito

Antes de criar qualquer gráfico ou slide, você precisa responder duas perguntas fundamentais:

1. **Quem** é seu público?
2. **O que** você precisa que ele **saiba ou faça**?

Só depois disso você pensa nos dados.

## Por Que Isso Importa

### Análise Exploratória vs Explanatório

| Tipo | O que é | Quando usar |
|---|---|---|
| **Exploratória** | Você vasculha dados para encontrar insights | Na sua análise, nunca na apresentação |
| **Explanatória** | Você mostra os insights encontrados | Na apresentação para o público |

**Erro comum:** Mostrar análise exploratória (todas as 100 ostras) em vez de explanatória (as 2 pérolas encontradas). Seu público não precisa ver todo o trabalho — precisa ver o resultado.

### Carga Cognitiva

Cada elemento adicionado a um slide consome poder de processamento mental do seu público. Se você não definir o contexto primeiro, corre o risco de:

- Mostrar informação irrelevante
- Perder a atenção do público
- Não conseguir transmitir a mensagem principal

## Como Aplicar

### 1.1 Quem é seu público?

Quanto mais específico, melhor. Evite "interessados internos e externos".

**Perguntas para se fazer:**
- Qual é o cargo/função do meu público?
- Qual o nível de conhecimento técnico?
- O que eles já sabem sobre o assunto?
- Eles são favoráveis ou céticos à minha mensagem?
- Qual a relação deles comigo (especialista, colega, subordinado)?

**Exemplo (Trabalho 1):**
```
Público: Professor da disciplina IC + banca avaliadora
Nível técnico: Alto (especialistas em ML)
Contexto: Sabem que é um trabalho de comparação RF vs RN
Atitude: Avaliadores, buscam profundidade técnica + clareza na comunicação
```

### 1.2 O que precisa que eles saibam ou façam?

Defina a **ação** que você quer provocar.

**Verbos de ação (Knaflic):**
aprovar | acreditar | apoiar | autorizar | concordar | contratar | decidir | financiar | implementar | investir | mudar | persuadir | recomendar

**Regra de ouro:** Se você não consegue articular o que quer que seu público faça em 1 frase, você não está pronto para criar conteúdo.

**Exemplo (Trabalho 1):**
```
Ação: "Reconhecer que a Random Forest superou a Rede Neural em dados tabulares,
e aprovar a entrega do relatório comparativo como trabalho final"
```

### 1.3 Mecanismo de comunicação

| Mecanismo | Controle sobre o público | Nível de detalhe necessário |
|---|---|---|
| **Apresentação ao vivo** | Alto (você dita o ritmo) | Baixo (você responde perguntas) |
| **Documento escrito** | Baixo (público lê no seu ritmo) | Alto (precisa ser auto-explicativo) |
| **Vídeo gravado** | Médio | Médio |
| **E-mail** | Baixo | Alto |

**Slidemento:** Tentar fazer um único material que sirva tanto para apresentação ao vivo quanto para leitura. Evite se possível. Se inevitável, priorize o formato principal e adicione notas de apoio.

### 1.4 Tom

| Tom | Quando usar | Implicações visuais |
|---|---|---|
| **Comemorativo** | Resultados positivos | Cores vibrantes, gráficos de sucesso |
| **Urgente** | Problema a resolver | Contraste alto, destaque para o problema |
| **Sério** | Assunto delicado | Cores neutras, tons mais baixos |
| **Informativo** | Relatório de andamento | Equilíbrio, sem exageros |

## A História de 3 Minutos e a Grande Ideia

### História de 3 Minutos

Se você tivesse **3 minutos** para dizer ao seu público o que ele precisa saber, o que diria?

**Exemplo (Trabalho 1):**
> "Neste trabalho comparamos Random Forest e Redes Neurais na classificação de saúde do sono. Usamos um dataset de 100 mil registros com 32 features. A Random Forest alcançou 74,15% de acurácia contra 73,23% da Rede Neural — e mesmo após otimização, a RN não superou a RF. Isso é consistente com a literatura: para dados tabulares, modelos baseados em árvore tendem a superar redes neurais. O melhor modelo geral foi o HistGradientBoosting com 74,25% e AUC de 82,58%. Concluímos que para este problema, a RF é a melhor escolha: performance similar à RN com muito menos complexidade."

### Grande Ideia

Reduza sua mensagem a **uma única frase** com 3 componentes (Nancy Duarte):

1. **Ponto de vista único**
2. **O que está em jogo**
3. **Frase completa**

**Exemplo (Trabalho 1):**
> "A Random Forest é a melhor escolha para classificar saúde do sono em dados tabulares, superando Redes Neurais com performance similar e complexidade muito menor, o que reforça que modelo mais simples é a melhor opção para este tipo de problema."

## O Storyboard

**Nunca comece com PowerPoint/Google Slides.** Comece com:

1. **Notas adesivas** (post-its) — uma ideia por nota
2. **Papel e caneta** — rabisque a estrutura
3. **Quadro branco** — visualize o fluxo

**Por quê:** É fácil descartar uma nota adesiva. É doloroso deletar um slide que levou 1 hora para fazer.

### Exemplo de Storyboard (Trabalho 1)

```
[Slide 1] Título: Comparação RF vs RN em Saúde do Sono
[Slide 2] Contexto: Dataset de 100k registros, 32 features
[Slide 3] Metodologia: Split estratificado, random_state=42
[Slide 4] Random Forest: 74.15% accuracy, GridSearchCV
[Slide 5] Rede Neural: 73.23% base → 74% otimizada
[Slide 6] Comparação: Gráfico de barras das 6 métricas
[Slide 7] Threshold Tuning: 0.35 maximiza F1
[Slide 8] Conclusão: RF > RN para dados tabulares
[Slide 9] Ação: Relatório aprovado
```

## Checklist

- [ ] Público específico identificado (cargo, nível técnico, contexto)
- [ ] Ação desejada articulada em 1 frase clara
- [ ] Mecanismo de comunicação definido (ao vivo/documento)
- [ ] Tom estabelecido (comemorativo, urgente, sério, informativo)
- [ ] História de 3 minutos escrita e testada em voz alta
- [ ] Grande Ideia reduzida a 1 frase
- [ ] Storyboard criado (em papel ou post-its)
- [ ] Storyboard aprovado pelo solicitante (se aplicável)

## Erros Comuns

| Erro | Correção |
|---|---|
| "Meu público é todo mundo" | Escolha o tomador de decisão principal |
| Mostrar análise exploratória | Selecione apenas os insights finais |
| Slide cheio de dados "por via das dúvidas" | Coloque detalhes no apêndice |
| Sem ação definida | Pergunte: "E daí? O que faço com isso?" |
| Começar pelo PowerPoint | Use post-its ou papel primeiro |
