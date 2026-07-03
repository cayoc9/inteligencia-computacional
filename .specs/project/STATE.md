# Project State

## 🛑 Decisions Made
1. **Descarte de Bases Sintéticas**: Descartou-se a base de AVC devido a alertas de dados sintéticos sem comprovação clínica. Optou-se por Heart Failure (BMC) e Breast Cancer (SEER).
2. **Métrica de Avaliação**: Definido o F1-Score (em vez da Acurácia) devido ao forte desbalanceamento de classes em cenários de saúde.
3. **Restrição de Bibliotecas**: O Algoritmo Genético foi codificado 100% do zero em NumPy/Python puro, evitando dependências externas como `DEAP` ou `PyGAD`, garantindo transparência total e controle sobre o cromossomo para a avaliação acadêmica.
4. **Alinhamento com Ementa**:
   - Taxa de mutação ajustada para `0.005` a partir do feedback extraído da disciplina (NotebookLM).
   - Otimização do AG expandida para selecionar Topologia (além de Features).
   - Evitou-se SMOTE e Cross-Validation (K-Fold) pois o material não os cobra formalmente (e evitam-se perguntas desnecessárias da banca).
5. **Neuro-Fuzzy Cooperativo**: Aceito o modelo onde Lógica Fuzzy alimenta uma MLP. A queda de desempenho (25% F1-Score) será justificada no relatório como "Perda informacional por discretização sem calibragem por especialista".

## 🚧 Blockers / Limitations
- **Overfitting Evolutivo (Projeto 1)**: O dataset muito pequeno (299 linhas) causou a memorização dos dados de validação pelo AG, fazendo o F1 cair no teste cego. (Mitigado pela seção "Trabalhos Futuros" no relatório, propondo K-fold no fitness function).

## 💡 Lessons Learned
- Sistemas híbridos não são garantias de ganho de performance. O Projeto 2 provou empiricamente que injetar regras heurísticas "amadoras" (Funções Triangulares sem oncologista) pode prejudicar severamente uma Rede Neural pura.
