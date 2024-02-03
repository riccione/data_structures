"""
AVL Tree

Inspired by William Fiset
https://github.com/williamfiset/
"""
from tree_printer import TreePrinter


class AVLTreeRecursive:
    class Node:
        def __init__(self, value):
            self.value = value
            self.bf = 0  # balance factor
            self.height = 1
            self.left = None
            self.right = None

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_text(self):
            return str(self.value)

    def __init__(self):
        self.root = None
        self.node_count = 0

    def height(self) -> int:
        return self.root.height if self.root else 0

    def size(self) -> int:
        return self.node_count

    def is_empty(self) -> bool:
        return self.size() == 0

    def contains(self, value) -> bool:
        return self._contains(self.root, value)

    def _contains(self, node, value) -> bool:
        if node is None:
            return False

        if value < node.value:
            return self._contains(node.left, value)
        elif value > node.value:
            return self._contains(node.right, value)

        # value == node.value
        return True

    def insert(self, value) -> bool:
        if value is None:
            return False

        if not self._contains(self.root, value):
            self.root = self._insert(self.root, value)
            self.node_count += 1
            return True
        return False

    def _insert(self, node, value) -> Node:
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        self.update(node)  # update balance factor and height

        return self.balance(node)  # rebalance tree

    # update balance factor and height
    def update(self, node):
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        # update this node's height
        node.height = 1 + max(left_height, right_height)

        # update BF
        node.bf = right_height - left_height

    def balance(self, node):
        # left heavy subtree
        if node.bf == -2:
            # left-left case
            if node.left.bf <= 0:
                return self.left_left_case(node)
            else:  # left-right case
                return self.left_right_case(node)
        elif node.bf == 2:  # right heavy subtree
            if node.right.bf >= 0:
                return self.right_right_case(node)
            else:  # right-left case
                return self.right_left_case(node)

        # node has balace 0, +1 or -1 => node is already balanced
        return node

    def left_left_case(self, node):
        return self.right_rotation(node)

    def left_right_case(self, node):
        node.left = self.left_rotation(node.left)
        return self.left_left_case(node)

    def right_right_case(self, node):
        return self.left_rotation(node)

    def right_left_case(self, node):
        node.right = self.right_rotation(node.right)
        return self.right_right_case(node)

    def left_rotation(self, node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        self.update(node)
        self.update(new_parent)
        return new_parent

    def right_rotation(self, node):
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        self.update(node)
        self.update(new_parent)
        return new_parent

    def remove(self, el) -> bool:
        if el is None:
            return False

        if self.contains(self.root, el):
            self.root = self._remove(self.root, el)
            self.node_count -= 1
            return True
        return False

    def _remove(self, node, el):
        if node is None:
            return None

        if el < node.value:  # go to left
            node.left = self._remove(node.left, el)
        elif el > node.value:
            node.right = self._remove(node.right, el)
        else:  # found a node for removing
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.height > node.right.height:
                    successor_value = self.find_max(node.left)
                    node.value = successor_value

                    node.left = self._remove(node.left, successor_value)
                else:
                    successor_value = self.find_min(node.right)
                    node.value = successor_value

                    node.right = self._remove(node.right, successor_value)

        self.update(node)
        return self.balance(node)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node.value

    def avl_iter(self):
        trav = self.root
        stack = []
        stack.append(trav)
        while trav is not None and trav.left is not None:
            stack.append(trav.left)
            trav = trav.left

        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
            trav = node.right

        yield node.value

    def __str__(self):
        return TreePrinter.display(self.root)

    def validate_bst_invariant(self, node):
        if node is None:
            return True
        val = node.value
        is_valid = True
        if node.left is not None:
            is_valid = is_valid and node.left.value < val
        if node.right is not None:
            is_valid = is_valid and node.right.value > val
        return (
            is_valid
            and self.validate_bst_invariant(node.left)
            and self.validate_bst_invariant(node.right)
        )


tree = AVLTreeRecursive()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(6)
print(tree)
