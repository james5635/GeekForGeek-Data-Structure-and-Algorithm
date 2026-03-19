# Find Tree Height/Depth
# Height is the number of edges on the longest path from root to leaf
# Depth of a node is the number of edges from the root to that node
# Height of tree with only root node is 0 (edges) or 1 (nodes)


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def tree_height_recursive(root):
    """
    Calculate height of tree using recursion.
    Returns height in terms of number of edges.
    For empty tree, height is -1.
    For single node tree, height is 0.
    """
    if root is None:
        return -1  # Base case: empty tree has height -1 (no edges)

    # Height is 1 + max of left and right subtree heights
    left_height = tree_height_recursive(root.left)
    right_height = tree_height_recursive(root.right)

    return max(left_height, right_height) + 1


def tree_height_iterative(root):
    """
    Calculate height of tree using iteration (level order traversal).
    Returns height in terms of number of edges.
    """
    if root is None:
        return -1

    height = -1  # Start at -1 because we'll increment for each level
    queue = [root]

    while queue:
        # Increment height for each level
        height += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return height


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

    print("Tree Height:")
    print("Recursive (edges):", tree_height_recursive(root))
    print("Iterative (edges):", tree_height_iterative(root))
    print("Recursive (nodes):", tree_height_recursive(root) + 1)  # Convert to nodes
    print("Iterative (nodes):", tree_height_iterative(root) + 1)  # Convert to nodes

    # Expected height: 2 (edges) or 3 (nodes)


if __name__ == "__main__":
    main()
