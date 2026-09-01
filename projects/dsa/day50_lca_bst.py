"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
Pattern: Binary Search Tree

*** DAY 50 MILESTONE: 50th DSA problem! ***

Given a BST and two nodes p and q, find their lowest common
ancestor (LCA) - the deepest node that has both p and q as
descendants (a node can be a descendant of itself).

Key insight (using the BST property):
- If both p and q are smaller than the current node, the LCA
  must be in the left subtree.
- If both p and q are larger than the current node, the LCA
  must be in the right subtree.
- Otherwise (they're on different sides, or one equals the
  current node), the current node IS the LCA - this is the
  split point where their paths diverge.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current


# Test cases
sol = Solution()

n0 = TreeNode(0)
n3 = TreeNode(3)
n5 = TreeNode(5)
n4 = TreeNode(4, n3, n5)
n2 = TreeNode(2, n0, n4)
n7 = TreeNode(7)
n9 = TreeNode(9)
n8 = TreeNode(8, n7, n9)
root = TreeNode(6, n2, n8)

print(sol.lowestCommonAncestor(root, n2, n8).val)
# Output: 6 (different sides -> root is LCA)

print(sol.lowestCommonAncestor(root, n0, n4).val)
# Output: 2 (both smaller than 6 -> go left; both descendants of 2 -> 2 is LCA)

print(sol.lowestCommonAncestor(root, n3, n5).val)
# Output: 4

# Time: O(h) - one path down the tree, h = tree height
# Space: O(1) - iterative, no recursion stack