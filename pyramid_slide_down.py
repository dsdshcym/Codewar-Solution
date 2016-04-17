def longest_slide_down(pyramid):
    f = [0] * (len(pyramid) + 1)
    for row in pyramid[::-1]:
        for i, length in enumerate(row):
            f[i] = max(f[i], f[i + 1]) + length
    return f[0]
