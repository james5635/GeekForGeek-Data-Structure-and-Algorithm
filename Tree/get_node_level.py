# Get Level of a Node in Binary Tree
# Level of root is considered as 1


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def get_level_recursive(root, target, level=1):
    """
    Recursively find the level of a target node.
    Returns 0 if node is not found.
    Level of root is 1.
    """
    if root is None:
        return 0

    if root.data == target:
        return level

    # Search in left subtree
    left_level = get_level_recursive(root.left, target, level + 1)
    if left_level != 0:
        return left_level

    # Search in right subtree
    return get_level_recursive(root.right, target, level + 1)


def get_level_iterative(root, target):
    """
    Iteratively find the level of a target node using level order traversal.
    Returns 0 if node is not found.
    Level of root is 1.
    """
    if root is None:
        return 0

    queue = [(root, 1)]  # (node, level)

    while queue:
        node, level = queue.pop(0)

        if node.data == target:
            return level

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return 0  # Node not found


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

    print("Get Node Level:")

    # Test cases
    test_nodes = [1, 2, 3, 4, 5, 6]  # 6 is not in tree

    for node in test_nodes:
        rec_level = get_level_recursive(root, node)
        iter_level = get_level_iterative(root, node)
        print(
            f"Node {node}: Recursive Level = {rec_level}, Iterative Level = {iter_level}"
        )

    # Specific test: find level of node 4
    print(f"\nSpecific test - Level of node 4: {get_level_recursive(root, 4)}")
    # Expected: level 3 (if root is level 1)


if __name__ == "__main__":
    main()
