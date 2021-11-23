import population
import crossbreed
import mutation
import numpy as np
import adaptation
import selection
import utils
import items
from decorator import measuretime
from params import *


def map_to_adaptation(population):
    return np.array(list(map(adaptation.adaptation_function, population)))


all_children = population.random_population()
# print()
# potential_parents = selection.roulette_selection(
#     all_children, POPULATION_SIZE)
# print(map_to_adaptation(potential_parents))
# count = crossbreed.get_crossbreed_pair_count()
# print(count)
# parents = crossbreed.get_parents(potential_parents, count)
# # print(parents)
# all_children = crossbreed.crossbreed_population(
#     all_children, selection.roulette_selection, crossbreed.make_new_generation_single_point)
# print(map_to_adaptation(all_children))


for i in range(NO_OF_ITERATIONS):
    copy = all_children
    potential_parents = selection.roulette_selection(
        all_children, POPULATION_SIZE)
    count = crossbreed.get_crossbreed_pair_count()
    parents = crossbreed.get_parents(potential_parents, count)
    all_children = crossbreed.crossbreed_population(
        all_children, selection.roulette_selection, crossbreed.make_new_generation_dual_point)
    all_children = crossbreed.fill_generation(copy, all_children)
    max = adaptation.get_highest_adaptation(
        all_children)
    if i % 5 == 0:
        print(max)

# print(next_max)
