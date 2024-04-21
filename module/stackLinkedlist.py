class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    # tranverse
    def __str__(self):
        curr = self.head
        out =""
        while curr :
            out =str(curr.data) + " "+ out
            curr = curr.next
        
        return out
            
    
    def isEmpty(self):
        return self.head == None
    
    def peek(self):
        if self.isEmpty():
            raise Exception ("Peeking from empty stack")
        return self.head.next.data
    
    def push(self, data):
 
        if self.head == None:
            self.head = Node(data)
 
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        self.size +=1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot Pop from Empty Stack")
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.data

if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(f"Original Stack: {stack}")
    stack.pop()
    
    print(f"Stack: {stack}")
    
    print(f"Peek:{stack.peek()}")
        