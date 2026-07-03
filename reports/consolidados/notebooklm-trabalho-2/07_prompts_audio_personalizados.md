# Prompts Personalizados de Audio - NotebookLM

Use estes prompts para gerar audios curtos, focados e numerados. Cada prompt assume que os arquivos `01` a `06` ja foram carregados no NotebookLM.

## 1. Panorama geral do projeto

**Prompt**

Crie um audio em portugues do Brasil, com tom didatico e tecnico, explicando o Projeto 2 da disciplina de Inteligencia Computacional. Estruture em: problema, objetivo, datasets usados, mudanca do SEER para o METABRIC, principais resultados e conclusao final. Evite floreio e deixe claro o que foi baseline corrigido e o que virou trilha canonica.

## 2. Erro metodologico original

**Prompt**

Crie um audio curto, em portugues do Brasil, explicando apenas o erro metodologico original do Projeto 2, por que `Survival Months` era problematico no modelo principal, como o ensemble estava fragil antes, e como esses problemas foram corrigidos. O foco deve ser em clareza metodologica e defesa oral.

## 3. EDA, dicionario de dados e saneamento

**Prompt**

Crie um audio em portugues do Brasil explicando a importancia do saneamento, do dicionario de dados e da EDA com metadados e relacoes no Projeto 2. Mostre por que isso nao foi burocracia e como essa etapa ajudou a detectar vazamento, inconsistencias de schema e escolhas ruins de modelagem.

## 4. Resultados do SEER corrigido

**Prompt**

Crie um audio em portugues do Brasil focado apenas na trilha SEER corrigida. Explique o papel dela como baseline educacional, os principais modelos, o resultado da Logistic Regression, o resultado do ensemble com threshold 0.22 e o trade-off entre recall e falsos positivos.

## 5. Limites do SEER

**Prompt**

Crie um audio em portugues do Brasil explicando por que o SEER, mesmo corrigido, continuou sendo limitado para melhoria continua. Destaque profundidade clinica, ausencia de biomarcadores, limite pedagogico e por que isso motivou a busca por outra base.

## 6. Justificativa da troca para o METABRIC

**Prompt**

Crie um audio em portugues do Brasil explicando por que o METABRIC foi escolhido como evolucao do projeto. Compare com o SEER em termos de tratamento, biomarcadores, subtipo molecular, potencial de feature engineering e valor para a defesa do trabalho.

## 7. Resultados do METABRIC

**Prompt**

Crie um audio em portugues do Brasil focado apenas na trilha METABRIC. Explique o melhor baseline individual, o ensemble com threshold 0.16, o significado de quase zerar falsos negativos e o que ainda foi pago em falsos positivos.

## 8. Ensemble e trade-offs

**Prompt**

Crie um audio em portugues do Brasil explicando o que e o ensemble do Projeto 2, como os pesos e thresholds foram escolhidos na validacao, por que isso importa metodologicamente e como interpretar o trade-off entre sensibilidade e falsos positivos sem exagerar conclusoes.

## 9. Papel do neuro-fuzzy

**Prompt**

Crie um audio em portugues do Brasil explicando o papel do neuro-fuzzy no Projeto 2. Diferencie neuro-fuzzy cooperativo de ANFIS, explique por que ele foi mantido no trabalho e por que ele nao foi o melhor modelo empiricamente.

## 10. Boas praticas de ciencia de dados aplicadas

**Prompt**

Crie um audio em portugues do Brasil resumindo as boas praticas de ciencia de dados aplicadas no Projeto 2: contrato de dados, EDA, leakage policy, split treino-validacao-teste, tuning sem contaminacao do teste, explicabilidade, calibracao, estabilidade e documentacao viva.

## 11. Limitacoes e trabalhos futuros

**Prompt**

Crie um audio em portugues do Brasil explicando com honestidade as limitacoes do Projeto 2 e os trabalhos futuros. Inclua survival analysis formal, explicabilidade local, robustez com validacao cruzada e validacao externa. O tom deve ser tecnico e sem vender alem do que o trabalho realmente entrega.

## 12. FAQ para a banca

**Prompt**

Crie um audio em portugues do Brasil em formato de perguntas e respostas, simulando uma banca de Inteligencia Computacional. Inclua: por que nao usar acuracia como metrica principal, por que `Survival Months` foi removido, se o neuro-fuzzy e ANFIS, por que o ensemble com mais falsos positivos pode ser valido e por que o METABRIC virou a trilha canonica.
