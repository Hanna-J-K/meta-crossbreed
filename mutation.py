import numpy as np
from utils import flip_child

rng = np.random.default_rng()

def get_mutation_array(array_length: int) -> np.ndarray:
    return rng.random(array_length)

def mutate_child(child: np.ndarray, probability: float) -> np.ndarray:
    return np.where((get_mutation_array(child.shape[0]) <= probability), flip_child(child), child)