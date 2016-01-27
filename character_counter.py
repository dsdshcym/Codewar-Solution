def validate_word(word):
    word = word.lower()
    return len(word) == len(set(word)) * word.count(word[0])
