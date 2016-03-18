def sum_pairs(nums, s):
    hash_table = {}
    for i, num in enumerate(nums):
        if s - num in hash_table:
            return [s - num, num]
        hash_table[num] = i
    return None
