from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join([str(ascii_lowercase.index(c) + 1)
                    for c in text.lower()
                    if c in ascii_lowercase])
