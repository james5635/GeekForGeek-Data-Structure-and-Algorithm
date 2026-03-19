class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def construct_from_2d_matrix(matrix):
    if not matrix or not matrix[0]:
        return None

    dummy = Node(0)
    current = dummy

    for row in matrix:
        for val in row:
            current.next = Node(val)
            current = current.next

    return dummy.next


def construct_row_wise(matrix):
    if not matrix or not matrix[0]:
        return None

    dummy = Node(0)
    current = dummy

    for row in matrix:
        for val in row:
            current.next = Node(val)
            current = current.next
        current.row_end = True

    return dummy.next


def construct_as_nested_list(matrix):
    if not matrix or not matrix[0]:
        return None

    dummy = Node(0)
    current = dummy
    row_heads = []

    for row in matrix:
        row_dummy = Node(0)
        row_current = row_dummy
        for val in row:
            row_current.next = Node(val)
            row_current = row_current.next
        row_heads.append(row_dummy.next)

    current = dummy
    for head in row_heads:
        current.next = head
        while current.next:
            current = current.next

    return dummy.next


if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("2D Matrix:")
    for row in matrix1:
        print(row)

    result1 = construct_from_2d_matrix(matrix1)
    print("\nConstructed Linked List:")
    current = result1
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    print("2D Matrix:")
    for row in matrix2:
        print(row)

    result2 = construct_from_2d_matrix(matrix2)
    print("\nConstructed Linked List:")
    current = result2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    matrix3 = [[1]]

    print("2D Matrix:")
    for row in matrix3:
        print(row)

    result3 = construct_from_2d_matrix(matrix3)
    print("\nConstructed Linked List:")
    current = result3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    matrix4 = [[10, 20], [30, 40], [50, 60]]

    print("2D Matrix:")
    for row in matrix4:
        print(row)

    result4 = construct_row_wise(matrix4)
    print("\nConstructed Linked List (Row-wise):")
    current = result4
    while current:
        if hasattr(current, "row_end") and current.row_end:
            print(current.data, end=" || ")
        else:
            print(current.data, end=" -> ")
        current = current.next
    print("None")
