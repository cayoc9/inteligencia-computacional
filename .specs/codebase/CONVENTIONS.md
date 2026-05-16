# Convenções do Projeto

## Organização de Arquivos

### Scripts Numerados (Pipeline)
Scripts na raiz seguem padrão `NN_nome_descritivo.py`:
- `01_check_data.py`: Inspeção inicial
- `02_eda.py`: Análise exploratória
- `03_random_forest.py`: Modelagem RF
- `04_neural_network.py`: Modelagem RN base
- `05_neural_network_optimized.py`: Modelagem RN otimizada

**Por que:** Numeração facilita ordem de execução e auditoria.

### Scripts de Suporte
Em `scripts/` para utilitários:
- `scripts/smoke_test.py`: Validação de ambiente
- `scripts/diagnose_model_limits.py`: Diagnóstico comparativo

### Diretórios de Artefatos
| Diretório | Conteúdo |
|---|---|
| `data/` | Dataset principal versionado + splits locais derivados |
| `models/` | Modelos treinados locais (.pkl, .h5, .keras), não versionados |
| `models/v2/` | Modelos locais da versão otimizada |
| `docs/` | Documentação técnica complementar, como dicionário de dados |
| `reports/figures/` | Visualizações usadas no relatório |
| `reports/fragmentos/` | Trechos de relatório (.md) |
| `reports/diagnostics/` | Diagnósticos (.csv, .json) |
| `reports/consolidados/` | Relatórios e camadas analíticas consolidadas |
| `notebooks/` | Notebooks de análise narrativa |

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
- **Nome:** `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`
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
- **Local:** `reports/fragmentos/`
- **Propósito:** Trechos reutilizáveis para relatório final
- **Exemplos:**
  - `01-resultados-comparativos.md`: Tabelas de métricas
  - `02-discussao-e-limitacoes.md`: Discussão crítica

## Execução

### Comandos de Validação
```bash
# Ambiente
python scripts/smoke_test.py

# Pipeline completo (na ordem)
python 01_check_data.py
python 02_eda.py
python 03_random_forest.py
python 04_neural_network.py
python 05_neural_network_optimized.py
python scripts/diagnose_model_limits.py
```

### Saída Esperada
- Scripts imprimem métricas no console
- Modelos salvos em `models/`
- Figuras salvas em `reports/figures/`
- Diagnósticos salvos em `reports/diagnostics/`

## Versionamento

### O Que Versionar
- ✅ Código (.py, .ipynb)
- ✅ Documentação (.md)
- ✅ Dataset (.csv em `data/`)
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
3. Validar: `python scripts/smoke_test.py`
4. Executar pipeline na ordem
5. Consultar `.specs/` para contexto e decisões

### Para Trabalhos Futuros
- Manter scripts como pipeline auditável
- Notebook único para narrativa (evitar fragmentação)
- Documentar decisões em `.specs/project/STATE.md`
- Congelar dependências: `pip freeze > requirements.lock.txt`
