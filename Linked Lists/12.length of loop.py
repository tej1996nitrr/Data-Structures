#%%
class Node:
    def __init__(self, val): 
        self.val = val 
        self.next = None
class LinkedList:
    def __init__(self): 
        self.head = None
    def AddNode(self, val): 
        if self.head is None: 
            self.head = Node(val) 
        else: 
            curr = self.head 
            while(curr.next): 
                curr = curr.next
            curr.next = Node(val) 
    def Createloop(self,n):
        # LoopNode is the connecting node to 
        # the last node of linked list 
        LoopNode = self.head
        for _ in range(1,n):
            LoopNode=LoopNode.next
        # end is the last node of the Linked List  
        end = self.head
        while(end.next):
            end=end.next 
        end.next=LoopNode
    def detectLoop(self):
        if self.head is None:
            return 0
        slow = self.head
        fast = self.head
        flag=0
        while slow and fast and fast.next:
            if slow==fast and flag != 0:
                count=1
                slow=slow.next 
                while(slow != fast): 
                    slow = slow.next
                    count += 1
                return count 
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0
myLL = LinkedList() 
myLL.AddNode(1) 
myLL.AddNode(2) 
myLL.AddNode(3) 
myLL.AddNode(4) 
myLL.AddNode(5) 
myLL.Createloop(2) 
loopLength = myLL.detectLoop() 
if myLL.head is None: 
    print("Linked list is empty") 
else: 
    print(str(loopLength)) 
# %%

