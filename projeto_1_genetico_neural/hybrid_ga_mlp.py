import argparse
import json
import random
import time
from pathlib import Path
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore", category=ConvergenceWarning)


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset" / "heart_failure_clinical_records_dataset.csv"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sistema hibrido GA-MLP para o dataset Heart Failure."
    )
    parser.add_argument("--generations", type=int, default=15, help="Numero de geracoes do AG.")
    parser.add_argument("--pop-size", type=int, default=30, help="Tamanho da populacao.")
    parser.add_argument("--mutation-rate", type=float, default=0.005, help="Taxa de mutacao bit a bit.")
    parser.add_argument("--seed", type=int, default=42, help="Semente reprodutivel.")
    parser.add_argument("--fitness-max-iter", type=int, default=500, help="Max iter da MLP usada no fitness.")
    parser.add_argument("--final-max-iter", type=int, default=1000, help="Max iter da MLP final.")
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Executa uma validacao curta: 3 geracoes, populacao 8 e MLPs menores.",
    )
    parser.add_argument(
        "--output",
        default=str(TABLES_DIR / "ga_mlp_results.json"),
        help="Caminho do JSON de resultados.",
    )
    return parser.parse_args()


def metric_row(y_true, y_pred, y_proba):
    return {
        "accuracy": round(float(accuracy_score(y_true, y_pred)), 6),
        "precision": round(float(precision_score(y_true, y_pred, zero_division=0)), 6),
        "recall": round(float(recall_score(y_true, y_pred, zero_division=0)), 6),
        "f1": round(float(f1_score(y_true, y_pred, zero_division=0)), 6),
        "roc_auc": round(float(roc_auc_score(y_true, y_proba)), 6),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }


def main():
    args = parse_args()
    if args.quick:
        args.generations = 3
        args.pop_size = 8
        args.fitness_max_iter = min(args.fitness_max_iter, 120)
        args.final_max_iter = min(args.final_max_iter, 300)
    if args.pop_size < 4:
        raise ValueError("--pop-size deve ser pelo menos 4 para selecao por torneio.")
    if args.pop_size % 2 != 0:
        raise ValueError("--pop-size deve ser par para crossover em pares.")

    start_time = time.time()
    random.seed(args.seed)
    np.random.seed(args.seed)
    REPORTS_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    print("="*65)
    print("SISTEMA HÍBRIDO: ALGORITMO GENÉTICO + REDE NEURAL (GA-MLP)")
    print("Otimização Dupla: Feature Selection + Topologia (Neurônios)")
    print("="*65)
    print(
        f"[CONFIG] seed={args.seed} | pop_size={args.pop_size} | "
        f"generations={args.generations} | mutation_rate={args.mutation_rate}",
        flush=True,
    )

    df = pd.read_csv(DATASET_PATH)
    feature_names = df.drop(columns=['DEATH_EVENT']).columns.tolist()
    X = df.drop(columns=['DEATH_EVENT']).values
    y = df['DEATH_EVENT'].values

    # Divisão: Treino (64%), Validação (16%), Teste (20%)
    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2, random_state=42, stratify=y_train_full)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    NUM_FEATURES = len(feature_names)
    TOPOLOGY_BITS = 5
    CHROMOSOME_SIZE = NUM_FEATURES + TOPOLOGY_BITS

    # Parametros do AG. A taxa padrao de mutacao segue a faixa discutida na aula.
    pop_size = args.pop_size
    generations = args.generations
    mutation_rate = args.mutation_rate

    def decode_neurons(chromosome):
        """Converte os últimos 5 bits do cromossomo no número de neurônios ocultos (5 a 160)"""
        topo_bits = chromosome[NUM_FEATURES:]
        decimal_val = int("".join(str(b) for b in topo_bits), 2)
        return (decimal_val + 1) * 5

    def calculate_fitness(chromosome):
        """
        Bits 0-11: Feature Selection.
        Bits 12-16: Topologia da Rede Neural.
        """
        features_bits = chromosome[:NUM_FEATURES]
        selected_indices = [i for i, bit in enumerate(features_bits) if bit == 1]
        
        if len(selected_indices) == 0:
            return 0.0 
        
        neurons = decode_neurons(chromosome)
        
        mlp = MLPClassifier(
            hidden_layer_sizes=(neurons,),
            activation='relu',
            alpha=0.01,
            max_iter=args.fitness_max_iter,
            random_state=args.seed,
        )
        mlp.fit(X_train_scaled[:, selected_indices], y_train)
        preds = mlp.predict(X_val_scaled[:, selected_indices])
        
        return f1_score(y_val, preds)

    # Inicialização da População
    print(f"\n[AG] Inicializando população de {pop_size} indivíduos...", flush=True)
    population = []
    for _ in range(pop_size):
        ind = [random.choice([0, 1]) for _ in range(CHROMOSOME_SIZE)]
        if sum(ind[:NUM_FEATURES]) == 0:
            ind[random.randint(0, NUM_FEATURES-1)] = 1
        population.append(ind)

    best_fitness_history = []
    best_overall_individual = None
    best_overall_fitness = -1

    print("[AG] Iniciando evolução...", flush=True)
    generation_history = []
    for generation in range(generations):
        fitness_scores = [calculate_fitness(ind) for ind in population]
        
        gen_best_fitness = max(fitness_scores)
        gen_best_idx = fitness_scores.index(gen_best_fitness)
        best_fitness_history.append(gen_best_fitness)
        
        if gen_best_fitness > best_overall_fitness:
            best_overall_fitness = gen_best_fitness
            best_overall_individual = population[gen_best_idx].copy()
            
        gen_row = {
            "generation": generation + 1,
            "best_f1_validation": round(float(gen_best_fitness), 6),
            "mean_f1_validation": round(float(np.mean(fitness_scores)), 6),
            "best_neurons": int(decode_neurons(population[gen_best_idx])),
        }
        generation_history.append(gen_row)
        print(
            f"Geração {generation + 1:02d} | "
            f"F1 melhor: {gen_row['best_f1_validation']:.4f} | "
            f"F1 médio: {gen_row['mean_f1_validation']:.4f} | "
            f"Neurônios: {gen_row['best_neurons']}",
            flush=True,
        )

        # Torneio
        selected_parents = []
        for _ in range(pop_size):
            competitors = random.sample(list(zip(population, fitness_scores)), 3)
            winner = max(competitors, key=lambda item: item[1])[0]
            selected_parents.append(winner)

        # Crossover
        next_generation = []
        for i in range(0, pop_size, 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[(i + 1) % pop_size]
            crossover_point = random.randint(1, CHROMOSOME_SIZE - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            next_generation.extend([child1, child2])

        # Mutação
        for i in range(pop_size):
            for j in range(CHROMOSOME_SIZE):
                if random.random() < mutation_rate:
                    next_generation[i][j] = 1 if next_generation[i][j] == 0 else 0
            if sum(next_generation[i][:NUM_FEATURES]) == 0:
                next_generation[i][random.randint(0, NUM_FEATURES-1)] = 1
                
        # Elitismo
        next_generation[0] = best_overall_individual.copy()
        population = next_generation

    # Resultados Finais
    print("\n" + "="*60)
    print(" EVOLUÇÃO CONCLUÍDA")
    print("="*60)
    
    best_features_bits = best_overall_individual[:NUM_FEATURES]
    selected_feat_idx = [i for i, bit in enumerate(best_features_bits) if bit == 1]
    selected_feat_names = [feature_names[i] for i in selected_feat_idx]
    optimal_neurons = decode_neurons(best_overall_individual)
    
    print(f"Topologia Otimizada (Neurônios Ocultos): {optimal_neurons}")
    print(f"Número de features selecionadas: {len(selected_feat_names)}")
    print("Features ótimas escolhidas pelo AG:")
    for f in selected_feat_names:
        print(f" - {f}")

    print("\n[AVALIAÇÃO FINAL] Treinando MLP otimizada e testando no conjunto TESTE...")
    
    X_train_final = np.vstack((X_train_scaled, X_val_scaled))
    y_train_final = np.concatenate((y_train, y_val))
    
    final_mlp = MLPClassifier(
        hidden_layer_sizes=(optimal_neurons,),
        activation='relu',
        alpha=0.01,
        max_iter=args.final_max_iter,
        random_state=args.seed,
    )
    final_mlp.fit(X_train_final[:, selected_feat_idx], y_train_final)
    
    preds_final = final_mlp.predict(X_test_scaled[:, selected_feat_idx])
    probs_final = final_mlp.predict_proba(X_test_scaled[:, selected_feat_idx])[:, 1]
    metrics = metric_row(y_test, preds_final, probs_final)
    
    print("\n--- Resultados: HÍBRIDO (AG + MLP) ---")
    print(f"Acurácia:  {metrics['accuracy']:.4f}")
    print(f"Precisão:  {metrics['precision']:.4f}")
    print(f"Recall:    {metrics['recall']:.4f}")
    print(f"F1-Score:  {metrics['f1']:.4f}")
    print(f"ROC AUC:   {metrics['roc_auc']:.4f}")
    print("Matriz de Confusão:")
    print(np.array(metrics["confusion_matrix"]))

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, generations + 1), best_fitness_history, marker='o', color='b')
    plt.title('Evolução do Algoritmo Genético (F1-Score)')
    plt.xlabel('Geração')
    plt.ylabel('F1-Score (Validação)')
    plt.grid(True)
    plot_path = FIGURES_DIR / "evolucao_genetica.png"
    legacy_plot_path = BASE_DIR / "evolucao_genetica.png"
    plt.savefig(plot_path)
    plt.savefig(legacy_plot_path)

    elapsed_seconds = round(time.time() - start_time, 3)
    result = {
        "experiment": "projeto_1_genetico_neural_ga_mlp",
        "mode": "quick" if args.quick else "full",
        "dataset": str(DATASET_PATH.relative_to(BASE_DIR)),
        "target": "DEATH_EVENT",
        "seed": args.seed,
        "parameters": {
            "population_size": pop_size,
            "generations": generations,
            "mutation_rate": mutation_rate,
            "fitness_max_iter": args.fitness_max_iter,
            "final_max_iter": args.final_max_iter,
            "topology_bits": TOPOLOGY_BITS,
        },
        "chromosome": {
            "size": CHROMOSOME_SIZE,
            "num_feature_bits": NUM_FEATURES,
            "num_topology_bits": TOPOLOGY_BITS,
            "best_individual": best_overall_individual,
        },
        "selection": {
            "selected_feature_count": len(selected_feat_names),
            "selected_features": selected_feat_names,
            "optimal_hidden_neurons": int(optimal_neurons),
            "best_validation_f1": round(float(best_overall_fitness), 6),
        },
        "test_metrics": metrics,
        "generation_history": generation_history,
        "artifacts": {
            "figure": str(plot_path.relative_to(BASE_DIR)),
            "legacy_figure": str(legacy_plot_path.relative_to(BASE_DIR)),
        },
        "elapsed_seconds": elapsed_seconds,
    }

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = BASE_DIR / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)

    print(f"\n[INFO] Resultados salvos em: {output_path}")
    print(f"[INFO] Figura salva em: {plot_path}")
    print(f"[INFO] Tempo total: {elapsed_seconds:.2f}s")

if __name__ == "__main__":
    main()
