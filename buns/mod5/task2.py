class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def print_queue(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Пример использования
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue() # 1 2 3
q.dequeue()
q.print_queue() # 2 3
print(q.peek()) # 2
print(q.is_empty()) # False
q.dequeue()
q.dequeue()
print(q.is_empty()) # True
