
############################################################
######              Binary Tree Traversal             ######
############################################################

# Inorder, Preorder, and Postorder binary tree traversal. (Variations of DFS.)

# Assuming this data structure:
# class BSTNode():
#     def __init__(self, data=None, parent=None):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = None
# class BSTree():
#     def __init__(self):
#         self.root = None

############################################################

def inorder(root):
    def _inorder(node):
        if node:
            for node in _inorder(node.left):
                yield node
            yield node.data
            for node in _inorder(node.right):
                yield node
    traversal = [node for node in _inorder(root)]
    return traversal

def preorder(root):
    def _preorder(node):
        if node:
            yield node.data
            for node in _preorder(node.left):
                yield node
            for node in _preorder(node.right):
                yield node
    traversal = [node for node in _preorder(root)]
    return traversal

def postorder(root):
    def _postorder(node):
        if node:
            for node in _postorder(node.left):
                yield node
            for node in _postorder(node.right):
                yield node
            yield node.data
    traversal = [node for node in _postorder(root)]
    return traversal

