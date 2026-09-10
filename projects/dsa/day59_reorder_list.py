"""
LeetCode 143: Reorder List
Pattern: Linked List (Fast-Slow Pointers + Reverse + Merge combined)

Given the head of a singly linked list L0 -> L1 -> ... -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

This combines three techniques:
1. Fast-slow pointers to find the middle (fast moves 2x speed,
   so when it reaches the end, slow is at the midpoint).
2. Reverse the second half (reusing the reverseList pattern
   from Day 38).
3. Merge the two halves alternately, one node from each side
   at a time.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        # Step 1: Find middle using fast-slow
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        second = prev

        # Step 3: Merge alternately
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


# Helpers for testing
def build_list(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
sol = Solution()

head1 = build_list([1, 2, 3, 4])
sol.reorderList(head1)
print(print_list(head1))
# Output: [1, 4, 2, 3]

head2 = build_list([1, 2, 3, 4, 5])
sol.reorderList(head2)
print(print_list(head2))
# Output: [1, 5, 2, 4, 3]

# Time: O(n) - each step (find middle, reverse, merge) is O(n)
# Space: O(1) - in-place, no extra data structure