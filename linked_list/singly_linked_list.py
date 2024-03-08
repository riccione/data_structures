"""
Singly linked list: simple implementation

Inspired by William Fiset
https://github.com/williamfiset/
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

    def size(self):
        return self.len

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        sx = ""
        if not self.is_empty():
            current = self.head
            while current:
                sx += f"{current.val}->"
                current = current.next
        sx += "None"
        return sx

    def __repr__(self):
        return self.__str__()

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
        if self.is_empty():
            raise ValueError("Empty list")
        rval = self.tail.val
        current = self.head
        while current.next.next:
            current = current.next
        self.tail = current
        current.next = None
        self.len -= 1
        return rval

    def pop_front(self):
        if self.is_empty():
            raise ValueError("Empty list")
        rval = self.head.val
        new_head = self.head.next
        self.head = new_head
        self.len -= 1
        return rval

    def remove(self, value):
        if self.is_empty():
            raise ValueError("Empty list")
        if self.head.val == value:
            return self.pop_front()
        elif self.tail.val == value:
            return self.pop_back()
        else:
            curr = self.head
            while curr.next:
                if curr.next.val == value:
                    break
                curr = curr.next
            if curr.next and curr.next.val == value:
                if curr.next.next:
                    curr = curr.next.next
                    self.len -= 1
                    return value
                """
                else:
                    return self.pop_back()
                """
            else:
                return None

    # remove at certain index
    def remove_at(self, index):
        if self.is_empty():
            raise ValueError("Empty list")
        if index == 0:
            return self.pop_front()
        elif index == self.size() - 1:
            return self.pop_back()
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            rval = curr.next.val
            curr.next = curr.next.next
            self.len -= 1
            return rval

    def peek_first(self):
        if self.is_empty():
            raise ValueError("Empty list")
        return self.head.val

    def peek_last(self):
        if self.is_empty():
            raise ValueError("Empty list")
        return self.tail.val

    def push(self, index, value):
        if index < 0 or index > self.size():
            raise ValueError("Illegal index")
        if index == 0:
            self.push_front(value)
        elif index == self.size():
            self.push_back(value)
        else:
            tmp = self.head
            for i in range(index - 1):
                tmp = tmp.next
            tmp_next = tmp.next
            new_node = Node(value)
            tmp.next = new_node
            new_node.next = tmp_next
            self.len += 1

    def index_of(self, v):
        if self.is_empty():
            raise ValueError("Empty list")
        curr = self.head
        i = 0
        while curr:
            if curr.val == v:
                return i
            curr = curr.next
            i += 1


list = LinkedList()

print(list)
list.push_back(1)
list.push_back(2)
list.push_back(3)
list.push_back(4)
print(list)
list.remove(100)
print(list)
"""
list.push(1, 10)
print(list)
list.remove_at(1)
print(list)
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
list.push_back(102)
list.push_back(103)
list.push_back(104)
print(list)
list.push_front(99)
print(list)
print(f"pop_back: {list.pop_back()}")
print(list)
print(list.head.val, list.tail.val)
print(f"pop_front: {list.pop_front()}")
print(list)
print(f"Head: {list.head.val}, tail: {list.tail.val}")
"""
