# Especificacao: Experimento V2 - Target Composto `sono_restaurador`

## Status

- **Estado:** Proposto
- **Origem:** Aprendizado da V1 sobre subjetividade de `felt_rested`
- **Nao faz parte da entrega oficial V1**, salvo como trabalho futuro

## Problema

Criar uma versao mais robusta do experimento de classificacao em saude do sono, combinando uma dimensao subjetiva de descanso com uma dimensao objetiva de desempenho cognitivo.

## Hipotese

Um alvo composto pode representar melhor a ideia de sono restaurador do que `felt_rested` isoladamente.

`felt_rested` responde se a pessoa se percebeu descansada. `cognitive_performance_score` representa um desfecho objetivo associado ao funcionamento cognitivo apos o descanso. Como as duas variaveis sao relacionadas, mas nao equivalentes, a combinacao pode reduzir a fragilidade de depender apenas de autorrelato.

A V2 tambem ajuda a testar se o teto de aproximadamente 74% observado na V1 era consequencia do target subjetivo ou uma limitacao mais geral das features disponiveis.

## Definicao Proposta Do Target

Nome canonico:

```text
sono_restaurador
```

Definicao inicial:

```text
sono_restaurador = 1 se:
  felt_rested == 1
  e cognitive_performance_score >= limiar_cognitivo

sono_restaurador = 0 caso contrario
```

## Limiar Cognitivo

Duas opcoes devem ser avaliadas:

| Opcao | Limiar | Positivos esperados | Trade-off |
|---|---:|---:|---|
| Mediana | `>= 60.4` | ~29.1% | Mais simples e menos desbalanceado |
| Percentil 60 | `>= 66.4` | ~24.9% | Mais exigente e semanticamente mais forte |

Recomendacao inicial: comecar pela mediana para manter o problema menos desbalanceado e depois testar o percentil 60 como sensibilidade.

## Regras Contra Vazamento

- Se `cognitive_performance_score` compoe o target, ela deve ser removida das features.
- `felt_rested` tambem deve ser removida das features.
- `sleep_disorder_risk` deve permanecer fora do treino principal para evitar misturar alvo alternativo com preditor clinico derivado.
- O split deve continuar estratificado e reproduzivel.

## Perguntas De Pesquisa

- O alvo composto aumenta ou reduz a capacidade dos modelos em relacao a `felt_rested`?
- A Random Forest continua superior a Rede Neural em dados tabulares?
- O target composto melhora a interpretabilidade clinica da tarefa?
- O desbalanceamento adicional prejudica recall e F1?
- O threshold tuning continua oferecendo ganho relevante?
- A priorizacao de precision continua adequada quando o target passa a representar sono restaurador subjetivo + objetivo?

## Criterios De Sucesso

- Dataset derivado criado de forma reprodutivel.
- Distribuicao do novo target documentada.
- Modelos RF e RN reexecutados com o mesmo protocolo da V1.
- Metricas comparaveis: accuracy, balanced accuracy, precision, recall, F1, matriz de confusao, ROC AUC e PR AUC.
- Relatorio V2 separado da V1.
