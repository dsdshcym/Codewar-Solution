def accum(s):
    return '-'.join([((i + 1) * c).capitalize() for i, c in enumerate(s)])
