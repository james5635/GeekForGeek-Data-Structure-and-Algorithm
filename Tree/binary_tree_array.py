# Binary Tree using Array Representation


class BinaryTreeArray:
    def __init__(self, size):
        """Initialize binary tree with fixed size array"""
        self.size = size
        self.tree = [None] * size  # Array to store tree nodes
        self.last_index = -1  # Track last used index

    def insert(self, value):
        """Insert a value at the next available position"""
        if self.last_index + 1 >= self.size:
            print("Tree is full!")
            return False

        self.last_index += 1
        self.tree[self.last_index] = value
        return True

    def get_parent(self, index):
        """Get parent index of node at given index"""
        if index <= 0 or index >= self.size:
            return None
        return (index - 1) // 2

    def get_left_child(self, index):
        """Get left child index of node at given index"""
        left = 2 * index + 1
        if left >= self.size or left > self.last_index:
            return None
        return left

    def get_right_child(self, index):
        """Get right child index of node at given index"""
        right = 2 * index + 2
        if right >= self.size or right > self.last_index:
            return None
        return right

    def get_value(self, index):
        """Get value at given index"""
        if 0 <= index <= self.last_index:
            return self.tree[index]
        return None

    def level_order_print(self):
        """Print tree in level order"""
        if self.last_index == -1:
            print("Tree is empty")
            return

        result = []
        for i in range(self.last_index + 1):
            if self.tree[i] is not None:
                result.append(str(self.tree[i]))
            else:
                result.append("None")
        print("Level Order: ", " ".join(result))

    def print_tree_structure(self):
        """Print tree structure showing relationships"""
        if self.last_index == -1:
            print("Tree is empty")
            return

        print("Tree Structure:")
        for i in range(self.last_index + 1):
            if self.tree[i] is not None:
                parent_idx = self.get_parent(i)
                left_idx = self.get_left_child(i)
                right_idx = self.get_right_child(i)

                parent_val = self.tree[parent_idx] if parent_idx is not None else None
                left_val = self.tree[left_idx] if left_idx is not None else None
                right_val = self.tree[right_idx] if right_idx is not None else None

                print(
                    f"Node {self.tree[i]}: "
                    f"Parent={parent_val}, "
                    f"Left={left_val}, "
                    f"Right={right_val}"
                )


def main():
    # Test with array representation of tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    # Array: [1, 2, 3, 4, 5, None, 6]

    print("Creating binary tree using array representation")
    tree = BinaryTreeArray(10)  # Size 10 to accommodate our tree

    # Insert values in level order: 1, 2, 3, 4, 5, None, 6
    values = [1, 2, 3, 4, 5, None, 6]
    print(f"Inserting values: {values}")

    for val in values:
        if val is not None:  # Skip None values as they represent empty nodes
            tree.insert(val)
        else:
            # For None values, we still need to increment index to maintain positions
            if tree.last_index + 1 < tree.size:
                tree.last_index += 1
                tree.tree[tree.last_index] = None

    print("\nLevel order traversal:")
    tree.level_order_print()

    print("\nTree structure:")
    tree.print_tree_structure()

    # Test parent/child relationships
    print("\nTesting parent/child relationships:")
    # Node 1 (index 0): left=2 (index 1), right=3 (index 2)
    print(
        f"Node 1 (index 0): left child index={tree.get_left_child(0)}, right child index={tree.get_right_child(0)}"
    )
    # Node 2 (index 1): left=4 (index 3), right=5 (index 4)
    print(
        f"Node 2 (index 1): left child index={tree.get_left_child(1)}, right child index={tree.get_right_child(1)}"
    )
    # Node 3 (index 2): left=None, right=6 (index 6)
    print(
        f"Node 3 (index 2): left child index={tree.get_left_child(2)}, right child index={tree.get_right_child(2)}"
    )

    # Verify the array representation matches expected: [1, 2, 3, 4, 5, None, 6]
    expected = [1, 2, 3, 4, 5, None, 6]
    actual = tree.tree[:7]  # First 7 elements

    print(f"\nExpected array representation: {expected}")
    print(f"Actual array representation:   {actual}")

    if actual == expected:
        print("Test PASSED: Array representation matches expected")
    else:
        print("Test FAILED: Array representation does not match expected")


if __name__ == "__main__":
    main()
