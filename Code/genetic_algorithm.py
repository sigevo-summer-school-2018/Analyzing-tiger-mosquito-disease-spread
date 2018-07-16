import random
import copy
import numpy as np

import evaluation
import automaton

MAX_GENERATION = 100
MUTATION_RATE = 0.15
POPULATION_SIZE = 200
TOURNAMENT_SIZE = 3

INITIAL_LETTICE = np.zeros((100,100), dtype="int32")
MAX_AUTOMATA_T = 100
NEIGHBOURHOOD_SIZE = 8


# Runs the whole procedure
def run():
	population = initial()

	for i in range(0, MAX_GENERATION):
		population_results = map(lambda i: automaton.run(INITIAL_LETTICE, i, MAX_AUTOMATA_T), population)
		population_qualities = map(evaluation.run, population_results)

		print(f"geneneration {i}:")
		best_individuum_idx = population_qualities.index(max(population_qualities))
		print(f"    best individuum {population[best_individuum_idx]}")
		print(f"    best quality {population_qualities[best_individuum_idx]}")
		print()

		population = generational_replacement(population, qualities)


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


def parent_id_selection(population, qualities): # Select an individual
    tournament = map(lambda i: random.randint(0, len(population)), range(0, TOURNAMENT_SIZE))
	return tournament.index(max(tournament))


def generational_replacement(population, qualities):
	elite = qualities.index(max(qualities)) # best individual always survives

	new_population = [elite]

	for i in range(1, len(population)):
		p1 = parent_id_selection(population, qualities)
		p2 = parent_id_selection(population, qualities)

		child = crossover(p1, p2)
		child = mutate(child)

		new_population.add(child)
	
	return new_population


def initial(): # Returns the intial population
	return list(map(random_individuum, range(0, POPULATION_SIZE)))

   
def random_individuum():
	return [
		list(map(random.random, range(0, NEIGHBOURHOOD_SIZE)),
		list(map(random.random, range(0, NEIGHBOURHOOD_SIZE)),
	]


def get_copy(individual):
    return copy.deepcopy(individual)

run()
