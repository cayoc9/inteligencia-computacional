# Camada Analitica V1 - Teto, Precision E Risco De Burnout

## Objetivo

Este documento registra a camada adicional de interpretacao criada apos o diagnostico de performance e a elaboracao do dicionario de dados.

A intencao e enriquecer a conclusao da V1 sem alterar seu escopo oficial: o target continua sendo `felt_rested`, e o alvo composto `sono_restaurador` fica reservado para a V2.

## 1. Teto De Performance

Os modelos testados convergiram para uma faixa proxima de 73,4% a 74,5% de acuracia. Esse comportamento apareceu em abordagens diferentes, incluindo Random Forest, Rede Neural e Gradient Boosting.

A leitura mais defensavel e que o teto esta menos ligado a incapacidade de um modelo especifico e mais a ambiguidade do target. `felt_rested` e subjetivo: individuos com perfis semelhantes de sono, estresse e rotina podem relatar sensacoes diferentes de descanso.

## 2. Precision Como Metrica Operacional

Na codificacao da V1, a classe positiva significa `felt_rested = 1`, ou seja, "a pessoa se sentiu descansada".

Nesse contexto:

- **Falso positivo:** o modelo diz que a pessoa esta descansada, mas ela nao esta.
- **Falso negativo:** o modelo diz que a pessoa nao esta descansada, mas ela esta.

Para uma aplicacao de saude ocupacional, o falso positivo e especialmente delicado, pois pode mascarar fadiga acumulada. Por isso, destacar precision da classe positiva e coerente: maior precision significa menos falsos alarmes de descanso.

## 3. Burnout: Como Escrever Sem Exagerar

A V1 nao diagnostica burnout. O dataset nao possui uma variavel clinica de burnout, acompanhamento longitudinal ou validacao medica.

A formulacao correta para o relatorio e:

> Em um contexto de monitoramento de fadiga, falsos positivos podem ser mais problematicos porque classificam uma pessoa como descansada quando ela nao esta. Isso pode atrasar a identificacao de fadiga acumulada, um fator associado a risco ocupacional.

Evitar formulacoes fortes como:

> O modelo previne burnout.

ou:

> O modelo detecta burnout.

## 4. Papel Do `cognitive_performance_score`

`cognitive_performance_score` e uma medida objetiva de desempenho cognitivo pos-descanso. Ele nao deve entrar como feature na V1 porque representa um desfecho posterior e poderia gerar vazamento conceitual.

Seu melhor uso na V1 e interpretativo:

- ajuda a mostrar que descanso subjetivo e desempenho objetivo sao relacionados, mas nao identicos;
- fortalece a discussao sobre limite do target `felt_rested`;
- justifica a V2 com alvo composto `sono_restaurador`.

## 5. Consequencia Para A Narrativa Final

A conclusao da V1 deve defender tres pontos:

1. Random Forest/Gradient Boosting foram mais adequados ao dado tabular do que a MLP.
2. O teto de aproximadamente 74% sugere limite do target e das variaveis disponiveis, nao falta de tentativa.
3. Precision e uma metrica importante porque o erro de classificar alguem como descansado quando nao esta tem custo operacional maior.

