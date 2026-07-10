# Distillation: Architect

## Layer 1

O sistema apresentado nao e uma unica tecnica isolada. Ele e uma arquitetura experimental de ciencia de dados: contrato de dados, limpeza, EDA, split treino-validacao-teste, modelos tabulares, ensemble ponderado e comparativo neuro-fuzzy.

## Layer 2

A fronteira central e entre duas trilhas. A trilha SEER e o baseline corrigido: ela mostra a remocao de vazamento, a reconstrucao do pipeline e o aprendizado sobre sensibilidade. A trilha METABRIC e a evolucao canonica: ela usa informacao clinica mais rica, como tratamento, receptores hormonais, HER2, PAM50, NPI e mutation count.

O ensemble combina saidas de modelos tabulares e desloca o threshold para alta sensibilidade. O neuro-fuzzy e cooperativo: fuzzificacao manual alimentando MLP. Ele nao e ANFIS completo e nao deve ser vendido como modelo campeao.
