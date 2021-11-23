import numpy as np
from items import items_length
from utils import random_binary_array
from params import POPULATION_SIZE


def random_population() -> np.ndarray:
    return np.array([random_binary_array(items_length) for _ in range(POPULATION_SIZE)])
