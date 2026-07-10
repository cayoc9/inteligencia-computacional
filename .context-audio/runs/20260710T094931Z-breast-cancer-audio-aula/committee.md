# Committee Synthesis

## Historia Unificada

O audio deve ensinar o Trabalho 2 como uma aula curta de metodologia aplicada. A tese e que o projeto evoluiu de uma trilha SEER metodologicamente corrigida para uma trilha METABRIC canonica. O ganho central nao veio de "usar IA mais complexa", mas de corrigir a pergunta, proteger o teste, escolher metricas adequadas e usar dados clinicos mais informativos.

## Eixo Tecnico

O problema e classificar obito observado em cancer de mama. No SEER, a classe positiva e `Status = Dead`; no METABRIC, `Overall Survival Status = Deceased`. A variavel de sobrevida em meses nao entra no modelo principal porque carrega informacao posterior ao diagnostico e contamina a pergunta.

## Eixo Metodologico

O protocolo correto e: treino ajusta modelos, validacao escolhe pesos e threshold, teste apenas reporta. Essa frase precisa aparecer no audio porque protege o trabalho de uma pergunta provavel da banca.

## Eixo de Resultados

SEER individual: Logistic Regression com F2 0.4832, recall 0.6098, PR AUC 0.3525 e 48 falsos negativos. SEER ensemble: threshold 0.22, recall 0.7642, F2 0.5188, 29 falsos negativos e 320 falsos positivos.

METABRIC individual: GradientBoosting com F2 0.7787, recall 0.7953, PR AUC 0.7600 e 44 falsos negativos. METABRIC ensemble: threshold 0.16, recall 0.9953, F2 0.8770, 1 falso negativo e 146 falsos positivos.

## Eixo de Defesa Oral

O grupo deve dizer que o ensemble e um ponto operacional experimental de alta sensibilidade. Nao deve dizer que e modelo clinico seguro, nem que erradicou risco, nem que e o classificador universalmente melhor.

## Incertezas e Limites

Nao houve validacao clinica externa. O problema e classificacao binaria, nao survival analysis formal. O neuro-fuzzy e comparativo academico com fuzzificacao manual + MLP, nao ANFIS completo.
