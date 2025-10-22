from numpy.random import rand, randint, uniform
import numpy as np
import matplotlib.pyplot as plt


# Define fitness function
def fitness_func(solution):
    x=solution[0]
    y=solution[1]

    objective_max=(3*(x**2 - y)**2 + (100+x)**2 + (y-x))
    return objective_max

# Main Attributes
bounds =[[0,31],[0,31]] # X, Y
no_generation=500
pop_size=10                # no. of chromosomes
genes=5                    # no. of genes (No. of bits) from 0 to 31
no_mating=pop_size//2      # no. of mating produced from selection
crossover_rate=0.7         # Crossover rate
mutation_rate=0.1          # Mutation rate
# -----------------------------------------------------------
# Decoding chromosome from binary format to integer, depends on no. of variables, e.g. x and y
def decoding(chromosome):
    real_chromosome=[]
    for i in range(len(bounds)):
        start,end=i*genes,