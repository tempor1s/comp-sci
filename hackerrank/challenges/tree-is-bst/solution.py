""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
temp = []
def checkBST(root):
    if root is None:
        return True

    if root.left:
        checkBST(root.left)
    temp.append(root.data)
    if root.right:
        checkBST(root.right)

    tmp = 0
    for val in temp:
        if val > tmp:
            tmp = val
        else:
            return False
    return True

# INT_MAX = 4294967296
# INT_MIN = -4294967296
# def checkBST(root):
#     return isBSTUtil(root, INT_MIN, INT_MAX)

# def isBSTUtil(node, mini, maxi):
#     if node is None:
#         return True

#     if node.data < mini or node.data > maxi:
#         return False

#     return isBSTUtil(node.left, mini, node.data - 1) and isBSTUtil(node.right, node.data + 1, maxi)

