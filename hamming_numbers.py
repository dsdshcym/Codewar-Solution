import heapq

def hamming(n):
    seeds = [2, 3, 5]
    hamming_number = [1]
    count = 1

    def generate(seed):
        for num in hamming_number:
            yield seed * num

    heap = heapq.merge(*map(generate, seeds))

    while count < n:
        next_hamming = next(heap)
        if next_hamming != hamming_number[-1]:
            hamming_number.append(next_hamming)
            count += 1

    return hamming_number[-1]
