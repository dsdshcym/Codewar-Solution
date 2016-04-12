class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def front_back_split(source, front, back):
    assert(source and front and back)
    assert(source.data and source.next)
    slow, fast = source, source.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    back.data = slow.next.data
    back.next = slow.next.next

    slow.next = None

    front.data = source.data
    front.next = source.next
