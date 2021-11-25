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


def nayeon(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Oh, I'm so curious!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def jeongyeon(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} sonjabgo ttandanttandanttan")
        value = func(*args, **kwargs)
        return value
    return wrapper


def momo(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Once, let's turn into pigs!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def sana(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Yes, I'm Sana!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def jihyo(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} yageun? OK!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def mina(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} :(")
        value = func(*args, **kwargs)
        return value
    return wrapper


def dahyun(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Bonjour")
        value = func(*args, **kwargs)
        return value
    return wrapper


def chaeyoung(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Risky risky, wiggy wiggy!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def tzuyu(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} Thank you it was very boring.")
        value = func(*args, **kwargs)
        return value
    return wrapper


def somi(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def np_cache(function):
    @lru_cache(maxsize=None)
    def cached_wrapper(hashable_array):
        array = np.array(hashable_array)
        return function(array)

    @wraps(function)
    def wrapper(array):
        return cached_wrapper(tuple(array))

    # copy lru_cache attributes over too
    wrapper.cache_info = cached_wrapper.cache_info
    wrapper.cache_clear = cached_wrapper.cache_clear

    return wrapper
