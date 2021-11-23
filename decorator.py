import timeit


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
        print(f"{args[0].__name__} Oh, I'm so curious!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def jihyo(func):
    def wrapper(*args, **kwargs):
        print(f"야근? OK!")
        value = func(*args, **kwargs)
        return value
    return wrapper
