
############################################################
#####           Binary Search Tree                     #####
############################################################


class BSTNode():
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BSTree():
    def __init__(self):
        self.root = None

    def add(self, data):
        def _add(node, data):
            if node.data > data:
                if node.left:
                    _add(node.left, data)
                else:
                    node.left = BSTNode(data, node.left)
            else:
                if node.right:
                    _add(node.right, data)
                else:
                    node.right = BSTNode(data, node.right)

        if self.root:
            self._add(self.root, data)
        else:
            self.root = BSTNode(data)


    def delete(self, key):
        def _delete(node, key):
            if node.data == key:
                if node.left and node.right:
                    successor = self.successor(node.right)

                    if successor.parent.left == successor:
                        successor.parent.left = successor.right
                    else:
                        successor.parent.left = successor.left

                    successor.left = node.left
                    successor.right = node.right
                    return successor
                else:
                    if node.left:
                        return node.left
                    else:
                        return node.right
            else:
                if node.data > key:
                    if node.left:
                        node.left = _delete(node.left, key)
                else:
                    if node.right:
                        node.right = _delete(node.right, key)
            return node

        if self.root.data == key:
            self.root = _delete(self.root, key)
        else:
            _delete(self.root, key)

#### Helper Functions

    def successor(self, node):
        if node.right:
            successor =  self.find_min(node.right)
        else:
            if node.parent:
                if node.parent.data > node.data:
                    successor = node.parent
                else:
                    successor = None
        return successor

    def predecessor(self, node):
        if node.left:
            predecessor = self.find_max(node.left)
        else:
            predecessor = None
        return predecessor

    def find_min(self, node):
        minimum = node
        while node.left:
            minimum = node.left
        return minimum

    def find_max(self, node):
        maximum = node
        while node.right:
            maximum = node.right
        return maximum
