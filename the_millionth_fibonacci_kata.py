def fib(n):
    if n < 0:
        return fib(-n) if n % 2 == 1 else -fib(-n)
    return quick_power([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)[0][1]

def quick_power(x, n, identity, mult):
    if n == 0:
        return identity
    if n == 1:
        return x

    temp = quick_power(x, n // 2, identity, mult)
    temp = mult(temp, temp)
    if n % 2:
        return mult(temp, x)
    else:
        return temp

def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_A, col_B))
             for col_B in BT]
            for row_A in A]

def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for j in r] for i in r]
