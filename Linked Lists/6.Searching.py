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

    def search(self,what):
        current = self.head
        while current is not None:
            if current.data==what:
                return True
            current = current.next
        return False

if __name__=="__main__":
    l = LinkedList()   
    l.push(10)
    l.push(170)
    l.push(140)
    l.push(120)
    l.printList()
    print(l.search(10))
# %%
