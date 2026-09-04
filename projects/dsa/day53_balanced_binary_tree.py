"""
LeetCode 110: Balanced Binary Tree
Pattern: Binary Tree (Recursion, track state across calls)

Given a binary tree, determine if it is height-balanced -
meaning for every node, the height difference between its
left and right subtrees is no more than 1.

Key insight: checking only the root is NOT enough - a tree can
look balanced at the root while a deeper subtree is unbalanced.
The check must happen at every single node. self.balanced is
used (not a local variable) because it needs to persist and be
shared across all the recursive calls - a local variable would
reset on every call and any earlier "unbalanced" finding would
be lost.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
            return 1 + max(left_height, right_height)

        height(root)
        return self.balanced


# Test cases
sol = Solution()

root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.isBalanced(root1))
# Output: True

root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
print(sol.isBalanced(root2))
# Output: False

print(sol.isBalanced(TreeNode(1)))
# Output: True

print(sol.isBalanced(None))
# Output: True

# Time: O(n) - every node visited once
# Space: O(h) - recursion call stack, h = tree height