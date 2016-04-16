def dig_pow(n, p):
    s = sum(int(c) ** (p + i) for i, c in enumerate(str(n)))
    if s % n == 0:
        return s // n
    return -1
