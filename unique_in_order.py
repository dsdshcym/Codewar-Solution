def unique_in_order(iterable):
    ans = []
    for element in iterable:
        if not ans or element != ans[-1]:
            ans.append(element)
    return ans
