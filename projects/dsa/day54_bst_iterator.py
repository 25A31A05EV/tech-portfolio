"""
LeetCode 173: Binary Search Tree Iterator
Pattern: Binary Search Tree (Design + In-order Traversal)

Design an iterator over a BST that returns values in ascending
(in-order) order, one at a time via next(), with hasNext()
checking if more values remain.

Design approach - "Precompute + Pointer":
1. In the constructor, do a full in-order traversal once and
   store all values in a sorted list (BST in-order = sorted).
2. Track position with an index pointer (self.index), not a
   local variable - state must persist across separate next()
   and hasNext() calls, and self.attributes are what survive
   between method calls on the same object.
3. next() reads the current value, THEN advances the pointer -
   doing it in the other order would return the wrong value.
4. hasNext() uses strict '<' (not '<='): once index equals
   len(values), every valid index (0 to len-1) has already
   been consumed.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root):
        self.values = []
        self.index = 0
        self._inorder(root)

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        self.values.append(node.val)
        self._inorder(node.right)

    def next(self):
        value = self.values[self.index]
        self.index += 1
        return value

    def hasNext(self):
        return self.index < len(self.values)


# Test case
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
it = BSTIterator(root)
print(it.next())     # 3
print(it.next())     # 7
print(it.next())     # 9
print(it.hasNext())  # True
print(it.next())     # 15
print(it.next())     # 20
print(it.hasNext())  # False

# Time: O(n) to build (constructor), O(1) per next()/hasNext() call
# Space: O(n) - stores all values in the list