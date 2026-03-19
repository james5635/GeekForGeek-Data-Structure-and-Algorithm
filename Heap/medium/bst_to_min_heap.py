"""
Convert BST to Min Heap - GeeksforGeeks
https://www.geeksforgeeks.org/dsa/convert-bst-min-heap/

Problem: Given a Binary Search Tree (which is also a complete binary tree),
convert it into a Min Heap where:
- All values in left subtree < all values in right subtree for each node
- Parent has smaller value than children (min-heap property)

Approach: Two-step process
1. Store inorder traversal (sorted values) in an array
2. Perform preorder traversal and replace node values with sorted values

This works because preorder of a BST visits root before children,
which matches heap's level-order property (parent before children).

Time Complexity: O(n)
Space Complexity: O(n) for storing inorder traversal + O(h) recursion stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root, inorder_arr):
    """
    Perform inorder traversal and store values in sorted order.
    """
    if root is None:
        return

    inorder_traversal(root.left, inorder_arr)
    inorder_arr.append(root.data)
    inorder_traversal(root.right, inorder_arr)


def preorder_fill(root, inorder_arr, index):
    """
    Perform preorder traversal and fill node values from sorted array.
    """
    if root is None:
        return index

    root.data = inorder_arr[index]
    index += 1

    index = preorder_fill(root.left, inorder_arr, index)
    index = preorder_fill(root.right, inorder_arr, index)

    return index


def bst_to_min_heap(root):
    """
    Convert BST to Min Heap.

    Args:
        root: Root of the BST

    Returns:
        None (modifies tree in-place)
    """
    inorder_arr = []

    inorder_traversal(root, inorder_arr)

    preorder_fill(root, inorder_arr, 0)


def preorder_print(root):
    """Print tree in preorder (to verify min-heap structure)."""
    if root is None:
        return

    print(root.data, end=" ")
    preorder_print(root.left)
    preorder_print(root.right)


def level_order_print(root):
    """Print tree in level order (to see heap structure)."""
    if root is None:
        return

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def is_min_heap(root):
    """Check if tree satisfies min-heap property."""
    if root is None:
        return True

    queue = [root]
    flag = False

    while queue:
        node = queue.pop(0)

        if node.left:
            if flag or node.left.data < node.data:
                return False
            queue.append(node.left)
        else:
            flag = True

        if node.right:
            if flag or node.right.data < node.data:
                return False
            queue.append(node.right)
        else:
            flag = True

    return True


if __name__ == "__main__":
    # Construct the Binary Search Tree
    #          4
    #        /   \
    #       2     6
    #      / \   / \
    #     1   3 5   7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print("Original BST (preorder):")
    preorder_print(root)
    print()

    print("Original BST (level order):")
    print(level_order_print(root))

    bst_to_min_heap(root)

    print("\nAfter converting to Min Heap (preorder):")
    preorder_print(root)
    print()

    print("After converting to Min Heap (level order):")
    print(level_order_print(root))

    print(f"\nIs valid min heap: {is_min_heap(root)}")
