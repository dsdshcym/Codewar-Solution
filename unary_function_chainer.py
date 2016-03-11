def chained(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)
