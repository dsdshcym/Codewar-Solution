import re

def solution(string, markers):
    if markers:
        pattern = '[' + re.escape(''.join(markers)) + ']'
    else:
        pattern = ''
    return '\n'.join(re.split(pattern, s)[0].rstrip()
                     for s in string.splitlines())

result = solution('strawberries apples -\npears\nlemons watermelons @\n. lemons avocados @\ncherries bananas lemons lemons',
                  ['?', '!', '#', '-', '^', "'"])
print result
