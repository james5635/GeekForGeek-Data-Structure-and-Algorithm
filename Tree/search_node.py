# Search for a Node in Binary Tree


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def search_recursive(root, key):
    """
    Recursively search for a key in the binary tree.
    Returns True if found, False otherwise.
    """
    # Base case: root is None
    if root is None:
        return False

    # Key is present at root
    if root.data == key:
        return True

    # Recursively search in left and right subtrees
    return search_recursive(root.left, key) or search_recursive(root.right, key)


def search_iterative(root, key):
    """
    Iteratively search for a key in the binary tree using level order traversal.
    Returns True if found, False otherwise.
    """
    if root is None:
        return False

    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.data == key:
            return True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


def build_test_tree():
    """Build the test tree: 
         1
        / \
       2   3
      / \
     4   5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def main():
    root = build_test_tree()

    print("Search Node in Binary Tree:")

    # Test cases
    test_keys = [5, 10]  # 5 exists, 10 doesn't

    for key in test_keys:
        rec_result = search_recursive(root, key)
        iter_result = search_iterative(root, key)
        print(f"Search for {key}: Recursive = {rec_result}, Iterative = {iter_result}")

    # Expected: True for 5, False for 10


if __name__ == "__main__":
    main()
