from collections import deque
# implemented using linked lists in background. Used for optimized push pop operations.

dq = deque([1, 2, 3, 4, 5])
print('original dq', dq, '\n')

# All these operations are O(1)
dq.append(6)
print('append right', dq, '\n')

dq.pop()
print('pop right', dq, '\n')

dq.appendleft(0)
print('append left', dq, '\n')

dq.popleft()
print('pop left', dq, '\n')

# deque is used to implement stacks and queues

# FIFO (first in first out) is implemented here
print("Stack FIFO: ")
stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

while len(stack) > 0:
    element = stack.pop()
    print(element)
print('\n')

# LIFO (last in first out) is implemented here
print("Queue LIFO: ")
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

while len(queue) > 0:
    element = queue.popleft()
    print(element)
