from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head


def display(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" ".join(result))


def segregate_even_odd(head):
    if head is None:
        return head

    even_deque = deque()
    odd_deque = deque()

    curr = head
    while curr:
        if curr.data % 2 == 0:
            even_deque.appendleft(curr.data)
        else:
            odd_deque.append(curr.data)
        curr = curr.next

    result_deque = deque()
    result_deque.extend(even_deque)
    result_deque.extend(odd_deque)

    new_head = None
    new_tail = None
    for val in result_deque:
        new_node = Node(val)
        if new_head is None:
            new_head = new_node
            new_tail = new_node
        else:
            new_tail.next = new_node
            new_tail = new_node

    return new_head


def main():
    # Test Case 1: 1->2->3->4->5->6->7->8->9->10 -> 10 8 6 4 2 1 3 5 7 9
    print("Test Case 1: 1->2->3->4->5->6->7->8->9->10")
    head1 = None
    for i in range(1, 11):
        head1 = insert_at_end(head1, i)
    print("Original: ", end="")
    display(head1)
    print("After segregation (even first, preserving even order): ", end="")
    head1 = segregate_even_odd(head1)
    display(head1)
    print()

    # Test Case 2: 4->3->2->1 -> 2 4 3 1
    print("Test Case 2: 4->3->2->1")
    head2 = None
    for val in [4, 3, 2, 1]:
        head2 = insert_at_end(head2, val)
    print("Original: ", end="")
    display(head2)
    print("After segregation: ", end="")
    head2 = segregate_even_odd(head2)
    display(head2)
    print()

    # Test Case 3: Empty list
    print("Test Case 3: Empty list")
    head3 = None
    print("Original: None")
    print("After segregation: ", end="")
    head3 = segregate_even_odd(head3)
    display(head3)
    print()

    # Test Case 4: All even numbers
    print("Test Case 4: All even numbers (2->4->6)")
    head4 = None
    for val in [2, 4, 6]:
        head4 = insert_at_end(head4, val)
    print("Original: ", end="")
    display(head4)
    print("After segregation: ", end="")
    head4 = segregate_even_odd(head4)
    display(head4)
    print()

    # Test Case 5: All odd numbers
    print("Test Case 5: All odd numbers (1->3->5)")
    head5 = None
    for val in [1, 3, 5]:
        head5 = insert_at_end(head5, val)
    print("Original: ", end="")
    display(head5)
    print("After segregation: ", end="")
    head5 = segregate_even_odd(head5)
    display(head5)


if __name__ == "__main__":
    main()
