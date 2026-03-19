class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def delete_deepest(root, d_node):
    """Delete the deepest node from the tree."""
    if not root:
        return None
    if root == d_node:
        return None
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)
    return root


def delete_node(root, key):
    """Delete a node with given key by replacing it with the deepest node."""
    if not root:
        return None

    if not root.left and not root.right:
        if root.val == key:
            return None
        else:
            return root

    # Find the node to delete and the deepest node
    key_node = None
    queue = [root]
    temp = None
    last = None

    while queue:
        temp = queue.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        last = temp  # This will be the last node in level order

    if key_node is None:
        return root  # Key not found

    # Replace key_node's data with deepest node's data
    key_node.val = last.val
    # Delete the deepest node
    delete_deepest(root, last)
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
    # Create the tree:
    #       10
    #      /  \
    #     11    9
    #    / \   / \
    #   7  12 15  8
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before deleting 11:", inorder_traversal(root))

    # Delete 11
    root = delete_node(root, 11)
    print("Inorder traversal after deleting 11:", inorder_traversal(root))


if __name__ == "__main__":
    main()
