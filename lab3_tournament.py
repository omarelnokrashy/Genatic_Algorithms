import random

from numpy.random import rand, randint, uniform
import numpy as np
import matplotlib.pyplot as plt


# Define fitness function
def fitness_func(solution):
    x = solution[0]

    objective_max = (5*x-x**2)
    return objective_max


# Main Attributes
bounds = [[0, 31]]           # X
no_generation = 10           # No. of generation
pop_size = 12                 # No. of chromosomes
no_mating = pop_size//2      # No. of mating produced from selection
genes = 5                    # No. of genes (No. of bits)
crossover_rate = 0.7         # Crossover rate
mutation_rate = 0.1          # Mutation rate


# -----------------------------------------------------------
# Decoding chromosome from binary format to integer, depends on no. of variables, e.g. x and y
def decoding(chromosome):
    real_chromosome = []
    for i in range(len(bounds)):
        start, end = i * genes, (i * genes) + genes

        sub = chromosome[start:end]
        chars = ''.join([str(s) for s in sub])
        integer = int(chars, 2)

        real_val = (integer / (2**genes-1)) * (bounds[i][1] - bounds[i][0]) + bounds[i][0]
        real_chromosome.append(real_val)

    return real_chromosome


# Selection by Tournament Selection
def selection(pop, fitness, no_mating):
    next_generation = []                            # Parents

    indices = np.arange(0, len(pop))
    k = 3
    for _ in range(no_mating):
        random_choice = random.choices(indices, k=k)
        index = 0
        fittest = fitness[random_choice[0]]
        for idx in random_choice:
            if fitness[idx] >= fittest:
                fittest = fitness[idx]
                index = idx

        next_generation.append(pop[index])

    return next_generation


# Crossover using single point/ multi points (commented)
def crossover(pop, crossover_rate):
    offspring = []

    pop_len = len(pop)
    length = pop_len//2 + 1 if pop_len % 2 != 0 else pop_len//2

    for i in range(length):
        p1 = pop[i * 2 - 1].copy()
        p2 = pop[i * 2].copy()

        if rand() < crossover_rate:
            cp = randint(1, len(p1)-1)
            c1 = p1[:cp] + p2[cp:]
            c2 = p2[:cp] + p1[cp:]

            offspring.append(c1)
            offspring.append(c2)
        else:
            offspring.append(p1)
            offspring.append(p2)

    return offspring


# Mutation by random one time.
def mutation(pop, mutation_rate):
    offspring = []

    for i in range(int(len(pop))):
        p1 = pop[i].copy()

        if rand() < mutation_rate:
            cp = randint(0, len(p1))
            c1 = p1

            if c1[cp] == 1:
                c1[cp] = 0
            else:
                c1[cp] = 1

            offspring.append(c1)
        else:
            offspring.append(p1)

    return offspring


def run_ga():
    # Initial population
    population = [randint(0, 2, genes*len(bounds)).tolist() for _ in range(pop_size)]
    print(population)

    # Best fitness, solution each generation
    best_fitness = []
    best_solution = []

    # 1. Decode chromosome to int
    # 2. Calculate each chromosome fitness score
    # 3. natural selection
    # 4. Crossover
    # 5. mutation
    # 6. new population
    # repeat
    for gen in range(no_generation):
        # 1
        real_chromosome = [decoding(chromosome) for chromosome in population]
        # print(real_chromosome)
        # 2
        fitness = [fitness_func(rc) for rc in real_chromosome]
        #
        index = np.argmax(fitness)
        best_solution.append(real_chromosome[index])
        best_fitness.append(max(fitness))
        print(f"Generation {gen}, best solution = {real_chromosome[index]}, best fitness = {max(fitness)}")
        # 3
        population = selection(population, fitness, no_mating)
        # 4
        offspring = crossover(population, crossover_rate)
        # 5
        offspring = mutation(offspring, mutation_rate)
        # 6
        for s in offspring:
            population.append(s)

    fitness, solutions = zip(*sorted(zip(best_fitness, best_solution), reverse=True))

    fig = plt.figure()
    plt.plot(best_fitness)
    fig.suptitle('Evaluation')
    plt.xlabel('Generations')
    plt.ylabel('Fitness Value')
    print(f"max value = {fitness[0]}")
    print(f"Best solution = {solutions[0]}")
    plt.show()


run_ga()