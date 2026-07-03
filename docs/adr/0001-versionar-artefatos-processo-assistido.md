# ADR 0001: Versionar Artefatos Pequenos Do Processo Assistido

## Status

Aceito

## Contexto

O experimento foi conduzido com apoio de skills e agentes. Esses artefatos influenciaram a escolha do dataset, a estrategia de analise, a documentacao e a narrativa de apresentacao.

Em um projeto comum, diretorios como `.agents/` poderiam ser tratados como configuracao de ferramenta local. Neste projeto, parte desse conteudo funciona como evidencia de processo e ajuda a explicar como as decisoes foram produzidas.

## Decisao

Manter versionados os artefatos pequenos que documentam o processo assistido:

- `.agents/skills/data-science-expert-SKILL.md`
- `.agents/skills/kaggle/`
- `skills-lock.json`
- `data-storytelling/`
- `DATA-STORYTELLING-SKILLS.md`

Continuar ignorando artefatos locais, pesados ou derivados:

- `.venv/`
- `models/`
- `data/*.pkl`
- `.playwright-cli/`
- `.qwen/`
- `.claude/`
- PDFs externos

## Alternativas Consideradas

1. **Remover todos os artefatos de agentes/skills.**
   - Vantagem: repositorio mais limpo.
   - Desvantagem: perde parte da trilha metodologica usada para conduzir o experimento.

2. **Versionar tudo, incluindo logs e configuracoes locais.**
   - Vantagem: maxima captura de contexto bruto.
   - Desvantagem: aumenta ruido, risco de dados locais e baixa utilidade para reproducao.

3. **Versionar apenas manifesto reduzido.**
   - Vantagem: repositorio mais enxuto.
   - Desvantagem: exige curadoria adicional e pode perder detalhes uteis da skill.

## Consequencias

- O repositorio fica um pouco maior, mas ainda leve: `.agents/` e `data-storytelling/` somam menos de 1 MB.
- Futuros leitores conseguem entender melhor a trilha de decisao assistida por agentes.
- A politica de limpeza precisa diferenciar artefato de processo de lixo local.
- Se o projeto crescer, a decisao pode ser revisada para substituir diretorios vendorizados por manifestos com hash e instrucoes de instalacao.

## Verificacao

Foi feita busca por termos sensiveis como `token`, `secret`, `password`, `api_key`, `credential` e similares. Nao foram encontrados valores reais de credenciais nos artefatos mantidos; os scripts consultam variaveis de ambiente ou arquivos externos ao repositorio, como `~/.kaggle`.

