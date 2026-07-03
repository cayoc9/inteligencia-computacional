# Validação e Testes

## Validação Existente

### Scripts de Pipeline
Cada script é auto-validado: imprime métricas no console e salva artefatos.

| Script | Gate Check |
|---|---|
| `01_check_data.py` | ✅ Imprime shape, tipos, nulos, duplicatas |
| `02_eda.py` | ✅ Salva figuras em `reports/figures/` |
| `03_random_forest.py` | ✅ Imprime 6 métricas + salva modelo `.pkl` |
| `04_neural_network.py` | ✅ Imprime 6 métricas + salva modelo `.h5` |
| `05_neural_network_optimized.py` | ✅ Imprime 6 métricas + salva modelo `.keras` |
| `scripts/diagnose_model_limits.py` | ✅ Compara 5 modelos + threshold tuning |
| `scripts/smoke_test.py` | ✅ Valida dependências do ambiente |

### Métricas Obrigatórias (Trabalho 1)
Todas impressas no console após treino:
1. **Acurácia (Accuracy)**
2. **Matriz de Confusão**
3. **Precisão (Precision)**
4. **Recall (Sensibilidade)**
5. **F1-Score**
6. **ROC AUC**

### Métricas Adicionais (Diagnóstico)
- **Balanced Accuracy** (importante para dataset desbalanceado)
- **Precision-Recall Curve (PR AUC)**
- **Threshold tuning** (encontra melhor ponto de corte por métrica)
- **Permutation Importance** (interpretabilidade)

## Gates de Validação

### Pipeline Completo
```bash
# Validação de ambiente
python scripts/smoke_test.py
# Alternativa sem ativar venv:
.venv/bin/python scripts/smoke_test.py

# Execução completa (na ordem)
python 01_check_data.py
python 02_eda.py
python 03_random_forest.py
python 04_neural_network.py
python 05_neural_network_optimized.py
python scripts/diagnose_model_limits.py
```

### Notebook (quando consolidado)
```bash
# Executar e validar notebook
jupyter nbconvert --to notebook --execute notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb
```

## Resultados de Referência (2026-05-14)

| Modelo | Accuracy | Balanced Acc | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|
| Random Forest Tuned | 0.7415 | 0.7309 | 0.6528 | 0.6999 | 0.6756 | 0.8218 |
| HistGradientBoosting | 0.7425 | 0.7250 | 0.6787 | 0.6453 | 0.6616 | 0.8258 |
| Neural Network Base | 0.7323 | ~0.72 | ~0.64 | ~0.68 | ~0.66 | ~0.81 |
| Neural Network Otimizada | ~0.74 | ~0.73 | ~0.65 | ~0.69 | ~0.67 | ~0.82 |

**Threshold Otimizado (HistGradientBoosting):**
- **F1 máximo:** threshold=0.35 → F1=0.7017, recall=0.8491
- **Balanced Acc máximo:** threshold=0.39 → balanced_acc=0.7424, F1=0.6981

## Lacunas

### Testes Automatizados
- [ ] Não há testes unitários (pytest/unittest)
- [ ] Não há teste de integração entre scripts
- [ ] Não há validação de schema dos dados

### Reprodutibilidade Cruzada
- [ ] Não há script único "make all" para rodar trilha completa
- [ ] Não há validação de que notebook e scripts produzem mesmos resultados

### Validação de Modelo
- [ ] Validação cruzada (5-10 folds) apenas em diagnóstico parcial
- [ ] Não há teste de estabilidade (múltiplas sementes)

## Recomendação para Trabalhos Futuros
1. Criar `tests/` com pytest para validação de pré-processamento
2. Adicionar `Makefile` ou script `run_all.py` para pipeline único
3. Usar validação cruzada sistemática (não apenas holdout)
4. Congelar versões exatas (`pip freeze > requirements.lock.txt`)

## Projeto 2: Breast Cancer Gates

```bash
# Testes unitarios/documentais do Projeto 2
projeto_2_neuro_fuzzy/.venv/bin/python -m pytest projeto_2_neuro_fuzzy/tests -q

# Pipeline completo do Projeto 2
projeto_2_neuro_fuzzy/.venv/bin/python projeto_2_neuro_fuzzy/run_pipeline.py

# Notebook narrativo do Projeto 2
projeto_2_neuro_fuzzy/.venv/bin/jupyter nbconvert \
  --to notebook \
  --execute projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb \
  --output /tmp/projeto_2_breast_cancer_survival.executed.ipynb

# Suite configurada do repositorio
projeto_2_neuro_fuzzy/.venv/bin/python -m pytest -q
```

O `pytest.ini` restringe a coleta aos diretorios `tests/` e `projeto_2_neuro_fuzzy/tests/`, evitando coletar scripts utilitarios como `scripts/smoke_test.py`.

### Status de Lacunas Atualizado

- [x] Projeto 2 possui testes unitarios com pytest.
- [x] Projeto 2 possui validacao de schema/sanitizacao.
- [x] Projeto 2 possui runner unico (`run_pipeline.py`).
- [x] Projeto 2 possui validacao de notebook por `nbconvert`.
- [ ] Trabalho 1 ainda depende majoritariamente de scripts auto-validados.
