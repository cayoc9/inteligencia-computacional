# Status Executivo do Projeto

**Última atualização:** 2026-07-02  
**Disciplina:** Inteligência Computacional — UFPA 2026.1  
**Grupo:** 5 alunos (conforme planilha da disciplina)

---

## 📊 Resumo em 1 Minuto

| Item | Status |
|---|---|
| **Trabalho 1 (RF vs RN)** | ✅ **100% concluído** — entregue em 15/05/2026 |
| **Projeto 1 / Trabalho 2 (GA-MLP)** | ✅ **implementado e validado** — EDA, baseline, GA-MLP completo, JSON/CSV e notebook único |
| **Projeto 2 / Trabalho 2 (Breast Cancer)** | ✅ **pipeline spec-driven executado** — EDA, dicionário, notebook, modelos, ensemble e neuro-fuzzy comparativo |
| **Prazo da segunda avaliação** | **03/07/2026** |
| **Insight Projeto 1** | GA-MLP demonstra o híbrido, mas Random Forest foi superior no teste cego |
| **Próximos passos** | Redigir discussão final/PDF/apresentação com os resultados dos Projetos 1 e 2 |

---

## 🧬 Projeto 1 / Trabalho 2: Sistema Genético-Neural GA-MLP

### Objetivo
Projetar e avaliar um sistema híbrido Genético-Neural para classificação de óbito em insuficiência cardíaca (`DEATH_EVENT`), usando Algoritmo Genético como meta-otimizador de seleção de features e topologia de uma MLP.

### Dataset
- **Nome:** Heart Failure Clinical Records
- **Tamanho:** 299 registros, 13 colunas
- **Target:** `DEATH_EVENT`
- **Desbalanceamento:** classe positiva em ~32,1%

### Artefatos Entregues
| Artefato | Localização |
|---|---|
| Spec TLC | `.specs/features/projeto-1-genetico-neural/spec.md` |
| Design TLC | `.specs/features/projeto-1-genetico-neural/design.md` |
| Tasks TLC | `.specs/features/projeto-1-genetico-neural/tasks.md` |
| Notebook único | `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb` |
| Script híbrido auditável | `projeto_1_genetico_neural/hybrid_ga_mlp.py` |
| Resultado GA-MLP completo | `projeto_1_genetico_neural/reports/tables/ga_mlp_results.json` |
| Comparação final | `projeto_1_genetico_neural/reports/tables/model_comparison.csv` |

### Resultados Principais
| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.8333 | 0.8000 | 0.6316 | 0.7059 | 0.9101 |
| MLP | 0.7167 | 0.5714 | 0.4211 | 0.4848 | 0.7754 |
| GA-MLP completo | 0.7667 | 0.7778 | 0.3684 | 0.5000 | 0.7766 |

### Conclusões Técnicas
1. **O sistema híbrido está metodologicamente alinhado** à segunda avaliação: combina AG e MLP, com comunicação explícita por cromossomo, fitness e topologia.
2. **O GA-MLP não superou a Random Forest** no teste cego, especialmente em recall e F1.
3. **O ganho sobre a MLP simples foi marginal**, indicando que a busca genética não compensou o tamanho pequeno do dataset.
4. **A principal discussão acadêmica é o trade-off:** arquitetura híbrida válida, mas sujeita a overfitting evolutivo em 299 registros.

---

## 🧠 Projeto 2 / Trabalho 2: Breast Cancer Survival Risk

### Objetivo Corrigido
Prever risco de óbito (`Status = Dead`) a partir de atributos clínicos disponíveis no diagnóstico, sem usar `Survival Months` como feature principal.

### Dataset
- **Nome:** SEER Breast Cancer / Kaggle Breast_Cancer.csv
- **Tamanho bruto:** 4.024 registros, 16 colunas
- **Tamanho analítico:** 4.023 registros após remover 1 duplicata
- **Target:** `Status` (`Alive = 0`, `Dead = 1`)
- **Desbalanceamento:** `Dead = 616` casos (~15,31%)

### Artefatos Entregues
| Artefato | Localização |
|---|---|
| Spec TLC | `.specs/features/trabalho-2-breast-cancer/spec.md` |
| Design TLC | `.specs/features/trabalho-2-breast-cancer/design.md` |
| Tasks TLC | `.specs/features/trabalho-2-breast-cancer/tasks.md` |
| Dicionário de dados | `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` |
| Notebook do Projeto 2 | `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb` |
| EDA metadados/relações | `projeto_2_neuro_fuzzy/reports/tables/metadata_profile.csv`, `numeric_relationships.csv`, `categorical_relationships.csv` |
| Relatório técnico | `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md` |

### Resultados Principais Sem `Survival Months`
| Modelo | Accuracy | Precision | Recall | F2 | PR AUC | Falsos Negativos |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.6919 | 0.2744 | 0.6179 | 0.4941 | 0.3686 | 47 |
| Random Forest | 0.7814 | 0.3037 | 0.3333 | 0.3270 | 0.2826 | 82 |
| HistGradientBoosting | 0.8360 | 0.4000 | 0.1463 | 0.1676 | 0.3124 | 105 |
| Ensemble ponderado (threshold 0.21) | 0.4857 | 0.2119 | 0.8699 | 0.5366 | 0.3344 | 16 |
| Neuro-fuzzy cooperativo | 0.7764 | 0.2683 | 0.2683 | 0.2683 | 0.2365 | 90 |

### Conclusões Técnicas
1. **`Survival Months` é variável de acompanhamento** e não deve entrar no modelo principal de predição em diagnóstico.
2. **Acurácia isolada é enganosa** neste dataset; a classe `Dead` é minoritária.
3. **Threshold tuning muda a decisão clínica:** o ensemble com threshold 0.21 reduz falsos negativos para 16, mas aumenta falsos positivos.
4. **Neuro-fuzzy ficou como comparativo acadêmico**, não como modelo campeão: a fuzzificação manual + MLP não é ANFIS completo e teve recall baixo.

---

## 🎯 Trabalho 1: Classificação em Saúde

### Objetivo
Comparar Random Forest vs Redes Neurais na classificação de `felt_rested` (sensação de descanso) usando dataset de saúde do sono.

### Dataset
- **Nome:** Sleep Health & Daily Performance Dataset
- **Tamanho:** 100.000 registros, 32 features
- **Target:** `felt_rested` (binária: 61% classe 0, 39% classe 1)
- **Qualidade:** 0 nulos, 0 duplicatas

### Resultados Consolidados

| Modelo | Accuracy | Balanced Acc | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|
| **HistGradientBoosting** | **0.7425** | 0.7250 | **0.6787** | 0.6453 | 0.6616 | **0.8258** |
| Random Forest Tuned | 0.7415 | **0.7309** | 0.6528 | **0.6999** | **0.6756** | 0.8218 |
| Logistic Regression | 0.7315 | 0.7332 | 0.6332 | 0.7410 | 0.6828 | 0.8126 |
| Neural Network Otimizada | ~0.74 | ~0.73 | ~0.65 | ~0.69 | ~0.67 | ~0.82 |

**Threshold Otimizado (HistGradientBoosting):**
- Threshold **0.35**: F1=**0.7017** (vs 0.66 no threshold 0.5)
- Threshold **0.39**: Balanced Acc=**0.7424**

### Conclusões Técnicas

1. **Random Forest venceu** em dataset tabular — consistente com literatura
2. **Rede Neural não fracassou** — encontrou mesmo teto com maior complexidade
3. **Teto de ~74%** parece ser limite prático do alvo `felt_rested` (subjetivo)
4. **4 features dominam:** `sleep_quality`, `sleep_duration`, `stress`, `wake_episodes`
5. **Threshold tuning** entregou ganho real sem retreinar modelo

---

## 📋 Status De Fechamento

### Trabalho 1
- [x] **T1-10:** Gerar gráficos comparativos das 6 métricas + PR Curve
- [x] **T1-11:** Redigir relatório técnico (5-7 páginas)
- [x] **T1-12:** Incorporar análise de threshold no notebook final
- [x] **Entrega:** Submetido em 15/05/2026

### Próximas Trilhas
- [ ] **V2 sono restaurador:** executar experimento especificado em `.specs/features/experimento-v2-sono-restaurador/`
- [x] **Trabalho 2:** spec, EDA, dicionário, notebook e pipeline executados em `projeto_2_neuro_fuzzy/`
- [ ] **Opcional:** aprofundar análise de erro por ocupação/segmento ou SHAP se for útil para apresentação futura

---

## 🗺️ Roadmap Geral

### Trabalho 1
- **Prazo:** 15/05/2026
- **Status:** 100% concluído — entregue
- **Entregáveis:** Relatório + Notebook + Scripts

### Experimento V2: Sono Restaurador
- **Prazo:** Pós-entrega do Trabalho 1
- **Status:** Especificado, não executado
- **Decisão:** Evolução metodológica separada da V1 oficial

### Trabalho 2: Sistema Híbrido ou Ensemble
- **Prazo:** 03/07/2026
- **Status:** Pipeline spec-driven executado
- **Tema:** Breast Cancer Survival Risk
- **Entregáveis:** Dicionário de dados, EDA de metadados/relações, notebook, modelos tabulares, ensemble ponderado e neuro-fuzzy comparativo

---

## 📁 Onde Encontrar Coisas

### Documentação
| Documento | Localização |
|---|---|
| **Status detalhado + decisões** | `.specs/project/STATE.md` |
| **Roadmap completo** | `.specs/project/ROADMAP.md` |
| **Revisão estrutural do repo** | `.specs/project/REPO_CLEANUP_REVIEW.md` |
| **Dicionário de dados** | `docs/DATA_DICTIONARY.md` |
| **Reprodutibilidade assistida** | `docs/PROCESS_REPRODUCIBILITY.md` |
| **ADR de processo assistido** | `docs/adr/0001-versionar-artefatos-processo-assistido.md` |
| **Requisitos do Trabalho 1** | `.specs/features/trabalho-1/spec.md` |
| **Spec V2 sono restaurador** | `.specs/features/experimento-v2-sono-restaurador/spec.md` |
| **Tarefas e progresso** | `.specs/features/trabalho-1/tasks.md` |
| **Relatórios de rodada** | `.specs/features/trabalho-1/relatorio_rodada_*.md` |
| **Relatórios consolidados** | `reports/consolidados/` |
| **Spec Trabalho 2** | `.specs/features/trabalho-2-breast-cancer/spec.md` |
| **Spec Projeto 1 GA-MLP** | `.specs/features/projeto-1-genetico-neural/spec.md` |
| **Notebook Projeto 1 GA-MLP** | `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb` |
| **Dicionário Projeto 2** | `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` |
| **Notebook Projeto 2** | `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb` |

### Código e Artefatos
| Artefato | Localização |
|---|---|
| **Pipeline de scripts** | `01_*.py` a `05_*.py` |
| **Notebook principal** | `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` |
| **Modelos treinados** | `models/*.pkl`, `models/*.h5`, `models/v2/*.keras` |
| **Figuras e visualizações** | `reports/figures/*.png` |
| **Diagnósticos** | `reports/diagnostics/*.csv`, `*.json` |
| **Projeto 1 GA-MLP** | `projeto_1_genetico_neural/hybrid_ga_mlp.py` |
| **Resultados Projeto 1** | `projeto_1_genetico_neural/reports/tables/*.json`, `model_comparison.csv` |
| **Pipeline Projeto 2** | `projeto_2_neuro_fuzzy/run_pipeline.py` |

### Comandos Úteis
```bash
# Validar ambiente
python scripts/smoke_test.py
# ou, sem ativar o venv:
.venv/bin/python scripts/smoke_test.py

# Executar pipeline completo
python 01_check_data.py && python 02_eda.py && python 03_random_forest.py && python 04_neural_network.py && python 05_neural_network_optimized.py

# Diagnóstico de limites
python scripts/diagnose_model_limits.py
```

---

## 🚦 Bloqueios e Riscos

| Bloqueio/Risco | Impacto | Mitigação |
|---|---|---|
| **Prazo do T1** (15/05) | Resolvido | Entrega concluída; manter registro como histórico |
| **Subjetividade do alvo** | Médio | Justificar no relatório como limitação do dataset |
| **GPU local limitada** | Baixo | Modelo já convergiu; ganhos adicionais têm retorno decrescente |

---

## 💡 Lições Aprendidas

### O Que Funcionou
- Scripts numerados facilitaram reprodutibilidade
- Mesmo random_state=42 permitiu comparação justa
- Diagnóstico de Rodada 3 revelou gargalo real (alvo, não modelo)
- Threshold tuning entregou ganho sem custo de retreino

### O Que Não Funcionou
- Rede Neural profunda em dataset tabular não superou Random Forest
- Feature engineering adicionou complexidade sem ganho proporcional
- Acurácia como métrica principal mascarou desempenho real

### Surpresas
- Teto do alvo: `felt_rested` parece subjetivo
- Poucas features importam: 4 features carregam 80% do sinal
- Threshold 0.5 é arbitrário: ajustar para 0.35 melhorou F1 em 6%

---

## 👥 Equipe e Responsabilidades

| Papel | Responsável | Status |
|---|---|---|
| **Grupo** | 5 alunos | Conforme planilha da disciplina |

*Detalhes da equipe em `.specs/project/PROJECT.md`*

---

## 📞 Contato e Suporte

- **Professor:** [Ver syllabus da disciplina]
- **Planilha da disciplina:** [Ver link no classroom]
- **Repositório:** Este diretório

---

*Documento gerado automaticamente a partir do estado do projeto. Para atualizações, editar `.specs/project/STATE.md` e `.specs/project/ROADMAP.md`.*
