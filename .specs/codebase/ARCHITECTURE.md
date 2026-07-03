# Arquitetura dos Sistemas Híbridos

## Projeto 1: Sistema Genético-Neural (GA-MLP)
- **Paradigma**: Otimização (Evolutivo + Conexionista).
- **Dataset**: `heart_failure_clinical_records_dataset.csv`
- **Fluxo**:
  1. O Algoritmo Genético gera indivíduos (Cromossomos de 17 bits).
  2. Bits [0:11] mascaram as features do dataset.
  3. Bits [12:16] são convertidos em número de neurônios (Topologia Oculta de 5 a 160).
  4. Uma MLP é instanciada e treinada no subconjunto de Treino.
  5. A MLP prevê o subconjunto de Validação. O F1-Score é retornado como *Fitness*.
  6. Pais são selecionados por Torneio (K=3), cruzam (1 ponto), sofrem mutação (0.5%) e repassam o melhor filho por Elitismo.

## Projeto 2: Neuro-Fuzzy Cooperativo (ANFIS Simplificado)
- **Paradigma**: Extração Semântica e Inferência (Fuzzy + Conexionista).
- **Dataset**: `Breast_Cancer.csv`
- **Fluxo**:
  1. O script Fuzzy lê as variáveis contínuas cruas (Idade, Tamanho, Nódulos).
  2. Funções Triangulares (*Trimf*) convertem os dados em 9 graus de pertinência (ex: Jovem, Adulto, Idoso).
  3. As variáveis categóricas recebem One-Hot Encoding.
  4. A matriz unida (Fuzzy + Categorical) alimenta um `MLPClassifier(100, 50)`.
  5. A rede ajusta os pesos sinápticos e atua como Base de Regras implícita para prever o risco de óbito.
