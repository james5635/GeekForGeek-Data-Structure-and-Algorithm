# AVL Tree Insertion Implementation


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node (leaf node has height 1)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the AVL tree"""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        """Helper method to insert recursively and balance the tree"""
        # Step 1: Perform normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        else:
            # Duplicate keys not allowed
            return root

        # Step 2: Update height of this ancestor node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Step 3: Get the balance factor to check whether this node became unbalanced
        balance = self._get_balance(root)

        # Step 4: If this node becomes unbalanced, then there are 4 cases

        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        # Return the (unchanged) node pointer
        return root

    def _left_rotate(self, z):
        """Left rotation"""
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    def _right_rotate(self, z):
        """Right rotation"""
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    def _get_height(self, root):
        """Get height of a node"""
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        """Get balance factor of a node"""
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def inorder_traversal(self):
        """Return inorder traversal of the AVL tree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        """Helper method for inorder traversal"""
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

    def preorder_traversal(self):
        """Return preorder traversal of the AVL tree"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, root, result):
        """Helper method for preorder traversal"""
        if root:
            result.append(root.key)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)


def main():
    # Insert: 10, 20, 30, 40, 50, 25
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    print("Creating AVL Tree with values:", values)
    for val in values:
        avl.insert(val)

    print("\nInorder traversal (should be sorted):")
    inorder = avl.inorder_traversal()
    print(" ".join(map(str, inorder)))
    # Expected: 10 20 25 30 40 50

    print("\nPreorder traversal (to check tree structure):")
    preorder = avl.preorder_traversal()
    print(" ".join(map(str, preorder)))
    # Should show a balanced tree

    # Verify BST property (inorder should be sorted)
    is_sorted = all(inorder[i] <= inorder[i + 1] for i in range(len(inorder) - 1))
    print(f"\nBST Property Verified (Inorder is sorted): {is_sorted}")

    # Check if tree is balanced by verifying height differences
    def check_balance(node):
        if not node:
            return True, 0

        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)

        balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1
        )
        height = 1 + max(left_height, right_height)

        return balanced, height

    is_balanced, _ = check_balance(avl.root)
    print(f"AVL Property Verified (Tree is balanced): {is_balanced}")


if __name__ == "__main__":
    main()
