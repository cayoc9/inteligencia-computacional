# Inteligência Computacional - UFPA 2026.1

## Visão Geral
Repositório para as atividades e trabalhos da disciplina de Inteligência Computacional do Mestrado em Engenharia Elétrica (PPGEE - UFPA).

**Status:** ✅ Trabalho 1 concluído e entregue; próxima decisão é Trabalho 2/V2  
**Última atualização:** 2026-06-05

## Objetivos
- ✅ Aplicar técnicas de IA (Random Forest, Redes Neurais) em problema real de saúde
- ✅ Desenvolver análise crítica de modelos e métricas de desempenho
- ✅ Documentar experimentos seguindo padrões acadêmicos

## Equipe
- **Grupo:** 5 alunos (conforme definido na planilha da disciplina)
- **Divisão de tarefas:** Ver `.specs/features/trabalho-1/tasks.md`

## Trabalhos

### Trabalho 1: Comparação RF vs Redes Neurais (Saúde)
- **Prazo:** 15/05/2026
- **Status:** ✅ 100% concluído — entregue em 15/05/2026
- **Dataset:** Sleep Health & Daily Performance (100k rows, 32 cols)
- **Target:** `felt_rested` (binária: 61%/39%)
- **Melhor modelo:** HistGradientBoosting (74.25% accuracy, 82.58% ROC AUC)
- **Entregáveis:** Relatório técnico + Notebook + Scripts

### Experimento V2: Sono Restaurador
- **Prazo:** Pós-entrega do Trabalho 1
- **Status:** 📝 Especificado, não executado
- **Ideia:** Alvo composto `sono_restaurador` combinando `felt_rested` e `cognitive_performance_score`
- **Regra:** Evolução metodológica separada; não altera os resultados oficiais da V1

### Trabalho 2: Sistema Híbrido ou Ensemble
- **Prazo:** 03/07/2026
- **Status:** ⚪ Não iniciado
- **Ideias:** Stacking ensemble, Neuro-Fuzzy, Otimização Genética

## Documentação

| Documento | Localização |
|---|---|
| **Status executivo** | `STATUS.md` (visão geral rápida) |
| **README** | `README.md` (setup e execução) |
| **Roadmap** | `.specs/project/ROADMAP.md` |
| **Estado atual** | `.specs/project/STATE.md` |
| **Revisão estrutural** | `.specs/project/REPO_CLEANUP_REVIEW.md` |
| **Dicionário de dados** | `docs/DATA_DICTIONARY.md` |
| **Reprodutibilidade assistida** | `docs/PROCESS_REPRODUCIBILITY.md` |
| **ADR de processo assistido** | `docs/adr/0001-versionar-artefatos-processo-assistido.md` |
| **Especificação T1** | `.specs/features/trabalho-1/spec.md` |
| **Especificação V2** | `.specs/features/experimento-v2-sono-restaurador/spec.md` |
| **Tarefas T1** | `.specs/features/trabalho-1/tasks.md` |

## Links Úteis
- **Syllabus da disciplina:** [Ver classroom]
- **Planilha de grupos:** [Ver link na disciplina]
- **PDF de avaliação do Trabalho 1:** [Ver classroom]
