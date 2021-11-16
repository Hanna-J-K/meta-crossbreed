import numpy as np
from adaptation import adaptation_function, calculate_total_adaptation
from utils import get_random_pair

rng = np.random.default_rng()


def calculate_chance(row: np.ndarray, sum: int) -> float:
    return adaptation_function(row) / sum


def calculate_chances(population: np.ndarray) -> list:
    return [calculate_chance(row, calculate_total_adaptation(population)) for row in population]


def roulette_selection(population: np.ndarray, new_size: int) -> np.ndarray:
    return rng.choice(population, size=new_size, p=calculate_chances(population))


def get_pair_winner(pair: np.ndarray) -> np.ndarray:
    return pair[0] if adaptation_function(pair[0]) > adaptation_function(pair[1]) else pair[1]


def tournament_selection(population: np.ndarray, new_size: int) -> np.ndarray:
    return np.array([get_pair_winner(get_random_pair(population)) for _ in range(new_size)])
