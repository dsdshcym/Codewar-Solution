def valid_parentheses(string):
    count = 0
    for c in string:
        count += (c == '(') - (c == ')')
        if count < 0:
            return False
    return count == 0

assert(valid_parentheses("  (") == False)
assert(valid_parentheses(")test") == False)
assert(valid_parentheses("") == True)
assert(valid_parentheses("hi())(") == False)
assert(valid_parentheses("hi(hi)()") == True)
