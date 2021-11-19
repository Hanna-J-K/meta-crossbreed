import population
import crossbreed
import mutation
import numpy as np
import adaptation
import selection
import utils
import items
from decorator import measuretime

CROSSING_PROBABILITY = .3
MUTATION_PROBABILITY = .001
POPULATION_SIZE = 500
NO_OF_ITERATIONS = 3000


x = population.random_population(POPULATION_SIZE)



def make_new_child(population: np.ndarray):
    parents = utils.get_random_pair(population)
    crossbred = crossbreed.do_crossbreed_single_point(parents, np.random.randint(1, items.items_length))
    return mutation.mutate_child(crossbred[0], MUTATION_PROBABILITY)


def foo(population):
    population = selection.roulette_selection(population, POPULATION_SIZE)
    population = np.array([make_new_child(population) for _ in range(POPULATION_SIZE)])


for iteration in range(NO_OF_ITERATIONS):
    foo(x)

last_generation_adaptation = np.array(list(map(adaptation.adaptation_function, x)))
index = np.argmax(last_generation_adaptation)

print(max(last_generation_adaptation))
print(last_generation_adaptation[index], adaptation.row_weight(x[index]))