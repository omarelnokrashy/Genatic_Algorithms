import pygad


def fitness_func(ga_instance, solution, solution_idx):
    x = solution[0]
    y = solution[1]
    print(solution)
    Z = 3*(x**2 -y)**2 +(100+x)**2 + (y-x)
    return Z


last_fitness = 0


def on_generation(gai_instance):
    global last_fitness
    print(f"Generation = {gai_instance.generations_completed}")
    print(f"Fitness    = {gai_instance.best_solution(gai_instance.last_generation_fitness)[1]}")
    print(f"Change     = {gai_instance.best_solution(gai_instance.last_generation_fitness)[1] - last_fitness}")
    last_fitness = gai_instance.best_solution(gai_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=5,
                       sol_per_pop=10,
                       num_genes=2,
                       gene_space={"low": -4, "high": 4},
                       mutation_by_replacement=True,
                       fitness_func=fitness_func,
                       on_generation=on_generation)

ga_instance.run()

ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Solution: ", solution)
print(f"Fitness value of the best solution = {solution_fitness}")