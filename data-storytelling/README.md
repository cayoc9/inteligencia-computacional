# data-storytelling

> **"O poder corrompe. O PowerPoint corrompe totalmente."** — Edward Tufte

Skill de storytelling com dados baseada nos ensinamentos de **Cole Nussbaumer Knaflic** (ex-Google, autora do livro *Storytelling com Dados*).

## Como Usar

### Modo Consulta (Passivo)
Navegue pelos diretórios para consultar princípios, templates, checklists e exemplos conforme sua necessidade:

```
01-principles/01-contexto.md     → Entender o público e a ação desejada
02-templates/grande-ideia.md     → Resumir sua mensagem em 1 frase
03-checklists/revisao-graficos.md → Verificar se um gráfico está pronto
04-references/arvore-decisao.md  → Escolher o tipo de gráfico ideal
```

### Modo Comando (Ativo)
Invoque a skill com comandos diretos:

| Comando | Para que serve | Exemplo |
|---|---|---|
| `/story contexto` | Definir público, ação e mecanismo | `/story contexto --publico "banca" --acao "aprovar"` |
| `/story visual` | Criar gráfico + aplicar princípios | `/story visual dados.csv --tipo "barras"` |
| `/story revisar` | Revisar gráfico existente | `/story revisar grafico.png` |
| `/story narrativa` | Construir história completa | `/story narrativa --dados resultados.csv --publico "professor"` |
| `/story slide` | Gerar slide ou seção | `/story slide "comparacao rf vs rn"` |
| `/story checklist` | Exibir checklist específico | `/story checklist "apresentacao"` |
| `/story exercicio` | Sugerir exercício prático | `/story exercicio saturacao` |

## Os 6 Princípios

| # | Princípio | Página no Livro | Arquivo |
|---|---|---|---|
| 1 | **Entenda o contexto** | Cap 1 | `01-principles/01-contexto.md` |
| 2 | **Escolha um visual eficaz** | Cap 2 | `01-principles/02-visual-eficaz.md` |
| 3 | **Elimine a saturação** | Cap 3 | `01-principles/03-saturacao.md` |
| 4 | **Foque a atenção** | Cap 4 | `01-principles/04-foco-atencao.md` |
| 5 | **Pense como um designer** | Cap 5 | `01-principles/05-design.md` |
| 6 | **Conte uma história** | Cap 7 | `01-principles/06-storytelling.md` |

## Fluxo Recomendado

Para criar uma apresentação completa:

```
1. /story contexto          → Defina quem, o quê e como
2. /story template          → Crie storyboard + Grande Ideia
3. /story visual            → Gere gráficos aplicando princípios 2-5
4. /story narrativa         → Conte a história (princípio 6)
5. /story checklist revisar → Verifique tudo antes de apresentar
6. /story template          → Prepare-se para a apresentação ao vivo
```

## Exemplos Disponíveis

| Exemplo | Descrição |
|---|---|
| `06-examples/trabalho-1/` | Classificação RF vs RN (seu projeto atual) |
| `06-examples/genericos/` | Exemplos independentes reutilizáveis |

## Referência Rápida

**Gráficos que funcionam:** Barras, linhas, dispersão, tabelas, mapas de calor  
**Gráficos a evitar:** Pizza, rosca, 3D, eixo Y secundário (salvo exceções)  
**Cores:** Use cor para destacar 1 coisa por vez; o resto em cinza  
**Storytelling:** Início (contexto) → Meio (dados) → Fim (ação recomendada)  
**Treino:** Apresente em voz alta antes do grande dia
