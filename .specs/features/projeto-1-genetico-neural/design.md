# Design: Projeto 1 - Sistema Genetico-Neural GA-MLP

## Arquitetura

O Projeto 1 usa uma arquitetura hibrida do tipo **Genetico-Neural**:

1. O Algoritmo Genetico cria uma populacao de cromossomos.
2. Cada cromossomo representa uma candidata de modelagem.
3. Os primeiros bits selecionam features do dataset.
4. Os bits finais definem a topologia da MLP, especificamente o numero de neuronios ocultos.
5. Para cada individuo, uma MLP e treinada no conjunto de treino.
6. A MLP e avaliada no conjunto de validacao.
7. O F1-Score da validacao vira fitness do individuo.
8. Selecao por torneio, crossover, mutacao e elitismo criam novas geracoes.
9. A melhor configuracao e treinada em treino+validacao e avaliada no teste cego.

## Componentes

| Componente | Arquivo | Responsabilidade |
|---|---|---|
| Dataset | `projeto_1_genetico_neural/dataset/heart_failure_clinical_records_dataset.csv` | Base publica de insuficiencia cardiaca |
| EDA | `projeto_1_genetico_neural/eda_heart_failure.py` | Ausentes, boxplots e correlacao |
| Baseline | `projeto_1_genetico_neural/baseline.py` | Random Forest e MLP com GridSearchCV |
| Hibrido | `projeto_1_genetico_neural/hybrid_ga_mlp.py` | GA para selecao de features e topologia da MLP |

## Codificacao do Cromossomo

O cromossomo possui `NUM_FEATURES + 5` bits.

- Bits de features: ligam/desligam cada atributo de entrada.
- Bits de topologia: codificam um inteiro convertido para neuronios ocultos via `(decimal + 1) * 5`, resultando em faixa de 5 a 160 neuronios.

Essa escolha e defensavel para a disciplina porque torna visivel a comunicacao entre paradigma evolutivo e conexionista: o GA nao substitui o aprendizado da MLP, mas escolhe a configuracao estrutural que a MLP ira usar.

## Operadores Evolutivos

| Operador | Implementacao atual | Avaliacao |
|---|---|---|
| Inicializacao | Populacao aleatoria, evitando individuo sem features | Adequado |
| Fitness | F1-Score no conjunto de validacao | Adequado ao desbalanceamento |
| Selecao | Torneio com 3 competidores | Adequado e simples de explicar |
| Crossover | Um ponto | Adequado ao cromossomo binario |
| Mutacao | Bit flip com taxa 0.005 | Aderente ao material, mas deve ser justificada |
| Elitismo | Melhor individuo preservado | Adequado para nao perder a melhor solucao |

## Avaliacao

### Baseline validado localmente em 2026-07-02

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.8333 | 0.8000 | 0.6316 | 0.7059 | 0.9101 |
| MLP | 0.7167 | 0.5714 | 0.4211 | 0.4848 | 0.7754 |

### Hibrido GA-MLP

O codigo implementa a avaliacao final e salva resultados estruturados. Na revisao de 2026-07-02, o modo rapido persistiu `reports/tables/ga_mlp_results_quick.json` e o modo completo persistiu `reports/tables/ga_mlp_results.json`.

| Modo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| GA-MLP quick | 0.7833 | 0.7143 | 0.5263 | 0.6061 | 0.8472 |
| GA-MLP full | 0.7667 | 0.7778 | 0.3684 | 0.5000 | 0.7766 |

## Comparacao Contra Baseline

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.8333 | 0.8000 | 0.6316 | 0.7059 | 0.9101 |
| MLP | 0.7167 | 0.5714 | 0.4211 | 0.4848 | 0.7754 |
| GA-MLP full | 0.7667 | 0.7778 | 0.3684 | 0.5000 | 0.7766 |

Leitura: o GA-MLP completo foi ligeiramente superior a MLP em F1 e ROC AUC, mas perdeu para Random Forest em todas as metricas principais de teste, especialmente recall e F1. A defesa metodologica deve enfatizar que o hibrido cumpre o objetivo academico de combinar paradigmas e expor trade-offs, nao que ele e o melhor classificador para este dataset pequeno.

## Riscos Metodologicos

1. **Amostra pequena:** 299 linhas tornam o fitness instavel.
2. **Overfitting evolutivo:** o AG pode memorizar o conjunto de validacao ao longo das geracoes.
3. **Sem multiplas sementes:** uma unica semente nao mede estabilidade.
4. **Sem K-fold no fitness:** decisao aceitavel para prazo, mas deve ser apresentada como limitacao.
5. **Metricas incompletas no hibrido:** o script atual imprime apenas accuracy e F1.

## Melhorias de Design Necessarias

1. Opcional: repetir com 3 a 5 sementes e reportar media/desvio.
2. Registrar kernel Jupyter para executar o notebook por `nbconvert`.
3. Transformar a comparacao em texto final de relatorio/apresentacao.
