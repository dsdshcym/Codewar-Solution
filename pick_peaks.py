def pick_peaks(arr):
    arr = remove_duplicate(arr)
    results = [arr[i]
               for i in range(1, len(arr) - 1)
               if is_peak(arr[i - 1][1], arr[i][1], arr[i + 1][1])]
    print(arr, results)
    return {
        "pos": [pos for pos, _ in results],
        "peaks": [peak for _, peak in results]
    }

def is_peak(a, b, c):
    return (a < b > c)

def remove_duplicate(arr):
    return [(i, x)
            for i, x in enumerate(arr)
            if i == 0 or x != arr[i - 1]]

print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))
print(pick_peaks([12, 17, 13, 2, 19, 15, -3, -1, 17]))
