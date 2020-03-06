#%%

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def countNode(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count
    def countRecurr(self,node):
        if not node:
            return 0
        else: return 1+ self.countRecurr(node.next)
    def getCountRecurr(self):
        return self.countRecurr(self.head)


if __name__=="__main__":
    l = LinkedList()
    l.head  = Node(1)
    second = Node(2) 
    third = Node(3) 
    l.head.next = second
    second.next = third
    l.printList()
    print(l.countNode())
    print(l.getCountRecurr())

# %%
