"""
LeetCode 112: Path Sum
Pattern: Binary Tree (Recursion, path tracking)

Given the root of a binary tree and an integer targetSum,
return True if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

Key insight: instead of tracking the running sum, subtract each
node's value from the target as you go down. At a leaf node, if
the remaining target equals the leaf's own value, a valid path
was found. Using 'or' between the left and right recursive calls
means either branch succeeding is enough - the whole tree doesn't
need to match, just one path.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        remain = targetSum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


# Test cases
sol = Solution()

n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11, n7, n2)
n4a = TreeNode(4, n11)
n13 = TreeNode(13)
n4b = TreeNode(4, None, TreeNode(1))
n8 = TreeNode(8, n13, n4b)
root = TreeNode(5, n4a, n8)

print(sol.hasPathSum(root, 22))
# Output: True (path 5 -> 4 -> 11 -> 2 sums to 22)

print(sol.hasPathSum(root, 100))
# Output: False

print(sol.hasPathSum(None, 0))
# Output: False (empty tree)

print(sol.hasPathSum(TreeNode(5), 5))
# Output: True (single node)

# Time: O(n) - visits every node once in the worst case
# Space: O(h) - recursion call stack, h = tree height