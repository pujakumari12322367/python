from collections import deque

# Create an empty deque
dq = deque()

# Insert elements
dq.append(10)       # Insert at rear
dq.append(20)
dq.appendleft(5)    # Insert at front

# Display deque
print("Deque:", dq)