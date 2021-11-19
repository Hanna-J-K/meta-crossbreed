import numpy as np


rng = np.random.default_rng()


def random_binary_array(array_length: int) -> np.ndarray:
    return rng.choice([0, 1], size=array_length)


def get_random_pair(population: np.ndarray) -> np.ndarray:
    return rng.choice(population, size=2)


def join_arrays(first_array: np.ndarray, second_array: np.ndarray) -> np.ndarray:
    return np.concatenate((first_array, second_array))


def left(array: np.ndarray, split_point: int) -> np.ndarray:
    return array[:split_point]


def right(array: np.ndarray, split_point: int) -> np.ndarray:
    return array[split_point:]


def cross_arrays(pair: np.ndarray, cross_point: int) -> np.ndarray:
    return join_arrays(left(pair[0], cross_point), right(pair[1], cross_point))


def flip_gene(gene: int) -> int:
    return 0 if gene else 1

def flip_child(child: np.ndarray) -> np.ndarray:
    return np.vectorize(flip_gene)(child)