def lcs(x, y):
    n, m = len(x), len(y)
    f = [[0 for j in range(m + 1)] for i in range(n + 1)]
    length = 0
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                f[i+1][j+1] = f[i][j] + 1
            else:
                f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
    result = []
    while n != 0 and m != 0:
        if f[n][m] == f[n-1][m]:
            n -= 1
        elif f[n][m] == f[n][m-1]:
            m -= 1
        else:
            result.append(x[n-1])
            n, m = n - 1, m - 1
    return ''.join(result[::-1])

print(lcs("abcdef", "abc"))
print(lcs("abcdef", "acf"))
print(lcs("132535365", "123456789"))
