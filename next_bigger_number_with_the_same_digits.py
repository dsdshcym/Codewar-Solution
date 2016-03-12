def next_bigger(n):
    s = list(str(n))
    for i in reversed(range(1, len(s))):
        if s[i] > s[i - 1]:
            pos = i - 1
            for j in reversed(range(pos + 1, len(s))):
                if s[j] > s[pos]:
                    s[pos], s[j] = s[j], s[pos]
                    s[pos + 1:] = s[pos + 1:][::-1]
                    break
            return int(''.join(s))
    return -1

assert(next_bigger(8) == -1)
assert(next_bigger(12) == 21)
assert(next_bigger(513) == 531)
assert(next_bigger(2017) == 2071)
assert(next_bigger(414) == 441)
assert(next_bigger(144) == 414)
assert(next_bigger(999) == -1)
print("tests passed")
