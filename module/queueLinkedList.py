class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear= None
    
    def isEmpty(self):
        return self.front == 0
    
    def Enqueue(self,item):
        temp = Node(item)
        if self.rear== None:
            self.front = temp
            self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    
    def Dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        
        if(self.front == None):
            self.rear == None
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
              
            
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)
    print("Original Queue:")
    q.display()
    q.Dequeue()
    print("\nUpdated Queue:")
    q.display()
