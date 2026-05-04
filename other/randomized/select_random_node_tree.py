import random


class TreeNode:
    """Tree node with size attribute for random node selection."""

    def __init__(self, val: int):
        self.val = val
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None
        self.size = 1

    def insert(self, val: int) -> None:
        """Insert value into BST and update sizes."""
        if val <= self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        self.size += 1

    def _update_sizes(self) -> None:
        """Recalculate size of subtree."""
        self.size = 1
        if self.left:
            self.left._update_sizes()
            self.size += self.left.size
        if self.right:
            self.right._update_sizes()
            self.size += self.right.size


def select_random_node_tree(root: TreeNode) -> int:
    """Select a random node from tree with equal probability using subtree sizes."""
    r = random.randint(1, root.size)
    current = root

    while current:
        left_size = current.left.size if current.left else 0
        if r <= left_size:
            current = current.left
        elif r == left_size + 1:
            return current.val
        else:
            r -= left_size + 1
            current = current.right

    raise ValueError("Tree is empty")


if __name__ == "__main__":
    values = [5, 3, 7, 2, 4, 6, 8, 1]
    root = TreeNode(values[0])
    for v in values[1:]:
        root.insert(v)

    counts = {v: 0 for v in values}
    for _ in range(10000):
        selected = select_random_node_tree(root)
        counts[selected] += 1

    print("Tree values:", values)
    print("Selection distribution:")
    for v in sorted(values):
        print(f"  {v}: {counts[v]:4d} ({counts[v] / 100:.2f}%)")
