# Template: História de 3 Minutos

> Se você tivesse apenas 3 minutos com seu público, o que diria?

## Estrutura

| Tempo | Parte | Conteúdo |
|---|---|---|
| 0:00-0:30 | **Contexto** | O problema, por que importa |
| 0:30-1:30 | **Dados** | O que foi feito, o que foi descoberto |
| 1:30-2:30 | **Análise** | O que significa, insights |
| 2:30-3:00 | **Ação** | O que recomendamos, próximos passos |

## Instruções

1. Escreva a versão completa (sem limite de tempo)
2. Corte para 3 minutos (cerca de 450 palavras faladas)
3. Leia em voz alta e cronometre
4. Corte mais se necessário
5. Decore os pontos principais (não precisa decorar o texto literal)

## Exemplo Preenchido (Trabalho 1)

> "Bom dia. Neste trabalho comparamos duas abordagens clássicas de machine learning — Random Forest e Redes Neurais — aplicadas a um problema de classificação em saúde do sono.
>
> [Contexto] Usamos o dataset Sleep Health & Daily Performance, com 100 mil registros e 32 features sobre hábitos de sono, estilo de vida e indicadores de saúde. O objetivo era classificar se a pessoa se sentiu descansada ao acordar.
>
> [Dados] Treinamos três modelos: Random Forest com GridSearchCV, uma MLP base com 2 camadas densas, e uma versão otimizada com batch normalization e dropout. Também testamos HistGradientBoosting como baseline forte.
>
> Os resultados: Random Forest: 74,15% de acurácia e AUC de 82,18%. Rede Neural base: 73,23%. Rede Neural otimizada: ~74%. HistGradientBoosting: 74,25% e AUC de 82,58% — o melhor, mas com ganho marginal sobre a RF.
>
> [Análise] A principal descoberta é que o gargalo não está no modelo, mas no alvo. Apenas 4 features — qualidade do sono, duração, estresse e episódios de acordar — carregam 80% do sinal. E o alvo felt_rested é subjetivo: duas pessoas com sono similar podem responder diferente. Além disso, descobrimos que o threshold padrão de 0,5 não é ideal — ajustando para 0,35, ganhamos 6% no F1-score sem retreinar.
>
> [Ação] Concluímos que para dados tabulares, a Random Forest é a melhor escolha: performance próxima do estado da arte com complexidade muito menor. A Rede Neural não fracassou — ela encontrou o mesmo teto com maior custo computacional."
>
> Recomendação: Para problemas similares, comece com RF antes de investir em RN.

## Template em Branco

```
[Contexto — 30s]
_________________________________________________
_________________________________________________

[Dados — 60s]
_________________________________________________
_________________________________________________
_________________________________________________

[Análise — 60s]
_________________________________________________
_________________________________________________
_________________________________________________

[Ação — 30s]
_________________________________________________
_________________________________________________
```

## Verificação Final

- [ ] Cabe em 3 minutos (leia em voz alta e cronometre)
- [ ] Mensagem principal aparece pelo menos 2 vezes
- [ ] Termina com call-to-action claro
- [ ] Soa natural, não como leitura de relatório
- [ ] Dá para falar sem depender de slides
