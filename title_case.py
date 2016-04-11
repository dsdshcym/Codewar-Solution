def capitalize(s, minor_words=[]):
    s = s.lower()
    if s in minor_words:
        return s
    return s[0].upper() + s[1:]

def title_case(title, minor_words=''):
    if not title:
        return ''
    minor_words = [s.lower() for s in minor_words.split()]
    title = [capitalize(s, minor_words) for s in title.split()]
    title[0] = capitalize(title[0])
    return ' '.join(title)
