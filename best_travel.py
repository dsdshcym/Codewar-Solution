from itertools import combinations

def choose_best_sum(t, k, ls):
    sums = [sum(comb)
            for comb in combinations(ls, k)
            if sum(comb) <= t]
    if sums:
        return max(sums)
    return None
