import timeit

def measuretime(func):
    def wrapper(*args, **kwargs):
        function_start = timeit.default_timer()
        value = func(*args, **kwargs)
        execution_time = timeit.default_timer() - function_start
        print(f"{func.__name__} time: {execution_time}")
        return value
    return wrapper
