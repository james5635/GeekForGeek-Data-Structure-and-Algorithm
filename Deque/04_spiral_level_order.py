from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def spiral_level_order_traversal(root):
    """
    Spiral level order traversal using deque.

    Approach:
    - Use a deque with left-to-right flag
    - When left-to-right: pop from left, push children to right
    - When right-to-left: pop from right, push children to left
    - Alternate direction at each level

    Time Complexity: O(n)
    Space Complexity: O(n) for deque
    """
    if not root:
        return []

    result = []
    dq = deque([root])
    left_to_right = True

    while dq:
        level_size = len(dq)

        for _ in range(level_size):
            if left_to_right:
                node = dq.popleft()
                result.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                node = dq.pop()
                result.append(node.val)
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)

        left_to_right = not left_to_right

    return result


def level_order_traversal(root):
    """
    Standard level order traversal (left to right at each level).
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def print_tree(root):
    """Helper to visualize tree structure."""
    if not root:
        return "Empty Tree"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return " -> ".join(result)


def main():
    print("=== Spiral Level Order Traversal using Deque ===\n")

    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    print("Tree 1 (root=1, left=3, right=2):")
    print(f"  Structure: {print_tree(tree1)}")
    result1_spiral = spiral_level_order_traversal(tree1)
    result1_level = level_order_traversal(tree1)
    print(f"  Spiral: {' '.join(map(str, result1_spiral))}")
    print(f"  Level Order: {' '.join(map(str, result1_level))}")
    print(f"  Expected: 1 3 2")
    print()

    tree2 = TreeNode(10)
    tree2.left = TreeNode(20)
    tree2.right = TreeNode(30)
    print("Tree 2 (root=10, left=20, right=30):")
    print(f"  Structure: {print_tree(tree2)}")
    result2_spiral = spiral_level_order_traversal(tree2)
    result2_level = level_order_traversal(tree2)
    print(f"  Spiral: {' '.join(map(str, result2_spiral))}")
    print(f"  Level Order: {' '.join(map(str, result2_level))}")
    print(f"  Expected: 10 20 30")
    print()

    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(3)
    tree3.left.left = TreeNode(4)
    tree3.left.right = TreeNode(5)
    tree3.right.left = TreeNode(6)
    tree3.right.right = TreeNode(7)
    print("Tree 3 (More complex):")
    print(f"  Structure: {print_tree(tree3)}")
    result3_spiral = spiral_level_order_traversal(tree3)
    result3_level = level_order_traversal(tree3)
    print(f"  Spiral: {' '.join(map(str, result3_spiral))}")
    print(f"  Level Order: {' '.join(map(str, result3_level))}")
    print(f"  Expected: 1 3 2 4 5 6 7")


if __name__ == "__main__":
    main()
