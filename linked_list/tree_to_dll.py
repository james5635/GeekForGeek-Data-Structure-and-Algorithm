class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def tree_to_dll(root):
    if not root:
        return None

    dummy = DLLNode(0)
    prev = [None]

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        current = DLLNode(node.data)
        current.prev = prev[0]
        if prev[0]:
            prev[0].next = current
        else:
            dummy.next = current
        prev[0] = current

        inorder(node.right)

    inorder(root)
    return dummy.next


def tree_to_dll_bidirectional(root):
    if not root:
        return None, None

    left_head, left_tail = tree_to_dll_bidirectional(root.left)

    current = DLLNode(root.data)

    if left_tail:
        left_tail.next = current
        current.prev = left_tail
    else:
        left_head = current

    right_head, right_tail = tree_to_dll_bidirectional(root.right)

    if right_head:
        current.next = right_head
        right_head.prev = current
        return left_head, right_tail
    else:
        return left_head, current


def print_dll_forward(head):
    if not head:
        print("Empty DLL")
        return
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" <-> ".join(elements))


def print_dll_backward(tail):
    if not tail:
        print("Empty DLL")
        return
    elements = []
    current = tail
    while current:
        elements.append(str(current.data))
        current = current.prev
    print(" <-> ".join(elements))


if __name__ == "__main__":
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.right = TreeNode(20)

    print("Binary Tree:")
    print("       10")
    print("      /  \\")
    print("     5    15")
    print("    / \\    \\")
    print("   3   7    20")

    dll1 = tree_to_dll(root1)
    print("\nDoubly Linked List (Forward):")
    print_dll_forward(dll1)

    tail1 = dll1
    while tail1 and tail1.next:
        tail1 = tail1.next
    print("Doubly Linked List (Backward):")
    print_dll_backward(tail1)

    print("\n" + "=" * 40 + "\n")

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)

    print("Binary Tree:")
    print("        1")
    print("      /   \\")
    print("     2     3")
    print("    / \\   / \\")
    print("   4   5 6   7")

    dll2, _ = tree_to_dll_bidirectional(root2)
    print("\nDoubly Linked List (Forward):")
    print_dll_forward(dll2)

    tail2 = dll2
    while tail2 and tail2.next:
        tail2 = tail2.next
    print("Doubly Linked List (Backward):")
    print_dll_backward(tail2)

    print("\n" + "=" * 40 + "\n")

    root3 = TreeNode(25)
    root3.left = TreeNode(15)
    root3.left.left = TreeNode(10)
    root3.left.right = TreeNode(20)
    root3.right = TreeNode(30)

    print("Binary Tree:")
    print("       25")
    print("      /  \\")
    print("     15   30")
    print("    /  \\")
    print("   10  20")

    dll3 = tree_to_dll(root3)
    print("\nDoubly Linked List (Forward):")
    print_dll_forward(dll3)

    tail3 = dll3
    while tail3 and tail3.next:
        tail3 = tail3.next
    print("Doubly Linked List (Backward):")
    print_dll_backward(tail3)
