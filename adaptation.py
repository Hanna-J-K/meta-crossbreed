import numpy as np
from items import items, KNAPSACK_SIZE, WEIGHT, VALUE
from decorator import measuretime


def map_row_to_property(row: np.ndarray, property: int) -> np.ndarray:
    return np.where(row == 1, items[:, property], 0).astype(int)


def row_weight(row: np.ndarray) -> int:
    return np.sum(map_row_to_property(row, WEIGHT))


def row_value(row: np.ndarray) -> int:
    return np.sum(map_row_to_property(row, VALUE))


def adaptation_function(row: np.ndarray) -> int:
    return row_value(row) if row_weight(row) <= KNAPSACK_SIZE else 0


def calculate_total_adaptation(population: np.ndarray) -> np.int64:
    x = np.array([adaptation_function(row)
                 for row in population], dtype=np.int64).sum()
    if x == 0:
        print(f"WARNING: x == 0")
    return x


def get_highest_adaptation(population: np.ndarray) -> int:
    return np.array(list(map(adaptation_function, population))).max()
