from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(5)

print("Deque:", dq)

print("Removed from left:", dq.popleft())
print("Removed from right:", dq.pop())

print("Final Deque:", dq)