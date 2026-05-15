# Status Executivo do Projeto

**Última atualização:** 2026-05-15  
**Disciplina:** Inteligência Computacional — UFPA 2026.1  
**Grupo:** 5 alunos (conforme planilha da disciplina)

---

## 📊 Resumo em 1 Minuto

| Item | Status |
|---|---|
| **Trabalho 1 (RF vs RN)** | 🟡 **85% concluído** — Consolidando resultados finais |
| **Prazo de entrega** | ⚠️ **15/05/2026** (urgente) |
| **Melhor modelo** | HistGradientBoosting: **74.25%** accuracy, **82.58%** ROC AUC |
| **Principal insight** | RF > RN em dataset tabular; teto limitado pela subjetividade do alvo |
| **Próximos passos** | Gráficos comparativos + relatório técnico (5-7 páginas) |

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

## 📋 Pendências (Próximos 2 Dias)

### Prioritário (Entrega 15/05)
- [ ] **T1-10:** Gerar gráficos comparativos das 6 métricas + PR Curve
- [ ] **T1-11:** Redigir relatório técnico (5-7 páginas)
- [ ] **T1-12:** Incorporar análise de threshold no notebook final
- [ ] **Entrega:** Submeter até 23:59 de 15/05/2026

### Opcional (se sobrar tempo)
- [ ] Análise de erro por ocupação/segmento
- [ ] SHAP feature importance (alternativa: usar permutation importance já calculada)

---

## 🗺️ Roadmap Geral

### Trabalho 1 (Atual)
- **Prazo:** 15/05/2026
- **Status:** 85% concluído
- **Entregáveis:** Relatório + Notebook + Scripts

### Trabalho 2: Sistema Híbrido ou Ensemble
- **Prazo:** 03/07/2026
- **Status:** Não iniciado
- **Ideias:** Stacking ensemble, Neuro-Fuzzy, Otimização Genética

---

## 📁 Onde Encontrar Coisas

### Documentação
| Documento | Localização |
|---|---|
| **Status detalhado + decisões** | `.specs/project/STATE.md` |
| **Roadmap completo** | `.specs/project/ROADMAP.md` |
| **Requisitos do Trabalho 1** | `.specs/features/trabalho-1/spec.md` |
| **Tarefas e progresso** | `.specs/features/trabalho-1/tasks.md` |
| **Relatórios de rodada** | `.specs/features/trabalho-1/relatorio_rodada_*.md` |

### Código e Artefatos
| Artefato | Localização |
|---|---|
| **Pipeline de scripts** | `01_*.py` a `05_*.py` |
| **Notebook principal** | `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb` |
| **Modelos treinados** | `models/*.pkl`, `models/*.h5`, `models/v2/*.keras` |
| **Figuras e visualizações** | `reports/figures/*.png` |
| **Diagnósticos** | `reports/diagnostics/*.csv`, `*.json` |

### Comandos Úteis
```bash
# Validar ambiente
python scripts/smoke_test.py

# Executar pipeline completo
python 01_check_data.py && python 02_eda.py && python 03_random_forest.py && python 04_neural_network.py && python 05_neural_network_optimized.py

# Diagnóstico de limites
python scripts/diagnose_model_limits.py
```

---

## 🚦 Bloqueios e Riscos

| Bloqueio/Risco | Impacto | Mitigação |
|---|---|---|
| **Prazo curto** (15/05) | Alto | Focar em consolidar resultados, não em novos experimentos |
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
