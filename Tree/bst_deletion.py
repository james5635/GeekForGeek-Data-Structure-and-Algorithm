# Binary Search Tree Deletion Implementation


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper method to insert recursively"""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # If key is already present, don't insert (no duplicates)

    def delete(self, key):
        """Delete a key from the BST"""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """Helper method to delete recursively"""
        if node is None:
            return node

        # Find the node to be deleted
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        """Find the node with minimum value in a subtree"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Return inorder traversal of the BST"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


def main():
    # Create BST as specified:
    #       10
    #      /  \
    #     5    15
    #         /  \
    #        12   18
    bst = BST()
    values = [10, 5, 15, 12, 18]

    print("Creating BST with values:", values)
    for val in values:
        bst.insert(val)

    print("\nInorder traversal before deletion:")
    inorder_before = bst.inorder_traversal()
    print(" ".join(map(str, inorder_before)))
    # Expected: 5 10 12 15 18

    # Delete 15
    print("\nDeleting 15...")
    bst.delete(15)

    print("\nInorder traversal after deletion:")
    inorder_after = bst.inorder_traversal()
    print(" ".join(map(str, inorder_after)))
    # Expected: 5 10 12 18

    # Verify the result
    expected = [5, 10, 12, 18]
    if inorder_after == expected:
        print("\nTest PASSED: Output matches expected result")
    else:
        print(f"\nTest FAILED: Expected {expected}, got {inorder_after}")


if __name__ == "__main__":
    main()
