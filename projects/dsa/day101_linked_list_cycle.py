
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    # No cycle
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a.next = b
    b.next = c

    assert hasCycle(a) is False

    # Cycle: 3 -> 2
    c.next = b

    assert hasCycle(a) is True

    # Empty list
    assert hasCycle(None) is False

    print("All Day 101 tests passed!")
