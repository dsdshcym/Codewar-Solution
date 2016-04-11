def title_case(title, minor_words=''):
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    return ' '.join(s
                    if i and s in minor_words
                    else s.capitalize()
                    for i, s in enumerate(title))
