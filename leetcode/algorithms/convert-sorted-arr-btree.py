# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0
        right = len(nums) - 1 # because of zero based indexing
        root = None
        return self.BSThelper(root, left, right, nums)

    def BSThelper(self, node, left, right, nums):
        if left > right:
            return

        mid = (left + right) // 2 # otherwise returns a float
        root = TreeNode(nums[mid])
        root.left = self.BSThelper(right, left, mid-1, nums)
        root.right = self.BSThelper(left, mid+1, right, nums)

        return root

