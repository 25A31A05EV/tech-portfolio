"""
LeetCode 104: Maximum Depth of Binary Tree
Pattern: Trees (Recursion / DFS)

Given the root of a binary tree, return its maximum depth
(the number of nodes along the longest path from the root
node down to the farthest leaf node).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0  # base case: empty tree has depth 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)  # +1 to count current node


# Test cases
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))
# Output: 3

print(maxDepth(TreeNode(1)))
# Output: 1 (single node)

print(maxDepth(None))
# Output: 0 (empty tree)