from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(5)

print("Deque:", dq)

print("Removed from left:", dq.popleft())
print("Removed from right:", dq.pop())

print("Final Deque:", dq)





stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek
print("Top element:", stack[-1])

# Pop
print("Removed:", stack.pop())

print("Final Stack:", stack)




# Create an empty stack
stack = []

# Insert (Push) elements
stack.append(10)
stack.append(20)
stack.append(30)

# Display stack
print("Stack:", stack)