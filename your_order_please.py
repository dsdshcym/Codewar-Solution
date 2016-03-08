def order(sentense):
    """
    Digits will be sorted to the beginning of the sorted results
    """
    return " ".join(sorted(sentense.split(),
                           key=lambda x: sorted(x)))

assert(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
print("tests passed")
