# Revisao Estrutural Do Repositorio

**Data:** 2026-05-15  
**Escopo:** estrutura, redundancias, sujeira local, documentacao desatualizada e politica de versionamento.

## Resumo Executivo

O projeto esta funcional e tem boa separacao entre pipeline executavel, notebook, relatorios e `.specs`. A principal sujeira nao esta no codigo do experimento, mas em artefatos de ferramenta/agente e derivados pesados gerados localmente.

## Estrutura Canonica Atual

| Area | Caminho | Decisao |
|---|---|---|
| Pipeline executavel | `01_*.py` a `05_*.py`, `scripts/` | Manter |
| Notebook narrativo | `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` | Manter |
| Dataset principal | `data/sleep_health_dataset.csv` | Manter versionado |
| Artefatos derivados | `models/`, `data/*.pkl` | Ignorar/regenerar |
| Figuras do relatorio | `reports/figures/` | Manter versionadas enquanto usadas no relatorio |
| Diagnosticos | `reports/diagnostics/` | Manter como evidencia da Rodada 3 |
| Relatorios consolidados | `reports/consolidados/` | Manter |
| Specs oficiais | `.specs/features/trabalho-1/`, `.specs/features/experimento-v2-sono-restaurador/` | Manter |
| Skills/agentes locais | `.agents/`, `data-storytelling/`, `.qwen/`, `.claude/`, `.playwright-cli/` | Tratar como ferramenta local, nao nucleo do projeto |

## Redundancias Encontradas

| Item | Diagnostico | Acao |
|---|---|---|
| `trabalho-1-v1-oficial/` | Duplicava a spec canonica `trabalho-1/spec.md` | Ja consolidado e removido |
| `reports/fragmentos/` vs `reports/consolidados/` | Fragmentos sao material de composicao; consolidados sao fechamento | Manter ambos com papeis claros |
| `STATUS.md`, `README.md`, `.specs/project/STATE.md` | Sobreposicao aceitavel: status rapido, setup e memoria viva | Manter, mas evitar repetir detalhes demais |
| `DATA-STORYTELLING-SKILLS.md` e `data-storytelling/` | Material de apoio a apresentacao, nao pipeline | Manter fora do status git via `.gitignore` ou mover depois para docs se virar parte oficial |

## Sujeira Local Pesada

| Item | Tamanho aproximado | Status | Recomendacao |
|---|---:|---|---|
| `.venv/` | 2.8 GB | Ignorado | Manter local, pode ser recriado |
| `models/` | 396 MB | Ignorado | Nao versionar; regenerar por scripts |
| `.playwright-cli/` | 216 KB | Ignorado | Pode apagar localmente quando nao precisar de logs |
| `.qwen/`, `.claude/` | Pequeno | Ignorado | Ferramenta local |
| `data/*.pkl` | ~15 MB | Ignorado | Derivado; regeneravel |

## Itens Versionados Que Merecem Atenção

| Item | Situacao | Recomendacao |
|---|---|---|
| `.agents/skills/...` | Esta rastreado no git e parece vendor de skills, nao codigo do projeto | Em limpeza futura, considerar `git rm -r --cached .agents` apos confirmar que nada do trabalho depende disso |
| `reports/figures/*.png` | Figuras estao rastreadas | Manter se forem usadas no relatorio; caso contrario, regenerar e remover depois |
| `reports/diagnostics/*.csv/json` | Evidencias da Rodada 3 | Manter |
| `data/sleep_health_dataset.csv` | Dataset principal rastreado | Manter, pois README ja declara dataset versionado |

## Documentacao Atualizada Nesta Revisao

- `.gitignore`: reforcado para ferramentas locais e caches.
- `.specs/codebase/CONVENTIONS.md`: politica de versionamento alinhada ao estado real.
- `.specs/codebase/STRUCTURE.md`: adicionados `docs/`, `reports/consolidados/` e spec V2.
- `.specs/codebase/STACK.md`: corrigida descricao de artefatos derivados e figuras reais.
- `.specs/codebase/ARCHITECTURE.md`: ajustada camada de persistencia e split.
- `README.md`, `STATUS.md` e `.specs/codebase/TESTING.md`: registrada alternativa `.venv/bin/python` para ambientes sem alias `python`.

## Validacao Executada

- `python scripts/smoke_test.py`: falhou porque o shell atual nao possui comando `python`.
- `.venv/bin/python scripts/smoke_test.py`: passou; dependencias e dataset foram validados.

## Proximas Limpezas Recomendadas

1. Decidir se `.agents/` deve sair do versionamento. Minha recomendacao tecnica: sim, mas fazer em commit separado.
2. Consolidar `STATUS.md` apos a entrega para remover linguagem de urgencia ("prazo curto") se ficar historicamente desatualizada.
3. Decidir se `data-storytelling/` vira doc oficial em `docs/` ou permanece skill local ignorada.
4. Se o relatorio final incluir novos graficos, substituir fragmentos soltos por um documento final unico ou manter `reports/consolidados/` como fonte de fechamento.
