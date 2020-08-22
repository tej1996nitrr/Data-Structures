#%%
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def update(root):
    if not root:
        return 0

    if root.left is None and root.right is None:
        return root.data
    leftsum = update(root.left)
    rightsum = update(root.right)

    root.data += leftsum
    root.data += rightsum

    return root.data

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)  

root = Node(10)  
root.left = Node(5)  
root.right = Node(15)  
root.left.left = Node(1)  
root.left.right = Node(7)  
root.right.right = Node(20)
root.right.left = Node(11)  
root.right.left.right = Node(12)  


update(root)  
print("Inorder traversal")  
inorder(root) 


# %%
