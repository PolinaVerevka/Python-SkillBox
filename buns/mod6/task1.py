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
            while current.next:
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
        for i in range(index-1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(n-1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)

print(linked_list.get(0))  # Output: 1
print(linked_list.get(1))  # Output: 2
print(linked_list.get(2))  # Output: 3

linked_list.insert(1, 4)
print(list(linked_list))  # Output: [1, 4, 2, 3]

linked_list.remove(2)
print(list(linked_list))  # Output: [1, 4, 3]
