
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next


def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    assert to_list(mergeTwoLists(
        build_list([1, 2, 4]),
        build_list([1, 3, 4])
    )) == [1, 1, 2, 3, 4, 4]

    assert to_list(mergeTwoLists(
        build_list([]),
        build_list([0])
    )) == [0]

    assert to_list(mergeTwoLists(
        build_list([]),
        build_list([])
    )) == []

    print("All Day 100 tests passed!")
