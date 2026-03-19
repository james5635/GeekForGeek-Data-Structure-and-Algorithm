class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructAncestorMatrix(root):
    """
    Construct ancestor matrix from a given binary tree
    Args:
        root: Root node of the binary tree
    Returns:
        ancestor matrix as a 2D list
    """
    if not root:
        return []

    # First, we need to get all nodes in the tree to determine matrix size
    def getAllNodes(node, nodes):
        if not node:
            return
        nodes.append(node.data)
        getAllNodes(node.left, nodes)
        getAllNodes(node.right, nodes)

    # Get all unique node values
    nodes = []
    getAllNodes(root, nodes)
    unique_nodes = sorted(list(set(nodes)))

    # Create mapping from node value to index
    node_to_index = {val: idx for idx, val in enumerate(unique_nodes)}
    n = len(unique_nodes)

    # Initialize ancestor matrix with zeros
    ancestor_matrix = [[0] * n for _ in range(n)]

    # Fill the ancestor matrix
    def fillAncestorMatrix(node, ancestors):
        if not node:
            return

        # Current node's ancestors are all nodes in the ancestors list
        current_idx = node_to_index[node.data]
        for ancestor_val in ancestors:
            ancestor_idx = node_to_index[ancestor_val]
            ancestor_matrix[current_idx][ancestor_idx] = 1

        # Add current node to ancestors list for children
        ancestors.append(node.data)

        # Recurse for left and right children
        fillAncestorMatrix(node.left, ancestors)
        fillAncestorMatrix(node.right, ancestors)

        # Remove current node from ancestors list when backtracking
        ancestors.pop()

    fillAncestorMatrix(root, [])
    return ancestor_matrix


def printMatrix(matrix):
    """Helper function to print matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


def test_constructAncestorMatrix():
    # Test case 1
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    print("Test 1 - Tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\")
    print("   4   5")
    print()
    print("Ancestor Matrix:")
    result1 = constructAncestorMatrix(root1)
    printMatrix(result1)
    print("Expected:")
    print("0 0 0 0 0")
    print("1 0 0 0 0")
    print("1 0 0 0 0")
    print("1 1 0 0 0")
    print("1 1 0 0 0")
    print()

    # Test case 2
    #       1
    #      / \
    #     2   3
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    print("Test 2 - Tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print()
    print("Ancestor Matrix:")
    result2 = constructAncestorMatrix(root2)
    printMatrix(result2)
    print("Expected:")
    print("0 0 0")
    print("1 0 0")
    print("1 0 0")
    print()


if __name__ == "__main__":
    test_constructAncestorMatrix()
