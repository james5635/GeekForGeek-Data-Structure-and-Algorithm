# Red-Black Tree Insertion Implementation


class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.color = color  # RED or BLACK
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, color="BLACK")  # Null node (sentinel)
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):
        """Insert a key into the Red-Black tree"""
        # Step 1: Perform normal BST insertion
        node = Node(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED"  # New node is always red

        # Find the position to insert
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # If new node is a root node, simply return
        if node.parent is None:
            node.color = "BLACK"
            return

        # If the parent is black, return
        if node.parent.color == "BLACK":
            return

        # Fix the tree
        self._fix_insert(node)

    def _fix_insert(self, k):
        """Fix Red-Black tree violations after insertion"""
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == "RED":
                    # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    # Case 2: Uncle is black and k is left child
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    # Case 3: Uncle is black and k is right child
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left  # Uncle
                if u.color == "RED":
                    # Case 1: Uncle is red
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    # Case 2: Uncle is black and k is right child
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    # Case 3: Uncle is black and k is left child
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def _left_rotate(self, x):
        """Left rotation"""
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """Right rotation"""
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self):
        """Return inorder traversal of the Red-Black tree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal"""
        if node != self.TNULL:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def print_tree(self):
        """Print the tree structure with colors"""
        print("Tree structure (key, color):")
        self._print_recursive(self.root, "", True)

    def _print_recursive(self, node, indent, last):
        """Helper method to print tree structure"""
        if node != self.TNULL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            color = "RED" if node.color == "RED" else "BLACK"
            print(f"{node.key}({color})")

            self._print_recursive(node.left, indent, False)
            self._print_recursive(node.right, indent, True)


def main():
    # Insert: 7, 3, 18, 10, 22, 8, 11, 26
    rbt = RedBlackTree()
    values = [7, 3, 18, 10, 22, 8, 11, 26]

    print("Creating Red-Black Tree with values:", values)
    for val in values:
        rbt.insert(val)

    print("\nInorder traversal (should be sorted):")
    inorder = rbt.inorder_traversal()
    print(" ".join(map(str, inorder)))
    # Expected: 3 7 8 10 11 18 22 26

    print("\nTree structure:")
    rbt.print_tree()

    # Verify BST property (inorder should be sorted)
    is_sorted = all(inorder[i] <= inorder[i + 1] for i in range(len(inorder) - 1))
    print(f"\nBST Property Verified (Inorder is sorted): {is_sorted}")

    # Additional verification: root should be black
    print(f"Root is Black: {rbt.root.color == 'BLACK'}")


if __name__ == "__main__":
    main()
