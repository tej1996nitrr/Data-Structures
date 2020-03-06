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
    # Returns data at given index in linked list
    def getNth(self, idx):
        current = self.head
        count = 0
        while(current):
            if(count==idx):
                return current.data
            count+=1
            current = current.next
        assert(False)
        return 0



if __name__=="__main__":
    l = LinkedList()   
    l.push(10)
    l.push(170)
    l.push(140)
    l.push(120)
    l.printList()
    print(l.getNth(0))
# %%
