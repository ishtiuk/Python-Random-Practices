
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_TREE:
    def insertNode(self, root, data):
        if root == None:
            return Node(data)

        elif data < root.data:
            root.left = self.insertNode(root.left, data)

        elif data > root.data:
            root.right = self.insertNode(root.right, data)


        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        BF = self.getBalance(root)
        
        if BF > 1  and data < root.left.data:
            return self.rightRotate(root)

        if BF < -1  and data > root.right.data:
            return self.leftRotate(root)

        if BF > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            
            return self.rightRotate(root)

        if BF < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)

            return self.leftRotate(root)

        return root

    
    def deleteNode(self, root, data):
        if root == None:
            return root

        if data < root.data:
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

            temp = self.getMinValueNode(root.right)
            root.data = temp.data

            root.right = self.deleteNode(root.right, temp.data)

        if root == None:
            return root

        ## Re-Balancing:
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

        return root


    def binary_search(self, root, data):
        if root == None or data == root.data:
            return root

        if data < root.data:
            return self.binary_search(root.left, data)
        else:
            return self.binary_search(root.right, data)

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
        

    def getHeight(self, root):
        if root == None:
            return 0

        return root.height

    def getBalance(self, root):
        if root == None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)


    def inorderPrint(self, root):
        if root.left != None:
            self.inorderPrint(root.left)

        print(root.data, end=" -> ")

        if root.right != None:
            self.inorderPrint(root.right)


    def getMinValueNode(self, node):
        if node.left == None:
            return node

        return self.minValueNode(node.left)

    ## NOTE: works the same thing:

    # def minValueNode(self, node):
    #     current = node

    #     while current.left != None:
    #         current = current.left
    #     return current



my_AVL = AVL_TREE()

root = None
root = my_AVL.insertNode(root, 9)
root = my_AVL.insertNode(root, 20)
root = my_AVL.insertNode(root, 8)
root = my_AVL.insertNode(root, 2)


my_AVL.inorderPrint(root)
print()

root = my_AVL.deleteNode(root, 9)
print()

my_AVL.inorderPrint(root)

