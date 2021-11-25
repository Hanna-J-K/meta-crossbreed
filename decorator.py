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


def jeongyeon(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} 손잡고 딴단딴단딴")
        value = func(*args, **kwargs)
        return value
    return wrapper


def momo(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} Once, let's turn into pigs!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def sana(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} Yes, I'm Sana!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def jihyo(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} 야근? OK!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def mina(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} :(")
        value = func(*args, **kwargs)
        return value
    return wrapper


def dahyun(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} Bonjour")
        value = func(*args, **kwargs)
        return value
    return wrapper


def chaeyoung(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} Risky risky, wiggy wiggy!")
        value = func(*args, **kwargs)
        return value
    return wrapper


def tzuyu(func):
    def wrapper(*args, **kwargs):
        print(f"{args[0].__name__} Thank you it was very boring.")
        value = func(*args, **kwargs)
        return value
    return wrapper
