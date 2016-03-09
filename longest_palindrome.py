def longest_palindrome (s):
    s = '*'.join('^{}$'.format(s))
    len_s = len(s)
    center = 0
    max_right = 0
    ans = 0
    P = [0] * len_s
    for i in range(1, len_s - 1):
        P[i] = int(max_right > i) and min(max_right - i,
                                          P[2 * center - i])
        while s[i - P[i] - 1] == s[i + P[i] + 1]:
            P[i] += 1
        ans = max(ans, P[i])
        if i + P[i] > max_right:
            center, max_right = i, i + P[i]
    return ans

assert(longest_palindrome("a") == 1)
assert(longest_palindrome("aa") == 2)
assert(longest_palindrome("baa") == 2)
assert(longest_palindrome("aab") == 2)
assert(longest_palindrome("abcdefghba") == 1)
assert(longest_palindrome("baablkj12345432133d") == 9)
print("tests passed")
