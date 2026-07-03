# Roadmap: Inteligência Computacional - Atividade 2

## 📝 Phase 1: Setup & Validação Teórica (✅ Concluído)
- [x] Extração de temas da disciplina (PDFs).
- [x] Geração de Podcasts de revisão via NotebookLM (8 episódios gravados).
- [x] Escolha de Datasets Reais (Descarte do dataset de AVC devido a alertas de integridade; seleção de Heart Failure e Breast Cancer - SEER).

## 🔬 Phase 2: Projeto 1 - Genético-Neural (🟡 Implementado, validação final pendente)
- [x] Divisão Holdout (Treino/Validação/Teste) do dataset Heart Failure.
- [x] Implementação do baseline (Random Forest e MLP simples).
- [x] Implementação de Algoritmo Genético do zero (Numpy) para Feature Selection.
- [x] Expansão do cromossomo do AG para Topologia (seleção simultânea de Neurônios e Features).
- [x] Calibração fina da Taxa de Mutação (0.005) baseado na ementa da professora.
- [x] Realização de EDA (Análise Exploratória) com Heatmaps e Boxplots.
- [x] Registro TLC-Spec-Driven em `.specs/features/projeto-1-genetico-neural/`.
- [x] Parametrização auditável do GA-MLP com saída JSON e modo rápido.
- [x] Notebook único do processo em `projeto_1_genetico_neural/notebooks/projeto_1_genetico_neural_ga_mlp.ipynb`.
- [x] Execução completa do GA-MLP sem `--quick` com resultados persistidos.
- [x] Comparação final baseline vs híbrido em tabela rastreável.
- [ ] Discussão crítica de ganho/perda, overfitting evolutivo e trabalhos futuros.

## 🧠 Phase 3: Projeto 2 - Breast Cancer Survival Risk (✅ Revisado e Executado)
- [x] Divisão Holdout (Treino/Validacao/Teste) do dataset Breast Cancer.
- [x] Fuzzificação manual via Funções de Pertinência Triangulares.
- [x] One-Hot Encoding das variáveis categóricas.
- [x] Treinamento da RNA como motor de inferência.
- [x] Análise crítica acadêmica da queda de desempenho devido à perda informacional na discretização sem calibragem especialista.
- [x] Registro TLC-Spec-Driven em `.specs/features/trabalho-2-breast-cancer/`.
- [x] Revisão do objetivo testado: `Survival Months` removido do modelo principal por risco de vazamento/follow-up.
- [x] Sanitização centralizada do dataset Breast Cancer.
- [x] Dicionário de dados específico em `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md`.
- [x] EDA com metadados e relações (`metadata_profile.csv`, `numeric_relationships.csv`, `categorical_relationships.csv`).
- [x] Notebook narrativo próprio em `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb`.
- [x] Suite de modelos tabulares sem vazamento e análise de sensibilidade com `Survival Months`.
- [x] Ensemble ponderado com pesos e threshold escolhidos na validacao e reporte final no teste intocado.
- [x] Neuro-fuzzy mantido como comparativo acadêmico, não como modelo campeão.
- [x] Explicabilidade da Logistic Regression e calibração comparativa adicionadas ao pipeline.
- [x] Otimizações adicionais no pipeline SEER: novas features clínicas, imputação robusta, cenários de threshold e métricas de calibração/utilidade.
- [x] Fork clínico METABRIC criado e validado em `projeto_2_neuro_fuzzy_metabric_clinico/`.
- [x] Notebook próprio do fork METABRIC em `projeto_2_neuro_fuzzy_metabric_clinico/notebooks/projeto_2_metabric_clinico.ipynb`.
- [x] Feature canônica da evolução METABRIC registrada em `.specs/features/trabalho-2-breast-cancer-metabric/`.
- [x] Auditoria explícita de boas práticas de ciência de dados consolidada para SEER v1 e METABRIC v2.

## 📦 Phase 4: Documentação Final (Em andamento)
- [x] Relatório Técnico Científico gerado em Markdown.
- [x] Guia de Ação e Roteiro Metodológico.
- [x] Registro TLC-Spec-Driven (.specs).
- [x] Relatório técnico do Projeto 2 em `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`.
- [x] Relatório de execução do Trabalho 2 em `.specs/features/trabalho-2-breast-cancer/relatorio_execucao.md`.
- [x] Relatório técnico do fork METABRIC em `projeto_2_neuro_fuzzy_metabric_clinico/reports/relatorio_tecnico_projeto_2_metabric.md`.
- [x] Checklist de aderência à segunda avaliação em `.specs/project/TRABALHO_2_AVALIACAO_CHECKLIST.md`.
- [x] Review de boas práticas de ciência de dados em `.specs/project/TRABALHO_2_DATA_SCIENCE_BEST_PRACTICES_REVIEW.md`.
- [x] Feature TLC do relatório histórico canônico registrada em `.specs/features/trabalho-2-relatorio-historico/`.
- [x] Relatório técnico final consolidado do Projeto 2 em `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md`.
- [x] Roteiro final de apresentação do Projeto 2 em `reports/consolidados/roteiro-final-apresentacao-trabalho-2.md`.
- [x] Pacote NotebookLM do Projeto 2 com fontes e prompts numerados em `reports/consolidados/notebooklm-trabalho-2/`.
- [x] Notebook final do Trabalho 2 criado via CLI `notebooklm` com 12 audios concluidos.
- [x] Template inicial do artigo adaptado a partir de `docs/template/Sleep_Health/` para `docs/template/Trabalho_2_Breast_Cancer/`.
- [x] PDF do artigo reproduzido via `xelatex` em container e salvo como `docs/template/Trabalho_2_Breast_Cancer/artigo_final_trabalho_2.pdf`.
- [ ] Relatório técnico do Projeto 1 revisado com base na spec `projeto-1-genetico-neural`.
- [ ] Revisão final do artigo no Overleaf com emails, metadados bibliograficos, figuras/tabelas e limite de paginas.
- [x] Geração do PDF base do artigo.
- [ ] Conversão do roteiro em slides finais.
- [ ] Conferência qualitativa dos audios NotebookLM concluídos e definição da ordem de escuta.
- [ ] Apresentação/Defesa.
