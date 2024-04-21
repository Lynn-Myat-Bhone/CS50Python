class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # initialize as null 
        #this is because at the time of creating a node, we might not necessarily know what the next node in the linked list will be.

class linklist:
    def __init__(self): # initialize the first node
        self.head = None
    #tranverse list
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':
    a= linklist()
    a.head = Node(1)
    second = Node(2)
    third = Node(3)
    # after create node, lets link
    a.head.next = second
    second.next = third
    a.printlist()