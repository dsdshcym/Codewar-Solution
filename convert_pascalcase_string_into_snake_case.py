import re

def cut(string):
    r = r'[A-Z]?[^A-Z]*'
    return [s.lower() for s in re.findall(r, string) if s]

def to_underscore(string):
    words = cut(str(string))
    return '_'.join(words)
