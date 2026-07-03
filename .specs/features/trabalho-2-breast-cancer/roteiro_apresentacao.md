# Roteiro de Apresentacao

## Estrutura Geral

1. Abertura e problema.
2. Escolha do tema e do dataset.
3. Limpeza, sanitizacao e EDA.
4. Feature engineering e primeira rodada de modelos.
5. Limites encontrados no SEER.
6. Mudanca para o fork METABRIC.
7. Refinamentos tecnicos.
8. Comparacao final e conclusao.

## Fala Sugerida

### 1. Abertura e problema

Comecar situando o trabalho no tema de cancer de mama e explicando que o objetivo foi estimar risco de obito observado a partir de variaveis clinico-patologicas. Aqui vale deixar claro que o projeto nao foi tratado como validacao clinica real, mas como um estudo academico de classificacao tabular com foco em falsos negativos.

### 2. Escolha do tema e do dataset

Explicar que a primeira trilha foi construida sobre o SEER Breast Cancer porque ele permitia montar toda a cadeia de ciencia de dados exigida na disciplina. Destacar que a escolha nao foi aleatoria: o dataset ja trazia variaveis clinicas, alvo binario e um cenario interessante de desbalanceamento.

### 3. Limpeza, sanitizacao e EDA

Mostrar que antes de modelar foi necessario limpar e padronizar o dataset, ajustar nomes de colunas, remover duplicatas e construir um dicionario de dados. Em seguida, apresentar a EDA com metadados, cardinalidade, relacoes numericas e categoricas, destacando o papel de `Survival Months` como possivel fonte de vazamento conceitual.

### 4. Feature engineering e primeira rodada de modelos

Explicar que foram criadas features clinicas derivadas para capturar padroes de risco, e que a primeira rodada incluiu modelos tabulares basicos e hibridos. Aqui e importante nao vender a primeira rodada como sucesso final, mas como etapa de descoberta do problema.

### 5. Limites encontrados no SEER

A parte central da narrativa e esta: o SEER mostrou limites estruturais. O conjunto era util para validar o pipeline, mas nao bastava para sustentar uma narrativa forte de performance. O ensemble ajudava a reduzir falsos negativos, mas em troca gerava muitos falsos positivos, e isso exigia uma leitura cuidadosa do ponto operacional.

### 6. Mudanca para o fork METABRIC

Dizer que, diante desses limites, foi criada uma segunda trilha com METABRIC. O objetivo da troca nao foi "recomeçar do zero", mas testar a mesma metodologia em um dataset clinicamente mais rico, com tratamento, biomarcadores e subtipo molecular.

### 7. Refinamentos tecnicos

Apontar os refinamentos feitos ao longo da segunda iteracao:

- ensemble com pesos e threshold definidos na validacao;
- artefatos de explicabilidade da Logistic Regression;
- curvas de calibracao e Brier score;
- estabilidade por seeds;
- comparativo neuro-fuzzy como evidencia academica, nao como modelo campeao.

### 8. Comparacao final e conclusao

Fechar com a conclusao principal: o trabalho nao mostra apenas um modelo melhor, mas uma evolucao metodologica. O SEER serviu para revelar os limites da primeira formulação; o METABRIC permitiu continuar a investigacao com mais informacao clinica. A mensagem final deve ser que a qualidade do trabalho esta na trilha completa, no rigor da validacao e na forma critica de interpretar os resultados.

## Frase de Fechamento

> O resultado mais importante do trabalho nao e apenas um numero de F2 ou recall, mas a capacidade de construir, revisar e justificar um pipeline de ciencia de dados completo, detectando limites do dataset, corrigindo vazamentos e refinando a modelagem ate chegar a uma leitura tecnicamente defensavel.
