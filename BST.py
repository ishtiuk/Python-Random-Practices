class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root.left:
        inorder(root.left)

    print(root.data, end=" -> ")

    if root.right:
        inorder(root.right)

def search(root, data):
    if root == None or data == root.data:
        return root

    if data < root.data:
        return search(root.left, data)

    elif data > root.data:
        return search(root.right, data)


## Inorder Successor
def minValueNode(node):
    current = node

    while node.left != None:
        current = current.left
    return current


def insertNode(node, data):
    if node == None:
        return Node(data)

    if data < node.data:
        node.left = insertNode(node.left, data)

    elif data > node.data:
        node.right = insertNode(node.right, data)

    return node


def deleteNode(root, data):
    if root == None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)

    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:                     ## this means "data == root.data"
        if root.left == None:
            temp = root.right
            root = None
            return temp

        elif root.right == None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)          ## getting Right Inorder Sucessor

        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root


root = None
root = insertNode(root, 6)
root = insertNode(root, 8)
root = insertNode(root, 3)
root = insertNode(root, 10)
root = insertNode(root, 2)

inorder(root)
print()

deleteNode(root, 6)

inorder(root)

if search(root, 10):
    print("\n\nfound")
else:
    print("\n\nnot found")