def loop_size(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0
