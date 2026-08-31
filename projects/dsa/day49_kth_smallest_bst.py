"""
LeetCode 230: Kth Smallest Element in a BST
Pattern: Binary Search Tree (In-order Traversal)

Given the root of a BST and an integer k, return the kth
smallest value (1-indexed) among all node values.

Key insight: In-order traversal (Left -> Node -> Right) of a
BST visits nodes in sorted order, because every left subtree
holds smaller values and every right subtree holds larger
values (the BST property).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]


# Test cases
sol = Solution()

root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(sol.kthSmallest(root, 3))
# Output: 4

print(sol.kthSmallest(root, 1))
# Output: 2

print(sol.kthSmallest(root, 5))
# Output: 8

# Time: O(n) - visits every node once
# Space: O(n) - result list stores all values (+ O(h) recursion stack)