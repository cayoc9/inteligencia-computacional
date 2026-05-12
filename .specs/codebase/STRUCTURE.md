# Estrutura do Projeto

## Scripts Principais
- `01_check_data.py`: inspeção básica do dataset, nulos, duplicatas e distribuição do target.
- `02_eda.py`: EDA com correlações e geração de figuras em `reports/figures/`.
- `03_random_forest.py`: pipeline de pré-processamento, Random Forest, `GridSearchCV`, métricas e persistência do modelo.
- `04_neural_network.py`: MLP baseline com TensorFlow/Keras, split estratificado e avaliação.
- `05_neural_network_optimized.py`: MLP v2 com feature engineering, batch normalization, dropout e scheduler de learning rate.

## Notebook Principal
- `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`: notebook único com contexto, EDA, preparação dos dados, Random Forest, MLP baseline, MLP otimizada, comparação final e síntese para relatório.

## Fragmentos de Relatório
- `reports/fragmentos/01-resultados-comparativos.md`: trecho de resultados comparativos.
- `reports/fragmentos/02-discussao-e-limitacoes.md`: trecho de discussão, limitações e conclusão interpretativa.

## Documentação Viva
- `.specs/project/PROJECT.md`: visão do projeto da disciplina.
- `.specs/project/ROADMAP.md`: plano dos trabalhos.
- `.specs/project/STATE.md`: decisões e status atual.
- `.specs/features/trabalho-1/`: requisitos, tarefas, relatórios de rodada e log de execução.

## Observação
A estrutura agora combina um pipeline executável por scripts com um notebook único para análise narrativa e apresentação dos resultados.
