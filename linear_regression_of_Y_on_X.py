def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line
        (Y on X).
    """
    n = len(x)

    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sumx2 = sum(x_i * x_i for x_i in x)

    a = float(sumx2 * sumy - sumx * sumxy) / float(n * sumx2 - sumx ** 2)
    b = float(n * sumxy - sumx * sumy) / float(n * sumx2 - sumx ** 2)

    return round(a, 4), round(b, 4)
