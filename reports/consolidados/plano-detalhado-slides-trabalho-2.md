# Plano Descritivo Completo dos Slides - Trabalho 2

## Sistema de Inteligencia Computacional para Risco de Obito em Cancer de Mama

**Objetivo deste arquivo:** servir como briefing unico para duas frentes simultaneas:

1. construcao local em Markdown/HTML;
2. geracao de slide deck pelo NotebookLM, com posterior exportacao para PowerPoint.

**Fonte narrativa principal:**

- `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md`
- `reports/consolidados/roteiro-final-apresentacao-trabalho-2.md`
- `reports/consolidados/plano-slides-apresentacao-trabalho-2.md`

**Recorte:** somente Projeto 2. O Projeto 1 fica fora desta apresentacao.

**Tese central:** a maior contribuicao do trabalho foi evoluir de uma implementacao inicial metodologicamente fragil para um pipeline defensavel: SEER corrigido como baseline educacional e METABRIC como trilha canonica, mantendo ensemble e neuro-fuzzy dentro de uma leitura critica.

## Mapa de assets e referencias visuais

| Codigo | Tipo | Caminho | Uso sugerido |
|---|---|---|---|
| G1 | Figura | `projeto_2_neuro_fuzzy/reports/figures/target_distribution.png` | Distribuicao do alvo na trilha SEER |
| G2 | Figura | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/target_distribution.png` | Distribuicao do alvo na trilha METABRIC |
| G3 | Figura | `projeto_2_neuro_fuzzy/reports/figures/numeric_correlation_heatmap.png` | EDA SEER: relacoes numericas |
| G4 | Figura | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/numeric_correlation_heatmap.png` | EDA METABRIC: relacoes numericas |
| G5 | Figura | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/pam50_deceased_rate.png` | Evidencia visual da riqueza clinica/molecular do METABRIC |
| G6 | Figura | `projeto_2_neuro_fuzzy/reports/figures/calibration_curves.png` | Calibracao SEER |
| G7 | Figura | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/calibration_curves.png` | Calibracao METABRIC |
| G8 | Figura | `projeto_2_neuro_fuzzy/reports/figures/logistic_regression_top_coefficients.png` | Explicabilidade SEER |
| G9 | Figura | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/logistic_regression_top_coefficients.png` | Explicabilidade METABRIC |
| T1 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage_test.csv` | Resultados individuais SEER sem vazamento |
| T2 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/model_comparison_no_leakage_test.csv` | Resultados individuais METABRIC sem vazamento |
| T3 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/ensemble_test_summary.csv` | Resultado final do ensemble SEER |
| T4 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/ensemble_test_summary.csv` | Resultado final do ensemble METABRIC |
| T5 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/neuro_fuzzy_comparison.csv` | Comparativo neuro-fuzzy SEER |
| T6 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/neuro_fuzzy_comparison.csv` | Comparativo neuro-fuzzy METABRIC |
| T7 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/ensemble_threshold_scenarios.csv` | Cenarios de threshold SEER |
| T8 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/ensemble_threshold_scenarios.csv` | Cenarios de threshold METABRIC |
| T9 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/calibration_summary.csv` | Brier/calibracao SEER |
| T10 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/calibration_summary.csv` | Brier/calibracao METABRIC |
| T11 | Tabela | `projeto_2_neuro_fuzzy/reports/tables/stability_summary.csv` | Estabilidade SEER |
| T12 | Tabela | `projeto_2_neuro_fuzzy_metabric_clinico/reports/tables/stability_summary.csv` | Estabilidade METABRIC |

## Guia de design para os slides

- Cada slide deve ter uma mensagem dominante.
- Resultados numericos devem aparecer como tabela curta ou cards, nunca como CSV bruto.
- Usar no maximo um grafico principal por slide.
- Slides 13 a 16 sao os mais importantes para defesa; devem ser visualmente mais objetivos.
- A fala oral explica detalhes metodologicos; o slide deve expor a decisao.
- Sempre que aparecer alto recall, mostrar tambem falsos positivos para evitar conclusao exagerada.

## Slide 1 - Capa

**Funcao:** abrir o trabalho e posicionar o recorte final.

**Titulo:** Sistema de Inteligencia Computacional para Risco de Obito em Cancer de Mama

**Subtitulo:** Ensemble tabular com comparativo neuro-fuzzy: SEER corrigido e evolucao METABRIC

**Conteudo no slide:**

- Disciplina: Inteligencia Computacional - UFPA
- Projeto escolhido: Projeto 2
- Integrantes
- Data

**Visual:** mini fluxo `SEER corrigido -> METABRIC canonico`.

**Assets:** sem grafico externo; diagrama simples criado no slide.

**Fala curta:** "Este trabalho mostra a evolucao do Projeto 2: corrigimos a metodologia do SEER, identificamos limites do dataset e evoluimos para o METABRIC como trilha canonica."

**Cuidado:** nao prometer validacao clinica.

## Slide 2 - Roteiro da Apresentacao

**Funcao:** alinhar a apresentacao ao modelo da avaliacao.

**Conteudo no slide:**

1. Introducao
2. Desenvolvimento da solucao
3. Avaliacao experimental
4. Conclusao

**Visual:** timeline de quatro blocos.

**Assets:** sem grafico externo.

**Fala curta:** "A estrutura segue o formato da avaliacao, partindo do problema ate resultados, limitacoes e trabalhos futuros."

## Slide 3 - Introducao

**Funcao:** justificar por que o problema exige cuidado metodologico.

**Conteudo no slide:**

- Classificacao supervisionada em saude.
- Custo de falso negativo e relevante.
- Acuracia isolada pode enganar em dados desbalanceados.
- Sistema final combina modelos tabulares, ensemble e comparativo neuro-fuzzy.

**Visual:** cards: `Saude`, `Desbalanceamento`, `Falso negativo`, `Sistema inteligente`.

**Assets opcionais:** G1 ou G2 como miniatura de distribuicao de classe.

**Fala curta:** "Em saude, o erro nao tem sempre o mesmo custo. Por isso, o trabalho prioriza recall, F2 e falsos negativos."

## Slide 4 - Problema Proposto

**Funcao:** deixar claro o objetivo corrigido e a politica contra vazamento.

**Conteudo no slide:**

- SEER: prever `Status = Dead`.
- METABRIC: prever `Overall Survival Status = Deceased`.
- `Survival Months` fica fora do modelo principal.
- O modelo usa variaveis clinicas, patologicas, moleculares e de tratamento, conforme a trilha.

**Visual:** diagrama `features permitidas -> classificador -> obito observado`; `Survival Months` aparece como variavel bloqueada.

**Assets:** sem grafico externo.

**Fala curta:** "A pergunta nao e prever status usando o proprio tempo de acompanhamento. Esse seria um atalho metodologico, nao uma predicao defensavel."

## Slide 5 - Dataset

**Funcao:** explicar por que existem duas trilhas.

**Conteudo no slide:**

| Trilha | Papel | Registros analiticos | Diferencial |
|---|---:|---:|---|
| SEER | baseline corrigido | 4.023 | maior, mas menos profundo clinicamente |
| METABRIC | v2 canonica | 1.876 | tratamento, biomarcadores, PAM50, NPI, mutacoes |

**Visual principal:** tabela SEER vs METABRIC.

**Assets:** G1, G2 e G5 como opcionais; G5 e o melhor apoio visual para justificar METABRIC.

**Fala curta:** "O SEER foi util para estruturar o pipeline, mas o METABRIC traz variaveis mais proximas da complexidade clinica do cancer de mama."

## Slide 6 - Arquitetura Geral do Sistema

**Funcao:** apresentar a cadeia completa do sistema.

**Conteudo no slide:**

1. dataset bruto;
2. saneamento e contrato de dados;
3. EDA e metadados;
4. engenharia de features;
5. modelos individuais;
6. ensemble ponderado;
7. neuro-fuzzy comparativo;
8. avaliacao e relatorio.

**Visual:** fluxograma horizontal.

**Assets:** sem grafico externo; usar diagrama autoral.

**Fala curta:** "A arquitetura foi organizada para que cada resultado tenha rastreabilidade desde o dado bruto ate a metrica final."

## Slide 7 - Pre-processamento dos Dados

**Funcao:** mostrar maturidade de ciencia de dados.

**Conteudo no slide:**

- Sanitizacao de nomes e tipos.
- Dicionario de dados.
- Perfil de metadados.
- Analise de relacoes.
- Imputacao e codificacao.
- Politica de vazamento.

**Visual principal:** checklist de pipeline + heatmap pequeno.

**Assets:** G3 e G4; usar G4 como principal se o foco for METABRIC.

**Fala curta:** "A EDA nao foi apenas exploratoria; ela definiu o contrato do dado e evitou que a modelagem respondesse uma pergunta errada."

## Slide 8 - Modelos Inteligentes Utilizados

**Funcao:** cobrir a exigencia de modelos e baseline.

**Conteudo no slide:**

| Familia | Modelos |
|---|---|
| Baseline explicavel | Logistic Regression |
| Arvores/boosting | Random Forest, ExtraTrees, GradientBoosting, HistGradientBoosting, AdaBoost |
| Redes/kernel | MLP, SVM calibrado |
| Sistema combinado | ensemble ponderado |
| Hibrido academico | neuro-fuzzy cooperativo |

**Visual:** tabela por familia.

**Assets:** sem grafico externo.

**Fala curta:** "A comparacao foi ampla o suficiente para separar ganho de modelo, ganho de dataset e ganho de threshold."

## Slide 9 - Arquitetura Hibrida / Ensemble

**Funcao:** defender o elemento de Inteligencia Computacional pedido pela disciplina.

**Conteudo no slide:**

- Ensemble por soft voting ponderado.
- Pesos escolhidos na validacao.
- Threshold escolhido na validacao.
- Teste reservado para reporte final.
- Neuro-fuzzy: fuzzificacao manual + MLP.

**Visual:** diagrama com modelos individuais convergindo no ensemble; bloco lateral para neuro-fuzzy.

**Assets:** T3, T4, T5 e T6 para backup; nao colocar tudo no slide.

**Fala curta:** "O ensemble e o sistema combinado principal. O neuro-fuzzy fica como comparativo hibrido, mas sem ser vendido como ANFIS completo."

## Slide 10 - Pipeline de Treinamento

**Funcao:** responder antecipadamente sobre contaminacao do teste.

**Conteudo no slide:**

- Treino: ajusta modelos.
- Validacao: escolhe pesos e threshold.
- Teste: reporta resultado final.
- Estabilidade por 5 seeds.
- Notebooks e CSVs preservam reproducibilidade.

**Visual:** diagrama `train -> validation -> test`.

**Assets:** T11 e T12 como suporte para estabilidade; nao precisam aparecer completos.

**Fala curta:** "A correcao central foi impedir que o teste virasse ferramenta de escolha."

## Slide 11 - Metodologia Experimental

**Funcao:** mostrar que SEER e METABRIC foram avaliados com disciplina equivalente.

**Conteudo no slide:**

| Etapa | SEER | METABRIC |
|---|---|---|
| dicionario | sim | sim |
| EDA/metadados | sim | sim |
| leakage policy | sim | sim |
| treino/validacao/teste | sim | sim |
| ensemble validado | sim | sim |
| explicabilidade/calibracao | sim | sim |

**Visual:** matriz de completude.

**Assets:** docs e relatorios; sem grafico externo obrigatorio.

**Fala curta:** "A troca de base nao foi uma troca oportunista; a v2 repetiu as mesmas fases metodologicas da v1 corrigida."

## Slide 12 - Metricas de Avaliacao

**Funcao:** justificar a leitura dos resultados.

**Conteudo no slide:**

- Recall: capacidade de capturar positivos.
- F2-score: pesa recall mais que precisao.
- PR AUC: mais informativa em desbalanceamento.
- Falsos negativos: principal risco operacional.
- Acuracia: secundaria.

**Visual:** quadro `FN custa mais que FP` + mini explicacao do F2.

**Assets:** sem grafico externo.

**Fala curta:** "Um modelo com acuracia menor pode ser melhor para o objetivo se reduz falsos negativos de forma controlada."

## Slide 13 - Resultados dos Modelos Individuais

**Funcao:** mostrar que o METABRIC melhora antes mesmo do ensemble.

**Conteudo no slide:**

| Trilha | Melhor modelo individual | Accuracy | Recall | F2 | PR AUC | FN |
|---|---|---:|---:|---:|---:|---:|
| SEER | Logistic Regression | 0.6807 | 0.6098 | 0.4832 | 0.3525 | 48 |
| METABRIC | GradientBoosting | 0.7048 | 0.7953 | 0.7787 | 0.7600 | 44 |

**Visual:** tabela compacta + destaque em F2/PR AUC.

**Assets:** T1 e T2.

**Fala curta:** "O salto de desempenho nao aparece apenas no ensemble. Ele ja surge no melhor modelo individual, o que reforca a tese de qualidade do dataset."

## Slide 14 - Resultados do Sistema Hibrido

**Funcao:** apresentar ensemble e neuro-fuzzy sem exagerar conclusoes.

**Conteudo no slide:**

| Trilha | Sistema | Threshold | Recall | F2 | FN | FP |
|---|---|---:|---:|---:|---:|---:|
| SEER | ensemble ponderado | 0.22 | 0.7642 | 0.5188 | 29 | 320 |
| METABRIC | ensemble ponderado | 0.16 | 0.9953 | 0.8770 | 1 | 146 |
| SEER | neuro-fuzzy | - | 0.2764 | 0.2886 | - | - |
| METABRIC | neuro-fuzzy | - | 0.6512 | 0.6548 | - | - |

**Visual:** tabela + marcador forte em `1 falso negativo` no METABRIC.

**Assets:** T3, T4, T5 e T6.

**Fala curta:** "O ensemble final quase elimina falsos negativos no METABRIC, mas a apresentacao deve mostrar tambem o custo em falsos positivos."

## Slide 15 - Comparacao Geral

**Funcao:** sintetizar a historia SEER vs METABRIC.

**Conteudo no slide:**

- SEER individual: F2 0.4832.
- SEER ensemble: F2 0.5188.
- METABRIC individual: F2 0.7787.
- METABRIC ensemble: F2 0.8770.
- Melhor dataset elevou o teto; ensemble deslocou o ponto operacional.

**Visual:** grafico de barras de F2 e recall; tabela pequena de FN/FP.

**Assets:** T1, T2, T3, T4. O grafico pode ser gerado localmente a partir desses valores.

**Fala curta:** "A comparacao geral mostra dois efeitos: dados melhores melhoram discriminacao; threshold/ensemble melhoram sensibilidade."

## Slide 16 - Analise dos Resultados

**Funcao:** interpretar os trade-offs com honestidade tecnica.

**Conteudo no slide:**

- SEER: reduz FN, mas gera muitos FP.
- METABRIC: recall quase maximo, mas FP ainda relevante.
- Neuro-fuzzy nao superou os modelos tabulares fortes.
- Explicabilidade, calibracao e estabilidade reforcam a defesa.

**Visual:** matriz de decisao `sensibilidade alta` x `custo de falso positivo`.

**Assets:** T7, T8, G6, G7, G8, G9 como backup visual.

**Fala curta:** "O resultado nao deve ser lido como 'ensemble sempre vence', e sim como escolha de um ponto operacional de alta sensibilidade."

## Slide 17 - Principais Conclusoes

**Funcao:** fechar a tese central.

**Conteudo no slide:**

1. Corrigir vazamento e validacao tornou o experimento defensavel.
2. METABRIC foi melhor para a pergunta por conter maior profundidade clinica.
3. Ensemble foi util como ponto de alta sensibilidade.
4. Neuro-fuzzy teve papel academico comparativo, nao de campeao.

**Visual:** quatro blocos numerados.

**Assets:** sem grafico externo.

**Fala curta:** "A principal entrega nao e so uma metrica maior, mas uma evolucao metodologica com leitura critica."

## Slide 18 - Limitacoes do Trabalho

**Funcao:** mostrar maturidade e evitar defesa exagerada.

**Conteudo no slide:**

- Datasets publicos.
- Sem validacao clinica externa.
- Classificacao binaria, nao survival analysis formal.
- Neuro-fuzzy nao e ANFIS completo.
- Comparacao SEER vs METABRIC nao e benchmark perfeito entre bases identicas.
- Falsos positivos ainda precisam ser controlados.

**Visual:** lista curta em cards.

**Assets:** sem grafico externo.

**Fala curta:** "Essas limitacoes delimitam o escopo academico do trabalho e indicam proximas evolucoes."

## Slide 19 - Trabalhos Futuros

**Funcao:** transformar limitacoes em plano cientifico.

**Conteudo no slide:**

- Survival analysis formal.
- Validacao externa.
- Validacao cruzada repetida.
- Explicabilidade local.
- Analise de decisao por custo clinico.
- Calibragem fuzzy com especialista.

**Visual:** roadmap em tres etapas: `robustez`, `interpretabilidade`, `validacao clinica`.

**Assets:** sem grafico externo.

**Fala curta:** "A evolucao natural e aproximar o problema de prognostico real e validar melhor custo de erro."

## Slide 20 - Encerramento / Perguntas

**Funcao:** encerrar e preparar a arguição.

**Conteudo no slide:**

- SEER: baseline corrigido.
- METABRIC: trilha canonica.
- Mensagem final: bons dados e boa validacao foram mais importantes que complexidade isolada.
- Perguntas.

**Visual:** frase final + lista curta de perguntas provaveis.

**Perguntas provaveis:**

- Por que nao usar acuracia?
- Por que remover `Survival Months`?
- O ensemble foi ajustado no teste?
- O neuro-fuzzy e ANFIS?
- Por que METABRIC e melhor que SEER?
- Como justificar tantos falsos positivos?

**Fala curta:** "A apresentacao termina reforcando que o valor do trabalho esta na evolucao metodologica e na interpretacao critica dos resultados."

## Ordem de geracao das duas solucoes

### Solucao A - Markdown/HTML local

1. Usar este plano como fonte.
2. Criar `reports/consolidados/slides-trabalho-2/index.html`.
3. Referenciar imagens reais com caminhos relativos.
4. Criar tabelas compactas diretamente no HTML a partir dos valores finais.
5. Validar no navegador.

### Solucao B - NotebookLM / PowerPoint

1. Adicionar este plano como fonte no notebook `22e638a3-d0ca-447e-8a02-45b0d942865e`.
2. Gerar slide deck em portugues do Brasil, formato `presenter`, seguindo exatamente os 20 slides.
3. Baixar como PPTX para ajustes finos.
4. Comparar com a versao local e aproveitar o melhor layout/conteudo de cada uma.

