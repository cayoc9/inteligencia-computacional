import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import random
import os
import warnings

# Suprimir avisos de convergência da MLP
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

def main():
    print("="*65)
    print("SISTEMA HÍBRIDO: ALGORITMO GENÉTICO + REDE NEURAL (GA-MLP)")
    print("Otimização Dupla: Feature Selection + Topologia (Neurônios)")
    print("="*65)

    df = pd.read_csv('dataset/heart_failure_clinical_records_dataset.csv')
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

    # ==========================================
    # PARÂMETROS DO ALGORITMO GENÉTICO
    # ==========================================
    POP_SIZE = 30        
    GENERATIONS = 15     
    MUTATION_RATE = 0.005  # Aderente ao material da aula (~0.001 a 0.01)

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
        
        mlp = MLPClassifier(hidden_layer_sizes=(neurons,), activation='relu', alpha=0.01, max_iter=500, random_state=42)
        mlp.fit(X_train_scaled[:, selected_indices], y_train)
        preds = mlp.predict(X_val_scaled[:, selected_indices])
        
        return f1_score(y_val, preds)

    # Inicialização da População
    print(f"\n[AG] Inicializando população de {POP_SIZE} indivíduos...")
    population = []
    for _ in range(POP_SIZE):
        ind = [random.choice([0, 1]) for _ in range(CHROMOSOME_SIZE)]
        if sum(ind[:NUM_FEATURES]) == 0:
            ind[random.randint(0, NUM_FEATURES-1)] = 1
        population.append(ind)

    best_fitness_history = []
    best_overall_individual = None
    best_overall_fitness = -1

    print("[AG] Iniciando evolução...")
    for generation in range(GENERATIONS):
        fitness_scores = [calculate_fitness(ind) for ind in population]
        
        gen_best_fitness = max(fitness_scores)
        gen_best_idx = fitness_scores.index(gen_best_fitness)
        best_fitness_history.append(gen_best_fitness)
        
        if gen_best_fitness > best_overall_fitness:
            best_overall_fitness = gen_best_fitness
            best_overall_individual = population[gen_best_idx].copy()
            
        print(f"Geração {generation + 1:02d} | F1: {gen_best_fitness:.4f} | Neurônios: {decode_neurons(population[gen_best_idx])}")

        # Torneio
        selected_parents = []
        for _ in range(POP_SIZE):
            competitors = random.sample(list(zip(population, fitness_scores)), 3)
            winner = max(competitors, key=lambda item: item[1])[0]
            selected_parents.append(winner)

        # Crossover
        next_generation = []
        for i in range(0, POP_SIZE, 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[(i + 1) % POP_SIZE]
            crossover_point = random.randint(1, CHROMOSOME_SIZE - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            next_generation.extend([child1, child2])

        # Mutação
        for i in range(POP_SIZE):
            for j in range(CHROMOSOME_SIZE):
                if random.random() < MUTATION_RATE:
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
    
    final_mlp = MLPClassifier(hidden_layer_sizes=(optimal_neurons,), activation='relu', alpha=0.01, max_iter=1000, random_state=42)
    final_mlp.fit(X_train_final[:, selected_feat_idx], y_train_final)
    
    preds_final = final_mlp.predict(X_test_scaled[:, selected_feat_idx])
    
    print("\n--- Resultados: HÍBRIDO (AG + MLP) ---")
    print(f"Acurácia:  {accuracy_score(y_test, preds_final):.4f}")
    print(f"F1-Score:  {f1_score(y_test, preds_final):.4f}")

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, GENERATIONS + 1), best_fitness_history, marker='o', color='b')
    plt.title('Evolução do Algoritmo Genético (F1-Score)')
    plt.xlabel('Geração')
    plt.ylabel('F1-Score (Validação)')
    plt.grid(True)
    plt.savefig('evolucao_genetica_v2.png')

if __name__ == "__main__":
    main()
