# Revisao Estrutural Do Repositorio

**Data:** 2026-05-15  
**Escopo:** estrutura, redundancias, sujeira local, documentacao desatualizada e politica de versionamento.

## Resumo Executivo

O projeto esta funcional e tem boa separacao entre pipeline executavel, notebook, relatorios e `.specs`. A principal sujeira nao esta no codigo do experimento; ela se concentra em derivados pesados gerados localmente e em logs/configuracoes locais de ferramenta. Parte dos artefatos de skills/agentes foi reclassificada como evidencia de processo assistido.

## Estrutura Canonica Atual

| Area | Caminho | Decisao |
|---|---|---|
| Pipeline executavel | `projeto_sleep_health_rf_vs_rn/01_*.py` a `05_*.py`, `projeto_sleep_health_rf_vs_rn/scripts/` | Manter |
| Notebook narrativo | `projeto_sleep_health_rf_vs_rn/notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` | Manter |
| Dataset principal | `projeto_sleep_health_rf_vs_rn/data/sleep_health_dataset.csv` | Manter versionado |
| Artefatos derivados | `projeto_sleep_health_rf_vs_rn/models/`, `projeto_sleep_health_rf_vs_rn/data/*.pkl` | Ignorar/regenerar |
| Figuras do relatorio | `projeto_sleep_health_rf_vs_rn/reports/figures/` | Manter versionadas enquanto usadas no relatorio |
| Diagnosticos | `projeto_sleep_health_rf_vs_rn/reports/diagnostics/` | Manter como evidencia da Rodada 3 |
| Relatorios consolidados | `reports/consolidados/` | Manter |
| Specs oficiais | `.specs/features/trabalho-1/`, `.specs/features/experimento-v2-sono-restaurador/` | Manter |
| Evidencia de processo assistido | `.agents/`, `data-storytelling/`, `skills-lock.json` | Manter versionado para reprodutibilidade do processo |
| Config/log local de ferramenta | `.qwen/`, `.claude/`, `.playwright-cli/` | Ignorar; nao e insumo estavel do experimento |

## Redundancias Encontradas

| Item | Diagnostico | Acao |
|---|---|---|
| `trabalho-1-v1-oficial/` | Duplicava a spec canonica `trabalho-1/spec.md` | Ja consolidado e removido |
| `reports/fragmentos/` vs `reports/consolidados/` | Fragmentos sao material de composicao; consolidados sao fechamento | Manter ambos com papeis claros |
| `STATUS.md`, `README.md`, `.specs/project/STATE.md` | Sobreposicao aceitavel: status rapido, setup e memoria viva | Manter, mas evitar repetir detalhes demais |
| `DATA-STORYTELLING-SKILLS.md` e `data-storytelling/` | Material de apoio a apresentacao e reproducao da narrativa | Manter versionado enquanto for citado no processo |

## Sujeira Local Pesada

| Item | Tamanho aproximado | Status | Recomendacao |
|---|---:|---|---|
| `.venv/` | 2.8 GB | Ignorado | Manter local, pode ser recriado |
| `projeto_sleep_health_rf_vs_rn/models/` | 396 MB | Ignorado | Nao versionar; regenerar por scripts |
| `.playwright-cli/` | 216 KB | Ignorado | Pode apagar localmente quando nao precisar de logs |
| `.qwen/`, `.claude/` | Pequeno | Ignorado | Config local de ferramenta |
| `projeto_sleep_health_rf_vs_rn/data/*.pkl` | ~15 MB | Ignorado | Derivado; regeneravel |

## Itens Versionados Que Merecem Atenção

| Item | Situacao | Recomendacao |
|---|---|---|
| `.agents/skills/...` | Esta rastreado no git e documenta skills/agentes usados | Manter por enquanto; remover apenas se substituido por manifesto suficiente |
| `projeto_sleep_health_rf_vs_rn/reports/figures/*.png` | Figuras estao rastreadas | Manter se forem usadas no relatorio; caso contrario, regenerar e remover depois |
| `projeto_sleep_health_rf_vs_rn/reports/diagnostics/*.csv/json` | Evidencias da Rodada 3 | Manter |
| `projeto_sleep_health_rf_vs_rn/data/sleep_health_dataset.csv` | Dataset principal rastreado | Manter, pois README ja declara dataset versionado |

## Documentacao Atualizada Nesta Revisao

- `.gitignore`: reforcado para ferramentas locais e caches; `.agents/` foi retirado do ignore por ser evidencia de processo versionada.
- `.specs/codebase/CONVENTIONS.md`: politica de versionamento alinhada ao estado real.
- `.specs/codebase/STRUCTURE.md`: adicionados `docs/`, `reports/consolidados/` e spec V2.
- `.specs/codebase/STACK.md`: corrigida descricao de artefatos derivados e figuras reais.
- `.specs/codebase/ARCHITECTURE.md`: ajustada camada de persistencia e split.
- `README.md`, `STATUS.md` e `.specs/codebase/TESTING.md`: registrada alternativa `.venv/bin/python` para ambientes sem alias `python`.
- `docs/PROCESS_REPRODUCIBILITY.md` e `docs/adr/0001-versionar-artefatos-processo-assistido.md`: registrada politica de manter artefatos pequenos de skills/agentes para reproducao do processo.

## Validacao Executada

- `python projeto_sleep_health_rf_vs_rn/scripts/smoke_test.py`: falhou porque o shell atual nao possui comando `python`.
- `.venv/bin/python projeto_sleep_health_rf_vs_rn/scripts/smoke_test.py`: passou; dependencias e dataset foram validados.

## Proximas Limpezas Recomendadas

1. Decidir se `.agents/` inteiro deve continuar versionado ou se basta manter um manifesto reduzido com hashes e instrucoes. Minha recomendacao atual: manter ate a entrega, reduzir depois se necessario.
2. Consolidar `STATUS.md` apos a entrega para remover linguagem de urgencia ("prazo curto") se ficar historicamente desatualizada.
3. Decidir se `data-storytelling/` continua como skill vendorizada ou vira uma secao menor em `docs/`.

## Revisao De Reprodutibilidade Assistida

Esta revisao foi reaberta apos esclarecer que parte dos artefatos "de fora" foi versionada intencionalmente para preservar como o experimento foi conduzido com apoio de skills e agentes.

### Classificacao Atual

| Artefato | Papel | Manter? | Racional |
|---|---|---:|---|
| `.agents/skills/data-science-expert-SKILL.md` | Skill usada na analise de dados | Sim | Ajuda a reproduzir criterio analitico e checklist de DS |
| `.agents/skills/kaggle/` | Skill usada para aquisicao/analise via Kaggle | Sim, com ressalva | Pequeno; documenta comandos e processo. Nao contem credenciais reais |
| `skills-lock.json` | Hash/fonte da skill Kaggle | Sim | E o melhor artefato de reproducao de procedencia da skill |
| `data-storytelling/` | Skill/guia usado para narrativa e apresentacao | Sim | Reproduz decisoes de comunicacao visual/narrativa |
| `DATA-STORYTELLING-SKILLS.md` | Pesquisa/registro sobre storytelling skills | Sim ou arquivar depois | Evidencia de processo; pode ser condensado apos entrega |
| `.playwright-cli/` | Logs/snapshots locais de navegacao | Nao | Evidencia bruta local; ja existe resumo em `analise_datasets_health.md` |
| `.qwen/`, `.claude/` | Configuracao local de ferramentas | Nao | Nao afeta reproducao do experimento academico |
| `.venv/` | Ambiente instalado local | Nao | Pesado e substituido por `requirements.txt` |
| `projeto_sleep_health_rf_vs_rn/models/`, `projeto_sleep_health_rf_vs_rn/data/*.pkl` | Artefatos derivados | Nao | Regeneraveis pelos scripts |

## Artefatos Finais Detectados Em 2026-05-16

Durante a revisao de reprodutibilidade, apareceram novos artefatos ainda nao rastreados no git:

| Artefato | Classificacao | Recomendacao |
|---|---|---|
| `relatorio-tecnico.md` | Entregavel principal | Manter/versionar se for a versao final do relatorio |
| `projeto_sleep_health_rf_vs_rn/scripts/generate_final_graphs.py` | Script gerador de graficos finais | Manter/versionar, mas revisar rigor metodologico |
| `projeto_sleep_health_rf_vs_rn/reports/figures/comparacao_metricas.png` | Figura final | Manter se entrar no relatorio |
| `projeto_sleep_health_rf_vs_rn/reports/figures/confusion_matrix_histgb.png` | Figura final | Manter se entrar no relatorio |
| `projeto_sleep_health_rf_vs_rn/reports/figures/threshold_otimizacao.png` | Figura final | Manter se entrar no relatorio |
| `projeto_sleep_health_rf_vs_rn/reports/figures/feature_importance.png` | Figura final | Manter se entrar no relatorio |
| `projeto_sleep_health_rf_vs_rn/reports/figures/feature_auc_individual.png` | Figura final | Manter se entrar no relatorio |
| `projeto_sleep_health_rf_vs_rn/reports/figures/curvas_roc.png` | Figura final | Usar com ressalva: revisar se a curva foi gerada com probabilidades reais |
| `projeto_sleep_health_rf_vs_rn/reports/figures/curvas_pr.png` | Figura final | Usar com ressalva: revisar se a curva foi gerada com probabilidades reais |

### Alerta Metodologico Sobre Curvas

O script `projeto_sleep_health_rf_vs_rn/scripts/generate_final_graphs.py` atualmente indica que as curvas ROC e Precision-Recall sao aproximadas a partir de AUC/métricas agregadas, nao calculadas diretamente de `y_true` e `y_proba`.

Para relatorio academico, a recomendacao e:

1. Preferir curvas calculadas a partir das probabilidades reais dos modelos.
2. Se isso nao estiver disponivel, rotular explicitamente como visualizacao aproximada/ilustrativa.
3. Nao apresentar curvas aproximadas como evidência estatistica equivalente a `roc_curve` ou `precision_recall_curve` do scikit-learn.

### Resultado Da Auditoria De Segredos

Nao foram encontrados tokens reais nos artefatos versionados. Os scripts de Kaggle referenciam variaveis de ambiente e arquivos em `~/.kaggle`, mas nao armazenam valores de credenciais no repositorio.
4. Se o relatorio final incluir novos graficos, substituir fragmentos soltos por um documento final unico ou manter `reports/consolidados/` como fonte de fechamento.
