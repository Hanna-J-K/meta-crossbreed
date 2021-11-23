import numpy as np
from utils import flip_child
from params import MUTATION_PROBABILITY

rng = np.random.default_rng()


def get_mutation_array(array_length: int) -> np.ndarray:
    return rng.random(array_length)


def mutate_child(child: np.ndarray) -> np.ndarray:
    return np.where((get_mutation_array(child.shape[0]) <= MUTATION_PROBABILITY), flip_child(child), child)


def mutate_children(children: np.ndarray) -> np.ndarray:
    return np.array([mutate_child(child) for child in children])
