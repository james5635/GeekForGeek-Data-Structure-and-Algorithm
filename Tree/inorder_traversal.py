# Inorder Traversal (Left, Root, Right)
# Recursive and Iterative implementations


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inorder_recursive(root):
    """Return list of inorder traversal using recursion."""
    result = []

    def helper(node):
        if node:
            helper(node.left)
            result.append(node.data)
            helper(node.right)

    helper(root)
    return result


def inorder_iterative(root):
    """Return list of inorder traversal using iteration (stack)."""
    result = []
    stack = []
    current = root

    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        # Current must be None at this point
        current = stack.pop()
        result.append(current.data)
        # We have visited the node and its left subtree.
        # Now, it's right subtree's turn
        current = current.right

    return result


def build_test_tree():
    """Build the test tree: 1(2(4,5),3(6))"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    return root


def main():
    root = build_test_tree()

    print("Inorder Traversal:")
    print("Recursive:", " ".join(map(str, inorder_recursive(root))))
    print("Iterative:", " ".join(map(str, inorder_iterative(root))))

    # Expected: 4 2 5 1 3 6


if __name__ == "__main__":
    main()
