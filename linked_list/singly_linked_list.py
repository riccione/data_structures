"""
Singly linked list: simple implementation
"""
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def printl(self):
        if not self.is_empty():
            current = self.head
            while(current):
                print(f"{current.val}->", end="")
                current = current.next
        print("None")

    def push_back(self, val):
        if self.is_empty():
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val)
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        self.len += 1

    def push_front(self, val):
        if self.is_empty():
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.len += 1

    def pop_back(self):
        rval = self.tail.val
        current = self.head
        while(current.next.next):
            current = current.next
        self.tail = current
        current.next = None
        self.len -= 1
        return rval

    def pop_front(self):
        rval = self.head.val
        new_head = self.head.next
        self.head = new_head
        self.len -= 1
        return rval


list = LinkedList()

list.printl()
"""
l1 = Node(100)
list.len += 1
list.head = l1
l2 = Node(101)
l1.next = l2
l3 = Node(102)
l2.next = l3
l4 = Node(103)
l3.next = l4
list.tail = l4
list.printl()
"""
list.push_back(102)
list.push_back(103)
list.push_back(104)
list.printl()
list.push_front(99)
list.printl()
print(f"pop_back: {list.pop_back()}")
list.printl()
print(list.head.val, list.tail.val)
print(f"pop_front: {list.pop_front()}")
list.printl()
print(f"Head: {list.head.val}, tail: {list.tail.val}")
