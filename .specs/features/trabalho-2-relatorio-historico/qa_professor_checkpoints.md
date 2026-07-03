# QA Professorial - Relatorio Historico do Trabalho 2

## P1 - Evidencia

### Pergunta
De onde veio cada numero relevante do Projeto 2?

### Resposta
- SEER baseline explicavel sem vazamento: [projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy/docs/PROJECT_EXECUTION_SUMMARY.md) e [projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage.csv](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage.csv)
- SEER ensemble corrigido: [projeto_2_neuro_fuzzy/reports/tables/ensemble_test_summary.csv](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy/reports/tables/ensemble_test_summary.csv)
- METABRIC melhor modelo individual: [projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/model_comparison_no_leakage.csv](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/model_comparison_no_leakage.csv)
- METABRIC ensemble corrigido: [projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/ensemble_test_summary.csv](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/ensemble_test_summary.csv)

### Pergunta
Isso veio de teste ou validacao?

### Resposta
- Os numeros principais de comparacao final devem vir do teste.
- Threshold e pesos do ensemble vieram da validacao separada.
- Quando um numero vier de validacao, isso deve ser rotulado explicitamente como numero de selecao, nao de desempenho final.

### Pergunta
Isso veio do repositorio ou de uma sessao de agente?

### Resposta
- Resultado final, metrica e status de implementacao: repositorio.
- Sequencia de decisao, bifurcacoes, pedidos do usuario e racional de conducao: sessoes de agentes.
- Regra de desempate: o repositorio prevalece.

### Divergencias identificadas e tratadas

1. **ID de sessao Codex truncado na spec inicial**
   - Forma incorreta anterior: `019f255f-88a8-7a81-b002-957841c027`
   - Forma existente no historico local: `019f255f-88a8-7a81-b002-957841c02760`
   - Acao: corrigido nas specs da feature historica.

2. **SEER como "base canonica" no relatorio antigo de execucao**
   - O [relatorio_execucao.md](/mnt/storage/Documentos/02%20-%20Responsabilidades/ufpa%20-%20mestrado/Disciplinas/Inteligencia%20Computacional/.specs/features/trabalho-2-breast-cancer/relatorio_execucao.md) ainda descreve a trilha SEER como base canonica do Projeto 2 em seu contexto original.
   - Leitura correta atual: SEER e baseline corrigido v1; METABRIC e evolucao canonica v2.
   - Acao: manter o documento antigo como registro historico e usar a feature METABRIC v2 para a leitura canonica atual.

## P2 - Coerencia metodologica

### Pergunta
Qual era o erro metodologico original?

### Resposta
O erro mais grave era usar `Survival Months` na pergunta principal e, em etapa posterior, ajustar pesos e threshold do ensemble com contaminacao do teste. Isso enfraquecia a defesa do experimento como classificacao clinica tabular auditavel.

### Pergunta
Em que momento ele foi corrigido?

### Resposta
Foi corrigido ao longo da reestruturacao spec-driven consolidada em 2026-07-02 e 2026-07-03, quando:
- `Survival Months` passou a ser excluido do modelo principal e mantido apenas como analise de sensibilidade;
- o ensemble passou a usar `treino / validacao / teste`;
- a trilha ganhou dicionario de dados, EDA com metadados, explicabilidade, calibracao e estabilidade.

### Pergunta
Por que o METABRIC entrou?

### Resposta
Porque o dataset SEER corrigido continuava limitado em profundidade clinica para a ambicao de melhoria continua. O METABRIC adiciona tratamento, biomarcadores e subtipo molecular, elevando o teto pedagogico e analitico do projeto.

### Pergunta
O que mudou e o que nao mudou na pergunta do projeto?

### Resposta
- **Nao mudou**: continua sendo um problema de classificacao supervisionada em saude, com foco em risco de obito e avaliacao de modelos hibridos/ensemble.
- **Mudou**: a qualidade do dataset e o rigor metodologico da trilha evoluida; a v2 deixa de ser so correcao de pipeline e passa a ser melhoria de base e de capacidade explicativa.

## Status da Fase 1

- P1 evidencias reconciliadas
- P2 coerencia metodologica respondida
- Fase 1 apta para avancar para comparacao e tese

## P3 - Justica comparativa

### Pergunta
Ha risco de cherry-picking ao trocar do SEER para o METABRIC?

### Resposta
O risco existe se a narrativa escondesse o SEER. Isso nao acontece aqui, porque:
- o SEER foi mantido como baseline corrigido;
- a troca de dataset foi justificada documentalmente;
- a comparacao continua mostrando limites e trade-offs nas duas trilhas.

### Pergunta
Os targets sao comparaveis o bastante para a narrativa?

### Resposta
Sim, no nivel em que a narrativa esta sendo feita: ambas as trilhas foram enquadradas como classificacao supervisionada de obito observado no dataset. O que muda e a riqueza da base, nao o enquadramento geral do problema.

### Pergunta
O ganho veio do modelo ou da base?

### Resposta
Veio dos dois, mas o componente dominante foi a base. O pipeline corrigido existe em ambas as trilhas; o salto maior aparece quando a base passa a incluir informacao clinica e molecular melhor.

### Pergunta
Por que a troca melhora o valor pedagogico e clinico?

### Resposta
Porque permite discutir feature engineering, explicabilidade e trade-offs sobre um conjunto de variaveis mais plausivel para risco oncológico do que o SEER original.

## P4 - Perguntas de banca

### Por que nao usar acuracia como metrica principal?

- **Resposta curta**: porque o problema e desbalanceado e o custo de falso negativo e mais relevante.
- **Resposta longa**: em saude, perder casos de obito potencial pesa mais do que inflar acuracia acertando a classe majoritaria. Por isso recall, F2, PR AUC e falsos negativos foram priorizados.

### Por que `Survival Months` foi removido?

- **Resposta curta**: porque e informacao de acompanhamento posterior e introduz vazamento conceitual.
- **Resposta longa**: se a pergunta principal e predicao com base em variaveis clinicas registradas, usar tempo de sobrevida observado desloca a tarefa para outra pergunta. Ele foi mantido apenas como sensibilidade para mostrar esse efeito.

### O neuro-fuzzy e ANFIS?

- **Resposta curta**: nao.
- **Resposta longa**: o que foi implementado e um modelo cooperativo de fuzzificacao manual com MLP, util para a disciplina, mas nao um ANFIS completo com aprendizagem de regras e parametros fuzzy integrados.

### Por que um ensemble com mais falsos positivos ainda pode ser valido?

- **Resposta curta**: porque o objetivo operacional pode ser reduzir falsos negativos.
- **Resposta longa**: quando se trabalha com risco clinico, pode ser aceitavel aumentar alertas falsos se isso praticamente elimina casos perdidos. Esse e o sentido do threshold baixo no ensemble.

### Quais limitacoes precisam ser assumidas sem maquiagem?

- **Resposta curta**: dataset publico, ausencia de validacao clinica externa e falta de survival analysis formal.
- **Resposta longa**: o projeto e forte como exercicio metodologico e comparativo, mas nao deve ser vendido como sistema clinico pronto ou como estudo de prognostico temporal completo.

## P5 - Prontidao final

### Check final de coerencia

- O relatorio historico usa o repositorio como verdade final.
- A apresentacao deve usar a mesma tese central do relatorio.
- O artigo precisa manter a mesma leitura de baseline corrigido versus evolucao canonica.
- O audio deve simplificar sem distorcer a hierarquia das fontes e dos resultados.

### Riscos residuais

1. Exagerar o METABRIC como se fosse comparacao perfeitamente controlada de benchmark.
2. Tratar o ensemble como melhor modelo universal em vez de ponto operacional.
3. Apresentar o neuro-fuzzy como ANFIS.
4. Sugerir uso clinico real sem validacao externa.

### O que nao deve ser exagerado na defesa

- generalizacao clinica;
- causalidade;
- superioridade absoluta do ensemble;
- comparabilidade perfeita entre datasets heterogeneos.
