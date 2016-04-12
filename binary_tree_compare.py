def compare(a, b):
    if not a or not b:
        return a is b
    if a.val == b.val:
        return compare(a.left, b.left) and compare(a.right, b.right)
    return False
