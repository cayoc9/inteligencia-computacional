# Trabalho 2: Evolucao Clinica METABRIC do Projeto 2 - Tasks

**Design**: `.specs/features/trabalho-2-breast-cancer-metabric/design.md`  
**Status**: Done

## Task Breakdown

### T1: Registrar feature canonica da v2 ✅

**What**: Criar spec, design e tasks da evolucao METABRIC como continuacao canonica da v1.  
**Where**: `.specs/features/trabalho-2-breast-cancer-metabric/`  
**Depends on**: None  
**Requirement**: BCM-01

### T2: Fechar paridade metodologica no pipeline METABRIC ✅

**What**: Garantir que a v2 tenha as mesmas fases essenciais do SEER corrigido.  
**Where**: `projeto_2_neuro_fuzzy_metabric_clinico/`  
**Depends on**: T1  
**Requirement**: BCM-02

### T3: Sincronizar estado global do repositorio ✅

**What**: Atualizar `ROADMAP.md`, `STATE.md` e `STATUS.md` para refletir a hierarquia v1 -> v2.  
**Where**: `.specs/project/`, `STATUS.md`  
**Depends on**: T2  
**Requirement**: BCM-01

### T4: Auditar boas praticas de ciencia de dados ✅

**What**: Gerar um review objetivo de completude metodologica para o Trabalho 2.  
**Where**: `.specs/project/TRABALHO_2_DATA_SCIENCE_BEST_PRACTICES_REVIEW.md`  
**Depends on**: T2  
**Requirement**: BCM-04

### T5: Registrar a execucao da v2 ✅

**What**: Consolidar o que foi implementado, validado e o resultado principal da evolucao METABRIC.  
**Where**: `.specs/features/trabalho-2-breast-cancer-metabric/relatorio_execucao.md`  
**Depends on**: T4  
**Requirement**: BCM-02, BCM-03, BCM-04
