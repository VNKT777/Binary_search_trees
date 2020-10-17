class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.val = val

def newnode(node,val):
    if (node.val < val):
        print(node.val)
        if(node.right == None):
            node.right = Node(val)
        else:
            node = node.right
            newnode(node,val)
    else:
        print(node.val)
        if(node.left == None):
            node.left = Node(val)
        else:
            node = node.left
            newnode(node,val)
def preorder(node):
    if(node == None):
        return
    else:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
        
def inorder(node):
    if(node == None):
        return
    else:
        inorder(node.left)
        print(node.val)
        inorder(node.right)
        
def  postorder(node):
    if(node == None):
        return
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.val)




root = Node(77)
ch = 1
choice = "y"
while(choice == "y"):
    opt = int(input("1 - ADD | 2 - Preorder Traverse|3 - Inorder Travesral|4 -  PostOrder Traversal"))
    if (opt == 1):
        val = int(input("Enter The Value of The Node >>>"))
        newnode(root,val)
    elif(opt == 2):
        preorder(root)
    elif(opt == 3):
        inorder(root)
    elif(opt == 4):
        postorder(root)
    choice = input("Enter y to continue >>>")
    
