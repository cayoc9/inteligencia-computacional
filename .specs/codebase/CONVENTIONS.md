# Convenções Observadas

## Organização
- Scripts numerados por etapa do pipeline.
- Comentários em português explicando intenção acadêmica e técnica.
- Artefatos separados por diretório: `data/`, `reports/`, `models/`.
- Requisitos e decisões rastreados em `.specs/`.

## Código
- Caminhos relativos a partir da raiz do projeto.
- Uso de `random_state=42` para reprodutibilidade.
- Métricas impressas no console e modelos persistidos em disco.

## Convenção Recomendada
- Manter scripts como pipeline auditável e reexecutável.
- Usar um único notebook principal para narrativa de Data Science: `notebooks/trabalho_1_classificacao_saude_rf_vs_rn.ipynb`.
- Evitar fragmentar notebooks por etapa neste trabalho; a fragmentação aceita fica restrita aos trechos de relatório em `reports/fragmentos/`.
