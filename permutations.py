def permutations(string):
    return reduce(lambda perms, s: [p[:i] + s + p[i:]
                                    for p in perms
                                    for i in range((p+s).index(s)+1)],
                  string, [''])

print(permutations('a'))
print(permutations('aabb'))
