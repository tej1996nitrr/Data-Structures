class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_Node = Node(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def printList(self):
        tNode = self.head
        while tNode != None:
            print(tNode.data)
            tNode = tNode.next


