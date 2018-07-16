import random
import copy

MAX_GENERATION = 100
MUTATION_RATE = 0.15
POPULATION_SIZE = 200


# Runs the whole procedure
def run():
    pass

def crossover(parent1, parent2): # Returns child
    pass

def mutate(individual): # Returns mutated individual
    if(random.random() > MUTATION_RATE):
        return get_copy(individual)
    
    transition_idx = random.randint(0, 1) # mutate healthy or sick transition?
    transition_len = len(individual[transition_idx]) # which entry should be changed?
    rule_idx = random.randint(0, transition_len)

    mutant = get_copy(individual) # Do not mutate inplace!
    mutant[transition_idx][rule_idx] += random.gauss(0, 1)

    mutant[transition_idx][rule_idx] = max(0.0, min(1.0, mutant[transition_idx][rule_idx])) # Do not exceed interval [0,1]
    
    return mutant

def select(population): # Select an individual
    pass

def initial(): # Returns the intial population size
    pass

def get_copy(individual):
    return copy.deepcopy(individual)

run()
