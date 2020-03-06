#%%
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def push(self,data):
        ''' Insertion of data at beginning of LL'''
        new_node =  Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next    

    def insertAfter(self,prev_node,data):
        ''' Insertion after a given node'''
        if prev_node is None:
            print("Previous Node is None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,data):
        '''Insertion at the end of LL'''
        new_node = Node(data)
        if self.head is None:
            self.head =new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node

if __name__=="__main__":
    l = LinkedList()
    l.head  = Node(1)
    second = Node(2) 
    third = Node(3) 
    l.head.next = second
    second.next = third
    l.append(6) 
    l.push(10)
    l.insertAfter(l.head.next, 8) 
    l.printList()
# %%
