def is_prime(num):
    num = abs(num)
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
        if i * i >= num:
            break
    return True
