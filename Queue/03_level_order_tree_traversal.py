from __future__ import annotations
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def height(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    return max(lheight, rheight) + 1


def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    else:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)


def level_order_rec(root):
    h = height(root)
    for i in range(1, h + 1):
        print_given_level(root, i)


def level_order_iterative(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Level Order Traversal (Recursive):")
    level_order_rec(root)
    print()

    print("Level Order Traversal (Iterative):")
    level_order_iterative(root)
    print()

    print()

    root2 = Node(10)
    root2.left = Node(20)
    root2.right = Node(30)
    root2.left.left = Node(40)
    root2.left.right = Node(60)

    print("Level Order Traversal (Recursive):")
    level_order_rec(root2)
    print()

    print("Level Order Traversal (Iterative):")
    level_order_iterative(root2)
    print()
