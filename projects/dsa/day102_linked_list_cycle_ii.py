
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head):
    slow = head
    fast = head

    # Step 1: Detect whether a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    # Step 2: Find the cycle's starting node
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    # Cycle: 3 -> 2
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    assert detectCycle(a) == b

    # No cycle
    x = ListNode(1)
    y = ListNode(2)
    x.next = y

    assert detectCycle(x) is None

    # Empty list
    assert detectCycle(None) is None

    print("All Day 102 tests passed!")
