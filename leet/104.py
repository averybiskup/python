# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        a = self.maxDepth(root.right) + 1 if root.right else 1
        b = self.maxDepth(root.left) + 1 if root.left else 1
        return a if a >= b else b
