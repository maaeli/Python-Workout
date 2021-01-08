import functools

def my_sum(*args):
    return functools.reduce(lambda x,y: x + y, args, 0)
