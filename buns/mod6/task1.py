class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        if current is None:
            return None
        return current.data

    def remove(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                return
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n <= 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(n - 1):
                if current.next is None:
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item
