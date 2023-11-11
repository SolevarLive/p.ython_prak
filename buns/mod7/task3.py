import time
def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'start_t'):
            wrapper.start_t = time.time()
            result = func(*args, **kwargs)
            wrapper.end_t = time.time()
            print(f"Time taken: {wrapper.end_t - wrapper.start_t } milliseconds")
            delattr(wrapper,'start_t')
            delattr(wrapper, 'end_t')
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@validate_args
@timer
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(21))