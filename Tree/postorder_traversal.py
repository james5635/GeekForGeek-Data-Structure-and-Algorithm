# Postorder Traversal (Left, Right, Root)
# Recursive and Iterative implementations


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def postorder_recursive(root):
    """Return list of postorder traversal using recursion."""
    result = []

    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            result.append(node.data)

    helper(root)
    return result


def postorder_iterative(root):
    """Return list of postorder traversal using iteration (two stacks)."""
    if not root:
        return []

    result = []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        result.append(node.data)

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

    print("Postorder Traversal:")
    print("Recursive:", " ".join(map(str, postorder_recursive(root))))
    print("Iterative:", " ".join(map(str, postorder_iterative(root))))

    # Expected: 4 5 2 6 3 1


if __name__ == "__main__":
    main()
