import population
import crossbreed
import mutation
import numpy as np
import adaptation
import selection
import utils
import items

CROSSING_PROBABILITY = .3
MUTATION_PROBABILITY = .001
POPULATION_SIZE = 500
NO_OF_ITERATIONS = 1000


x = population.random_population(POPULATION_SIZE)



def make_new_child(population: np.ndarray):
    parents = utils.get_random_pair(population)

    crossbred = crossbreed.do_crossbreed_single_point(parents, np.random.randint(1, items.items_length))

    return mutation.mutate_child(crossbred[0], MUTATION_PROBABILITY)


for generation in range(NO_OF_ITERATIONS):
    x = selection.roulette_selection(x, POPULATION_SIZE)
    x = np.array([make_new_child(x) for _ in range(POPULATION_SIZE)])

print(list(map(adaptation.adaptation_function, x)))
# for row in x:
#     print(row, items.adaptation_function(row))


# y = items.tournament_selection(x, 8)

# print(y)

# a = np.array(['1', '2', '3', '4', '5', '6', '7'])
# b = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# print(crossbreed.do_crossbreed_single_point(np.array([a, b]), 4))
