# Auditoria Critica - Projeto 2 Breast Cancer

**Objetivo:** mapear falhas minuciosas no processo de dados, riscos de raciocinio, roteiro de explicabilidade e perguntas provaveis da banca.  
**Escopo:** Projeto 2 escolhido para apresentacao da segunda avaliacao.  
**Fontes:** relatorio tecnico, specs, scripts, tabelas geradas e critica independente por subagente.  
**Data:** 2026-07-02

## Summary

O projeto e forte como auditoria de vazamento e comparacao critica de modelos em dados medicos tabulares, mas precisa evitar duas afirmacoes fortes demais: que prediz "no diagnostico" e que o ensemble e o melhor modelo final. A defesa mais segura e apresentar o trabalho como **classificacao de risco de obito a partir de variaveis clinico-patologicas registradas, sem informacao de acompanhamento (`Survival Months`)**, com threshold ajustado como analise de ponto operacional sensivel.

## Falhas Minuciosas Encontradas

### F1 - Horizonte temporal indefinido do alvo

**Severidade:** alta  
**Problema:** o alvo `Status = Dead` nao define "morreu ate quando". Como existe `Survival Months`, o problema original tem natureza de sobrevivencia/censura. Pacientes `Alive` podem estar vivos no ultimo acompanhamento, nao necessariamente livres do evento.  
**Impacto:** uma professora pode questionar se classificacao binaria e a formulacao correta.  
**Como mitigar na apresentacao:** dizer que, por limite do trabalho e por nao modelar censura, o projeto trata `Status` como desfecho observado no registro, nao como probabilidade temporal calibrada.  
**Como melhorar se houver tempo:** adicionar uma secao "Por que nao survival analysis?" e tratar Cox/Kaplan-Meier como trabalho futuro.

### F2 - "Diagnostico" pode estar temporalmente forte demais

**Severidade:** alta  
**Problema:** o relatorio dizia "atributos clinicos disponiveis no diagnostico", mas variaveis como `regional_node_examined`, `regional_node_positive`, `n_stage`, `6th_stage` e talvez `a_stage` podem depender de estadiamento clinico-patologico ou procedimento posterior.  
**Impacto:** risco de a banca apontar outro tipo de vazamento temporal, mesmo sem `Survival Months`.  
**Mitigacao:** trocar a narrativa para "variaveis clinico-patologicas registradas no dataset antes da informacao de acompanhamento".  
**Melhoria:** separar em dois cenarios: "pre-tratamento" vs "pos-estadiamento", se houver metadados suficientes.

### F3 - Threshold e pesos do ensemble foram escolhidos no conjunto de teste

**Severidade:** critica  
**Status atual:** corrigido em 2026-07-02.  
**Correcao aplicada:** `04_threshold_and_ensemble.py` agora usa split `treino / validacao / teste`; pesos do ensemble sao derivados do desempenho de validacao e o threshold final (`0.22`) e escolhido na validacao, depois congelado para o teste.  
**Risco residual:** ainda falta medir estabilidade por multiplas sementes ou validacao cruzada.

### F4 - Ensemble melhora recall por threshold, nao necessariamente por discriminacao

**Severidade:** alta  
**Evidencia:** PR AUC do ensemble no teste = 0.3196, menor que Logistic Regression = 0.3525, GradientBoosting = 0.3503 e SVM calibrado = 0.3439.  
**Impacto:** dizer que o ensemble e "melhor" seria logicamente fraco. Ele escolhe um limiar agressivo, mas nao separa melhor as classes globalmente.  
**Mitigacao:** apresentar o ensemble como "configuracao de alta sensibilidade", nao como modelo campeao.  
**Frase segura:** "O ensemble oferece um ponto de operacao com poucos falsos negativos, mas a regressao logistica manteve PR AUC superior; a escolha depende do custo de erro."

### F5 - Falsos positivos muito altos

**Severidade:** alta  
**Evidencia:** ensemble threshold 0.22 no teste: FP=320, FN=29, precision=0.2271.  
**Impacto:** quase 4 em cada 5 alertas positivos sao falsos. Isso pode ser indefensavel se apresentado como triagem clinica pronta.  
**Mitigacao:** explicar como ferramenta de triagem sensivel, nao diagnostico. Alertas positivos exigiriam avaliacao posterior.

### F6 - Uma unica divisao dos dados

**Severidade:** media-alta  
**Problema:** resultados dependem de `random_state=42` e um unico holdout. O teste tem cerca de 123 casos positivos; pequenas mudancas podem alterar recall/F2.  
**Impacto:** conclusoes quantitativas parecem mais fortes do que a evidencia suporta.  
**Mitigacao:** registrar como limitacao.  
**Melhoria:** validacao cruzada estratificada, bootstrap ou repeticao por sementes.

### F7 - Calibracao probabilistica nao verificada

**Severidade:** media  
**Status atual:** parcialmente mitigado.  
**Problema remanescente:** threshold 0.22 nao significa necessariamente risco real de 22%; apesar de agora existirem `Brier score`, `calibration_summary.csv` e `calibration_curves.png`, isso ainda nao equivale a validacao clinica de risco absoluto.  
**Impacto:** se a apresentacao falar "probabilidade", a banca pode cobrar calibracao.  
**Mitigacao:** usar "score/probabilidade estimada pelo modelo" e nao "risco real calibrado".  
**Melhoria:** recalibrar com isotonic/platt em validacao cruzada, se houver tempo.

### F8 - Features derivadas calculadas antes do split

**Severidade:** baixa-media  
**Evidencia:** `add_clinical_features` e aplicado no DataFrame inteiro antes do split.  
**Analise:** as features derivadas sao linha-a-linha (`node_positive_ratio`, flags, multiplicacao), sem aprender estatisticas globais. Portanto, nao ha vazamento estatistico evidente.  
**Risco:** a banca pode perguntar; responder que sao transformacoes deterministicas por paciente, nao ajustadas no conjunto completo.

### F9 - Neuro-fuzzy fraco como contribuicao principal

**Severidade:** media  
**Problema:** e fuzzificacao manual + MLP, nao ANFIS completo; metricas baixas: recall=0.2683, PR AUC=0.2365, FN=90.  
**Impacto:** nao deve ser vendido como "o hibrido vencedor".  
**Mitigacao:** manter como comparativo academico que mostra limitacao de regras fuzzy manuais sem especialista.

### F10 - Interpretabilidade ainda muito baseada em tabelas, nao em atribuicao de modelo

**Severidade:** media  
**Status atual:** parcialmente mitigado.  
**Evidencia nova:** foram gerados `logistic_regression_top_coefficients.csv` e `logistic_regression_permutation_importance.csv`.  
**Impacto residual:** a pergunta "por que este paciente especifico foi classificado assim?" ainda nao esta plenamente respondida, porque a interpretabilidade continua global, nao local.  
**Melhoria:** SHAP ou analise local por instancia.

## Roteiro de Explicabilidade

### 1. Historia do problema

Comecar dizendo que o projeto nasceu com uma pergunta aparentemente simples: prever `Status = Dead` em Breast Cancer. A primeira descoberta importante foi que uma coluna (`Survival Months`) carregava informacao de acompanhamento posterior e contaminava a previsao se usada como feature.

**Mensagem:** antes de escolher modelo, foi necessario corrigir a pergunta.

### 2. Historia dos dados

Mostrar que o dataset bruto tinha 4024 linhas e 16 colunas; apos remover uma duplicata, ficou com 4023 linhas. A classe positiva `Dead` tem 616 casos, aproximadamente 15,3%.

**Explicabilidade:** o desbalanceamento torna acuracia enganosa; por isso o projeto prioriza recall, F2, PR AUC e falsos negativos.

### 3. Decisao de vazamento

Explicar que `Survival Months` foi removido do modelo principal porque responde a outra pergunta: acompanhamento/sobrevida, nao predicao sem follow-up.

**Forma defensavel:** "Nao estamos dizendo que `Survival Months` e irrelevante; estamos dizendo que ele nao pode entrar no modelo principal sem contaminar a tarefa."

### 4. Decisao sobre variaveis clinico-patologicas

Evitar dizer "diagnostico inicial" se nao puder provar disponibilidade temporal. Usar:

> "variaveis clinico-patologicas registradas no dataset, excluindo informacao de acompanhamento."

### 5. Historia dos baselines

Mostrar que modelos com alta acuracia podem falhar na classe `Dead`:

- SVM calibrado: accuracy 0.8522, recall 0.0732, FN 114.
- HistGradientBoosting: accuracy 0.8224, recall 0.1463, FN 105.
- Logistic Regression: accuracy 0.6807, recall 0.6098, FN 48.

**Mensagem:** o "melhor" depende do custo do erro.

### 6. Historia do ensemble

Explicar que o ensemble combina modelos tabulares e usa threshold baixo para operar em alta sensibilidade. Resultado:

- threshold 0.22, escolhido na validacao;
- recall 0.7642 no teste;
- FN 29;
- FP 320;
- precision 0.2271;
- PR AUC 0.3196.

**Mensagem segura:** "Este e um ponto operacional sensivel, nao um classificador clinico pronto."

### 7. Historia do neuro-fuzzy

Explicar que o neuro-fuzzy foi incluido para dialogar com a disciplina, mas como comparativo:

- funcoes triangulares manuais;
- MLP como motor de inferencia;
- nao e ANFIS completo;
- nao superou os tabulares.

**Mensagem:** sistemas hibridos exigem calibragem e conhecimento especialista; hibridizar nao garante ganho.

### 8. Conclusao critica

Fechar com:

> O principal resultado nao e "um modelo campeao", mas uma trilha metodologica: corrigimos vazamento, documentamos dados, comparamos modelos sob metricas adequadas e mostramos trade-offs entre sensibilidade e falsos positivos.

## Perguntas Provaveis da Professora e Respostas Seguras

| Pergunta | Resposta segura |
|---|---|
| Qual e o horizonte temporal da predicao? | O dataset foi tratado como classificacao do desfecho observado, nao como modelo temporal. Como existe censura/tempo de sobrevivencia, survival analysis e trabalho futuro. |
| Por que nao usar `Survival Months`? | Porque e informacao de acompanhamento posterior; usar essa coluna melhora metricas, mas responde uma pergunta contaminada. |
| Essas features estao disponiveis no diagnostico? | Melhor formulacao: variaveis clinico-patologicas registradas no dataset, excluindo follow-up. A disponibilidade temporal precisa de metadado clinico adicional. |
| O threshold foi escolhido no teste? | Nao. A versao corrigida escolhe pesos e threshold na validacao e reporta o ensemble final no teste intocado. |
| Por que aceitar 320 falsos positivos? | Nao e uma decisao clinica final; e um experimento de alta sensibilidade para reduzir falsos negativos. A aceitabilidade depende do custo operacional. |
| Se o PR AUC do ensemble e menor que o da regressao logistica, por que usar ensemble? | O ensemble nao e melhor globalmente; ele foi usado para explorar um ponto de recall alto. Para discriminacao geral, Logistic Regression/SVM têm argumento forte por PR AUC. |
| O modelo esta calibrado? | Foi adicionada analise de Brier score e curva de calibracao, mas isso ainda nao significa risco clinico absoluto calibrado. |
| O neuro-fuzzy e ANFIS? | Nao. E fuzzy manual + MLP, um modelo cooperativo; isso foi explicitado para nao exagerar a contribuicao. |

## Recomendacao de Ajuste Antes da Apresentacao

### Obrigatorio

1. Trocar "predicao no diagnostico" por "predicao/classificacao de risco com variaveis clinico-patologicas registradas, sem follow-up".
2. Dizer que o ensemble com threshold 0.22 e um ponto operacional selecionado na validacao, nao o melhor discriminador global.
3. Apresentar Logistic Regression como baseline forte de sensibilidade e PR AUC.
4. Tratar neuro-fuzzy como comparativo academico, nao como modelo principal.

### Forte se houver tempo

1. Avaliar estabilidade por multiplas sementes ou validacao cruzada.
2. Ampliar calibracao para metodo de recalibracao explicito.
3. Adicionar explicabilidade local por instancia.
4. Adicionar slide "Limites assumidos" antes das conclusoes.

## Bottom Line

O projeto e apresentavel, mas a narrativa deve continuar focada em "trilha critica de modelagem, removendo vazamento e analisando trade-offs". A falha mais grave do ensemble foi corrigida; as limitacoes relevantes agora sao estabilidade, horizonte temporal e calibracao clinica.
