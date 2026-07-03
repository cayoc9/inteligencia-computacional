# Plano de Slides - Trabalho 2

## Sistema de Inteligencia Computacional para Risco de Obito em Cancer de Mama

**Base narrativa:** `roteiro-final-apresentacao-trabalho-2.md` e `relatorio-final-trabalho-2-breast-cancer.md`  
**Formato-alvo:** estrutura de avaliacao com 20 slides  
**Recorte:** somente Projeto 2, com SEER como baseline corrigido e METABRIC como trilha canonica  
**Duracao-alvo:** 12 a 15 minutos
**Overleaf do artigo:** https://www.overleaf.com/2412565471zbrmcvmybryy#a785ee

## Camadas da apresentacao

1. **Camada academica:** mostrar aderencia ao pedido da disciplina: sistema inteligente, hibrido/ensemble, comparacao experimental, metricas, conclusoes e limitacoes.
2. **Camada metodologica:** defender que o projeto foi corrigido: sem `Survival Months` no modelo principal, split treino/validacao/teste, EDA, dicionario, politica de vazamento e teste preservado.
3. **Camada narrativa:** contar a evolucao natural: SEER revelou limites, METABRIC aumentou a qualidade da base e melhorou o teto de desempenho.
4. **Camada critica:** evitar vender o ensemble como solucao universal; apresenta-lo como ponto operacional de alta sensibilidade com trade-off de falsos positivos.
5. **Camada de defesa:** preparar respostas para perguntas sobre acuracia, vazamento, neuro-fuzzy, falso positivo, validacao clinica e comparacao entre datasets.

## Distribuicao sugerida de tempo

| Bloco | Slides | Tempo |
|---|---:|---:|
| Abertura e problema | 1-5 | 3 min |
| Desenvolvimento da solucao | 6-10 | 4 min |
| Avaliacao experimental | 11-16 | 5 a 6 min |
| Conclusao | 17-20 | 2 min |

## Slide 1 - Capa

**Titulo:** Sistema de Inteligencia Computacional para Risco de Obito em Cancer de Mama  
**Subtitulo:** Ensemble tabular com comparativo neuro-fuzzy: SEER corrigido e evolucao METABRIC  
**Conteudo:** disciplina, turma, UFPA, integrantes e data.  
**Mensagem oral:** "Este trabalho apresenta a evolucao do Projeto 2, desde a correcao metodologica da base SEER ate a versao canonica com METABRIC."  
**Visual sugerido:** titulo limpo + diagrama pequeno `SEER corrigido -> METABRIC canonico`.  
**Pergunta de banca que o slide antecipa:** qual projeto foi escolhido e qual e a contribuicao central?

## Slide 2 - Roteiro da Apresentacao

**Titulo:** Roteiro  
**Conteudo:** quatro blocos: Introducao, Desenvolvimento da Solucao, Avaliacao Experimental, Conclusao.  
**Mensagem oral:** "A apresentacao segue a estrutura da avaliacao: problema, solucao, experimentos e conclusoes."  
**Visual sugerido:** timeline horizontal com os 4 blocos e numeros de slides.  
**Pergunta que antecipa:** a apresentacao cobre todos os itens exigidos?

## 1. Introducao

## Slide 3 - Introducao

**Titulo:** Contexto e Motivacao  
**Conteudo-chave:**
- problema de classificacao em saude com dados tabulares;
- custo de falso negativo e relevante;
- disciplina exige sistema hibrido ou ensemble;
- projeto prioriza rigor metodologico, nao apenas maior acuracia.
**Mensagem oral:** "Em problemas medicos desbalanceados, acertar a maioria nao basta; perder casos positivos pode ser mais grave."  
**Visual sugerido:** card simples com `risco clinico`, `dados tabulares`, `ensemble/neuro-fuzzy`, `validacao`.  
**Pergunta que antecipa:** por que nao usar acuracia como criterio principal?

## Slide 4 - Problema Proposto

**Titulo:** Problema e Objetivo Corrigido  
**Conteudo-chave:**
- prever obito observado em cancer de mama;
- SEER: `Status = Dead`;
- METABRIC: `Overall Survival Status = Deceased`;
- `Survival Months` removido do modelo principal por ser informacao de acompanhamento.
**Mensagem oral:** "A pergunta final nao e prever sobrevida usando tempo de sobrevida; e classificar risco de obito a partir de variaveis disponiveis sem vazamento."  
**Visual sugerido:** diagrama `features clinicas -> modelo -> classe obito`, com `Survival Months` marcado como excluido do modelo principal.  
**Pergunta que antecipa:** por que remover uma variavel tao preditiva?

## Slide 5 - Dataset

**Titulo:** SEER como Baseline e METABRIC como Evolucao Canonica  
**Conteudo-chave:**
- SEER: `4024x16` bruto, `4023` registros apos remover 1 duplicata, classe positiva `15,31%`;
- METABRIC: `2509x34` bruto, `1876` registros apos saneamento, classe positiva `57,30%`;
- METABRIC inclui tratamento, ER/PR/HER2, PAM50, NPI e mutation count;
- trade-off do METABRIC: base mais rica, mas com missingness mais serio e `633` linhas removidas.
**Mensagem oral:** "O SEER foi importante para corrigir o pipeline; o METABRIC foi escolhido porque traz mais informacao clinica para a mesma pergunta, mas essa troca tambem trouxe um custo real de missingness."  
**Visual sugerido:** tabela comparativa SEER vs METABRIC com colunas `bruto`, `apos saneamento`, `classe positiva`, `vantagem`, `trade-off`.  
**Pergunta que antecipa:** por que trocar de dataset no meio do projeto?

## 2. Desenvolvimento da Solucao

## Slide 6 - Arquitetura Geral do Sistema

**Titulo:** Arquitetura Geral  
**Conteudo-chave:**
- trilha oficial: tema cancer de mama -> SEER -> sanitizacao -> EDA -> feature engineering;
- primeira rodada: baselines, ensemble ponderado e neuro-fuzzy;
- identificacao dos limites estruturais do SEER;
- migracao justificada para METABRIC;
- rerun completo com a mesma disciplina metodologica;
- leitura final: SEER como baseline corrigido, METABRIC como v2 canonica.
**Mensagem oral:** "A arquitetura da solucao tambem e uma arquitetura de decisao: primeiro corrigimos a trilha SEER, depois usamos seus limites para justificar a evolucao METABRIC."  
**Visual sugerido:** fluxograma cronologico `SEER corrigido -> limites -> METABRIC v2 -> resultados finais`.  
**Pergunta que antecipa:** onde entram o sistema hibrido e o ensemble?

## Slide 7 - Pre-processamento dos Dados

**Titulo:** Pre-processamento e Politica de Vazamento  
**Conteudo-chave:**
- sanitizacao centralizada;
- dicionario de dados;
- EDA com metadados e relacoes;
- imputacao robusta;
- one-hot encoding;
- exclusao de variaveis de vazamento.
**Mensagem oral:** "O pre-processamento deixou de ser apenas limpeza e passou a ser uma politica metodologica."  
**Visual sugerido:** checklist de pipeline + destaque para `leakage policy`.  
**Pergunta que antecipa:** como garantir que o teste nao foi contaminado?

## Slide 8 - Modelos Inteligentes Utilizados

**Titulo:** Modelos Avaliados  
**Conteudo-chave:**
- Logistic Regression como baseline explicavel;
- Random Forest, ExtraTrees e GradientBoosting;
- HistGradientBoosting, AdaBoost, SVM calibrado e MLP;
- neuro-fuzzy cooperativo como comparativo academico.
**Mensagem oral:** "A comparacao inclui modelos simples, modelos de arvore, MLP e uma camada hibrida compatível com a proposta da disciplina."  
**Visual sugerido:** tabela por familia: linear, arvores, redes, ensemble, neuro-fuzzy.  
**Pergunta que antecipa:** qual e o baseline e qual e o modelo inteligente principal?

## Slide 9 - Arquitetura Hibrida / Ensemble

**Titulo:** Ensemble Ponderado e Neuro-fuzzy Cooperativo  
**Conteudo-chave:**
- ensemble por soft voting ponderado;
- pesos derivados da validacao;
- threshold escolhido na validacao;
- teste preservado para reporte final;
- neuro-fuzzy = fuzzificacao manual + MLP, nao ANFIS completo.
**Mensagem oral:** "O ensemble foi usado como ponto operacional de alta sensibilidade; o neuro-fuzzy foi mantido como comparativo hibrido, mas sem afirmar que e ANFIS."  
**Visual sugerido:** diagrama com modelos individuais alimentando ensemble e bloco separado neuro-fuzzy.  
**Pergunta que antecipa:** o hibrido realmente melhora? Em qual criterio?

## Slide 10 - Pipeline de Treinamento

**Titulo:** Pipeline de Treinamento e Validacao  
**Conteudo-chave:**
- treino / validacao / teste;
- validacao escolhe pesos e threshold;
- teste usado uma vez para reporte;
- estabilidade por 5 seeds;
- notebook e relatorios como rastreabilidade.
**Mensagem oral:** "A mudanca metodologica mais importante foi separar escolha de modelo e avaliacao final."  
**Visual sugerido:** trilha `train -> validation -> test`, com setas para selecao e reporte.  
**Pergunta que antecipa:** o threshold foi escolhido olhando o teste?

## 3. Avaliacao Experimental

## Slide 11 - Metodologia Experimental

**Titulo:** Desenho Experimental  
**Conteudo-chave:**
- duas trilhas comparaveis: SEER corrigido e METABRIC canonico;
- mesma disciplina metodologica nas duas;
- METABRIC nao substitui silenciosamente o SEER: ele executa novamente saneamento, EDA, features, modelos, ensemble, neuro-fuzzy e avaliacao;
- analise sem `Survival Months` como resultado principal;
- analise de sensibilidade com variavel de sobrevida separada.
**Mensagem oral:** "A comparacao nao apaga o SEER; ela mostra por que uma base mais rica melhora o teto do experimento quando a mesma disciplina metodologica e reaplicada."  
**Visual sugerido:** matriz `SEER` x `METABRIC` com fases iguais marcadas: saneamento, EDA, features, baselines, ensemble, neuro-fuzzy, teste.  
**Pergunta que antecipa:** a comparacao entre bases e justa?

## Slide 12 - Metricas de Avaliacao

**Titulo:** Metricas e Custo do Erro  
**Conteudo-chave:**
- recall;
- F2-score;
- PR AUC;
- falsos negativos;
- acuracia como secundaria.
**Mensagem oral:** "O F2 foi priorizado porque pesa mais o recall; isso faz sentido quando falso negativo tem custo maior."  
**Visual sugerido:** formula/intuicao do F2 e quadro `FN > FP` em custo clinico.  
**Pergunta que antecipa:** por que o modelo com menor acuracia pode ser aceitavel?

## Slide 13 - Resultados dos Modelos Individuais

**Titulo:** Modelos Individuais: SEER vs METABRIC  
**Conteudo-chave:**
- SEER: Logistic Regression F2 `0.4832`, recall `0.6098`, PR AUC `0.3525`, FN `48`;
- METABRIC: GradientBoosting F2 `0.7787`, recall `0.7953`, PR AUC `0.7600`, FN `44`;
- salto de desempenho associado a melhor qualidade dos dados.
**Mensagem oral:** "Antes do ensemble, o METABRIC ja melhora muito o baseline individual."  
**Visual sugerido:** tabela compacta com os dois melhores modelos individuais.  
**Pergunta que antecipa:** o ganho veio do ensemble ou do dataset?

## Slide 14 - Resultados do Sistema Hibrido

**Titulo:** Resultados do Ensemble e Neuro-fuzzy  
**Conteudo-chave:**
- SEER ensemble threshold `0.22`: F2 `0.5188`, recall `0.7642`, FN `29`, FP `320`;
- METABRIC ensemble threshold `0.16`: F2 `0.8770`, recall `0.9953`, FN `1`, FP `146`;
- neuro-fuzzy: SEER F2 `0.2886`; METABRIC F2 `0.6548`.
**Mensagem oral:** "O ensemble aumenta sensibilidade; o neuro-fuzzy e metodologicamente relevante, mas nao foi campeao."  
**Visual sugerido:** tabela de resultados hibridos + destaque de FN.  
**Pergunta que antecipa:** por que manter neuro-fuzzy se ele nao venceu?

## Slide 15 - Comparacao Geral

**Titulo:** Comparacao Geral dos Cenarios  
**Conteudo-chave:**
- SEER individual vs SEER ensemble;
- METABRIC individual vs METABRIC ensemble;
- METABRIC supera SEER em qualidade de dados e desempenho;
- ensemble deve ser lido como ponto operacional, nao como melhor universal.
**Mensagem oral:** "A melhor leitura e dupla: o dataset elevou o teto, e o ensemble deslocou o ponto de operacao para sensibilidade."  
**Visual sugerido:** grafico de barras para F2/recall e tabela de FN/FP.  
**Pergunta que antecipa:** qual modelo voce escolheria na pratica?

## Slide 16 - Analise dos Resultados

**Titulo:** Interpretacao Critica  
**Conteudo-chave:**
- SEER: ganho de recall com muitos falsos positivos;
- METABRIC: quase elimina falsos negativos, mas tambem aumenta falsos positivos;
- explicabilidade, calibracao e estabilidade reforcam a defesa;
- resultado nao equivale a validacao clinica.
**Mensagem oral:** "A conclusao nao e que o ensemble sempre vence, e sim que ele cria um ponto de operacao defensavel quando o objetivo e sensibilidade."  
**Visual sugerido:** matriz de trade-off `recall alto` x `falsos positivos`.  
**Pergunta que antecipa:** esse modelo poderia ser usado em clinica real?

## 4. Conclusao

## Slide 17 - Principais Conclusoes

**Titulo:** Conclusoes Principais  
**Conteudo-chave:**
- metodologia corrigida aumentou a credibilidade;
- METABRIC virou trilha canonica por qualidade clinica;
- ensemble funcionou como ponto de alta sensibilidade;
- neuro-fuzzy mostrou valor comparativo, nao superioridade empirica.
**Mensagem oral:** "O principal resultado foi construir um pipeline mais correto e mais defensavel, nao apenas reportar uma metrica maior."  
**Visual sugerido:** quatro conclusoes em blocos.  
**Pergunta que antecipa:** qual e a principal contribuicao do trabalho?

## Slide 18 - Limitacoes do Trabalho

**Titulo:** Limitacoes  
**Conteudo-chave:**
- datasets publicos, sem validacao clinica externa;
- classificacao supervisionada, nao survival analysis formal;
- neuro-fuzzy nao e ANFIS completo;
- SEER vs METABRIC nao e benchmark perfeito entre bases identicas;
- METABRIC tem missingness relevante: `633` linhas removidas, sendo `528` por ausencia simultanea de status e `survival_months`;
- falsos positivos ainda relevantes.
**Mensagem oral:** "Essas limitacoes nao invalidam o trabalho; elas delimitam corretamente o escopo academico e deixam claro que uma base clinicamente mais rica tambem exige decisoes mais fortes de saneamento."  
**Visual sugerido:** lista de limitacoes em coluna unica.  
**Pergunta que antecipa:** o que impede uso clinico direto?

## Slide 19 - Trabalhos Futuros

**Titulo:** Trabalhos Futuros  
**Conteudo-chave:**
- survival analysis formal;
- explicabilidade local;
- validacao cruzada repetida;
- analise de decisao por custo clinico;
- calibragem fuzzy com especialista;
- validacao externa.
**Mensagem oral:** "A proxima evolucao natural e sair da classificacao simples e aproximar a avaliacao do uso clinico."  
**Visual sugerido:** roadmap curto de evolucao.  
**Pergunta que antecipa:** como melhorar a pesquisa depois da disciplina?

## Slide 20 - Encerramento / Perguntas

**Titulo:** Perguntas  
**Conteudo-chave:**
- mensagem final: SEER corrigido como baseline; METABRIC como v2 canonica;
- frase de fechamento: "bons dados e boa validacao foram mais importantes que complexidade isolada";
- perguntas provaveis.
**Mensagem oral:** "Ficamos a disposicao para perguntas, principalmente sobre metricas, vazamento, ensemble e papel do neuro-fuzzy."  
**Visual sugerido:** tela limpa com mensagem final e contato/equipe.  
**Perguntas provaveis para treinar:**
- por que nao usar acuracia?
- por que remover `Survival Months`?
- o ensemble foi escolhido no teste?
- o neuro-fuzzy e ANFIS?
- por que o METABRIC e melhor que o SEER?
- como justificar falsos positivos?

## Ordem recomendada dos audios NotebookLM

1. A ilusao das metricas na IA medica
2. Por que a IA falha sem biomarcadores
3. Por que acuracia alta engana no cancer
4. IA e alarmes falsos no cancer
5. Como a sobrevida invalidou a IA medica
6. IA a prova de vazamento no METABRIC
7. Como metadados salvaram o modelo oncologico
8. IA que erra mais para salvar vidas
9. Limites da IA no cancer de mama
10. Bons dados vencem algoritmos no cancer
11. Por que IA complexa falha no cancer
12. Ensembles na predicao de cancer de mama
