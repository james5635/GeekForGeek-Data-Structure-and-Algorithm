class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Insert a new node with given key in BST."""
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    """Search for a key in BST. Returns True if found, False otherwise."""
    if root is None or root.val == key:
        return root is not None

    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def inorder_traversal(root):
    """Return inorder traversal of the tree as a list."""
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result = result + inorder_traversal(root.right)
    return result


def main():
    # Start with empty tree
    root = None

    # Insert: 6, 2, 8, 7, 9
    keys = [6, 2, 8, 7, 9]
    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of BST:", inorder_traversal(root))

    # Search for 7 and 14
    print("Search for 7:", search(root, 7))  # Expected: True
    print("Search for 14:", search(root, 14))  # Expected: False


if __name__ == "__main__":
    main()
