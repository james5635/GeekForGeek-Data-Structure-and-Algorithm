from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1


def current_level(node, level, result):
    if node is None:
        return
    if level == 1:
        result.append(node.data)
    elif level > 1:
        current_level(node.left, level - 1, result)
        current_level(node.right, level - 1, result)


def level_order_recursive(root):
    if root is None:
        return []

    result = []
    h = height(root)

    for i in range(1, h + 1):
        level_nodes = []
        current_level(root, i, level_nodes)
        result.extend(level_nodes)

    return result


def level_order_iterative(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(14)
    root.right.right = Node(2)

    print("Tree structure:")
    print("        5")
    print("       / \\")
    print("     12   13")
    print("    / \\    \\")
    print("   7  14    2")
    print()

    print("Level Order Traversal (Recursive):")
    print(level_order_recursive(root))

    print("\nLevel Order Traversal (Iterative):")
    print(level_order_iterative(root))
