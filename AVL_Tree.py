
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

    def deleteNode(self, root, data):
        if root == None:
            return root

        elif data < root.data:
            root.left = self.deleteNode(root.left, data)

        elif data > root.data:
            root.right = self.deleteNode(root.right, data)

        else:
            if root.left == None:
                temp = root.right
                root = None

                return temp

            elif root.right == None:
                temp = root.left
                root = None

                return temp

            temp = self.getMinNode(root.right)
            root.data = temp.data

            root.right = self.deleteNode(root.right, temp.data)


        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)

            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)

            return self.leftRotate(root)


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

        new.left = node
        node.left = T3

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        new.height = 1 + max(self.getHeight(new.left), self.getHeight(new.right))

        return new


    ## inorderSucessor
    def getMinNode(self, root):
        while root.left != None:
            root = root.left
        print(root.data)

    def getHeight(self, node):
        if node == None:
            return 0
        return node.height

    def getBalance(self, node):
        if node == None:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)


    def Binary_Search(self, root, data):
        if root == None or root.data == data:
            return root

        elif data < root.data:
            return self.Binary_Search(root.left, data)

        else:
            return self.Binary_Search(root.right, data)

    def preorder(self, root):
        pass

    def inorderTrav(self, root):
        pass

    def postorder(self, root):
        pass

    def getSize(self, root):
        if root == None:
            return 0

        return 1 + (self.getSize(root.left) + self.getSize(root.right))


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



AVL = AVL_Tree()

root = None
# root = AVL.insertNode(root, 44)
# root = AVL.insertNode(root, 4)
# root = AVL.insertNode(root, 12)

for i in range(6):
    root = AVL.insertNode(root, i)

# print(root.data)

AVL.print_fancy(root, "", True)

search = AVL.Binary_Search(root, 5)
if search:
    print("\nFound:", search.data)


print("Total Elem:", AVL.getSize(root))

print("Total Layers:", root.height)