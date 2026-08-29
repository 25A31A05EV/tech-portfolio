# Day 47: Diameter of Binary Tree

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Diameter passing through current node
            diameter = max(diameter, left_height + right_height)

            # Return height of current node
            return 1 + max(left_height, right_height)

        height(root)
        return diameter