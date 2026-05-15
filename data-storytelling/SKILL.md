---
name: data-storytelling
description: Skill de storytelling com dados baseada no livro de Cole Nussbaumer Knaflic — crie, melhore, narre e revise visualizações de dados
type: skill
version: 1.0.0
author: Cole Nussbaumer Knaflic (adaptado)
tags: [storytelling, dados, visualização, apresentação, narrativa, Knaflic]
---

# data-storytelling

Skill baseada no livro **"Storytelling com Dados"** (Cole Nussbaumer Knaflic, Alta Books).

Aplicação prática dos 6 princípios para criar visualizações que comunicam com clareza, convencem com dados e preparam apresentações memoráveis.

## Escopo

| Função | Descrição |
|---|---|
| **Criar** | Gerar visualizações do zero a partir de dados brutos |
| **Melhorar** | Aplicar os 6 princípios em gráficos existentes |
| **Narrar** | Construir histórias completas para apresentações |
| **Revisar** | Criticar visualizações segundo os critérios do livro |

## Estrutura

```
data-storytelling/
├── 01-principles/      6 princípios fundamentais
├── 02-templates/       Storyboard, Grande Ideia, História 3min, etc.
├── 03-checklists/      Revisão de gráficos, slides, narrativa
├── 04-references/      Árvore de decisão, paleta de cores, gráficos a evitar
├── 05-exercicios/      Exercícios práticos por princípio
└── 06-examples/        Estudos de caso (Trabalho 1 + genéricos)
```

## Comandos

| Comando | Ação |
|---|---|
| `/story contexto` | Define público, ação e mecanismo |
| `/story visual [dados] [tipo]` | Cria gráfico aplicando os princípios |
| `/story revisar [caminho]` | Revisa gráfico segundo os 6 princípios |
| `/story narrativa [dados]` | Constrói narrativa completa para apresentação |
| `/story slide [tópico]` | Gera slide ou seção de apresentação |
| `/story checklist [tipo]` | Exibe checklist específico |
| `/story exercicio [principio]` | Sugere exercício prático |
