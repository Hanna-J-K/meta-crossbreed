import numpy as np
from adaptation import adaptation_function, calculate_total_adaptation
from utils import get_random_pair

rng = np.random.default_rng()


def calculate_chance(row: np.ndarray, sum: int) -> float:
    return adaptation_function(row) / sum


def calculate_chances(population: np.ndarray, total_adaptation: int) -> list:
    return [calculate_chance(row, total_adaptation) for row in population]


def roulette_selection(population: np.ndarray, new_size: int) -> np.ndarray:
    return rng.choice(population, size=new_size, p=calculate_chances(population, calculate_total_adaptation(population)))


def get_pair_winner(pair: np.ndarray) -> np.ndarray:
    return pair[0] if adaptation_function(pair[0]) > adaptation_function(pair[1]) else pair[1]


def tournament_selection(population: np.ndarray, new_size: int) -> np.ndarray:
    return np.array([get_pair_winner(get_random_pair(population)) for _ in range(new_size)])


def add_elite(current_population: np.ndarray, prev_population: np.ndarray) -> np.ndarray:
    return np.concatenate((np.array(sorted(list(prev_population), key=adaptation_function))[-2:], current_population[2:]))
