import numpy as np
from utils import twice, cross_arrays, dual_cross_arrays, get_pair_count, flatten_one_dimension
from typing import Callable
from params import *
from mutation import mutate_children
from adaptation import adaptation_function

rng = np.random.default_rng()


def do_crossbreed_single_point(pair: np.ndarray, cross_point: int) -> np.ndarray:
    return np.array([cross_arrays(pair, cross_point), cross_arrays(pair[::-1], cross_point)])


def do_crossbreed_dual_point(pair: np.ndarray, cross_points: tuple) -> np.ndarray:
    return np.array([dual_cross_arrays(pair, cross_points), dual_cross_arrays(pair[::-1], cross_points)])


def do_crossbreed_random_point(pair: np.ndarray) -> np.ndarray:
    return do_crossbreed_single_point(pair, np.random.randint(1, pair.shape[1]))


def do_crossbreed_random_points(pair: np.ndarray) -> np.ndarray:
    return do_crossbreed_dual_point(pair, twice(np.random.randint, 1, pair.shape[1]))


def get_crossbred_population_size() -> int:
    return round(POPULATION_SIZE * CROSSING_PROBABILITY)


def get_crossbreed_pair_count() -> int:
    return get_pair_count(get_crossbred_population_size())


def zip_potential_parents(potential_parents: np.ndarray, pair_count: int) -> np.ndarray:
    return np.dstack(twice(rng.choice, potential_parents, size=pair_count))


def get_parents(potential_parents: np.ndarray, pair_count: int) -> np.ndarray:
    return np.array([parents.T for parents in zip_potential_parents(potential_parents, pair_count)])


def get_children_matrix(parents: np.ndarray, generator: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    return np.array([generator(pair) for pair in parents])


def make_all_children_single_point(parents: np.ndarray) -> np.ndarray:
    return flatten_one_dimension(get_children_matrix(parents, do_crossbreed_random_point))


def make_all_children_dual_point(parents: np.ndarray) -> np.ndarray:
    return flatten_one_dimension(get_children_matrix(parents, do_crossbreed_random_points))


def make_new_generation_single_point(potential_parents: np.ndarray, pair_count: int) -> np.ndarray:
    return make_all_children_single_point(get_parents(potential_parents, pair_count))


def make_new_generation_dual_point(potential_parents: np.ndarray, pair_count: int) -> np.ndarray:
    return make_all_children_dual_point(get_parents(potential_parents, pair_count))


def crossbreed_population(population: np.ndarray, selection_method: Callable[[np.ndarray, int], np.ndarray], make_new_generation: Callable) -> np.ndarray:
    return make_new_generation(selection_method(population, POPULATION_SIZE), get_crossbreed_pair_count())


def fill_generation(prev_population: np.ndarray, children: np.ndarray) -> np.ndarray:
    return np.concatenate((mutate_children(children), np.array(sorted(list(prev_population), key=adaptation_function))[-(prev_population.shape[0] - children.shape[0]):]))
