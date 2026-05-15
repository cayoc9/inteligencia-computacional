# Exemplo: Narrativa Completa (Trabalho 1)

> Texto completo para apresentação de 10-15 minutos.

## Slide 1: Abertura (30s)

> "Bom dia. Meu nome é [nome] e vou apresentar o trabalho de comparação entre Random Forest e Redes Neurais para classificação em saúde do sono."

## Slide 2: Contexto e Problema (1 min)

> "O problema: classificar se uma pessoa se sentiu descansada ao acordar, usando dados de saúde do sono e estilo de vida. Por quê? Para comparar duas abordagens clássicas de Machine Learning — Random Forest e Redes Neurais — em um problema real de dados tabulares.
>
> O dataset é o Sleep Health & Daily Performance, com 100 mil registros e 32 features sobre hábitos de sono, estilo de vida e indicadores de saúde. Zero valores nulos, zero duplicatas. Um dataset limpo e robusto."

## Slide 3: Metodologia (1 min)

> "Nossa metodologia: split estratificado 70/30 com random_state=42 para garantir comparação justa. Pré-processamento com ColumnTransformer — one-hot para categóricas, padronização para numéricas. Três modelos principais: Random Forest com GridSearchCV, MLP base com 2 camadas densas, e MLP otimizada com batch normalization e dropout. Depois adicionamos o HistGradientBoosting como baseline forte no diagnóstico."

## Slide 4: Resultados — Random Forest (1 min)

> "Começando pela Random Forest. Com GridSearchCV otimizando n_estimators, max_depth e min_samples_split, alcançamos 74,15% de acurácia e AUC de 82,18%. Um resultado sólido, consistente com a literatura para dados tabulares."

## Slide 5: Resultados — Redes Neurais (1.5 min)

> "A Rede Neural base, uma MLP simples com 2 camadas densas, ficou em 73,23% de acurácia — cerca de 1% abaixo da RF.
>
> Otimizamos com batch normalization, dropout em duas camadas e ReduceLROnPlateau. O resultado chegou a aproximadamente 74%, ainda abaixo da RF. O ganho da otimização foi marginal — menos de 1 ponto percentual."

## Slide 6: Comparação Direta (2 min)

> "Colocando lado a lado: RF 74,15%, RN base 73,23%, RN otimizada ~74%, HistGradientBoosting 74,25%.
>
> O que isso nos diz? Primeiro: a RF é competitiva com o melhor modelo testado (HistGB) — diferença de apenas 0,1 ponto percentual. Segundo: a RN, mesmo otimizada, não superou a RF. Terceiro: a troca de modelo (RF → HistGB) mal justifica o esforço.
>
> Isso não significa que a Rede Neural 'falhou'. Ela encontrou o mesmo teto de performance com maior complexidade computacional."

## Slide 7: Threshold Tuning (1.5 min)

> "Uma descoberta importante: o threshold padrão de 0,5 não é o ideal.
>
> O dataset é desbalanceado: 61% classe 0, 39% classe 1. O threshold 0,5 sacrifica recall da classe positiva para manter precisão.
>
> Ajustando o threshold para 0,35, o F1-score sobe de 0,66 para 0,70 — um ganho de 6% sem retreinar o modelo. Com threshold 0,39, a balanced accuracy atinge 0,74.
>
> Isso mostra que o modelo ranqueia bem — o problema é o ponto de corte padrão."

## Slide 8: Feature Importance (1 min)

> "Por que modelos tão diferentes chegam ao mesmo teto? Porque apenas 4 features carregam 80% do sinal preditivo:
>
> 1. Qualidade do sono (sleep_quality)
> 2. Duração do sono (sleep_duration)
> 3. Estresse (stress_score)
> 4. Episódios de acordar (wake_episodes)
>
> As outras 28 features adicionam pouco sinal incremental. Não há informação suficiente nas features restantes para que um modelo mais complexo extraia mais performance."

## Slide 9: Conclusão (1 min)

> "Resumindo as principais conclusões:
>
> Primeiro: a Random Forest é a melhor escolha para dados tabulares — performance competitiva com complexidade muito menor que Redes Neurais.
>
> Segundo: o verdadeiro gargalo não é o modelo, é o alvo. felt_rested é subjetivo. Duas pessoas com o mesmo perfil de sono podem responder diferente sobre se se sentiram descansadas. Isso impõe um teto de ~74% que nenhum modelo consegue superar.
>
> Terceiro: o threshold padrão é arbitrário. Ajustar o ponto de corte entregou ganho real sem custo computacional."

## Slide 10: Call-to-Action (30s)

> "Com base nestes resultados, recomendo:
>
> 1. Para problemas tabulares de classificação, comecem com Random Forest antes de investir em Redes Neurais.
> 2. Sempre investiguem o threshold de decisão — ele pode render mais que horas de tuning de hiperparâmetros.
> 3. Entendam as limitações do alvo antes de culpar o modelo.
>
> O relatório completo está disponível. Perguntas?"
