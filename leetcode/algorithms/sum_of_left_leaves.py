# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Time Complexity:
    Best: O(1) where there are no items in the list
    Average: O(n) where we need to traverse every node
    Worst: O(n) we need to traverse every node
    """

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
            
    def helper(self, node, total):
        if not node:
            return 0
        total = self.helper(node.left, total) + self.helper(node.right, total)
        
        if node.left:
            if not node.left.left and not node.left.right:
                return total + node.left.val
        return total
