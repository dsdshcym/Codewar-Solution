def is_merge(s, part1, part2):
    len_0, len_1, len_2 = len(s), len(part1), len(part2)
    if len_0 != len_1 + len_2:
        return False

    f = [[False for j in range(len_2 + 1)] for i in range(len_1 + 1)]
    f[0][0] = True

    for i in range(len_1):
        f[i + 1][0] = s[i] == part1[i] and f[i][0]

    for j in range(len_2):
        f[0][j + 1] = s[j] == part2[j] and f[0][j]

    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            f[i][j] = (s[i + j - 1] == part1[i - 1] and f[i - 1][j]) or \
                      (s[i + j - 1] == part2[j - 1] and f[i][j - 1])

    return f[len_1][len_2]

assert(is_merge("codewars", "code", "wars"))
assert(is_merge("codewars", "cdw", "oears"))
assert(not is_merge("codewars", "cod", "wars"))
print("tests passed")
