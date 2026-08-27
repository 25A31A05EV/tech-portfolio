"""
LeetCode 226: Invert Binary Tree
Pattern: Binary Tree (Recursion)

Given the root of a binary tree, invert the tree
(mirror it) and return its root.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left_invert = self.invertTree(root.left)
        right_invert = self.invertTree(root.right)

        root.left = right_invert
        root.right = left_invert

        return root


# Helper for testing
def print_tree(root, level=0, label="Root"):
    if root is not None:
        print("  " * level + f"{label}: {root.val}")
        print_tree(root.left, level + 1, "L")