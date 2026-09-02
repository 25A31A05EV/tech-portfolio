="""
LeetCode 701: Insert into a Binary Search Tree
Pattern: Binary Search Tree (Recursive Insertion)

Given the root of a BST and a value to insert, insert the value
into the tree such that the BST property is maintained, and
return the root of the tree.

Key insight: recurse down comparing val to each node - go left
if smaller, right if larger - until an empty spot (None) is
found. That's where the new node belongs. The recursive
assignment (root.left = ...) is essential: without it, the
newly created node would be returned but never attached back
into the tree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# Helper for testing
def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    return result


# Test cases
sol = Solution()

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
new_root = sol.insertIntoBST(root, 5)
print(inorder(new_root, []))
# Output: [1, 2, 3, 4, 5, 7] (still sorted after insertion)

print(inorder(sol.insertIntoBST(None, 10), []))
# Output: [10] (insert into empty tree)

# Time: O(h) - one path down the tree, h = tree height
# Space: O(h) - recursion call stack