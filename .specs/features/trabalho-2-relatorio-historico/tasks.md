# Trabalho 2: Relatorio Historico Canonico - Tasks

**Design**: `.specs/features/trabalho-2-relatorio-historico/design.md`  
**Status**: Executed

## Execution Plan

### Phase 1: Base Factual

```
T1 -> T1A -> T2 -> T2A
```

### Phase 2: Comparacao e Tese

```
T2A -> T3 -> T3A -> T4 -> T4A
```

### Phase 3: Desdobramento Multi-Canal

```
T4A -> T5 -> T5A
```

## Task Breakdown

### T1: Consolidar inventario factual ✅

**What**: Mapear os artefatos canonicos e os numeros validos do Projeto 2.  
**Where**: `.specs/features/trabalho-2-relatorio-historico/`, docs e reports dos dois projetos  
**Depends on**: None  
**Requirement**: RHC-01, RHC-04

**Done when**:
- [x] Existe lista unica de arquivos canonicos.
- [x] Existe `SOURCE_MAP.md` com hierarquia de fontes e papel das sessoes de agentes.
- [x] Os resultados principais de SEER e METABRIC estao reconciliados com os CSVs reais.
- [x] Fica separado o que e baseline, evolucao e analise de sensibilidade.
- [x] As sessoes `019f2525-5a79-7723-b4eb-8759cc32ce9f`, `019f255f-88a8-7a81-b002-957841c02760` e `cd405d9c-1645-4090-8ada-150e8f2aea59` estao mapeadas como fontes complementares de processo.

**Tests**: docs consistency
**Gate**: `rg -n "019f2525-5a79-7723-b4eb-8759cc32ce9f|019f255f-88a8-7a81-b002-957841c02760|cd405d9c-1645-4090-8ada-150e8f2aea59|0.5188|0.8770|survival_months|threshold 0.22|threshold 0.16" .specs projeto_2_neuro_fuzzy projeto_2_neuro_fuzzy_metabric_clinico /home/cayo/.codex/history.jsonl /home/cayo/.gemini/antigravity-cli/history.jsonl`

### T1A: Loop professorial de evidencia ✅

**What**: Revisar T1 com perguntas de professora focadas em fonte, consistencia e rastreabilidade.  
**Where**: `.specs/features/trabalho-2-relatorio-historico/qa_professor_checkpoints.md`  
**Depends on**: T1  
**Requirement**: RHC-02

**Done when**:
- [x] Toda metrica relevante aponta para artefato executado.
- [x] Toda afirmacao de processo baseada em agente aponta para sessao ou artefato do agente.
- [x] Divergencias documentais foram corrigidas ou marcadas.
- [x] Perguntas "de onde veio esse numero?" e "isso foi teste ou validacao?" estao respondidas.
- [x] Pergunta "isso veio do repositorio ou de uma sessao de agente?" esta respondida para os pontos relevantes.

**Tests**: docs review
**Gate**: arquivo `qa_professor_checkpoints.md` contem bloco `P1 - Evidencia`

### T2: Construir linha do tempo e decisoes ✅

**What**: Escrever a cronologia do Projeto 2 do SEER inicial ate a v2 METABRIC.  
**Where**: `relatorio_historico.md`  
**Depends on**: T1A  
**Requirement**: RHC-01, RHC-04

**Done when**:
- [x] A cronologia inclui erros, correcoes, trocas de dataset e entregas finais.
- [x] Cada virada do projeto tem justificativa.
- [x] Nao ha mistura entre fato implementado e hipotese futura.
- [x] A cronologia registra quando a direcao veio dos agentes e quando virou artefato canonico no repositorio.

**Tests**: docs review
**Gate**: `relatorio_historico.md` contem secoes de linha do tempo

### T2A: Loop professorial de coerencia metodologica ✅

**What**: Revisar a cronologia com foco em pergunta cientifica, vazamento e mudanca de escopo.  
**Where**: `qa_professor_checkpoints.md`  
**Depends on**: T2  
**Requirement**: RHC-02

**Done when**:
- [x] Esta respondido qual era o erro metodologico original.
- [x] Esta respondido por que o METABRIC entrou.
- [x] Esta respondido o que mudou e o que nao mudou na pergunta do projeto.

**Tests**: docs review
**Gate**: arquivo `qa_professor_checkpoints.md` contem bloco `P2 - Coerencia metodologica`

### T3: Consolidar comparacao SEER vs METABRIC ✅

**What**: Criar comparacao justa entre baseline corrigido e evolucao canonica.  
**Where**: `relatorio_historico.md`  
**Depends on**: T2A  
**Requirement**: RHC-01, RHC-03

**Done when**:
- [x] A comparacao cobre dados, features, qualidade, metodologia e resultados.
- [x] O texto separa ganho por dataset de ganho por pipeline.
- [x] O texto nao vende o METABRIC como substituicao silenciosa.

**Tests**: docs review
**Gate**: `relatorio_historico.md` contem tabela comparativa SEER vs METABRIC

### T3A: Loop professorial de justica comparativa ✅

**What**: Testar se a comparacao entre datasets esta intelectualmente honesta.  
**Where**: `qa_professor_checkpoints.md`  
**Depends on**: T3  
**Requirement**: RHC-02

**Done when**:
- [x] Esta respondido se ha risco de cherry-picking.
- [x] Esta respondido se os targets sao comparaveis o bastante para a narrativa.
- [x] Esta respondido por que a troca de base melhora o valor pedagogico e clinico.

**Tests**: docs review
**Gate**: arquivo `qa_professor_checkpoints.md` contem bloco `P3 - Justica comparativa`

### T4: Escrever narrativa de defesa ✅

**What**: Montar a tese oral e escrita do Projeto 2, incluindo trade-offs e limitacoes.  
**Where**: `relatorio_historico.md`, `presentation_outline.md`  
**Depends on**: T3A  
**Requirement**: RHC-02, RHC-03

**Done when**:
- [x] Existe narrativa principal de 5 a 10 minutos.
- [x] Trade-offs de recall, F2, FN e FP estao explicados.
- [x] Limitacoes e trabalhos futuros ficam claros sem enfraquecer o que foi entregue.

**Tests**: docs review
**Gate**: `presentation_outline.md` contem narrativa resumida por blocos

### T4A: Loop professorial de banca ✅

**What**: Simular perguntas provaveis de banca e registrar respostas curtas e longas.  
**Where**: `qa_professor_checkpoints.md`  
**Depends on**: T4  
**Requirement**: RHC-02

**Done when**:
- [x] Ha respostas para metrica principal, vazamento, neuro-fuzzy, threshold e trade-off.
- [x] Cada resposta tem versao curta oral e versao detalhada tecnica.

**Tests**: docs review
**Gate**: arquivo `qa_professor_checkpoints.md` contem bloco `P4 - Perguntas de banca`

### T5: Desdobrar para artigo e audio ✅

**What**: Derivar outlines para artigo LaTeX e audio de repasse ao grupo.  
**Where**: `latex_article_outline.md`, `audio_briefing_script.md`  
**Depends on**: T4A  
**Requirement**: RHC-03

**Done when**:
- [x] O outline do artigo separa introducao, metodologia, resultados, discussao e limitacoes.
- [x] O roteiro do audio permite onboarding rapido de quem nao desenvolveu.
- [x] Ha mapeamento entre secoes do relatorio e os tres canais finais.

**Tests**: docs review
**Gate**: ambos os arquivos existem e referenciam `relatorio_historico.md`

### T5A: Loop professorial de prontidao final ✅

**What**: Verificar se a base final esta pronta para ser reutilizada sem distorcer o trabalho.  
**Where**: `qa_professor_checkpoints.md`  
**Depends on**: T5  
**Requirement**: RHC-02, RHC-03

**Done when**:
- [x] Ha check final de coerencia entre relatorio, apresentacao, artigo e audio.
- [x] Estao listados riscos residuais e o que nao deve ser exagerado na defesa.
- [x] A feature fica pronta para execucao documental completa.

**Tests**: docs review
**Gate**: arquivo `qa_professor_checkpoints.md` contem bloco `P5 - Prontidao final`

## Pos-T5A: Consolidacao final executada ✅

Depois do fechamento da trilha historica principal, a execucao foi estendida para materializar os entregaveis finais derivados.

### T6: Relatorio tecnico final consolidado ✅

**What**: Consolidar o relatorio tecnico final do Trabalho 2 em pasta de entregas finais.  
**Where**: `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md`  
**Depends on**: T5A  
**Requirement**: RHC-03

**Done when**:
- [x] Existe um relatorio tecnico final unico para o Projeto 2.
- [x] O texto diferencia SEER corrigido de METABRIC canonico.
- [x] O texto resume metodologia, resultados, trade-offs e limitacoes.

**Tests**: docs review  
**Gate**: arquivo consolidado existe e referencia ambas as trilhas

### T7: Pacote NotebookLM e prompts de audio ✅

**What**: Preparar pacote documental para NotebookLM e disparar a geracao dos audios numerados.  
**Where**: `reports/consolidados/notebooklm-trabalho-2/` e notebook `22e638a3-d0ca-447e-8a02-45b0d942865e`  
**Depends on**: T6  
**Requirement**: RHC-03, RHC-04

**Done when**:
- [x] As 7 fontes do pacote foram materializadas.
- [x] O notebook foi criado programaticamente via `notebooklm`.
- [x] As fontes ficaram com status `ready`.
- [x] Os 12 audios foram disparados.

**Tests**: `notebooklm source list --json`, `notebooklm artifact list --json`  
**Gate**: notebook contem 7 fontes e 12 artefatos de audio

### T8: Adaptacao do template do artigo ✅

**What**: Usar `docs/template/Sleep_Health/` como referencia para criar a base do artigo do Projeto 2.  
**Where**: `docs/template/Trabalho_2_Breast_Cancer/`  
**Depends on**: T6  
**Requirement**: RHC-03

**Done when**:
- [x] Existe uma nova pasta de template do artigo.
- [x] `main.tex` foi reescrito para o tema Breast Cancer.
- [x] A classe `IEEEtran.cls` foi copiada para a pasta derivada.
- [x] As pendencias remanescentes do artigo ficaram explicitas.

**Tests**: docs review  
**Gate**: pasta derivada existe com `main.tex`, `README.md` e `IEEEtran.cls`

## Gaps finais para encerramento

1. Revisar autoria final e emails no artigo.
2. Completar metadados bibliograficos finais e validar as referencias no Overleaf.
3. Revisar o PDF final no Overleaf, mantendo a compilacao por container como validacao local.
4. Converter o roteiro em slides finais da apresentacao.
5. Revisar a qualidade narrativa dos 12 audios NotebookLM ja concluidos e definir a ordem de escuta do grupo.

## Auditoria final de consistencia

- [x] Status dos audios NotebookLM conferido: 12 artefatos em `completed`.
- [x] Pendencia antiga sobre ensemble sem split de validacao corrigida como ponto historico.
- [x] Bloco de autores do artigo normalizado com os nomes reais da equipe.
- [x] Artigo recompilado por container apos ajuste editorial no `main.tex`.
- [x] Varredura final sem placeholders antigos, citacoes indefinidas ou referencias obsoletas a `in_progress`.

**Proximos passos liberados**: slides finais, revisao editorial no Overleaf, conferencia qualitativa dos audios e fechamento do pacote de defesa.
