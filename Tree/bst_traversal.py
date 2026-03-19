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


def inorder_traversal(root):
    """Return inorder traversal of the tree as a list."""
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result = result + inorder_traversal(root.right)
    return result


def preorder_traversal(root):
    """Return preorder traversal of the tree as a list."""
    result = []
    if root:
        result.append(root.val)
        result = result + preorder_traversal(root.left)
        result = result + preorder_traversal(root.right)
    return result


def postorder_traversal(root):
    """Return postorder traversal of the tree as a list."""
    result = []
    if root:
        result = result + postorder_traversal(root.left)
        result = result + postorder_traversal(root.right)
        result.append(root.val)
    return result


def main():
    # Start with empty tree
    root = None

    # Create BST:
    #       100
    #      /    \
    #     20    200
    #    /  \   /  \
    #   10  30 150 300
    keys = [100, 20, 200, 10, 30, 150, 300]
    for key in keys:
        root = insert(root, key)

    print(
        "Inorder traversal:", inorder_traversal(root)
    )  # Expected: 10 20 30 100 150 200 300
    print(
        "Preorder traversal:", preorder_traversal(root)
    )  # Expected: 100 20 10 30 200 150 300
    print(
        "Postorder traversal:", postorder_traversal(root)
    )  # Expected: 10 30 20 150 300 200 100


if __name__ == "__main__":
    main()
