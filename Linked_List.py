class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        if self.is_empty():
            return False
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next
        return False

    def get(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        raise IndexError("Index out of range")

    def print_list(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
        self.tail = None

    def to_list(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values