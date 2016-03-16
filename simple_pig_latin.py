def isalpha_filter(function):
    def f(text):
        if text.isalpha():
            return function(text)
        return text
    return f

@isalpha_filter
def shift_first_to_end(text):
    return text[1:] + text[:1]

@isalpha_filter
def add_ay_to_end(text):
    return text + 'ay'

def pig_it(text):
    return ' '.join(map(add_ay_to_end,
                        map(shift_first_to_end,
                            text.split())))

assert(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
assert(pig_it('This is my string') == 'hisTay siay ymay tringsay')
