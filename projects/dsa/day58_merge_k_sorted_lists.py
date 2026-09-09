"""
LeetCode 23: Merge k Sorted Lists
Pattern: Linked List (Sequential Merging, reusing Merge Two Sorted Lists)

Given an array of k linked-list heads, each sorted in ascending
order, merge all the linked-lists into one sorted linked list.

Approach: reuse mergeTwoLists() from Day 39. Take the first list
as the starting "result", then repeatedly merge it with each
remaining list, one at a time, building on top of the previous
merge each step.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists):
        if not lists:
            return None

        result = lists[0]
        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])

        return result


# Helpers for testing
def build_list(vals):
    if not vals:
        return None
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
lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
merged = sol.mergeKLists(lists)
print(print_list(merged))
# Output: [1, 1, 2, 3, 4, 4, 5, 6]

print(sol.mergeKLists([]))
# Output: None

print(print_list(sol.mergeKLists([build_list([1])])))
# Output: [1]

# Time: O(k*n) where k = number of lists, n = average length
# (sequential pairwise merging - a divide-and-conquer approach
# could improve this to O(n*log(k)))