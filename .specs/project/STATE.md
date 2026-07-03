# Project State

## 🛑 Decisions Made
1. **Descarte de Bases Sintéticas**: Descartou-se a base de AVC devido a alertas de dados sintéticos sem comprovação clínica. Optou-se por Heart Failure (BMC) e Breast Cancer (SEER).
2. **Métrica de Avaliação**: Definido o F1-Score (em vez da Acurácia) devido ao forte desbalanceamento de classes em cenários de saúde.
3. **Restrição de Bibliotecas**: O Algoritmo Genético foi codificado 100% do zero em NumPy/Python puro, evitando dependências externas como `DEAP` ou `PyGAD`, garantindo transparência total e controle sobre o cromossomo para a avaliação acadêmica.
4. **Alinhamento com Ementa**:
   - Taxa de mutação ajustada para `0.005` a partir do feedback extraído da disciplina (NotebookLM).
   - Otimização do AG expandida para selecionar Topologia (além de Features).
   - Evitou-se SMOTE e Cross-Validation (K-Fold) pois o material não os cobra formalmente (e evitam-se perguntas desnecessárias da banca).
5. **Neuro-Fuzzy Cooperativo**: Aceito o modelo onde Lógica Fuzzy alimenta uma MLP. A queda de desempenho (25% F1-Score) será justificada no relatório como "Perda informacional por discretização sem calibragem por especialista".
6. **Revisão Spec-Driven do Projeto 2**: O Projeto 2 foi reestruturado em `.specs/features/trabalho-2-breast-cancer/` com spec, design e tasks. A fonte canônica do plano passa a ser essa feature TLC.
7. **Objetivo Corrigido do Breast Cancer**: O modelo principal prevê `Status = Dead` a partir de atributos disponíveis no diagnóstico. `Survival Months` fica fora do modelo principal por ser informação de acompanhamento posterior e potencial vazamento.
8. **Notebook por Projeto**: Mantida a convenção de um notebook Jupyter narrativo por projeto. O Projeto 2 agora tem `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`.
9. **EDA Antes de Modelagem**: O Projeto 2 passa a exigir dicionário de dados, perfil de metadados e análise de relações antes da modelagem. Os artefatos ficam em `projeto_2_neuro_fuzzy/docs/` e `projeto_2_neuro_fuzzy/reports/tables/`.
10. **Métrica Principal do Projeto 2**: Para o dataset Breast Cancer, a leitura principal prioriza falsos negativos, recall, F2 e PR AUC. Acurácia isolada não define o modelo campeão.
11. **Revisão Data Science do Projeto 1**: O Projeto 1 foi reclassificado de "concluído" para "implementado, validação final pendente" durante a revisão, e depois teve execução completa registrada. EDA, baseline, GA-MLP rápido e GA-MLP completo foram validados; ainda falta redigir a discussão final para relatório/apresentação.
12. **Fonte Canônica do Projeto 1**: A documentação rastreável do Projeto 1 passa a ser `.specs/features/projeto-1-genetico-neural/`, contendo spec, design e tasks.
13. **Notebook Único do Projeto 1**: O processo completo do Projeto 1 passa a ter notebook narrativo em `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb`, mantendo os scripts como fonte operacional.

## 🚧 Blockers / Limitations
- **Overfitting Evolutivo (Projeto 1)**: O dataset muito pequeno (299 linhas) causou a memorização dos dados de validação pelo AG, fazendo o F1 cair no teste cego. (Mitigado pela seção "Trabalhos Futuros" no relatório, propondo K-fold no fitness function).
- **Rastreabilidade do GA-MLP (Projeto 1)**: O script hibrido salva métricas completas e resultado estruturado. O modo rápido gerou `reports/tables/ga_mlp_results_quick.json`; o modo completo gerou `reports/tables/ga_mlp_results.json`; a comparação consolidada está em `reports/tables/model_comparison.csv`.
- **Kernel Jupyter Ausente (Projeto 1)**: O notebook foi criado e validado como JSON, mas `nbconvert --execute` não rodou porque o ambiente não possui kernel Jupyter registrado.
- **Trade-off do Ensemble (Projeto 2)**: O threshold 0.21 do ensemble reduziu falsos negativos para 16, mas elevou falsos positivos. Isso deve ser apresentado como escolha de sensibilidade, não como melhoria universal.
- **Vazamento por `Survival Months` (Projeto 2)**: A análise de sensibilidade com `Survival Months` melhora métricas, mas não deve ser vendida como predição em diagnóstico.

## 💡 Lessons Learned
- Sistemas híbridos não são garantias de ganho de performance. O Projeto 2 provou empiricamente que injetar regras heurísticas "amadoras" (Funções Triangulares sem oncologista) pode prejudicar severamente uma Rede Neural pura.
- Dicionário de dados e análise de metadados não são burocracia: no Projeto 2 eles expuseram problemas de schema (`T Stage `, `Reginol Node Positive`, `Single `) e risco de vazamento.
- Para datasets médicos desbalanceados, threshold tuning pode ser mais importante que trocar o algoritmo.
- Para a segunda avaliação, a qualidade do Projeto 1 depende menos de "ganhar" do baseline e mais de explicar corretamente a arquitetura híbrida, a comunicação GA -> MLP, o resultado frente a baseline simples e as limitações metodológicas.
- No Projeto 1, o GA-MLP completo não superou a Random Forest: F1 0.5000 contra 0.7059 e recall 0.3684 contra 0.6316. Isso deve ser apresentado como evidência de que o hibrido foi metodologicamente válido, mas o dataset pequeno favoreceu o modelo de árvores.
