from itertools import combinations

def choose_best_sum(t, k, ls):
    return max([sum(comb)
                for comb in combinations(ls, k)
                if sum(comb) <= t] or [None])
