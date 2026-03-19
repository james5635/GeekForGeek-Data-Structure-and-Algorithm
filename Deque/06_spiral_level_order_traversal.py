from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def spiral_order(root):
    if not root:
        return []

    result = []
    current = deque([root])
    left_to_right = True

    while current:
        next_level = deque()
        level = []

        while current:
            node = current.pop()
            level.append(node.data)

            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        level.reverse()
        result.extend(level)
        current = next_level
        left_to_right = not left_to_right

    return result


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(7)
    root1.left.right = Node(6)
    root1.right.left = Node(5)
    root1.right.right = Node(4)
    assert spiral_order(root1) == [1, 2, 3, 4, 5, 6, 7]

    root2 = Node(10)
    root2.left = Node(20)
    root2.right = Node(30)
    assert spiral_order(root2) == [10, 20, 30]

    root3 = Node(1)
    root3.left = Node(2)
    root3.left.left = Node(3)
    assert spiral_order(root3) == [1, 2, 3]

    assert spiral_order(None) == []

    single = Node(5)
    assert spiral_order(single) == [5]

    root4 = Node(1)
    root4.left = Node(2)
    root4.right = Node(3)
    root4.left.left = Node(4)
    root4.left.right = Node(5)
    root4.right.left = Node(6)
    root4.right.right = Node(7)
    assert spiral_order(root4) == [1, 2, 3, 7, 6, 5, 4]

    print("All tests passed")
