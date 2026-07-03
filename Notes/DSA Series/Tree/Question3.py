class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)

tree = BinaryTree()

tree.inorder(root)