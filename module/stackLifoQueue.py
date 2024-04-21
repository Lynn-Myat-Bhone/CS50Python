from queue import LifoQueue

stack = LifoQueue(maxsize=3)
# put() function to push
stack.put('L')
stack.put('M')
stack.put('B')
print(f"Full : {stack.full()}") # check  list is full size
print(f"Size : {stack.qsize()}")# check list size

# get() function to pop
print(f"POP element : {stack.get()}")
print(f"list : {stack}")


