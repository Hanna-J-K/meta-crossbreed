import population
import crossbreed
import selection
import mutation
from params import *
from plot import plot__triple__comparison_population, plot_comparison, plot__triple__comparison


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


def generate_crossing_probability(values: tuple) -> None:
    i = 0
    while True:
        crossbreed.CROSSING_PROBABILITY = values[i]
        yield
        if i == 2:
            i = 0
        else:
            i = i + 1


def generate_mutation_probability(values: tuple) -> None:
    i = 0
    while True:
        mutation.MUTATION_PROBABILITY = values[i]
        yield
        if i == 2:
            i = 0
        else:
            i = i + 1


def generate_population_size(values: tuple) -> None:
    i = 0
    while True:
        population.POPULATION_SIZE = values[i]
        crossbreed.POPULATION_SIZE = values[i]
        yield
        if i == 2:
            i = 0
        else:
            i = i + 1


crossing_modifier_params = (0.1, 0.5, 0.9)
mutation_modifier_params = (0.001, 0.005, 0.009)
population_modifier_params = (10, 100, 1000)

plot__triple__comparison(
    method_rs, rs_name, generate_crossing_probability, crossing_modifier_params)
plot__triple__comparison(
    method_ts, ts_name, generate_crossing_probability, crossing_modifier_params)

plot__triple__comparison(
    method_rs, rs_name, generate_mutation_probability, mutation_modifier_params)
plot__triple__comparison(
    method_ts, ts_name, generate_mutation_probability, mutation_modifier_params)


plot__triple__comparison_population(
    method_rs, rs_name, generate_population_size, population_modifier_params)
plot__triple__comparison_population(
    method_ts, ts_name, generate_population_size, population_modifier_params)
