# Roteiro Detalhado e Curadoria Final - Defesa Trabalho 2

**Data:** 2026-07-09  
**Apresentacao original revisada:** `/home/cayo/Downloads/Breast_Cancer_Risk_Intelligence.pptx`  
**Apresentacao curada recomendada:** `/home/cayo/Downloads/Breast_Cancer_Risk_Intelligence_curado.pptx` e `reports/consolidados/finalizacao-defesa-2026-07-09/Breast_Cancer_Risk_Intelligence_curado.pptx`  
**PDF de revisao:** `reports/consolidados/finalizacao-defesa-2026-07-09/Breast_Cancer_Risk_Intelligence.pdf`  
**PDF da versao curada:** `reports/consolidados/finalizacao-defesa-2026-07-09/Breast_Cancer_Risk_Intelligence_curado.pdf`  
**Folha de contato:** `reports/consolidados/finalizacao-defesa-2026-07-09/pptx_contact_sheet.png`  
**Folha de contato curada:** `reports/consolidados/finalizacao-defesa-2026-07-09/pptx_contact_sheet_curado.png`  
**OCR auxiliar:** `reports/consolidados/finalizacao-defesa-2026-07-09/pptx_ocr.txt`

## Status Operacional dos Arquivos

- O artigo revisado corrente e `docs/template/Breast_Cancer/main.pdf`, com copia em `reports/consolidados/finalizacao-defesa-2026-07-09/artigo_prism_revisao_editorial_local.pdf`.
- O PPTX exportado em `/home/cayo/Downloads/Breast_Cancer_Risk_Intelligence.pptx` esta renderizado como imagens de slide; os textos problematicos aparecem no OCR, mas nao como caixas de texto editaveis no XML do PowerPoint.
- A versao `Breast_Cancer_Risk_Intelligence_curado.pptx` aplica patches visuais nos slides 11-14 para remover os claims mais arriscados: "clinico seguro", "erradicacao do risco", "modelo definitivo", "complexidade nao supera arvores" e "imortalizado".
- A conversao da versao curada para PDF foi validada com LibreOffice headless, gerando 15 paginas em 16:9.

## Tese da Defesa

O trabalho nao deve ser apresentado como "um modelo clinico pronto". A tese correta e:

> O Projeto 2 evoluiu de uma trilha SEER metodologicamente corrigida para uma trilha METABRIC canonica. A melhoria central veio da combinacao entre remocao de vazamento, separacao treino/validacao/teste, melhor qualidade informacional do dataset e leitura honesta do trade-off entre falsos negativos e falsos positivos.

## Diagnostico da Apresentacao Atual

A apresentacao atual esta forte e cobre os pontos essenciais:

- explica o custo assimetrico entre falso negativo e falso positivo;
- mostra por que `Survival Months` foi removido;
- separa SEER corrigido de METABRIC canonico;
- mostra validacao escolhendo threshold e teste apenas reportando;
- delimita o neuro-fuzzy como comparativo academico, nao ANFIS;
- exibe o trade-off do ensemble com `1` falso negativo e `146` falsos positivos;
- inclui limitacoes e apendice de perguntas metodologicas.

As melhorias restantes sao de linguagem defensiva, nao de estrutura.

## Ajustes Recomendados nos Slides

| Slide | Manter | Ajustar na fala ou no texto |
|---|---|---|
| 1 | Tese SEER corrigido -> METABRIC canonico. | Sem ajuste essencial. |
| 2 | Estrutura em 5 blocos. | Passar rapido; nao gastar tempo administrativo. |
| 3 | Foco em custo do erro. | Trocar oralmente "erros fatais" por "erros de maior custo no problema". |
| 4 | Vazamento por `Survival Months`. | Dizer que a variavel e informacao de acompanhamento posterior, nao feature de diagnostico. |
| 5 | Comparacao SEER vs METABRIC. | Reforcar que METABRIC nao apaga SEER; ele e evolucao depois de corrigir a base inicial. |
| 6 | Saneamento e EDA. | Nao interpretar cada grafico; dizer que EDA virou contrato antes da modelagem. |
| 7 | Features clinicas mais ricas. | Evitar causalidade; usar "sinais clinicamente plausiveis". |
| 8 | Validacao escolhe, teste reporta. | Frase obrigatoria: "pesos e threshold foram escolhidos na validacao; o teste ficou preservado". |
| 9 | Modelos e neuro-fuzzy. | Frase obrigatoria: "nao e ANFIS completo". |
| 10 | METABRIC melhora antes do ensemble. | Este e um slide central; mostrar que o ganho nao e so threshold agressivo. |
| 11 | Threshold `0.16`. | Trocar "clinico seguro" por "ponto operacional experimental de alta sensibilidade". |
| 12 | Matriz e trade-off. | Trocar "erradicacao do risco" e "modelo definitivo" por "reducao extrema de falsos negativos no protocolo". |
| 13 | Sintese do aprendizado. | Trocar "complexidade nao supera arvores" por "neste experimento, o neuro-fuzzy nao superou os melhores tabulares". |
| 14 | Limitacoes. | Trocar "imortalizado" por "documentado como baseline corrigido"; citar que SEER vs METABRIC nao e benchmark clinico estrito. |
| 15 | Perguntas metodologicas. | Usar como backup ou fechamento se sobrar tempo. |

## Roteiro Oral de 12 a 15 Minutos

### Slide 1 - Abertura (0:00 - 0:30)

**Objetivo:** estabelecer a historia do trabalho.

Fala sugerida:

> Este trabalho apresenta um sistema de inteligencia computacional para classificacao de obito observado em cancer de mama. A historia principal nao e apenas treinar varios modelos. A historia e corrigir uma pergunta metodologicamente contaminada, proteger o teste e mostrar como uma base clinica mais rica muda o teto do problema.

**Nao dizer:** "modelo clinico seguro" ou "sistema pronto para uso".

### Slide 2 - Estrutura (0:30 - 0:50)

**Objetivo:** orientar a banca rapidamente.

Fala sugerida:

> A defesa segue cinco partes: problema, processamento dos dados, treinamento, avaliacao e conclusao. Vou concentrar o tempo nas decisoes que afetam a validade do experimento: vazamento, validacao/teste, troca de dataset e trade-off entre falsos negativos e falsos positivos.

### Slide 3 - Custo Assimetrico do Erro (0:50 - 1:50)

**Objetivo:** justificar recall, F2, PR AUC e falsos negativos.

Fala sugerida:

> Em problemas de saude, acuracia pode ser enganosa. Se a classe positiva representa obito observado, um falso negativo tem custo conceitualmente maior que um falso positivo. Por isso, alem de precision e accuracy, a leitura principal aqui usa recall, F2, PR AUC e numero absoluto de falsos negativos.

**Ponto de cuidado:** nao falar como se o sistema estivesse tomando conduta medica real.

### Slide 4 - Vazamento por `Survival Months` (1:50 - 3:00)

**Objetivo:** defender a correcao metodologica mais importante.

Fala sugerida:

> A versao inicial usava `Survival Months` para prever status de obito. Isso cria um atalho: a variavel mede tempo de acompanhamento, portanto carrega informacao posterior ao desfecho. A correcao foi retirar essa coluna do modelo principal. Ela pode aparecer como analise de sensibilidade, mas nao como feature da pergunta central.

**Resposta curta para banca:** "Removemos porque tempo de sobrevida e informacao posterior; usar isso para prever obito contamina a pergunta."

### Slide 5 - SEER vs METABRIC (3:00 - 4:10)

**Objetivo:** justificar a evolucao canonica.

Fala sugerida:

> O SEER corrigido ficou como baseline metodologico: foi nele que saneamos a pergunta, a validacao e o pipeline. Mas ele tem menor profundidade clinica. O METABRIC entra como evolucao canonica porque traz tratamento, ER, PR, HER2, PAM50, NPI e mutacoes. A comparacao nao e um benchmark clinico estrito entre bases identicas; e uma evolucao pedagogica sob disciplina metodologica comum.

**Ponto forte:** menos registros no METABRIC, mas mais qualidade informacional.

### Slide 6 - Saneamento e EDA (4:10 - 4:55)

**Objetivo:** provar que a modelagem nao veio antes do contrato de dados.

Fala sugerida:

> Antes de treinar modelos, o projeto consolidou dicionario, metadados, distribuicao do alvo e relacoes principais. A EDA aqui nao foi decorativa; ela definiu schema, target, politica de vazamento e transformacoes permitidas.

### Slide 7 - Engenharia de Features (4:55 - 5:45)

**Objetivo:** mostrar por que METABRIC sustenta melhor a modelagem.

Fala sugerida:

> No SEER, a engenharia de features era mais limitada: proporcoes nodais e indicadores simples. No METABRIC, conseguimos representar burden tumoral e nodal, exposicao a tratamento, perfis moleculares e atributos fuzzy. Eu chamaria isso de sinais clinicamente plausiveis, nao de causalidade clinica provada.

### Slide 8 - Validacao Escolhe, Teste Reporta (5:45 - 6:55)

**Objetivo:** blindar contra pergunta sobre tuning no teste.

Fala sugerida:

> Este slide e um dos mais importantes. O treino ajusta os modelos. A validacao escolhe pesos e threshold. O teste fica separado e e usado so uma vez para reporte final. Portanto, o threshold `0.16` do METABRIC e os pesos do ensemble nao foram escolhidos olhando o teste.

**Resposta curta para banca:** "Validacao escolheu, teste apenas reportou."

### Slide 9 - Modelos e Neuro-Fuzzy (6:55 - 7:40)

**Objetivo:** enquadrar o requisito academico sem exagero.

Fala sugerida:

> A competicao real envolveu modelos tabulares. O neuro-fuzzy foi mantido como comparativo academico porque a disciplina pede sistemas hibridos ou ensemble. Mas ele nao e ANFIS completo; e um modelo cooperativo com fuzzificacao manual alimentando uma MLP.

### Slide 10 - Modelos Individuais (7:40 - 8:55)

**Objetivo:** provar que o ganho veio do dado, nao so do ensemble.

Fala sugerida:

> Antes do ensemble, o METABRIC ja melhora muito o resultado. No SEER, a Logistic Regression teve F2 `0.4832`, recall `0.6098` e PR AUC `0.3525`. No METABRIC, o GradientBoosting chegou a F2 `0.7787`, recall `0.7953` e PR AUC `0.7600`. Isso mostra que a qualidade informacional do dataset elevou o teto do projeto.

### Slide 11 - Otimizacao de Threshold (8:55 - 10:00)

**Objetivo:** explicar o papel do threshold.

Fala sugerida:

> O threshold padrao de `0.50` nao necessariamente atende ao objetivo de sensibilidade. O threshold `0.16` foi escolhido na validacao para deslocar o ponto operacional: aumentar recall e reduzir falsos negativos. Isso sacrifica precision, entao deve ser lido como decisao experimental de alta sensibilidade, nao como modelo universalmente melhor.

### Slide 12 - Trade-off Clinico/Operacional (10:00 - 11:40)

**Objetivo:** assumir o custo do resultado.

Fala sugerida:

> O resultado mais chamativo e `1` falso negativo no METABRIC. Mas ele vem junto com `146` falsos positivos. Entao a conclusao honesta nao e "erradicamos risco"; e "reduzimos falsos negativos de forma extrema neste protocolo, aceitando um custo operacional alto em alertas falsos". Isso e aceitavel como ponto experimental de triagem sensivel, nao como decisao clinica solitaria.

**Frase de defesa:** "O modelo nao decide tratamento; ele cria um ponto de alerta que ainda precisaria de validacao externa e analise de custo."

### Slide 13 - O Que Foi Comprovado (11:40 - 12:45)

**Objetivo:** sintetizar a tese.

Fala sugerida:

> O projeto comprovou tres coisas. Primeiro, corrigir metodologia importa: remover `Survival Months` e preservar o teste mudou a validade do trabalho. Segundo, o dataset eleva o teto: a maior mudanca veio da riqueza clinica do METABRIC. Terceiro, nem todo hibrido vence: neste experimento, o neuro-fuzzy foi pedagogicamente util, mas nao superou os melhores modelos tabulares.

### Slide 14 - Limitacoes e Estado Final (12:45 - 14:00)

**Objetivo:** fechar sem prometer demais.

Fala sugerida:

> As limitacoes sao claras: isto e classificacao tabular, nao survival analysis formal; usa bases publicas, sem validacao clinica externa; e ainda tem alto volume de falsos positivos. O SEER fica documentado como baseline corrigido, e o METABRIC fica como evolucao canonica por suportar engenharia clinica mais rica. O proximo passo natural seria survival analysis formal, explicabilidade local por instancia e validacao externa.

### Slide 15 - Apendice / Perguntas (14:00 - 15:00, se usado)

Use este slide so se houver tempo ou pergunta. Respostas curtas:

- **Por que nao acuracia?** Porque classe positiva e custo de erro tornam recall/F2/FN mais informativos.
- **Por que remover `Survival Months`?** Porque e informacao de acompanhamento posterior.
- **O threshold foi escolhido no teste?** Nao. Validacao escolheu; teste reportou.
- **E ANFIS?** Nao. E neuro-fuzzy cooperativo com fuzzificacao manual + MLP.

## Perguntas de Banca e Respostas Preparadas

### 1. Por que trocar SEER por METABRIC nao e cherry-picking?

Resposta:

> Porque o SEER nao foi descartado nem escondido. Ele ficou como baseline corrigido. O METABRIC entrou depois como evolucao canonica por ter variaveis clinicas e moleculares mais ricas para a mesma familia de problema. A comparacao e pedagogica e metodologica, nao um benchmark clinico estrito entre bases identicas.

### 2. O ensemble vale mesmo com `146` falsos positivos?

Resposta:

> Depende do objetivo. Se o objetivo e alta sensibilidade, o ponto `0.16` reduz falso negativo para `1`, mas aumenta falsos positivos para `146`. Por isso eu nao venderia como melhor modelo universal; venderia como ponto operacional experimental para triagem sensivel.

### 3. Isso poderia ser usado clinicamente?

Resposta:

> Nao diretamente. O trabalho e academico e usa datasets publicos. Para uso clinico seria necessario validacao externa, calibracao por contexto, analise de custo e provavelmente uma modelagem formal de sobrevivencia.

### 4. Por que manter neuro-fuzzy se ele perdeu?

Resposta:

> Porque ele cumpre papel de comparativo hibrido dentro da ementa. O resultado negativo tambem e informativo: fuzzificacao manual sem calibragem especialista pode perder informacao e ficar abaixo dos modelos tabulares.

### 5. Qual e a contribuicao principal?

Resposta:

> A contribuicao principal e metodologica: corrigir vazamento, proteger o teste, comparar baseline e evolucao com disciplina comum, e interpretar o ensemble com seus custos em falsos positivos.

## Checklist Final Antes da Apresentacao

- [ ] Trocar oralmente "clinico seguro" por "ponto operacional experimental de alta sensibilidade".
- [ ] Trocar oralmente "erradicacao do risco" por "reducao extrema de falsos negativos no protocolo".
- [ ] Garantir que `1 FN` sempre apareca junto de `146 FP`.
- [ ] Ensaiar a frase "validacao escolhe, teste reporta".
- [ ] Ensaiar a frase "nao e ANFIS completo".
- [ ] Ensaiar a limitacao "sem validacao clinica externa".
- [ ] Decidir se o slide 15 sera usado como fechamento ou apenas backup.
