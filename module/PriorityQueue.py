import queue

pq = queue.PriorityQueue()
pq.put(2)
pq.put(10)
pq.put(1)
while not pq.empty():
    priority = pq.get()
    print(f"Processing item with priority {priority}") 