# 2026-07-10 - Trabalho 2 Breast Cancer - Audio-aula para Apresentacao

## Metadados

- Run: `20260710T094931Z-breast-cancer-audio-aula`
- NotebookLM: `22e638a3-d0ca-447e-8a02-45b0d942865e`
- Projeto: Inteligencia Computacional UFPA 2026.1
- Objetivo: gerar audio em portugues ensinando o assunto da apresentacao, para ensaio do grupo.

## Pergunta

Como explicar, em formato de audio-aula, o Trabalho 2 sobre Breast Cancer SEER corrigido vs METABRIC canonico, ensemble ponderado e comparativo neuro-fuzzy?

## Fontes usadas

1. `STATUS.md`
2. `.specs/project/TRABALHO_2_AVALIACAO_CHECKLIST.md`
3. `.specs/project/STATE.md`
4. `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md`
5. `reports/consolidados/finalizacao-defesa-2026-07-09/roteiro-detalhado-e-curadoria-final.md`
6. `reports/consolidados/notebooklm-trabalho-2/09c_prompt_audio_unico_15min_padrao.md`
7. `docs/template/Breast_Cancer/main.tex`

## Tese para o audio

O Trabalho 2 nao deve ser apresentado como um modelo clinico pronto. A tese correta e que o projeto evoluiu de uma trilha SEER metodologicamente corrigida para uma trilha METABRIC canonica. A melhoria central veio de quatro fatores: remocao de vazamento, separacao treino-validacao-teste, melhor qualidade informacional do dataset e leitura honesta do trade-off entre falsos negativos e falsos positivos.

## Roteiro de audio-aula

### 1. Abertura

Explique que o trabalho e um sistema de inteligencia computacional para classificacao de obito observado em cancer de mama. O objetivo nao e prometer uso clinico direto. O objetivo academico e mostrar um workflow defensavel de ciencia de dados com ensemble e comparativo neuro-fuzzy.

### 2. Problema

A classe positiva e obito observado. No SEER, isso aparece como `Status = Dead`. No METABRIC, como `Overall Survival Status = Deceased`. Por isso, falso negativo importa: e o caso em que o sistema nao sinaliza um paciente da classe positiva.

### 3. Por que acuracia nao basta

Em dados desbalanceados, acuracia pode parecer boa mesmo ignorando a classe minoritaria. A apresentacao deve priorizar recall, F2, PR AUC e numero absoluto de falsos negativos. Accuracy deve aparecer apenas como contexto.

### 4. Correcao metodologica principal

A variavel `Survival Months` foi removida do modelo principal porque representa informacao de acompanhamento posterior. Usar essa variavel para prever obito observado cria vazamento conceitual.

Frase obrigatoria: "Survival Months pode aparecer como analise de sensibilidade, mas nao como feature da pergunta central."

### 5. Protocolo de validacao

Treino ajusta modelos. Validacao escolhe pesos e threshold. Teste apenas reporta. Essa disciplina impede que a equipe escolha threshold olhando o resultado final do teste.

Frase obrigatoria: "Validacao escolhe, teste reporta."

### 6. SEER corrigido

O SEER tem 4.023 registros analiticos e fica como baseline corrigido. Ele e util porque permitiu sanear a pergunta, reconstruir a validacao e demonstrar o trade-off entre sensibilidade e falsos positivos. Mas tem menor profundidade clinica.

Resultado individual SEER: Logistic Regression com F2 0.4832, recall 0.6098, PR AUC 0.3525 e 48 falsos negativos.

Resultado operacional SEER: ensemble com threshold 0.22, recall 0.7642, F2 0.5188, 29 falsos negativos e 320 falsos positivos.

### 7. METABRIC canonico

O METABRIC tem 1.876 registros analiticos e virou a trilha canonica porque traz tratamento, ER, PR, HER2, PAM50, NPI e mutation count. Ele tem menos linhas que o SEER, mas mais qualidade informacional para este problema.

Resultado individual METABRIC: GradientBoosting com F2 0.7787, recall 0.7953, PR AUC 0.7600 e 44 falsos negativos.

Resultado operacional METABRIC: ensemble com threshold 0.16, recall 0.9953, F2 0.8770, 1 falso negativo e 146 falsos positivos.

### 8. Modelos e requisito da disciplina

Foram avaliados modelos tabulares, ensemble ponderado e neuro-fuzzy cooperativo. O neuro-fuzzy nao e ANFIS completo. Ele usa fuzzificacao manual mais MLP e cumpre papel comparativo academico. Ele nao superou os melhores modelos tabulares.

### 9. Interpretacao correta

O METABRIC melhorou antes mesmo do ensemble, entao o ganho nao pode ser atribuido apenas ao threshold agressivo. O dataset clinicamente mais rico elevou o teto. O threshold e o ensemble deslocaram o ponto operacional para alta sensibilidade.

### 10. Trade-off

O resultado de 1 falso negativo no METABRIC e forte, mas so e honesto se aparecer junto dos 146 falsos positivos. O ensemble deve ser descrito como ponto operacional experimental de alta sensibilidade, nao como modelo definitivo.

### 11. Limitacoes

Nao houve validacao clinica externa. O problema e classificacao binaria, nao survival analysis formal. A comparacao SEER vs METABRIC e pedagogica e metodologica, nao um benchmark clinico estrito entre bases identicas.

### 12. Fechamento

Mensagem final: bons dados, validacao preservada e leitura honesta de trade-off foram mais importantes que complexidade isolada. O SEER ficou como baseline corrigido; o METABRIC virou a trilha canonica; o ensemble mostra sensibilidade com custo operacional; o neuro-fuzzy mostra que nem todo hibrido vence empiricamente.

## Perguntas provaveis e respostas curtas

- Por que nao usar acuracia? Porque a classe positiva e minoritaria e falsos negativos importam mais para esta leitura.
- Por que remover `Survival Months`? Porque e informacao posterior de acompanhamento e contamina a pergunta.
- O threshold foi escolhido no teste? Nao. Validacao escolheu, teste reportou.
- O neuro-fuzzy e ANFIS? Nao. E fuzzificacao manual mais MLP.
- O ensemble vale com 146 falsos positivos? Vale como ponto experimental de alta sensibilidade, nao como melhor modelo universal.
- Isso pode ser usado clinicamente? Nao diretamente. Precisaria de validacao externa, calibracao, analise de custo e talvez survival analysis formal.

## Prompt recomendado para gerar audio

Gere um audio em portugues do Brasil, com duracao alvo de 14 a 16 minutos, ensinando o assunto que o grupo vai apresentar no Trabalho 2. O publico sao integrantes do grupo que precisam entender e conseguir apresentar o projeto, mesmo que nao tenham participado de toda a implementacao. O tom deve ser didatico, natural e objetivo. Nao leia slides. Explique como uma aula preparatoria para defesa.

Cubra obrigatoriamente: tese SEER corrigido para METABRIC canonico; problema de obito observado; por que acuracia nao basta; vazamento por `Survival Months`; protocolo treino-validacao-teste; resultados SEER; resultados METABRIC; papel do ensemble; papel do neuro-fuzzy; trade-off entre 1 falso negativo e 146 falsos positivos; limitacoes e respostas de banca.

Regras negativas: nao incluir Projeto 1, nao vender como produto clinico, nao dizer validacao clinica externa, nao chamar neuro-fuzzy de ANFIS, nao dizer que ensemble e sempre melhor.
