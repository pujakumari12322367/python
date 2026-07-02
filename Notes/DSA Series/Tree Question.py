class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            return

        current = self.root

        while True: 
            if data < current.data:
                if current.left is None:
                    current.left = newNode
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    break
                else:
                    current = current.right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

tree = BinaryTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Inorder Traversal:")
tree.inorder(tree.root)

