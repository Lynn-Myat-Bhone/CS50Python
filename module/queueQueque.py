from queue import Queue

q = Queue(maxsize=3)
print(q.qsize())
 
# Adding of element to queue
q.put('L')
q.put('M')
q.put('B')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

print("\nElements dequeued from the queue")
print(q.get())
# print(q.get())
# print(q.get())
 
# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())
