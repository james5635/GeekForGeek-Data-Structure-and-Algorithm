# Find Parent of a Node in Binary Tree


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def find_parent_recursive(root, target):
    """
    Recursively find the parent of a target node.
    Returns None if node is root or not found.
    """
    # Base cases
    if root is None:
        return None

    # If current node is parent of target
    if (root.left and root.left.data == target) or (
        root.right and root.right.data == target
    ):
        return root.data

    # Recursively search in left and right subtrees
    left_result = find_parent_recursive(root.left, target)
    if left_result is not None:
        return left_result

    return find_parent_recursive(root.right, target)


def find_parent_iterative(root, target):
    """
    Iteratively find the parent of a target node using level order traversal.
    Returns None if node is root or not found.
    """
    if root is None:
        return None

    # Root has no parent
    if root.data == target:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)

        # Check if left child is the target
        if node.left and node.left.data == target:
            return node.data

        # Check if right child is the target
        if node.right and node.right.data == target:
            return node.data

        # Add children to queue for further exploration
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return None  # Target not found


def build_test_tree():
    """Build the test tree: 1(2(4,5),3)"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def main():
    root = build_test_tree()

    print("Find Parent of a Node:")

    # Test cases: find parent of 3 and 4
    test_nodes = [3, 4]

    for node in test_nodes:
        rec_parent = find_parent_recursive(root, node)
        iter_parent = find_parent_iterative(root, node)
        print(f"Parent of {node}: Recursive = {rec_parent}, Iterative = {iter_parent}")

    # Expected: 1 for both


if __name__ == "__main__":
    main()
