class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)

tree = BinaryTree()

print("Total Nodes:", tree.countNodes(root))