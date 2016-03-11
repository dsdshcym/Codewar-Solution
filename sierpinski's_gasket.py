def sierpinski(n):
    """
    Returns a string containing the nth iteration of the Sierpinski Gasket
    fractal
    """
    if n == 0:
        return 'L'
    prev = sierpinski(n-1).split('\n')
    n = len(prev[-1])
    return '\n'.join(prev + [s.ljust(n + 1) + s for s in prev])

assert(sierpinski(0) == 'L')
assert(sierpinski(1) == 'L\nL L')
assert(sierpinski(2) == 'L\nL L\nL   L\nL L L L'.strip())
print("tests passed")
