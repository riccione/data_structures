"""
Tree Printer format trees

Taken from @J.V. at:
https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

Inspired by William Fiset
https://github.com/williamfiset/
"""


class TreePrinter:
    @staticmethod
    def display(root) -> str:
        lines, *_ = TreePrinter._display_aux(root)
        s = ""
        for line in lines:
            s += f"{line}\n"
        return s

    @staticmethod
    def _display_aux(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = "%s" % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = TreePrinter._display_aux(node.left)
            s = "%s" % node.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = TreePrinter._display_aux(node.right)
            s = "%s" % node.value
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = TreePrinter._display_aux(node.left)
        right, m, q, y = TreePrinter._display_aux(node.right)
        s = "%s" % node.value
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
