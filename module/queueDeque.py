from collections import deque
queue = deque()
#add
queue.append('L')
queue.append('M')
queue.append('B')
#delete
queue.popleft()
print(queue)