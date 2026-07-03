# Fragmento do Relatorio - Discussao e Limitacoes

## Discussao

O resultado principal do experimento mostra que a Random Forest foi mais robusta do que as Redes Neurais para este problema especifico de classificacao em dados tabulares de saude do sono. A diferenca de desempenho nao e muito grande, mas e consistente o suficiente para justificar a escolha da Random Forest como modelo campeao.

A Rede Neural MLP continuou competitiva, especialmente considerando que o dataset possui 100.000 registros. No entanto, a arquitetura otimizada, mesmo com BatchNormalization, Dropout, ReduceLROnPlateau e novas features de interacao, trouxe apenas melhoria marginal. Isso reforca que aumentar a complexidade do modelo nao garante ganho proporcional quando o sinal disponivel nas features ja esta proximo do limite capturado pelos modelos.

## Limitacoes

- O dataset e sintentico-calibrado, o que reduz a generalizacao direta para populacoes reais.
- A avaliacao foi feita com uma divisao treino/teste estratificada, mas ainda pode ser expandida com validacao cruzada para as redes neurais.
- A comparacao usou `felt_rested` como alvo principal; outros targets, como `sleep_disorder_risk`, poderiam gerar conclusoes diferentes.
- A ausencia de GPU limita experimentos mais amplos com arquiteturas neurais, embora o impacto tenha sido pequeno para a MLP usada.

## Conclusao Interpretativa

Para este trabalho, a conclusao mais defensavel e que Redes Neurais nao sao automaticamente superiores. Em dados tabulares estruturados, modelos de arvores como Random Forest podem ser mais simples, estaveis e eficientes, oferecendo desempenho igual ou superior com menor custo de ajuste.
