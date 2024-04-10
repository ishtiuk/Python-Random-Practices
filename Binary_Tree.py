## Binary Tree Architechture

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()

        print(self.data, end=" >> ")

        if self.right:
            self.right.inorderTraversal()

    def preorderTraversal(self):
        print(self.data, end=" >> ")

        if self.left:
            self.left.preorderTraversal()

        if self.right:
            self.right.preorderTraversal()

    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()

        if self.right:
            self.right.postorderTraversal()

        print(self.data, end=" >> ")

    def checkFullBinary(self):
        if self == None:
            return True
        
        if self.left == None and self.right == None:
            return True

        if self.left and self.right:
            return self.left.checkFullBinary() and self.right.checkFullBinary()

        return False

    

        


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(6)
# root.left.right = Node(7)

print("Inorder: ", end=' ')
root.inorderTraversal()

print("\nPreorder: ", end=' ')
root.preorderTraversal()

print("\nPostorder: ", end=' ')
root.postorderTraversal()


if root.checkFullBinary():
    print("\n\n[Full Binary Tree]")
else:
    print("\n\n[Not a Full Binary Tree]")
