class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def insertNode(self, root, data):
        if root == None:
            return TNode(data)

        elif data < root.data:
            root.left = self.insertNode(root.left, data)

        elif data > root.data:
            root.right = self.insertNode(root.right, data)

        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)



        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)

        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)

        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)

            return self.rightRotate(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)

            return self.leftRotate(root)


        return root


    def leftRotate(self, node):
        new = node.right
        T2 = new.left

        new.left = node
        node.right = T2

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        new.height = 1 + max(self.getHeight(new.left), self.getHeight(new.right))

        return new

    def rightRotate(self, node):
        new = node.left
        T3 = new.right

        new.right = node
        node.left = T3

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        new.height = 1 + max(self.getHeight(new.left), self.getHeight(new.right))

        return new

    def getHeight(self, node):
        if node == None:
            return 0

        return node.height

    def getBalance(self, node):
        if node == None:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)


    def inOrderTrav(self, root):
        if root != None:
            self.inOrderTrav(root.left)

            print(root.data, end=" -> ")

            self.inOrderTrav(root.right)

    def print_fancy(self, root, indent, last):
        if root != None:
            print(indent, end="")

            if last:
                print("R---", end="")
                indent += "    "

            else:
                print("L---", end="")
                indent += "|   "
            
            print(root.data)

            self.print_fancy(root.left, indent, last=False)
            self.print_fancy(root.right, indent, last=True)


Tree = AVL_Tree()

root = None

for el in range(200, -1, -1):
    root = Tree.insertNode(root, el)

Tree.inOrderTrav(root)
print("\n")

print("root:", root.data, "\n")

Tree.print_fancy(root, "", True)