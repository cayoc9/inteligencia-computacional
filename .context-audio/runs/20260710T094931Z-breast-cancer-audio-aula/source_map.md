# Source Map

## Pergunta

Gerar audios em portugues ensinando o assunto que o grupo vai apresentar no Trabalho 2: sistema de inteligencia computacional para classificacao de obito observado em cancer de mama, com SEER corrigido, METABRIC canonico, ensemble ponderado e comparativo neuro-fuzzy.

## Fontes Selecionadas

| Fonte | Por que entra | O que prova | O que nao prova | Risco |
|---|---|---|---|---|
| `STATUS.md` | Visao executiva do projeto e estado final | SEER 20/20, METABRIC 7/7, tese de defesa e artefatos principais | Nao substitui relatorio tecnico | Baixo, atualizado pos-finalizacao |
| `.specs/project/TRABALHO_2_AVALIACAO_CHECKLIST.md` | Critérios da segunda avaliacao | Aderencia ao pedido da disciplina, status de relatorio/apresentacao e riscos de banca | Nao prova qualidade clinica externa | Baixo |
| `.specs/project/STATE.md` | Decisoes e limitacoes persistentes | Decisoes sobre vazamento, METABRIC canonico, validacao separada e limites | Nao prova runtime atual sozinho | Baixo |
| `reports/consolidados/relatorio-final-trabalho-2-breast-cancer.md` | Fonte tecnica principal | Metodologia, datasets, modelos, metricas e resultados | Nao e roteiro oral completo | Baixo |
| `reports/consolidados/finalizacao-defesa-2026-07-09/roteiro-detalhado-e-curadoria-final.md` | Roteiro final de defesa | Fala slide a slide, perguntas de banca e frases obrigatorias | Nao e fonte de metricas primaria | Baixo |
| `reports/consolidados/notebooklm-trabalho-2/09c_prompt_audio_unico_15min_padrao.md` | Prompt anterior de audio | Regras de duracao, tom e topicos obrigatorios | Nao inclui a curadoria final do PPTX curado | Medio, complementado pelo roteiro final |
| `docs/template/Breast_Cancer/main.tex` | Artigo revisado | Linguagem defensiva: observed mortality, internal validation, no clinical deployment readiness | Nao substitui leitura completa do PDF | Baixo |

## Fontes Excluidas

- Binarios (`.pptx`, `.pdf`, `.png`) ficam referenciados, mas nao copiados como conteudo textual principal.
- Logs de compilacao e arquivos auxiliares LaTeX foram excluidos porque nao ensinam o assunto.
- `.arquivos/` foi excluido por ser espelho antigo nao relacionado a esta rodada.
- Nenhuma credencial, `.env`, token ou dado sensivel foi incluido.
