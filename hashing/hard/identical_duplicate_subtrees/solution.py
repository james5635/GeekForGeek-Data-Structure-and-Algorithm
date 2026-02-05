"""
Find All Identical Duplicate Subtrees in a Binary Tree

Problem Description:
    Given a binary tree, find all duplicate subtrees.
    Two subtrees are duplicates if they have the same structure and values.

Approach:
    Use serialization with hash map to identify duplicate subtrees.
    Serialize each subtree and count occurrences using hash map.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Optional, Dict
from collections import defaultdict


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[TreeNode]:
    """
    Find all duplicate subtrees in a binary tree.

    Args:
        root: Root of the binary tree

    Returns:
        List of root nodes of duplicate subtrees (one per duplicate group)
    """
    if not root:
        return []

    subtree_map: Dict[str, int] = defaultdict(int)
    duplicates: List[TreeNode] = []

    def serialize(node: Optional[TreeNode]) -> str:
        """Serialize subtree rooted at node."""
        if not node:
            return "#"

        # Serialize in pre-order: node, left, right
        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        subtree_map[serial] += 1

        # If this is the second occurrence, add to duplicates
        if subtree_map[serial] == 2:
            duplicates.append(node)

        return serial

    serialize(root)
    return duplicates


def find_duplicate_subtrees_with_count(root: Optional[TreeNode]) -> Dict[str, int]:
    """
    Find all duplicate subtrees with their counts.

    Returns:
        Dictionary mapping subtree serialization to count
    """
    if not root:
        return {}

    subtree_map: Dict[str, int] = defaultdict(int)

    def serialize(node: Optional[TreeNode]) -> str:
        if not node:
            return "#"

        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        subtree_map[serial] += 1
        return serial

    serialize(root)

    # Return only duplicates (count > 1)
    return {k: v for k, v in subtree_map.items() if v > 1}


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert binary tree to list representation (level order).
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Create binary tree from list representation.
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(node: Optional[TreeNode], level=0, prefix="Root: "):
    """Print tree in a readable format."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def test_duplicate_subtrees():
    """Test cases for finding duplicate subtrees."""
    print("Running test cases for Identical Duplicate Subtrees:")
    print("=" * 60)

    # Test 1: Tree with duplicate leaf nodes
    print("\nTest 1: Tree with duplicate leaf nodes")
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   2   4
    #      /
    #     4
    root1 = list_to_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    print("Tree structure:")
    print_tree(root1)
    duplicates1 = find_duplicate_subtrees(root1)
    print(f"\nDuplicate subtrees found: {len(duplicates1)}")
    for i, dup in enumerate(duplicates1, 1):
        print(f"  {i}. Root value: {dup.val}, Subtree: {tree_to_list(dup)}")

    # Test 2: Tree with identical subtrees
    print("\n" + "=" * 60)
    print("\nTest 2: Tree with identical subtrees")
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 3  4
    root2 = list_to_tree([1, 2, 2, 3, 4, 3, 4])
    print("Tree structure:")
    print_tree(root2)
    duplicates2 = find_duplicate_subtrees(root2)
    print(f"\nDuplicate subtrees found: {len(duplicates2)}")
    for i, dup in enumerate(duplicates2, 1):
        print(f"  {i}. Root value: {dup.val}, Subtree: {tree_to_list(dup)}")

    # Test 3: Empty tree
    print("\n" + "=" * 60)
    print("\nTest 3: Empty tree")
    root3 = None
    duplicates3 = find_duplicate_subtrees(root3)
    print(f"Duplicate subtrees found: {len(duplicates3)} (expected: 0)")

    # Test 4: Single node
    print("\n" + "=" * 60)
    print("\nTest 4: Single node tree")
    root4 = list_to_tree([1])
    duplicates4 = find_duplicate_subtrees(root4)
    print(f"Duplicate subtrees found: {len(duplicates4)} (expected: 0)")


if __name__ == "__main__":
    # Example usage
    print("Example: Finding duplicate subtrees")
    print("=" * 60)

    # Create a tree with duplicates
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   2   4
    #      /
    #     4
    root = list_to_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])

    print("Tree:")
    print_tree(root)

    duplicates = find_duplicate_subtrees(root)
    print(f"\nFound {len(duplicates)} duplicate subtree(s):")
    for i, dup in enumerate(duplicates, 1):
        print(f"{i}. Subtree with root {dup.val}: {tree_to_list(dup)}")

    print()

    # Run tests
    test_duplicate_subtrees()
