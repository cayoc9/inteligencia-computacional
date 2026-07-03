# Roteiro Final de Apresentacao - Trabalho 2

## Duracao sugerida: 12 a 15 minutos

## 1. Abertura - 1 minuto

- Tema do trabalho
- Exigencia da disciplina: sistema hibrido ou ensemble
- Escolha do Projeto 2 como trilha final

## 2. Problema e objetivo - 2 minutos

- classificar risco de obito em cancer de mama com dados tabulares
- objetivo corrigido
- por que `Survival Months` nao entra no modelo principal

## 3. Trilha SEER corrigida - 3 minutos

- o que estava errado no inicio
- saneamento, EDA, dicionario e politica de vazamento
- resultados principais:
  - Logistic Regression como baseline explicavel
  - ensemble com threshold `0.22`
- leitura correta: ganho de sensibilidade com muito falso positivo

## 4. Limites do SEER e migracao para METABRIC - 2 minutos

- por que o SEER era limitado
- criterio para procurar nova base
- por que o METABRIC foi escolhido

## 5. Trilha METABRIC canonica - 3 minutos

- novas variaveis clinicas e moleculares
- mesmo rigor metodologico do SEER
- resultados principais:
  - GradientBoosting com F2 `0.7787`
  - ensemble com threshold `0.16`, recall `0.9953`, `1` falso negativo

## 6. Papel do neuro-fuzzy e da explicabilidade - 2 minutos

- neuro-fuzzy como comparativo academico
- nao e ANFIS completo
- explicabilidade, calibracao e estabilidade como reforco de defesa

## 7. Conclusao - 1 a 2 minutos

- metodologia corrigida aumentou a credibilidade
- melhorar o dataset aumentou muito o teto do projeto
- SEER fica como baseline corrigido
- METABRIC fica como trilha canonica
- trabalhos futuros

## Slide final: perguntas provaveis

- por que nao usar acuracia
- por que remover `Survival Months`
- por que o ensemble ainda vale com mais falsos positivos
- o neuro-fuzzy e ANFIS?
