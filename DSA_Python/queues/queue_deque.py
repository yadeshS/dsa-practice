from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()   # deque is perfect for queue operations

    def enqueue(self, x):
        self.q.append(x)   # add to the back

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.popleft()  # remove from the front

    def front(self):
        if self.is_empty():
            return None
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)


# Test
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Front:", q.front())     # A
print("Dequeue:", q.dequeue()) # A
print("Front:", q.front())     # B
print("Size:", q.size())       # 2