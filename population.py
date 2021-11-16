import numpy as np
from items import items_length
from utils import random_binary_array


def random_population(population_size: int) -> np.ndarray:
    return np.array([random_binary_array(items_length) for _ in range(population_size)])
