'''Reverse Level Order Traversal'''
#%%
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level>1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, 1+h)):
        printGivenLevel(root, i)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
reverseLevelOrder(root)



# %%
'''Using Stack, Queue'''
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverseOrder(root):
    q = deque()
    q.append(root)
    ans = deque()
    
    while q:
        node = q.popleft()
        if node is None:
            continue
        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)
             
        if node.left:
            q.append(node.left)
    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverseOrder(root)

    

# %%
