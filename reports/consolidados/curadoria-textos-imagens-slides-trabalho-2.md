# Curadoria de Textos e Imagens dos Slides - Trabalho 2

## Objetivo

Este documento revisa os textos usados como referencia para a apresentacao e transforma o material em um briefing slide a slide.

Fontes consideradas:

- `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md`
- `reports/consolidados/roteiro-final-apresentacao-trabalho-2.md`
- `reports/consolidados/plano-detalhado-slides-trabalho-2.md`
- `reports/consolidados/notebooklm-trabalho-2/03_qa_professorial.md`
- `reports/consolidados/slides-trabalho-2/index_v3.html`

Tese narrativa final:

> O trabalho evoluiu de uma trilha SEER metodologicamente corrigida para uma trilha METABRIC canonica. A melhoria central nao foi apenas trocar algoritmo: foi remover vazamento, separar treino/validacao/teste, enriquecer o dataset e assumir explicitamente o trade-off entre falsos negativos e falsos positivos.

## Regras editoriais

- O slide deve defender uma afirmacao, nao listar o relatorio.
- O texto visivel deve ser curto; a explicacao vai para a fala.
- Toda mencao a alto recall deve mostrar tambem falsos positivos.
- Nao vender o ensemble como melhor modelo universal; defender como ponto operacional.
- Nao sugerir uso clinico real sem validacao externa.
- Nao chamar o neuro-fuzzy de ANFIS.
- Usar imagens reais do projeto quando elas sustentarem a mensagem; quando nao sustentarem, usar visual autoral simples.

## Mapa de imagens recomendadas

| Codigo | Caminho | Uso preferencial |
|---|---|---|
| G1 | `projeto_2_neuro_fuzzy/reports/figures/target_distribution.png` | Apoio para classe alvo no SEER |
| G2 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/target_distribution.png` | Apoio para classe alvo no METABRIC |
| G3 | `projeto_2_neuro_fuzzy/reports/figures/numeric_correlation_heatmap.png` | Backup de EDA SEER |
| G4 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/numeric_correlation_heatmap.png` | EDA principal METABRIC |
| G5 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/pam50_deceased_rate.png` | Melhor evidencia visual da riqueza molecular |
| G6 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/threshold_otimizacao.png` | Apoio para trade-off de threshold |
| G7 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/confusion_matrix_ensemble.png` | Evidencia visual do ensemble METABRIC |
| G8 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/curvas_pr.png` | Apoio para PR AUC e desbalanceamento |
| G9 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/calibration_curves.png` | Backup para calibracao |
| G10 | `projeto_2_neuro_fuzzy_metabric_clinico/reports/figures/feature_importance.png` | Backup para explicabilidade |

## Slide 1 - Capa

**Claim revisado:** Dados clinicos melhores mudaram mais o resultado do que complexidade isolada.

**Texto visivel sugerido:**

- Sistema de Inteligencia Computacional para risco de obito em cancer de mama
- SEER corrigido como baseline; METABRIC como trilha canonica
- Ensemble tabular com comparativo neuro-fuzzy

**Fala de apoio:** "A historia deste trabalho nao e apenas treinar varios modelos. A historia e corrigir a pergunta, proteger o teste, entender o limite do primeiro dataset e evoluir para uma base clinica mais rica."

**Imagem/visual:** visual autoral, nao grafico externo. Usar fluxo editorial `SEER corrigido -> METABRIC canonico`, com tres numeros em destaque: `F2 0.4832`, `F2 0.7787`, `F2 0.8770`.

**Evitar:** capa generica com titulo longo e sem tese.

## Slide 2 - Roteiro

**Claim revisado:** A defesa segue quatro blocos, mas concentra tempo em problema, dataset, resultados e trade-off.

**Texto visivel sugerido:**

1. Problema e objetivo corrigido
2. Dataset e metodo
3. Resultados e trade-off
4. Conclusao e limites

**Fala de apoio:** "A apresentacao foi encurtada para nao dispersar em detalhes de implementacao. O foco fica nas decisoes que a banca tende a cobrar."

**Imagem/visual:** linha de progresso horizontal com quatro etapas. Sem imagem externa.

**Evitar:** roteiro com muitos subitens ou slide administrativo demais.

## Slide 3 - Introducao

**Claim revisado:** Em saude, acuracia alta pode esconder o erro mais caro.

**Texto visivel sugerido:**

- Falso negativo: caso de risco classificado como nao risco
- Falso positivo: alerta falso com custo operacional
- Por isso: recall, F2, PR AUC e FN importam mais que acuracia isolada

**Fala de apoio:** "Se a classe positiva representa obito observado, errar para baixo tem peso diferente. A metrica precisa refletir essa assimetria."

**Imagem/visual:** balanca simples `FN` versus `FP`, com `FN` em vermelho contido. Opcionalmente usar miniatura de G2 para mostrar desbalanceamento.

**Evitar:** texto de aula sobre metricas; a explicacao tecnica vem depois.

## Slide 4 - Problema Proposto

**Claim revisado:** `Survival Months` foi removido porque respondia uma pergunta contaminada.

**Texto visivel sugerido:**

- Entrada permitida: variaveis clinicas, patologicas, moleculares e tratamento
- Saida: obito observado
- Bloqueado no modelo principal: `Survival Months`

**Fala de apoio:** "Usar tempo de sobrevida para prever status de obito cria um atalho: o modelo passa a usar informacao posterior ao acompanhamento. A correcao foi separar essa variavel da pergunta principal."

**Imagem/visual:** diagrama `features permitidas -> classificador -> obito observado`, com `Survival Months` em bloco vermelho separado como variavel bloqueada.

**Evitar:** dizer apenas "removemos uma coluna"; a razao metodologica precisa aparecer.

## Slide 5 - Dataset

**Claim revisado:** METABRIC nao vence por ter mais linhas; vence por trazer sinais clinicos mais informativos.

**Texto visivel sugerido:**

- SEER: 4.023 registros analiticos, baseline corrigido, menor profundidade clinica
- METABRIC: 1.876 registros analiticos, tratamento, ER/PR/HER2, PAM50, NPI e mutacoes
- Leitura: menos volume, mais qualidade de sinal

**Fala de apoio:** "A troca de dataset nao foi cherry-picking escondido. O SEER continua como baseline corrigido. O METABRIC entra porque permite discutir risco com variaveis clinicas e moleculares mais plausiveis."

**Imagem/visual:** composicao principal `volume x profundidade clinica`. Usar G5 como apoio se houver espaco, porque PAM50 ajuda a mostrar que METABRIC tem informacao molecular real.

**Evitar:** tabela grande com colunas demais; o ponto central e qualidade de sinal.

## Slide 6 - Arquitetura Geral

**Claim revisado:** O sistema foi reorganizado para rastrear dado, validacao e decisao final no mesmo fluxo.

**Texto visivel sugerido:**

- Dados brutos
- Contrato de dados e EDA
- Engenharia de features
- Modelos individuais
- Ensemble e neuro-fuzzy
- Validacao, teste e relatorio

**Fala de apoio:** "A arquitetura serve para garantir rastreabilidade: cada numero final precisa voltar para uma decisao de dado, feature, modelo e protocolo."

**Imagem/visual:** diagrama autoral de pipeline. Nao usar grafico de resultado aqui.

**Evitar:** misturar arquitetura com resultados; este slide e mapa do sistema.

## Slide 7 - Pre-processamento e EDA

**Claim revisado:** EDA deixou de ser exploracao solta e virou contrato do experimento.

**Texto visivel sugerido:**

- Sanitizacao de nomes, tipos e alvo
- Dicionario e metadados
- Relacoes numericas e categoricas antes da modelagem
- Politica de vazamento

**Fala de apoio:** "A EDA foi usada para definir o que entrava no modelo, como as variaveis eram interpretadas e quais colunas poderiam contaminar a pergunta."

**Imagem/visual:** usar G4 como figura principal, mas em tamanho controlado. Alternativa melhor para apresentacao: recorte ou miniatura de G4 + lista curta do contrato de dados.

**Evitar:** heatmap grande demais que ninguem consegue ler; ele deve funcionar como evidencia de processo, nao como figura para decodificar detalhe.

## Slide 8 - Metodologia Experimental

**Claim revisado:** SEER e METABRIC passaram pelas mesmas fases essenciais.

**Texto visivel sugerido:**

- Dicionario, EDA e metadados
- Politica de vazamento
- Treino / validacao / teste
- Explicabilidade, calibracao e estabilidade
- Mesmas metricas principais

**Fala de apoio:** "A comparacao nao e perfeita porque os datasets sao diferentes, mas a disciplina metodologica foi repetida nas duas trilhas."

**Imagem/visual:** matriz de completude SEER x METABRIC com checks. Sem grafico externo.

**Evitar:** parecer que SEER e METABRIC sao benchmark controlado identico.

## Slide 9 - Resultados Individuais

**Claim revisado:** METABRIC melhora antes mesmo do ensemble.

**Texto visivel sugerido:**

- SEER Logistic Regression: F2 `0.4832`, recall `0.6098`, PR AUC `0.3525`, `48 FN`
- METABRIC GradientBoosting: F2 `0.7787`, recall `0.7953`, PR AUC `0.7600`, `44 FN`

**Fala de apoio:** "Esse slide e central porque mostra que o salto nao foi apenas threshold agressivo. O melhor modelo individual no METABRIC ja parte de uma base muito superior."

**Imagem/visual:** comparacao lado a lado com F2 como numero dominante. Opcional: mini barra de PR AUC abaixo de cada modelo.

**Evitar:** tabela completa com precision, accuracy e muitas linhas; isso dilui o argumento.

## Slide 10 - Sistema Hibrido / Ensemble

**Claim revisado:** O ensemble reduziu falsos negativos, mas comprou falsos positivos.

**Texto visivel sugerido:**

- SEER ensemble, threshold `0.22`: recall `0.7642`, F2 `0.5188`, `29 FN`, `320 FP`
- METABRIC ensemble, threshold `0.16`: recall `0.9953`, F2 `0.8770`, `1 FN`, `146 FP`
- Pesos e threshold escolhidos na validacao

**Fala de apoio:** "O ensemble e defendido como ponto operacional de alta sensibilidade. Ele nao deve ser apresentado como melhor modelo universal, porque o custo em falsos positivos continua relevante."

**Imagem/visual:** dois blocos `FN vs FP`, com `1 FN` grande no METABRIC e `146 FP` na mesma hierarquia visual. Usar G7 como backup ou slide extra, nao como figura principal se a matriz ficar pequena demais.

**Evitar:** mostrar so `1 FN` sem o `146 FP`.

## Slide 11 - Comparacao Geral

**Claim revisado:** Dados melhores elevaram o teto; threshold moveu o ponto operacional.

**Texto visivel sugerido:**

- SEER individual: F2 `0.4832`
- SEER ensemble: F2 `0.5188`
- METABRIC individual: F2 `0.7787`
- METABRIC ensemble: F2 `0.8770`

**Fala de apoio:** "Existem dois efeitos separados: o dataset melhora a discriminacao, e o ensemble com threshold ajustado desloca a operacao para maior sensibilidade."

**Imagem/visual:** barras horizontais de F2 normalizadas. Opcional: pequena anotacao visual mostrando `dataset` como salto maior e `threshold` como ajuste operacional.

**Evitar:** grafico com muitas metricas simultaneas; a mensagem e progressao de F2.

## Slide 12 - Trade-off

**Claim revisado:** O melhor resultado e um ponto operacional, nao uma verdade clinica pronta.

**Texto visivel sugerido:**

- METABRIC ensemble: `1 FN` e `146 FP`
- Alta sensibilidade exige custo operacional
- Uso clinico exigiria validacao externa e analise de custo

**Fala de apoio:** "Esse e o slide de maturidade tecnica. O resultado e bom para o objetivo academico, mas ainda nao e sistema clinico pronto."

**Imagem/visual:** matriz ou balanca `sensibilidade alta` x `custo operacional`. G6 pode entrar como apoio se mostrar claramente a relacao threshold/erro; caso contrario, usar grafico autoral simples.

**Evitar:** tom celebratorio; este slide precisa parecer critico.

## Slide 13 - Conclusoes

**Claim revisado:** O ganho principal foi metodologico e informacional.

**Texto visivel sugerido:**

1. Remover vazamento tornou o experimento defensavel.
2. METABRIC trouxe sinais clinicos mais ricos.
3. Ensemble ajudou como ponto de alta sensibilidade.
4. Neuro-fuzzy ensinou como comparativo, nao como campeao.

**Fala de apoio:** "A contribuicao e mostrar uma evolucao honesta: corrigir metodologia, melhorar dado, comparar modelos e assumir limites."

**Imagem/visual:** quatro aprendizados numerados. Sem imagem externa.

**Evitar:** repetir resultados numericos; eles ja foram defendidos.

## Slide 14 - Limitacoes e Futuro

**Claim revisado:** A defesa e academica hoje; o proximo passo exige validacao externa e survival analysis.

**Texto visivel sugerido:**

- Datasets publicos
- Sem validacao clinica externa
- Classificacao binaria, nao survival analysis formal
- Proximos passos: validacao externa, custo clinico, explicabilidade local e survival analysis

**Fala de apoio:** "Essas limitacoes nao enfraquecem o trabalho; elas delimitam corretamente o que foi feito e o que ainda seria necessario para aproximar de uso real."

**Imagem/visual:** roadmap curto em tres blocos: `robustez`, `interpretabilidade`, `validacao clinica`. G9 e G10 podem virar backup, nao precisam estar no slide principal.

**Evitar:** lista longa de backlog tecnico.

## Slide 15 - Encerramento

**Claim revisado:** SEER ficou como baseline corrigido; METABRIC virou a trilha canonica porque sustentou melhor o objetivo.

**Texto visivel sugerido:**

- SEER: baseline corrigido
- METABRIC: trilha canonica
- Mensagem final: bons dados e boa validacao foram mais importantes que complexidade isolada

**Fala de apoio:** "O projeto termina com uma leitura simples: corrigir a metodologia deu credibilidade; trocar para um dataset mais rico aumentou o teto; o ensemble serviu para escolher um ponto operacional de alta sensibilidade."

**Imagem/visual:** frase final forte + fluxo `SEER -> METABRIC -> trade-off assumido`. Sem grafico externo.

**Evitar:** colocar perguntas no mesmo slide de encerramento principal; perguntas ficam em extra.

## Slide 16 - Extras / Perguntas Provaveis

**Claim revisado:** As perguntas da banca devem reforcar as escolhas, nao abrir uma nova apresentacao.

**Texto visivel sugerido:**

- Por que nao usar acuracia?
- Por que remover `Survival Months`?
- O teste foi usado para escolher threshold?
- O neuro-fuzzy e ANFIS?
- Por que METABRIC e melhor que SEER?
- Como justificar falsos positivos?

**Fala de apoio:** respostas curtas devem vir do `03_qa_professorial.md`.

**Imagem/visual:** duas colunas: perguntas metodologicas e perguntas de modelagem. Sem imagem externa.

**Evitar:** transformar o slide extra em texto de estudo completo.

## Ajustes recomendados para a proxima iteracao do HTML

1. Capa: manter a tese, mas reduzir densidade vertical se o PDF continuar quebrando em mais paginas que slides.
2. Slide 5: incluir G5 ou um recorte visual de PAM50 se houver espaco, pois ele justifica melhor a frase "sinais clinicos mais informativos".
3. Slide 7: reduzir o heatmap ou trocar por miniatura anotada; a leitura de detalhe nao e necessaria na apresentacao.
4. Slide 10: manter `FN` e `FP` no mesmo plano visual; esse e o principal ganho da v3.
5. Slide 12: se G6 for legivel, usar como backup para threshold; se nao, manter visual autoral.

## Prompt curto para gerar imagens/visuais autorais

Use estes prompts quando for gerar figuras complementares fora dos graficos ja existentes:

1. **Fluxo metodologico:** "Diagrama editorial limpo em fundo claro mostrando SEER corrigido como baseline, METABRIC como trilha canonica, e uma seta central com 'metodologia corrigida + dados melhores'. Estilo academico, clinico, sem icones decorativos, cores azul escuro, cinza e teal."
2. **Dataset volume vs profundidade:** "Visual comparativo em fundo claro: SEER com maior volume de registros, METABRIC com menor volume mas maior profundidade clinica. Usar barras horizontais simples e marcadores para ER, PR, HER2, PAM50, NPI e tratamento. Estilo cientifico e contido."
3. **Trade-off FN vs FP:** "Infografico simples em fundo claro mostrando METABRIC ensemble com 1 falso negativo e 146 falsos positivos. O foco deve ser trade-off operacional, nao celebracao. Usar vermelho contido para erros e teal para alta sensibilidade."
4. **Conclusao:** "Slide visual minimalista com fluxo SEER baseline corrigido -> METABRIC canonico -> validacao e trade-off. Aparencia academica, sem elementos decorativos, com muito espaco branco e tipografia forte."
