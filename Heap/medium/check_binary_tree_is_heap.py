"""
Check if a Binary Tree is a Heap - GeeksforGeeks
https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-heap/

Problem: Given the root of a binary tree, determine if it's a valid max-heap.

A binary tree is a valid heap if:
1. It is a complete binary tree (all levels except possibly last are filled,
   and all nodes are as far left as possible)
2. Every node's value >= its children's values (max-heap property)

Time Complexity: O(n) for all approaches
Space Complexity: O(h) for recursive approaches, O(n) for iterative
"""

from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def count_nodes(root):
    """Count total number of nodes in the binary tree."""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_complete_util(root, index, number_of_nodes):
    """Check if binary tree is complete using index-based method."""
    if root is None:
        return True

    if index >= number_of_nodes:
        return False

    return is_complete_util(
        root.left, 2 * index + 1, number_of_nodes
    ) and is_complete_util(root.right, 2 * index + 2, number_of_nodes)


def is_heap_util(root):
    """Check heap property recursively."""
    if root.left is None and root.right is None:
        return True

    if root.right is None:
        return root.key >= root.left.key
    else:
        if root.key >= root.left.key and root.key >= root.right.key:
            return is_heap_util(root.left) and is_heap_util(root.right)
        return False


def is_heap(root):
    """
    Approach 1: Check completeness and heap property separately.
    Time: O(n), Space: O(h)
    """
    node_count = count_nodes(root)
    index = 0

    if is_complete_util(root, index, node_count) and is_heap_util(root):
        return True
    return False


def is_heap_single_pass(root, index, total_nodes):
    """
    Approach 2: Single-pass recursive check.
    Time: O(n), Space: O(h)
    """
    if root is None:
        return True

    if index >= total_nodes:
        return False

    if (root.left and root.left.key > root.key) or (
        root.right and root.right.key > root.key
    ):
        return False

    return is_heap_single_pass(
        root.left, 2 * index + 1, total_nodes
    ) and is_heap_single_pass(root.right, 2 * index + 2, total_nodes)


def is_heap_level_order(root):
    """
    Approach 3: Level order traversal with flag for completeness.
    Time: O(n), Space: O(n)
    """
    if root is None:
        return True

    q = deque()
    q.append(root)
    flag = False

    while q:
        temp = q.popleft()

        if temp.left:
            if flag or temp.left.key > temp.key:
                return False
            q.append(temp.left)
        else:
            flag = True

        if temp.right:
            if flag or temp.right.key > temp.key:
                return False
            q.append(temp.right)
        else:
            flag = True

    return True


if __name__ == "__main__":
    # Construct the Binary Tree (valid heap)
    #        97
    #       /  \
    #      46    37
    #     / \   / \
    #    12  3 7   31
    #   /  \
    #  6    9
    root = Node(97)
    root.left = Node(46)
    root.right = Node(37)
    root.left.left = Node(12)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(31)
    root.left.left.left = Node(6)
    root.left.left.right = Node(9)

    print("Is heap (Approach 1):", is_heap(root))  # True
    print(
        "Is heap (Approach 2):", is_heap_single_pass(root, 0, count_nodes(root))
    )  # True
    print("Is heap (Approach 3):", is_heap_level_order(root))  # True

    # Construct invalid heap (max heap property violated)
    #        3
    #       /  \
    #      4    5
    invalid = Node(3)
    invalid.left = Node(4)
    invalid.right = Node(5)

    print("Invalid tree is heap:", is_heap(invalid))  # False
