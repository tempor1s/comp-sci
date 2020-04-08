class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    # Base Case
    if root is None:
        return None

    # If either v1 or v2 matches with roots value, report
    # the presence by returning root (Note that if a key is
    # ancestor of other, then the ancestor key becomes LCA)
    if root.info == v1 or root.info == v2:
        return root

    # Look for keys in left and right subtrees
    left_lca = lca(root.left, v1, v2)
    right_lca = lca(root.right, v1, v2)

    # If both of the above valls return Non-None, then one key
    # is present in once subtree and the other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

