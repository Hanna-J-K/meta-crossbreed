import population
import crossbreed
import numpy as np
import adaptation
import selection
from decorator import measuretime
from params import *
from matplotlib import pyplot as plt
from plot import plot_comparison


def method_rs(x): return crossbreed.crossbreed_population(
    x, selection.roulette_selection, crossbreed.make_new_generation_single_point)


def method_rm(x): return crossbreed.crossbreed_population(
    x, selection.roulette_selection, crossbreed.make_new_generation_dual_point)


def method_ts(x): return crossbreed.crossbreed_population(
    x, selection.tournament_selection, crossbreed.make_new_generation_single_point)


def method_tm(x): return crossbreed.crossbreed_population(
    x, selection.tournament_selection, crossbreed.make_new_generation_dual_point)


rse_name = "Roulette, single, elite"
rsn_name = "Roulette, single, no elite"
rme_name = "Roulette, multi, elite"
rmn_name = "Roulette, multi, no elite"

tse_name = "Tournament, single, elite"
tsn_name = "Tournament, single, no elite"
tme_name = "Tournament, multi, elite"
tmn_name = "Tournament, multi, no elite"

plot_comparison(method_rs, method_rs, rse_name, rsn_name, elite_a=True)
plot_comparison(method_rm, method_rm, rme_name, rmn_name, elite_a=True)

plot_comparison(method_ts, method_ts, tse_name, tsn_name, elite_a=True)
plot_comparison(method_tm, method_tm, tme_name, tmn_name, elite_a=True)

rs_name = "Roulette, single"
rm_name = "Roulette, multi"
ts_name = "Tournament, single"
tm_name = "Tournament, multi"

plot_comparison(method_rs, method_ts, rs_name, ts_name)
plot_comparison(method_rm, method_tm, rm_name, tm_name)

plot_comparison(method_rs, method_rm, rs_name, rm_name)
plot_comparison(method_ts, method_tm, ts_name, tm_name)

# starting_population = population.random_population()
# all_children = starting_population
# priveleged_children = starting_population

# no_elite = []
# elite = []
# for _ in range(REPEATS):
#     all_children = starting_population
#     no_elite.append([])
#     for i in range(NO_OF_ITERATIONS):
#         all_copy = all_children
#         # priveleged_copy = priveleged_children

#         all_children = crossbreed.crossbreed_population(
#             all_children, selection.roulette_selection, crossbreed.make_new_generation_dual_point)
#         all_children = crossbreed.fill_generation(all_copy, all_children)

#         # priveleged_children = crossbreed.crossbreed_population(
#         #     priveleged_children, selection.roulette_selection, crossbreed.make_new_generation_dual_point)
#         # priveleged_children = crossbreed.fill_generation(
#         #     priveleged_copy, priveleged_children)
#         # priveleged_children = selection.add_elite(
#         #     priveleged_children, priveleged_copy)

#         no_elite[-1].append(adaptation.get_highest_adaptation(
#             all_children))
#         # elite.append(adaptation.get_highest_adaptation(
#         #     priveleged_children))

#         # if(np.unique(all_children, axis=0).shape[0] < POPULATION_SIZE * MIN_CHANGE_RATIO and i != 0):
#         #     print(f"Stopped due to no alterations in {i} iterations")
#         #     break

# no_elite = np.array(no_elite)
# mean = np.mean(no_elite, axis=0)
# print(f"No_elite: {mean[-1]}")
# # print(f"Elite: {elite[-1]}")
# max_index = np.argmax(no_elite[:, -1])
# min_index = np.argmin(no_elite[:, -1])
# # for element in no_elite:
# #     plt.plot(list(range(len(element))), element,
# #              color='pink', linewidth=1)
# plt.plot(list(range(len(no_elite[0]))), no_elite[max_index],
#          color='pink', label='max')
# plt.plot(list(range(len(no_elite[0]))), no_elite[min_index],
#          color='thistle', label='min')
# plt.plot(list(range(len(mean))), mean,
#          color='palevioletred', label='no_elite')

# # plt.plot(list(range(len(elite))), elite, color='black', label='elite')
# plt.legend()
# plt.show()
