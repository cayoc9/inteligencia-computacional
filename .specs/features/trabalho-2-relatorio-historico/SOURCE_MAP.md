# Mapa de Fontes - Relatorio Historico do Trabalho 2

## Hierarquia de Autoridade

| Nivel | Tipo de fonte | Exemplos | Papel | Regra de uso |
|---|---|---|---|---|
| 1 | Fonte canonica de entrega | `.specs/`, `README`, `docs/`, `reports/`, `notebooks/`, CSVs | verdade final sobre o que foi implementado e validado | prevalece em caso de conflito |
| 2 | Fonte complementar de processo | sessoes Codex e Antigravity | explica racional, bifurcacoes, ordens de execucao e criticas orientadoras | nunca substitui artefato canonico |
| 3 | Fonte interpretativa | audio, NotebookLM, notas e resumos | explica intencao, contexto e heuristicas | usar como apoio, nao como prova final isolada |

## Sessoes de Agentes Incluidas

### Codex

| Session ID | Local | Papel analitico |
|---|---|---|
| `019f2525-5a79-7723-b4eb-8759cc32ce9f` | `/home/cayo/.codex/history.jsonl` e `/home/cayo/.codex/sessions/2026/07/02/rollout-2026-07-02T20-23-52-019f2525-5a79-7723-b4eb-8759cc32ce9f.jsonl` | trilha principal do Projeto 2: audio, plano corretivo, troca de dataset, evolucao canonica v2 e relatorio historico |
| `019f255f-88a8-7a81-b002-957841c02760` | `/home/cayo/.codex/history.jsonl` e `/home/cayo/.codex/sessions/2026/07/02/rollout-2026-07-02T21-27-25-019f255f-88a8-7a81-b002-957841c02760.jsonl` | trilha paralela de auditoria: Projeto 1, comparacao entre projetos, critica de lacunas e criterios de escolha para apresentacao |

### Antigravity CLI

| Session ID | Local | Papel analitico |
|---|---|---|
| `cd405d9c-1645-4090-8ada-150e8f2aea59` | `/home/cayo/.gemini/antigravity-cli/history.jsonl` | pesquisa inicial de datasets, requisitos da atividade, guia de acao e parte da conducao de Projeto 1 e Projeto 2 |

## Artefatos de Processo do Antigravity

| Artifact | Local | Uso |
|---|---|---|
| `analise_atividade2.md` | `/home/cayo/.gemini/antigravity-cli/brain/cd405d9c-1645-4090-8ada-150e8f2aea59/analise_atividade2.md` | leitura inicial da atividade e enquadramento metodologico |
| `relatorio_projeto1_genetico_neural.md` | `/home/cayo/.gemini/antigravity-cli/brain/cd405d9c-1645-4090-8ada-150e8f2aea59/relatorio_projeto1_genetico_neural.md` | material historico do Projeto 1 |
| `guia_de_acao_ic.md` | `/home/cayo/.gemini/antigravity-cli/brain/cd405d9c-1645-4090-8ada-150e8f2aea59/guia_de_acao_ic.md` | referencia orientadora de tecnica e estrategia |

## Regra Operacional para a Analise

1. Usar as sessoes de agentes para reconstruir o processo e o racional.
2. Confirmar toda afirmacao final importante nos artefatos canonicos do repositorio.
3. Marcar explicitamente quando uma informacao veio apenas de sessao de agente.
4. Em caso de conflito, manter o repositorio como fonte final de verdade e registrar a divergencia no checkpoint professorial.
