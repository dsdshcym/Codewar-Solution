def to_underscore(string):
    string = str(string)
    if not string:
        return ""
    part = []
    results = []
    for c in string:
        if c.isupper():
            if part:
                results.append(''.join(part))
            part = []
        part.append(c.lower())
    if part:
        results.append(''.join(part))
    return '_'.join(results)
