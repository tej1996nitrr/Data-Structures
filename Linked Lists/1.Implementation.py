#%%
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

if __name__=="__main__":
    l = LinkedList()
    l.head  = Node(1)
    second = Node(2) 
    third = Node(3) 
    l.head.next = second
    second.next = third


# %%
