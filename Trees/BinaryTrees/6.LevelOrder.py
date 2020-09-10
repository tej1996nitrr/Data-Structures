class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 

def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.data,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 