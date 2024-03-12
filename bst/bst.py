"""
Binary Search Tree (BST)

Inspired by William Fiset
https://github.com/williamfiset/
"""
from enum import Enum
import queue
import sys

sys.path.append("../utils")
from tree_printer import TreePrinter


class Order(Enum):
    PRE_ORDER = 0
    IN_ORDER = 1
    POST_ORDER = 2
    LEVEL_ORDER = 3


class Node:
    def __init__(self, left, right, el):
        self.value = el
        self.left = left
        self.right = right


class BinarySearchTree:
    root: Node = None
    node_count = 0

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return self.node_count

    def add(self, el) -> bool:
        # returns Node
        # recursion
        def add_node(node, el):
            # special case for root node
            if self.root is None:
                self.root = Node(None, None, el)
                node = self.root
                return node
            # found a leaf Node, leaf Node is None
            if node is None:
                node = Node(None, None, el)
            else:
                # comparator < 0
                if el < node.value:
                    node.left = add_node(node.left, el)
                else:
                    node.right = add_node(node.right, el)
            return node

        if self.contains(el):
            return False
        else:
            self.root = add_node(self.root, el)
            self.node_count += 1
            return True

    # !!not safe fn to use - only to validate tree traversal
    # I need to use this fn, because this tree implementation is not
    # self-balanced and it is easy to get a tree like
    # 1
    # \
    # 2
    # \
    # 3 ...
    def _add(self, node, el, branch=None):
        if branch == "left":
            node.left = Node(None, None, el)
        else:
            node.right = Node(None, None, el)
        self.node_count += 1
        return node

    # remove a value from BST O(n)
    def remove(self, el) -> bool:
        if self.contains(el):
            self.root = self.remove_node(self.root, el)
            self.node_count -= 1
            return True
        return False

    def remove_node(self, node, el):
        if node is None:
            return None

        if el < node.value:  # < 0
            node.left = self.remove_node(node.left, el)
        elif el > node.value:
            node.right = self.remove_node(node.right, el)
        else:
            # only a right subtree
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # get the smallest node from right subtree
                tmp = self.find_min(node.right)
                # swap the value
                node.value = tmp.value
                node.right = self.remove_node(node.right, tmp.value)

                # get the largest node from left subtree
                # tmp = self.find_max(node.left)
                # node.value = tmp.value
                # node.left = self.remove_node(node.left, tmp.value)

        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    # need 2 fn due to the recursion
    def contains(self, el) -> bool:
        return self.contains_node(self.root, el)

    def contains_node(self, node, el) -> bool:
        if node is None:
            return False

        if el < node.value:
            return self.contains_node(node.left, el)
        elif el > node.value:
            return self.contains_node(node.right, el)
        else:
            return True

    def height(self) -> int:
        def h(node) -> int:
            if node is None:
                return 0
            return max(h(node.left), h(node.right)) + 1

        return h(self.root)

    def traverse(self, node, order):
        print(f"{order.name}: ", end="")

        def rt(node, order):
            if node is None:
                return None
            if order is Order.PRE_ORDER:  # pre_order_traversal
                print(f"{node.value}", end=" ")
                rt(node.left, Order.PRE_ORDER)
                rt(node.right, Order.PRE_ORDER)
            elif order is Order.IN_ORDER:  # in_order_traversal
                rt(node.left, Order.IN_ORDER)
                print(f"{node.value}", end=" ")
                rt(node.right, Order.IN_ORDER)
            elif order is Order.POST_ORDER:  # post_order_traversal
                rt(node.left, Order.POST_ORDER)
                rt(node.right, Order.POST_ORDER)
                print(f"{node.value}", end=" ")
            else:  # level_order
                self.level_order_traversal(node)

        rt(node, order)
        print()

    def level_order_traversal(self, node):
        # Breadth First Search
        q = queue.Queue()
        q.put(node)
        while node is not None and not q.empty():
            node = q.get()
            print(node.value, end=" ")
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def iter_pre(self, node, order):
        print(f"{order.name}: ", end="")
        stack = queue.LifoQueue()
        stack.put(node)
        while node is not None and not stack.empty():
            node = stack.get()
            # print(node.value, end=" ")
            yield node.value
            if node.right is not None:
                stack.put(node.right)
            if node.left is not None:
                stack.put(node.left)

    def iter_in(self, node, order):
        print(f"{order.name}: ", end="")
        stack = queue.LifoQueue()
        stack.put(node)
        trav = node
        while node is not None and not stack.empty():
            # left tree
            while trav is not None and trav.left is not None:
                stack.put(trav.left)
                trav = trav.left

            node = stack.get()

            if node.right is not None:
                stack.put(node.right)
                trav = node.right

            yield node.value

    def iter_post(self, node, order):
        print(f"{order.name}: ", end="")
        stack1 = []
        stack2 = []
        stack1.append(node)
        while len(stack1) > 0:
            node = stack1.pop()
            if node is not None:
                stack2.append(node)
                if node.left is not None:
                    stack1.append(node.left)
                if node.right is not None:
                    stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            yield node.value

    def __str__(self):
        if self.root is None:
            return "Tree is empty"
        return TreePrinter.display(self.root)

    def __repr__(self):
        return self.__str__()


bst = BinarySearchTree()
bst.add(11)
bst.add(6)
bst.add(15)
bst.add(3)
bst.add(8)
bst.add(13)
bst.add(17)
bst.add(1)
bst.add(5)
bst.add(12)
bst.add(14)
bst.add(19)
print(bst.root.value)
print(bst.node_count)
print(bst.height())
print(bst.contains(6))
print(bst.contains_node(bst.root, 6))
bst.traverse(bst.root, Order.PRE_ORDER)

for c in bst.iter_pre(bst.root, Order.PRE_ORDER):
    print(c, end=" ")
print()

bst.traverse(bst.root, Order.IN_ORDER)

for c in bst.iter_in(bst.root, Order.IN_ORDER):
    print(c, end=" ")
print()

bst.traverse(bst.root, Order.POST_ORDER)

xs = bst.iter_post(bst.root, Order.POST_ORDER)
for c in xs:
    print(c, end=" ")
print()

bst.traverse(bst.root, Order.LEVEL_ORDER)
print(bst.root.value)
print(bst.contains_node(bst.root, 6))
print(bst.contains(6))
bst.remove(6)
bst.traverse(bst.root, Order.IN_ORDER)
print(bst)
x = BinarySearchTree()
x.add(8)
x._add(x.root, 3, "left")
x._add(x.root.left, 1, "left")
x._add(x.root.left, 6, "right")
x._add(x.root, 10, "right")
x._add(x.root.right, 9, "left")
x._add(x.root.right, 14, "right")
print(x)
