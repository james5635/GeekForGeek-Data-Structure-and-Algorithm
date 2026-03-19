# Preorder Traversal (Root, Left, Right)
# Recursive and Iterative implementations


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def preorder_recursive(root):
    """Return list of preorder traversal using recursion."""
    result = []

    def helper(node):
        if node:
            result.append(node.data)
            helper(node.left)
            helper(node.right)

    helper(root)
    return result


def preorder_iterative(root):
    """Return list of preorder traversal using iteration (stack)."""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.data)
        # Push right first so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

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

    print("Preorder Traversal:")
    print("Recursive:", " ".join(map(str, preorder_recursive(root))))
    print("Iterative:", " ".join(map(str, preorder_iterative(root))))

    # Expected: 1 2 4 5 3 6


if __name__ == "__main__":
    main()
