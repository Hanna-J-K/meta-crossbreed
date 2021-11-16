import numpy as np
from utils import cross_arrays


def do_crossbreed_single_point(pair: np.ndarray, cross_point: int) -> np.ndarray:
    return np.array([cross_arrays(pair, cross_point), cross_arrays(pair[::-1], cross_point)])
