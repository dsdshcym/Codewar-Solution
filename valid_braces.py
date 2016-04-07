class BraceStack(object):
    def __init__(self, open_braces, closed_braces):
        self.brace_pairs = dict(zip(closed_braces, open_braces))
        self.stack = []

    def insert(self, brace):
        if brace in self.brace_pairs.keys():
            if self.empty():
                return False
            else:
                if self.stack[-1] == self.brace_pairs[brace]:
                    self.stack.pop()
                else:
                    return False
        else:
            self.stack.append(brace)
        return True

    def empty(self):
        return not self.stack

def validBraces(braces):
    brace_stack = BraceStack("([{", ")]}")
    for brace in braces:
        if not brace_stack.insert(brace):
            return False
    if not brace_stack.empty():
        return False
    return True

assert(validBraces( "(){}[]" ))
assert(not validBraces( "(}" ))
assert(not validBraces( "[(])" ))
assert(validBraces( "([{}])" ))
