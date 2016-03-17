def maxSequence(arr):
    result = s = 0
    for num in arr:
        s = max(0, s + num)
        result = max(result, s)
    return result

assert(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print("tests passed")
