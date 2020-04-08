# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ld = 0
        rd = 0
        if root is None:
            return 0
        if root.left:
            ld = self.maxDepth(root.left)
        if root.right:
            rd = self.maxDepth(root.right)

        return max(ld, rd) + 1
