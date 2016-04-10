def valid_parentheses(string):
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        elif c ==')':
            if not stack:
                return False
            stack.pop()
    return stack == []

assert(valid_parentheses("  (") == False)
assert(valid_parentheses(")test") == False)
assert(valid_parentheses("") == True)
assert(valid_parentheses("hi())(") == False)
assert(valid_parentheses("hi(hi)()") == True)
