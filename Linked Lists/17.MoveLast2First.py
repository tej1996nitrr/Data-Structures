#%%
class Node:     
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, new_data): 
        new_Node = Node(new_data) 
        new_Node.next = self.head  
        self.head = new_Node 

    def printList(self): 
        tNode = self.head 
        while tNode != None: 
            print (tNode.data)
            tNode = tNode.next
    def  moveFront(self):
        temp  = self.head
        sec_last = None
        if not temp or not temp.next:
            return
        while temp and temp.next:
            sec_last=temp
            temp=temp.next
        sec_last.next = None
        print("....",sec_last.data)
        temp.next = self.head #the last node as the first Node 
        self.head = temp
         
llist = LinkedList() 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
print ("Linked List before moving last to front ") 
llist.printList() 
llist.moveFront() 
print ("Linked List after moving last to front ") 
llist.printList() 
                

# %%


# %%
