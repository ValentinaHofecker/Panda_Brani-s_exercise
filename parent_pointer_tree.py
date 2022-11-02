#Binary tree with parent pointer

#Node class
class newNode:
    def __init__(self, item):
        self.key = item
        self.left = self.right = None
        self.parent = None


# A utility function to do in-order traversal of the tree
def inorder(root):
    if root != None:
        inorder(root.left)
        print("Node :", root.key, ", ", end="")
        if root.parent == None:
            #If the node is the root, it has no parent
            print("Parent : NULL")
        else:
            #Printing the parent of the node that is being added to the tree
            print("Parent : ", root.parent.key)
        inorder(root.right)


# A utility function to insert a new node with given key in the tree
def insert(node, key):
    # If the tree is empty, return a new Node
    if node == None:
        return newNode(key)

    # Otherwise, recur down the tree
    if key < node.key:
        lchild = insert(node.left, key)
        node.left = lchild

        # Set parent of root of left subtree
        lchild.parent = node
    elif key > node.key:
        rchild = insert(node.right, key)
        node.right = rchild

        # Set parent of root of right subtree
        rchild.parent = node

    # return the (unchanged) Node pointer
    return node


# Driver Code
if __name__ == '__main__':
    # Let us create following BST
    #         50
    #     /     \
    #     30     70
    #     / \ / \
    # 20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # print in-order traversal of the BST
    inorder(root)
