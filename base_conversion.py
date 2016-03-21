def convert(s, source, target):
    value = string_to_value(s, source)
    return value_to_string(value, target)

def string_to_value(s, encoding):
    n = len(encoding)
    result = 0
    for c in s:
        result = result * n + encoding.find(c)
    return result

def value_to_string(v, encoding):
    if not v:
        return encoding[0]
    n = len(encoding)
    result = []
    while v > 0:
        result.append(encoding[v % n])
        v //= n
    return ''.join(result[::-1])
