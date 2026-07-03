# Project Vision: Inteligência Computacional - Atividade 2

## 🎯 Goal
Implementar e avaliar Sistemas Híbridos de Inteligência Computacional para bases de dados médicas validadas (dados reais), com o objetivo de entregar a "Atividade 2" da disciplina de mestrado.

## 👥 Audience
- **Professora da disciplina**: Avaliadora rigorosa focada em justificativas metodológicas sólidas.
- **Banca avaliadora**: Espera rigor científico, tratamento correto de overfitting/desbalanceamento e explicações de como os módulos híbridos interagem.

## 🚀 Key Features
1. **Projeto 1 (Híbrido Genético-Neural)**: Usa Algoritmo Genético construído do zero em NumPy para atuar como meta-otimizador de uma Rede Neural (MLP), selecionando *features* e definindo o número ideal de neurônios ocultos simultaneamente.
2. **Projeto 2 (Neuro-Fuzzy Cooperativo)**: Fuzzifica variáveis contínuas cruas através de funções de pertinência triangulares e utiliza uma RNA como motor de inferência no lugar da matriz clássica de regras manuais.
3. **Análise Metodológica (NotebookLM/EDA)**: Revisão cruzada da teoria da aula para garantir alinhamento perfeito de hiperparâmetros (mutação, validação, baseline).

## 🛑 Non-Goals
- Não implementar algoritmos de *Cross-Validation* (K-Fold) de forma embutida, pois não compõe a exigência primária da disciplina e aumentaria o custo computacional além do razoável para a entrega (ficará como "Trabalhos Futuros").
- Não utilizar geração de dados sintéticos (SMOTE), priorizando a métrica F1-Score para avaliação em cenários desbalanceados.
- Não utilizar *datasets* puramente sintéticos do Kaggle (como o Stroke Prediction); foco 100% em bases confirmadas pelo NIH/CDC/BMC.
