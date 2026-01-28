class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)          # add to top

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()       # remove from top

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]         # see top element

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())     # 30
print("Pop:", s.pop())      # 30
print("Top:", s.peek())     # 20
print("Size:", s.size())    # 2