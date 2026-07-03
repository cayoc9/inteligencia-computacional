# Reprodutibilidade Do Processo Assistido

Este projeto nao registra apenas codigo e resultados. Ele tambem preserva parte do processo assistido por skills e agentes, porque essas ferramentas influenciaram escolhas de dataset, analise, narrativa e documentacao.

## O Que Faz Parte Da Reprodutibilidade

| Artefato | Motivo para manter |
|---|---|
| `.agents/skills/data-science-expert-SKILL.md` | Registra o enquadramento usado nas analises de dados e modelagem. |
| `.agents/skills/kaggle/` | Registra o fluxo auxiliar usado para trabalhar com Kaggle e aquisicao de dataset. |
| `skills-lock.json` | Guarda fonte e hash da skill Kaggle, permitindo verificar procedencia. |
| `data-storytelling/` | Registra a base usada para estruturar narrativa, graficos e apresentacao. |
| `DATA-STORYTELLING-SKILLS.md` | Evidencia a etapa de pesquisa/seleção de apoio para storytelling. |

## O Que Nao Faz Parte Da Reprodutibilidade

| Artefato | Motivo para nao versionar |
|---|---|
| `.venv/` | Ambiente pesado e dependente da maquina; `requirements.txt` substitui. |
| `models/` | Modelos derivados; devem ser regenerados pelos scripts. |
| `data/*.pkl` | Splits/resultados serializados derivados; regeneraveis. |
| `.playwright-cli/` | Logs e snapshots brutos de navegacao local. |
| `.qwen/`, `.claude/` | Configuracoes locais de ferramentas. |
| PDFs de aula/avaliacao | Materiais externos; manter localmente, mas nao versionar por padrao. |

## Regra Pratica

Manter no git o que ajuda outro leitor a entender **por que** o projeto tomou certas decisoes e como repetir a trilha intelectual do experimento.

Nao manter no git o que apenas representa estado local de maquina, cache, log bruto ou resultado derivado pesado.

## Decisao Arquitetural

A decisao de versionar artefatos pequenos do processo assistido esta registrada em `docs/adr/0001-versionar-artefatos-processo-assistido.md`.

## Segurança

As skills versionadas nao devem conter credenciais. Scripts que procuram chaves ou tokens devem ler esses valores de variaveis de ambiente ou de arquivos fora do repositorio, como `~/.kaggle`.
