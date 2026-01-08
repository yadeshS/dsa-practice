class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self, key):
        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            temp = temp.next
            position += 1

        print("Element not found")


# Test
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.search(20)
ll.search(40)