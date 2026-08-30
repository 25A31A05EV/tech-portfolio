"""
LeetCode 98: Validate Binary Search Tree
Pattern: Binary Tree (Range-passing Recursion) - Mock Interview #3

Given the root of a binary tree, determine if it is a valid
binary search tree (BST).

Key insight: checking only immediate parent-child relationships
is NOT enough. Every node must satisfy the BST property with
respect to ALL its ancestors, not just its direct parent. Each
node carries down a valid (low, high) range from its ancestors.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            # Left child must be less than this node -> becomes new "high"
            # Right child must be greater than this node -> becomes new "low"
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))


# Test cases
sol = Solution()

# Valid BST
root1 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8))
print(sol.isValidBST(root1))
# Output: True

# Invalid BST (the tricky case - looks locally fine but fails against an ancestor)
root2 = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(3), TreeNode(9)))
print(sol.isValidBST(root2))
# Output: False (node 3 < root 5, but sits in root's right subtree)

# Single node
print(sol.isValidBST(TreeNode(1)))
# Output: True

# Time: O(n) - every node visited once
# Space: O(h) - recursion call stack, h = tree height