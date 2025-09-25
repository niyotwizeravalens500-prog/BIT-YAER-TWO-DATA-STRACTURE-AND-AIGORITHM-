# Push elements onto the stack,"UR pushes["TopicX", "TopicY", "TopicZ"]
stack = []
stack.append("TopicX")
stack.append("TopicY")
stack.append("TopicZ")

# ***** Undo one (pop)******
stack.pop()

# Which is top?
print("Top of stack:", stack[-1])  

# -----Push elements onto the stack-----
stack = []
stack.append("StepX")
stack.append("StepY")
stack.append("StepZ")

# $$$$$ Undo all (pop all)-----
stack.pop()
stack.pop()
stack.pop()

# Which remains?
print("Stack after undo all:", stack)  

# Step 1: ==========Start with an empty stack,===========
stack = []


# Step 2: Push "A", "B", "C", "D"
stack.append("A")  # Stack: ["A"]
stack.append("B")  # Stack: ["A", "B"]
stack.append("C")  # Stack: ["A", "B", "C"]
stack.append("D")  # Stack: ["A", "B", "C", "D"]

# Step 3: Pop 3 elements==========***
stack.pop()        # Removes "D" -> ["A", "B", "C"]
stack.pop()        # Removes "C" -> ["A", "B"]
stack.pop()        # Removes "B" -> ["A"]

# Step 4: Push "E"
stack.append("E")  # Stack: ["A", "E"]

# Step 5: Which is top?
print("Top of stack:", stack[-1]) 

#why stack is limited  for Serving Clients===========

print("When serving clients, typically you want First-Come-First-Served (FCFS) order. That is, the first person who arrives should be served first")

# queue
from collections import deque

# 9 buses queue at Nyabugogo
buses = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5", "Bus6", "Bus7", "Bus8", "Bus9"])

# 4 buses depart (pop from front)
for _ in range(4):
    buses.popleft()

# Front bus
print("Front bus:", buses[0])

from collections import deque

# Create a queue of clients
clients = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7", "Client8"])

# Who is third in line?
third_client = list(clients)[2]  # index 2 = third position
print("The third client is:", third_client)

# Using Queue
medicine_queue = deque(["Med1", "Med2", "Med3"])
print("Queue order:", list(medicine_queue))
print("Serve first:", medicine_queue.popleft())  # FIFO


#FIFO SUPPORT FAIR
print("FIFO ensures fairness: the first person in line is the first to be served, preventing any bias or favoritism.")





      




