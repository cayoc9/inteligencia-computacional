# Log de Auditoria do Projeto (T1)

Este arquivo registra o "passo a passo" real, incluindo falhas e aprendizados, para subsidiar a seção de "Discussão e Desafios" da apresentação final.

| Data | Etapa | Descrição da Atividade | Decisões/Dificuldades | Resultado |
| :--- | :--- | :--- | :--- | :--- |
| 08/05 | Setup | Organização da estrutura `.specs` | Decidido usar padrão Spec-Driven para rastreabilidade total de requisitos. | Estrutura Criada |
| 08/05 | Dados | Análise comparativa de datasets | Descartado *Heart Disease* (70% duplicatas) e *Mental Health* (Regressão). Escolhido *Sleep Health* (100k rows) para favorecer a Rede Neural. | Dataset Selecionado |
| 08/05 | Execução | Download e Verificação de Dados (T1-1) | Criado ambiente virtual `.venv` devido a restrições do sistema (PEP 668). Instalado pandas, scikit-learn, matplotlib e seaborn. | Dataset Baixado e Validado |
| 08/05 | Execução | Análise Exploratória (EDA) (T1-2) | Gerados gráficos de correlação e boxplots. Identificadas features chave: `sleep_quality`, `stress_score` e `work_hours`. | Insights da EDA registrados |
| 08/05 | Execução | Random Forest e Pré-processamento (T1-3/4/5) | Implementado pipeline com OneHotEncoder e StandardScaler. Realizado GridSearchCV (36 fits). Melhores parâmetros: depth=20, estimators=200. | RF Treinada (Acc: 74%) |
| 08/05 | Execução | Rede Neural MLP (T1-6/7/8) | Instalado TensorFlow. Implementada MLP (64-32-16) com Dropout (0.2). EarlyStopping parou em 24 épocas. | RN Treinada (Acc: 73.2%) |
| 08/05 | Documentação | Relatório de Rodada 1 | Consolidado sumário executivo, métricas comparativas e achados da EDA em `relatorio_rodada_1.md`. | Milestone Baseline Concluído |
| 08/05 | Execução | Rodada 2: Otimização RN (T1-7) | Criadas 3 novas features de interação. Aprofundada rede para 128-64-32-16 com BatchNormalization e ReduceLROnPlateau. | RN v2 Treinada (Acc: 73.36%) |

---

## Diário de Bordo Técnico

### Decisões de Arquitetura
- **08/05:** Escolha do dataset sintético-calibrado (Sleep Health) em vez de datasets reais pequenos (UCI). 
  - *Motivo:* Redes Neurais exigem volume. A "qualidade clínica" do dataset da Sleep Foundation/CDC, mesmo sintética, oferece um desafio de engenharia maior.
- **08/05:** Uso de Ambiente Virtual (`.venv`).
  - *Justificativa:* O sistema Linux (Ubuntu/Debian moderno) impede a instalação global de pacotes Python via pip (externally-managed-environment). O isolamento garante que o projeto seja reproduzível.
- **08/05:** Pipeline do Scikit-Learn.
  - *Justificativa:* O uso de `Pipeline` + `ColumnTransformer` evita o *data leakage* durante a validação cruzada, garantindo que o `StandardScaler` não "veja" dados de teste.
- **08/05:** Arquitetura MLP (64-32-16).
  - *Justificativa:* Iniciamos com uma estrutura piramidal simples para evitar overfitting imediato em 100k registros, dado que o problema de classificação binária não parece exigir redes extremamente profundas.
- **08/05 (Rodada 2):** Inclusão de BatchNormalization e Engenharia de Atributos.
  - *Justificativa:* BatchNormalization estabiliza o treino de redes mais profundas, enquanto as interações de features (ex: `stress * work_hours`) tentam extrair sinais não-lineares explícitos para o modelo.

### Erros e Dificuldades Encontradas
- **Dificuldade Técnica (Instalação):** Erro `externally-managed-environment` ao tentar instalar `matplotlib`. Resolvido com a criação de um `venv`.
- **Dificuldade Técnica (Versão Pandas):** Aviso de depreciação do `select_dtypes` no Pandas 3.0. 
  - *Ação:* Atualizado código para ser explícito.
- **Limitação de Hardware:** Treinamento da RN rodou apenas em CPU (Cuda not found). Como o dataset é de 100k e a rede é leve, o impacto foi mínimo.
- **Teto de Performance:** Notou-se que mesmo duplicando a complexidade da rede na Rodada 2, o ganho de acurácia foi irrisório (+0.13%). Isso indica que chegamos ao limite do sinal disponível nas features atuais.

### Resultados e Comparação
- **Random Forest (Campeã):** Acurácia 74.15% | ROC AUC 0.82.
- **Rede Neural (Runner-up):** Acurácia 73.36% (Rodada 2).
- **Conclusão para Relatório:** Para este problema específico de saúde com dados tabulares, a Random Forest provou ser mais eficiente, robusta e fácil de treinar do que a Rede Neural profunda.

### Pivotagens (Mudanças de Rumo)
- **Mudança de Foco:** Decidido encerrar a exploração de arquiteturas de Redes Neurais após os resultados da Rodada 2 mostrarem retornos decrescentes. O foco agora será na documentação final de alta qualidade para garantir a nota máxima na apresentação.
