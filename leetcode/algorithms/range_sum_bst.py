# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# My Solution (Naive Approach lol)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        if root.left == None and root.right == None:
            total += self.check_val(root.val, L, R)
            return total
        if root.left:
            total += self.rangeSumBST(root.left, L, R)
        if root.right:
            total += self.rangeSumBST(root.right, L, R)
        total += self.check_val(root.val, L, R)
        return total

    def check_val(self, num, l, r):
        if num >= l and num <= r:
            return num
        return 0


# Faster Solution that uses BST
class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        if R < root.val:
            return self.rangeSumBST(root.left, L, R)
        elif L > root.val:
            return self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)


# Fastest Solution (88%)
class Solution3:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            # make sure node exists
            if node:
                # check if val is less than or equal to l and greater than or equal to R
                if L <= node.val <= R:
                    # if it is, add that val to our answer
                    self.ans += node.val
                # check if node.val is greater than L
                if L < node.val:
                    # run recurisve function
                    dfs(node.left)
                # check if node.val is less than R
                if node.val < R:
                    # run recursive function
                    dfs(node.right)
        # init answer to 0
        self.ans = 0
        # run dfs on root
        dfs(root)
        # return the answer
        return self.ans
