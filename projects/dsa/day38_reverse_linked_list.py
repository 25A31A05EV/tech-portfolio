"""
LeetCode 206: Reverse Linked List
Pattern: Linked List (new pattern family)

Given the head of a singly linked list, reverse the list,
and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Helper functions for testing
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
    print(" -> ".join(map(str, result)) + " -> None")


# Test cases
head = build_list([1, 2, 3, 4, 5])
print("Original:", end=" ")
print_list(head)

reversed_head = reverseList(head)
print("Reversed:", end=" ")
print_list(reversed_head)