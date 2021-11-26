from functools import lru_cache, wraps
import timeit
import numpy as np


def measuretime(func):
    def wrapper(*args, **kwargs):
        function_start = timeit.default_timer()
        value = func(*args, **kwargs)
        execution_time = timeit.default_timer() - function_start
        print(f"{func.__name__} time: {execution_time}")
        return value
    return wrapper


def np_cache(function):
    @lru_cache(maxsize=None)
    def cached_wrapper(hashable_array):
        array = np.array(hashable_array)
        return function(array)

    @wraps(function)
    def wrapper(array):
        return cached_wrapper(tuple(array))

    wrapper.cache_info = cached_wrapper.cache_info
    wrapper.cache_clear = cached_wrapper.cache_clear

    return wrapper
