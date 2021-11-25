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
from matplotlib import pyplot as plt


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
# print(parents)


all_children = crossbreed.crossbreed_population(
    all_children, selection.tournament_selection, crossbreed.make_new_generation_single_point)
priveleged_children = all_children

siema = []
elo = []
for i in range(NO_OF_ITERATIONS):
    all_copy = all_children
    priveleged_copy = priveleged_children

    all_children = crossbreed.crossbreed_population(
        all_children, selection.tournament_selection, crossbreed.make_new_generation_dual_point)
    all_children = crossbreed.fill_generation(all_copy, all_children)

    priveleged_children = crossbreed.crossbreed_population(
        priveleged_children, selection.tournament_selection, crossbreed.make_new_generation_dual_point)
    priveleged_children = crossbreed.fill_generation(
        priveleged_copy, priveleged_children)
    priveleged_children = selection.add_elite(
        priveleged_children, priveleged_copy)

    elo.append(adaptation.get_highest_adaptation(
        all_children))
    siema.append(adaptation.get_highest_adaptation(
        priveleged_children))

plt.plot(list(range(NO_OF_ITERATIONS)), siema)
plt.plot(list(range(NO_OF_ITERATIONS)), elo)
plt.show()
