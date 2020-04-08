# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# my solution
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(node, val):
            if node:
                if val == node.val:
                    return node
                elif val < node.val:
                    return search(node.left, val)
                elif node.val < val:
                    return search(node.right, val)
            return None

        return search(root, val)


# cleaned up
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
