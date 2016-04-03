def pick_peaks(arr):
    pos = []
    prob_peak = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prob_peak = i
        else:
            if arr[i] < arr[i - 1] and prob_peak:
                pos.append(prob_peak)
                prob_peak = None
    return {"pos": pos, "peaks": [arr[i] for i in pos]}

print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))
print(pick_peaks([12, 17, 13, 2, 19, 15, -3, -1, 17]))
