class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print_stack()  # Выводит: 3 2 1

print(stack.peek())  # Выводит: 3

print(stack.pop())   # Выводит: 3
print(stack.pop())   # Выводит: 2

stack.print_stack()  # Выводит: 1
