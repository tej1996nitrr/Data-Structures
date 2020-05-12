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
    
    def getlength(self):
        temp = self.head
        length=0
        while temp:
            length+=1
            temp=temp.next
        return length

    def getNthEnd(self,idx):
        """Time: O(n) where n is the length of linked list."""
        current=self.head
        count=0
        length = self.getlength()
        while(current):
            if(count==length-idx):
                return current.data 
            count+=1
            current=current.next 
        assert(False)
        return "Not Found"


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
    
    def NthLastUsingDoublePointer(self,n):
        """Use two pointers
        Time Complexity: O(n) where n is the length of linked list."""
        main_ptr = self.head
        ref_ptr = self.head
        count=0
        if self.head is not None:
            while count<n:
                if ref_ptr is None:
                    print (f"{n} is greater than the no. of nodes in list" ) 
                    return
                ref_ptr = ref_ptr.next
                count+=1
        while(ref_ptr is not None): 
            main_ptr = main_ptr.next 
            ref_ptr = ref_ptr.next
        print (f"Node no. {n} from last is {main_ptr.data}") 
  

if __name__=="__main__":
    l = LinkedList()   
    l.push(10)
    l.push(170)
    l.push(140)
    l.push(120)
    # l.printList()
    print(l.getNthEnd(2))

# %%

# %%
