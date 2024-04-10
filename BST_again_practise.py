## BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


## inorder Successor
def minValueNode(root):
    current = root
    while current.left != None:
        current = current.left

    return current

def inorderTrav(root):
    if root.left != None:
        inorderTrav(root.left)

    print(root.data, end=" -> ")

    if root.right != None:
        inorderTrav(root.right)

def search(root, data):
      
    if root is None or root.data == data:
        return root

    if data < root.data:
        return search(root.left, data)
    # else:
    #     return search(root.right, data)
    return search(root.right, data)


def insertNode(root, data):
    if root == None:
        return Node(data)

    if data < root.data:
        root.left = insertNode(root.left, data)

    elif data > root.data:
        root.right = insertNode(root.right, data)

    return root


def deleteNode(root, data):
    if root == None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)

    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        
        elif root.right == None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data

        root.right = deleteNode(root.right, temp.data)

    return root



root = Node(10)
root = insertNode(root, 5)
root = insertNode(root, 15)
root = insertNode(root, 25)
root = insertNode(root, 2)


inorderTrav(root)
print()

root = deleteNode(root, 15)
inorderTrav(root)
print()


if search(root, 15):
    print("\nFound: ", search(root, 15).data)

else:
    print("\nNot Found")