class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert_level_order(root, key):
    """Insert a new node with given key in level order."""
    if root is None:
        return Node(key)

    # Use queue for level order traversal
    queue = [root]

    while queue:
        temp = queue.pop(0)

        # Insert as left child if available
        if not temp.left:
            temp.left = Node(key)
            return root
        else:
            queue.append(temp.left)

        # Insert as right child if available
        if not temp.right:
            temp.right = Node(key)
            return root
        else:
            queue.append(temp.right)

    return root


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

    # Insert: 10, 11, 9, 7, 15, 8
    keys = [10, 11, 9, 7, 15, 8]
    for key in keys:
        root = insert_level_order(root, key)

    print("Inorder traversal before inserting 12:", inorder_traversal(root))

    # Insert 12
    root = insert_level_order(root, 12)
    print("Inorder traversal after inserting 12:", inorder_traversal(root))


if __name__ == "__main__":
    main()
