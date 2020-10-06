'''Find all possible binary trees with given Inorder Traversal'''

class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

def preOrder(root):
    if root is not None:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

'''Constructing all possible trees with given inorder traveral.
 given inorder traversal stored in an array from 
 arr[start] to arr[end]. The function returns a 
 vector of trees
 '''
def getTree(arr, start, end):

     #list to store all possible trees
    trees = []
    if start>end:
        trees.append(None)
        return trees
    
    for i in range(start, end+1):
        left_sub_trees = getTree(arr, start, i-1)
        right_sub_trees  = getTree(arr, i+1, end)
        for j in left_sub_trees:
            for k in right_sub_trees:

                # Making arr[i]  as root
                node = Node(arr[i])

                #connecting left subtree
                node.left = j
                #connecting right subtree
                node.right = k

                #adding this tree to list
                trees.append(node)
    return trees
inp = [4 , 5, 7] 
n = len(inp) 
  
trees = getTree(inp , 0 , n-1) 
  
print ("Preorder traversals of different possible Binary Trees are " )
for i in trees : 
    preorder(i); 
    print ("" ) 
                
