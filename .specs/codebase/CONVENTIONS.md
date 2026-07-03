# Convenções do Projeto

## Organização de Arquivos

### Scripts Numerados (Pipeline)
Scripts do projeto de sono seguem padrão `NN_nome_descritivo.py` em `projeto_sleep_health_rf_vs_rn/`:
- `projeto_sleep_health_rf_vs_rn/01_check_data.py`: Inspeção inicial
- `projeto_sleep_health_rf_vs_rn/02_eda.py`: Análise exploratória
- `projeto_sleep_health_rf_vs_rn/03_random_forest.py`: Modelagem RF
- `projeto_sleep_health_rf_vs_rn/04_neural_network.py`: Modelagem RN base
- `projeto_sleep_health_rf_vs_rn/05_neural_network_optimized.py`: Modelagem RN otimizada

**Por que:** Numeração facilita ordem de execução e auditoria.

### Scripts de Suporte
Em `projeto_sleep_health_rf_vs_rn/scripts/` para utilitários:
- `projeto_sleep_health_rf_vs_rn/scripts/smoke_test.py`: Validação de ambiente
- `projeto_sleep_health_rf_vs_rn/scripts/diagnose_model_limits.py`: Diagnóstico comparativo

### Diretórios de Artefatos
| Diretório | Conteúdo |
|---|---|
| `projeto_sleep_health_rf_vs_rn/data/` | Dataset principal versionado + splits locais derivados |
| `projeto_sleep_health_rf_vs_rn/models/` | Modelos treinados locais (.pkl, .h5, .keras), não versionados |
| `projeto_sleep_health_rf_vs_rn/models/v2/` | Modelos locais da versão otimizada |
| `projeto_sleep_health_rf_vs_rn/docs/` | Documentação técnica complementar, como dicionário de dados |
| `projeto_sleep_health_rf_vs_rn/reports/figures/` | Visualizações usadas no relatório |
| `projeto_sleep_health_rf_vs_rn/reports/fragmentos/` | Trechos de relatório (.md) |
| `projeto_sleep_health_rf_vs_rn/reports/diagnostics/` | Diagnósticos (.csv, .json) |
| `projeto_sleep_health_rf_vs_rn/reports/consolidados/` | Relatórios e camadas analíticas consolidadas |
| `projeto_sleep_health_rf_vs_rn/notebooks/` | Notebooks de análise narrativa |

## Código

### Estilo e Formatação
- **Comentários:** Em português, explicando intenção técnica/acadêmica
- **Nomes de variáveis:** Descritivos (ex: `X_train`, `y_test`, `column_transformer`)
- **Imports:** No topo do arquivo, padrão `import X`, `from X import Y`

### Random Seed
- **Valor:** `42` em todos os scripts
- **Aplicação:**
  - Scikit-learn: `random_state=42`
  - NumPy: `np.random.seed(42)`
  - TensorFlow: `tf.keras.utils.set_random_seed(42)`

### Estratificação
- **Split:** Estratificado por `y` para preservar distribuição do target
- **Por que:** Dataset levemente desbalanceado (61%/39%)

### Pipelines de Pré-processamento
- **Padrão:** `ColumnTransformer` + `Pipeline` do scikit-learn
- **Por que:** Evita data leakage (transformadores ajustam apenas no treino)

### Persistência
- **Modelos:** `joblib.dump(modelo, 'caminho/arquivo.pkl')`
- **Splits:** `joblib.dump(X_test, 'data/test_split.pkl')` para reuso
- **Históricos:** `joblib.dump(history.history, 'caminho/historico.pkl')`

## Notebook

### Notebook Único
- **Nome:** `projeto_sleep_health_rf_vs_rn/notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`
- **Propósito:** Narrativa de Data Science + apresentação
- **Conteúdo:**
  1. Contexto e objetivo
  2. EDA com visualizações
  3. Preparação dos dados
  4. Random Forest + tuning
  5. MLP baseline + otimizada
  6. Comparação (6 métricas)
  7. Discussão e limitações

### Sincronização com Scripts
- **Regra:** Notebook deve refletir resultados dos scripts
- **Como:** Usar mesmo `random_state=42` e mesmo split
- **Validação:** Métricas devem bater (± tolerância de plataforma)

## Documentação

### Especificação (.specs/)
- **Projetos:** `.specs/project/` (visão, roadmap, estado)
- **Codebase:** `.specs/codebase/` (stack, arquitetura, convenções)
- **Features:** `.specs/features/<nome>/` (spec, tasks, relatórios)

### Relatórios de Rodada
- **Formato:** `.specs/features/trabalho-1/relatorio_rodada_N.md`
- **Conteúdo:**
  - Pergunta da rodada
  - Metodologia
  - Resultados (tabelas, métricas)
  - Discussão
  - Próximos passos

### Fragmentos de Relatório
- **Local:** `projeto_sleep_health_rf_vs_rn/reports/fragmentos/`
- **Propósito:** Trechos reutilizáveis para relatório final
- **Exemplos:**
  - `01-resultados-comparativos.md`: Tabelas de métricas
  - `02-discussao-e-limitacoes.md`: Discussão crítica

## Execução

### Comandos de Validação
```bash
# Ambiente
python projeto_sleep_health_rf_vs_rn/scripts/smoke_test.py

# Pipeline completo (na ordem)
python projeto_sleep_health_rf_vs_rn/01_check_data.py
python projeto_sleep_health_rf_vs_rn/02_eda.py
python projeto_sleep_health_rf_vs_rn/03_random_forest.py
python projeto_sleep_health_rf_vs_rn/04_neural_network.py
python projeto_sleep_health_rf_vs_rn/05_neural_network_optimized.py
python projeto_sleep_health_rf_vs_rn/scripts/diagnose_model_limits.py
```

### Saída Esperada
- Scripts imprimem métricas no console
- Modelos salvos em `projeto_sleep_health_rf_vs_rn/models/`
- Figuras salvas em `projeto_sleep_health_rf_vs_rn/reports/figures/`
- Diagnósticos salvos em `projeto_sleep_health_rf_vs_rn/reports/diagnostics/`

## Versionamento

### O Que Versionar
- ✅ Código (.py, .ipynb)
- ✅ Documentação (.md)
- ✅ Dataset (.csv em `projeto_sleep_health_rf_vs_rn/data/`)
- ✅ Requisitos (requirements.txt)
- ✅ Figuras e diagnósticos quando usados como evidência do relatório
- ✅ Artefatos pequenos de reprodutibilidade do processo assistido (`.agents/`, `data-storytelling/`, `skills-lock.json`)

### O Que Não Versionar
- ❌ Modelos (.pkl, .h5, .keras) — derivados, pesados
- ❌ Splits e resultados serializados (.pkl) — derivados, regeneráveis
- ❌ Ambiente (.venv/) — local, específico da máquina
- ❌ Configurações e logs locais de ferramenta (`.qwen/`, `.claude/`, `.playwright-cli/`)
- ❌ Python cache (__pycache__/, .pyc)

### Diretórios Auxiliares
- `.agents/` é mantido como evidência pequena do processo assistido por skills/agentes. Não contém credenciais; os scripts de Kaggle buscam credenciais no ambiente ou em `~/.kaggle`.
- `data-storytelling/` é mantido como apoio reprodutível para a narrativa/apresentação, pois influenciou a forma de comunicar os resultados.
- `.qwen/`, `.claude/` e `.playwright-cli/` ficam fora do versionamento por serem configuração/log local de ferramenta, não insumo estável do experimento.

## Convenção Recomendada

### Para Novos Membros
1. Ler `README.md` e `STATUS.md`
2. Ativar ambiente: `source .venv/bin/activate`
3. Validar: `python projeto_sleep_health_rf_vs_rn/scripts/smoke_test.py`
4. Executar pipeline na ordem
5. Consultar `.specs/` para contexto e decisões

### Para Trabalhos Futuros
- Manter scripts como pipeline auditável
- Notebook único para narrativa (evitar fragmentação)
- Documentar decisões em `.specs/project/STATE.md`
- Congelar dependências: `pip freeze > requirements.lock.txt`

## Projeto 2: Convenções Especificas

### Notebook por Projeto
- **Trabalho 1:** `projeto_sleep_health_rf_vs_rn/notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`
- **Projeto 2:** `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`
- Cada projeto deve ter um notebook narrativo proprio.
- O notebook deve importar funcoes de scripts/modulos compartilhados e nao duplicar sanitizacao/modelagem.

### Politica de Vazamento
- O modelo principal do Projeto 2 nao usa `Survival Months` como feature.
- `Survival Months` so pode aparecer em analise de sensibilidade/vazamento.
- `Status = Dead` e a classe positiva (`1`).

### Split e Avaliacao
- O Projeto 2 usa `treino / validacao / teste` para o ensemble.
- Pesos do ensemble devem ser derivados de metricas de validacao.
- O threshold do ensemble deve ser escolhido na validacao e congelado para o teste.
- Resultados finais devem distinguir claramente tabelas de validacao e teste.

### Metricas
- Falso negativo significa prever `Alive` quando o registro real e `Dead`.
- A avaliacao deve reportar falsos negativos, recall, precision, F2 e PR AUC.
- Acuracia isolada nao define modelo campeao em dataset medico desbalanceado.

### Explicabilidade e Robustez
- Explicabilidade global do Projeto 2 deve ser derivada de artefatos persistidos, nao de interpretacao verbal ad hoc.
- Curvas de calibracao, Brier score e tabela de estabilidade por seeds fazem parte da documentacao oficial do projeto.
- O neuro-fuzzy deve ser descrito como comparativo academico, nao como ANFIS completo nem modelo campeao.

### Artefatos Canonicos do Projeto 2
- Resultados principais: `model_comparison_no_leakage.csv`, `ensemble_test_summary.csv`, `neuro_fuzzy_comparison.csv`
- Artefatos metodologicos: `ensemble_validation_summary.csv`, `calibration_summary.csv`, `stability_summary.csv`
- Artefatos narrativos: `README.md`, `reports/relatorio_tecnico_projeto_2.md`, notebook e specs TLC

### EDA
- A EDA do Projeto 2 deve incluir dicionario de dados, perfil de metadados e analise de relacoes antes da modelagem.
- Artefatos canonicos: `DATA_DICTIONARY.md`, `metadata_profile.csv`, `numeric_relationships.csv`, `categorical_relationships.csv`.
