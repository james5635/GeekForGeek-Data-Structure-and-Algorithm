# Level Order Traversal (Breadth-First Search)
# Iterative implementation using queue

from collections import deque


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def level_order_iterative(root):
    """Return list of level order traversal using queue."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level)

    return result


def build_test_tree():
    """Build the test tree: 
         1
        / \
       2   3
      / \   \
     4   5   6
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root


def main():
    root = build_test_tree()

    print("Level Order Traversal:")
    print(" ".join(map(str, level_order_iterative(root))))

    # Expected: 1 2 3 4 5 6 (level by level)


if __name__ == "__main__":
    main()
