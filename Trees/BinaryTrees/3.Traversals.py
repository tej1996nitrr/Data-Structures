#%%
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def printTreePreorder(root):
    if root:
        print(root.value)
        printTreeInorder(root.left)
        printTreeInorder(root.right)  

def printTreeInorder(root):
    if root:
        printTreeInorder(root.left)
        print(root.value)
        printTreeInorder(root.right)
      
def printTreePostorder(root):
    if root:
        printTreeInorder(root.left)
        printTreeInorder(root.right)  
        print(root.value)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print("Inorder")
printTreeInorder(root)
print("Preorder")
printTreePreorder(root)
print("Postorder")
printTreePostorder(root)
# %%
