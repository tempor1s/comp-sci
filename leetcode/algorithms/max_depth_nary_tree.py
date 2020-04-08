class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        def max_depth(node):
            if not node:
                return 0
            next_depth = 0
            for node in node.children:
                next_depth = max(next_depth, max_depth(node))
            return next_depth + 1

        return max_depth(root)
