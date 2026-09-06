class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True

            if t1 is None or t2 is None:
                return False

            if t1.val != t2.val:
                return False

            return (isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right)


# Test 1: Symmetric tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))   # True


# Test 2: Not symmetric
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(solution.isSymmetric(root2))  # False