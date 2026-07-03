# Revisao Critica e Estrategia Visual dos Slides - Trabalho 2

## Diagnostico rapido

Foram revisados tres artefatos:

- `reports/consolidados/plano-detalhado-slides-trabalho-2.md`
- `reports/consolidados/slides-trabalho-2/index.html`
- `reports/consolidados/slides-trabalho-2/notebooklm-trabalho-2-breast-cancer.pptx`

Tambem foram geradas capturas de apoio em:

- `reports/consolidados/slides-trabalho-2/review/html-desktop.png`
- `reports/consolidados/slides-trabalho-2/review/html-mobile.png`
- `reports/consolidados/slides-trabalho-2/review/pptx_pages/page-01.png` a `page-06.png`

Conclusao: os dois caminhos atuais acertam partes diferentes, mas nenhum deve ser tratado como versao final.

- **HTML atual:** correto, rastreavel e limpo, mas com aparencia de pagina/documentacao gerada, nao de apresentacao editorial.
- **PPTX NotebookLM:** tem mais estrutura visual de slide, mas e verboso, pesado, com bordas fortes, hierarquia irregular e cara de template automatico.

## Principio de redesign

O deck final precisa parecer uma apresentacao de defesa academica editada por humanos. A regra central passa a ser:

> Cada slide deve defender uma afirmacao, nao listar um topico.

Isso muda os titulos, a composicao e a selecao de graficos.

Exemplos:

- Antes: `Metricas de Avaliacao`
- Melhor: `F2 e recall foram priorizados porque falso negativo pesa mais`

- Antes: `Resultados do Sistema Hibrido`
- Melhor: `O ensemble quase elimina falsos negativos no METABRIC, mas aumenta falsos positivos`

- Antes: `Dataset`
- Melhor: `METABRIC virou canonico porque adiciona sinais clinicos ausentes no SEER`

## Problemas do HTML atual

### 1. Parece pagina, nao slide

O HTML usa cards, bordas, sombras e empilhamento vertical como se fosse relatorio web. Isso cria leitura de pagina longa. Para slide, cada tela precisa ter uma composicao fechada, com foco e respiracao.

**Correcao:** usar layout 16:9 fixo por slide, sem pagina corrida como experiencia principal. A navegacao pode existir, mas a composicao deve ser de palco.

### 2. Hierarquia generica

Quase todos os slides têm a mesma energia visual: kicker azul, titulo, cards/tabela. Isso passa sensacao de geracao automatica.

**Correcao:** variar composicoes por funcao:

- capa editorial;
- slide de tese;
- slide de comparacao;
- slide de pipeline;
- slide de resultado com numero hero;
- slide de trade-off;
- slide de conclusao.

### 3. Pouca narrativa visual

Os dados aparecem como tabela ou card, mas poucos slides fazem o olho entender "qual e a descoberta".

**Correcao:** transformar resultados em contrastes visuais:

- SEER vs METABRIC;
- individual vs ensemble;
- falsos negativos reduzidos vs falsos positivos aceitos;
- baseline corrigido vs evolucao canonica.

### 4. Mobile quebrado

A captura mobile mostrou titulo grande demais, fluxo quebrado e scroll horizontal.

**Correcao:** se houver versao web responsiva, criar leitura mobile propria:

- capa com titulo menor;
- slides em modo vertical;
- tabelas viram pares comparativos;
- graficos aparecem antes das notas;
- sem scroll horizontal.

## Problemas do PPTX NotebookLM

### 1. Verbosidade

Slides como o 3 e 5 tentam explicar tudo dentro da tela. Isso compete com a fala.

**Correcao:** cortar texto em 40 a 60%. Slide deve carregar o ponto; fala carrega o detalhe.

### 2. Bordas e caixas pesadas

O PPTX usa caixas grandes, contornos fortes e divisorias, criando uma grade visual dura. Isso parece template automatico.

**Correcao:** reduzir molduras. Usar alinhamento, espacamento e blocos de valor em vez de bordas.

### 3. Tipografia exagerada e pouco refinada

Titulos muito grandes e texto de corpo tambem grande em blocos longos. O resultado e poluido mesmo com poucos elementos.

**Correcao:** usar escala:

- titulo: 34-42 px;
- subtitulo/claim: 22-26 px;
- corpo: 18-22 px;
- notas: 12-14 px;
- numeros hero: 56-84 px quando forem foco.

### 4. Rodape e marca NotebookLM

O rodape do PPTX carrega metadados demais e a marca NotebookLM. Isso enfraquece a sensacao de autoria do grupo.

**Correcao:** remover rodape recorrente ou reduzir para slide number + disciplina. Remover marca NotebookLM na versao final.

### 5. Exportacao possivelmente como imagem

A extracao textual simples do PPTX nao encontrou texto editavel. Isso sugere que o deck pode ter sido exportado como composicao visual. Serve como referencia, mas e ruim como base final de edicao fina.

**Correcao:** usar NotebookLM como rascunho visual, nao como arquivo-mestre.

## Contrato visual recomendado

### Tom

Academico, clinico, analitico e controlado. Evitar estetica de startup, dashboard SaaS ou template automatico.

### Paleta

- fundo: branco quente ou cinza muito claro;
- texto principal: quase preto;
- azul escuro: metodologia / trilha METABRIC;
- cinza: baseline SEER / contexto;
- vermelho contido: risco, falso negativo, vazamento;
- verde/teal contido: melhoria ou resultado canonico.

Regra: cor so entra para significado. Nao usar azul em tudo.

### Layout

Usar 5 familias de slide:

1. **Tese editorial:** uma frase grande + diagrama simples.
2. **Comparacao lado a lado:** SEER vs METABRIC.
3. **Pipeline:** fluxo horizontal com tres fases dominantes.
4. **Resultado numerico:** numero hero + tabela minima.
5. **Trade-off:** dois pesos em tensao, por exemplo `1 FN` vs `146 FP`.

### Tipografia

Usar no maximo quatro niveis:

- claim/titulo;
- subtitulo/caveat;
- valor destacado;
- nota/fonte.

Evitar bullets longos. Preferir frases curtas com verbo.

## Nova narrativa de slides

O plano de 20 slides continua correto, mas precisa ser reescrito em formato de claims.

| Slide | Papel antigo | Claim recomendado |
|---:|---|---|
| 1 | Capa | O projeto evoluiu de SEER corrigido para METABRIC canonico |
| 2 | Roteiro | A defesa segue problema, solucao, experimento e conclusao |
| 3 | Introducao | Em saude, acuracia alta pode esconder erro grave |
| 4 | Problema | `Survival Months` foi removido para evitar vazamento |
| 5 | Dataset | METABRIC adiciona sinais clinicos que o SEER nao tem |
| 6 | Arquitetura | O sistema rastreia dado bruto ate decisao final |
| 7 | Pre-processamento | EDA virou contrato de dados, nao etapa decorativa |
| 8 | Modelos | A comparacao separa baseline, modelos fortes e hibrido |
| 9 | Hibrido | Ensemble e neuro-fuzzy cumprem papeis diferentes |
| 10 | Treinamento | Validacao escolhe, teste reporta |
| 11 | Metodologia | SEER e METABRIC passaram pelas mesmas fases essenciais |
| 12 | Metricas | F2 e recall respondem melhor ao custo do falso negativo |
| 13 | Individuais | METABRIC melhora antes mesmo do ensemble |
| 14 | Hibrido | Ensemble reduz FN, mas precisa assumir FP |
| 15 | Comparacao | Dados melhores elevaram o teto; threshold moveu sensibilidade |
| 16 | Analise | O melhor resultado e um ponto operacional, nao verdade clinica |
| 17 | Conclusoes | O ganho principal foi metodologico e informacional |
| 18 | Limitacoes | A defesa e academica, nao validacao clinica externa |
| 19 | Futuro | A proxima etapa e survival analysis e validacao externa |
| 20 | Perguntas | A banca deve questionar acuracia, vazamento, ANFIS e FP |

## Inventario de camadas visuais

| Slide | Camada visual | Job narrativo | Forma recomendada | Asset/base |
|---:|---|---|---|---|
| 1 | Evolucao do projeto | Mostrar transformacao | Diagrama editorial SEER -> METABRIC | autoral |
| 3 | Custo do erro | Mostrar por que FN importa | Dois blocos contrastivos FN vs FP | autoral |
| 5 | Dataset | Comparar profundidade | Tabela enxuta + destaque molecular | `pam50_deceased_rate.png` opcional |
| 6 | Arquitetura | Explicar fluxo | Pipeline horizontal simplificado | autoral |
| 7 | EDA | Provar maturidade | Checklist + mini heatmap | `numeric_correlation_heatmap.png` |
| 9 | Hibrido | Distinguir ensemble/neuro-fuzzy | Diagrama de caminhos paralelos | autoral |
| 10 | Split | Defender teste intocado | Train/validation/test com travas | autoral |
| 13 | Modelos individuais | Mostrar salto do dataset | Tabela de 2 linhas ou slope/dot | T1/T2 |
| 14 | Sistema hibrido | Mostrar ganho e custo | Numero hero `1 FN` + FP visivel | T3/T4/T5/T6 |
| 15 | Comparacao geral | Sintetizar progressao | Barras F2/recall com 4 cenarios | T1/T2/T3/T4 |
| 16 | Trade-off | Evitar exagero | Matriz recall alto vs FP alto | T7/T8 |
| 17 | Conclusao | Fixar tres aprendizados | Tres blocos numerados | autoral |

## Regras praticas para a nova versao

1. **Uma frase-tese por slide.** O titulo deve carregar a conclusao.
2. **Uma visualizacao principal por slide.** Se houver tabela e grafico, um deles deve ser subordinado.
3. **Maximo de 25 a 35 palavras por slide**, exceto tabelas técnicas dos resultados.
4. **Nao usar cards iguais em todos os slides.** Isso foi a principal causa da "cara de IA".
5. **Nao usar tabelas grandes cruas.** Transformar em comparacoes de 2 a 4 linhas.
6. **Sempre parear recall alto com FP.** Isso protege a defesa contra exagero.
7. **Usar anotacao curta no grafico.** Exemplo: `threshold escolhido na validacao`.
8. **Remover rodapes pesados.** Slide number discreto basta.
9. **Evitar bordas fortes.** Usar alinhamento e contraste de fundo.
10. **Criar duas versoes de layout:** 16:9 para apresentacao e vertical responsiva para revisao/leitura.

## Decisao recomendada

Usar o **HTML como base tecnica**, mas redesenhar completamente a linguagem visual.

Usar o **PPTX NotebookLM como referencia de conteudo bruto**, nao como master visual.

O caminho mais robusto e:

1. criar uma nova versao `index_v2.html` com layout editorial 16:9;
2. gerar graficos compostos proprios para os slides 13-16;
3. exportar screenshots/PDF ou converter depois para PPTX;
4. manter o NotebookLM PPTX apenas como material alternativo de brainstorming.

## Prioridade de redesign

### Alta

- Slide 1: capa precisa de identidade academica e tese.
- Slide 3: transformar em hook forte sobre custo do erro.
- Slide 5: melhorar comparacao SEER vs METABRIC.
- Slide 13: criar comparacao visual clara dos modelos individuais.
- Slide 14: tornar `1 falso negativo` o foco, mas mostrar `146 falsos positivos`.
- Slide 15: criar grafico de progressao F2/recall.
- Slide 16: explicitar trade-off.

### Media

- Slides 6, 9 e 10: refazer diagramas com menos caixas.
- Slides 17-20: reduzir texto e transformar em encerramento de defesa.

### Baixa

- Slides 2, 8, 11, 12: podem ser mais simples, mas com titulos-claim.

