class Stack:
    def __init__(self):
        self.item= []
    def push(self,item):
        self.item.append(item)
    def pop (self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Cannot pop from empty stack")
    def is_empty(self):
        return len(self.item)==0
    
    def display(self):
        print(self.item)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)
stack.display()