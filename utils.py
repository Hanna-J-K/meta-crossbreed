import numpy as np
import math
from decorator import nayeon, jeongyeon, momo, sana, jihyo, mina, dahyun, chaeyoung, tzuyu
from typing import Callable


rng = np.random.default_rng()


def twice(callback: Callable, *args, **kwargs) -> tuple:
    return tuple(callback(*args, **kwargs) for _ in range(2))


def random_binary_array(array_length: int) -> np.ndarray:
    return rng.choice([0, 1], size=array_length)


def get_random_pair(population: np.ndarray) -> np.ndarray:
    return rng.choice(population, size=2)


def get_random_chromosomes(population: np.ndarray, size: int) -> np.ndarray:
    return rng.choice(population, size=size)


def join_arrays(*arrays) -> np.ndarray:
    return np.concatenate((arrays))


def left(array: np.ndarray, split_point: int) -> np.ndarray:
    return array[:split_point]


def right(array: np.ndarray, split_point: int) -> np.ndarray:
    return array[split_point:]


def middle(array: np.ndarray, split_points: tuple) -> np.ndarray:
    return array[split_points[0]:split_points[1]]


def cross_arrays(pair: np.ndarray, cross_point: int) -> np.ndarray:
    return join_arrays(left(pair[0], cross_point), right(pair[1], cross_point))


def dual_cross_arrays(pair: np.ndarray, cross_points: tuple) -> np.ndarray:
    return join_arrays(left(pair[0], min(cross_points)), middle(pair[1], sorted(cross_points)), right(pair[0], max(cross_points)))


def flip_gene(gene: int) -> int:
    return 0 if gene else 1


def flip_child(child: np.ndarray) -> np.ndarray:
    return np.vectorize(flip_gene)(child)


def get_pair_count(population_size: int) -> int:
    return math.ceil(population_size / 2)


def flatten_one_dimension(array: np.ndarray) -> np.ndarray:
    return array.reshape(-1, array.shape[-1])
