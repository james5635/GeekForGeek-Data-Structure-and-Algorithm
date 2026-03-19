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

    def to_number(self):
        result = 0
        current = self.head
        while current:
            result = result * 10 + current.data
            current = current.next
        return result


def multiply_linked_lists(head1, head2):
    num1 = 0
    num2 = 0

    current = head1
    while current:
        num1 = num1 * 10 + current.data
        current = current.next

    current = head2
    while current:
        num2 = num2 * 10 + current.data
        current = current.next

    product = num1 * num2

    if product == 0:
        return Node(0)

    dummy = Node(0)
    current = dummy

    for digit in str(product):
        current.next = Node(int(digit))
        current = current.next

    return dummy.next


def multiply_linked_lists_direct(head1, head2):
    num1 = []
    num2 = []

    current = head1
    while current:
        num1.append(current.data)
        current = current.next

    current = head2
    while current:
        num2.append(current.data)
        current = current.next

    num1.reverse()
    num2.reverse()

    result = [0] * (len(num1) + len(num2) + 1)

    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]

    for i in range(len(result) - 1):
        result[i + 1] += result[i] // 10
        result[i] = result[i] % 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result.reverse()

    if not result:
        return Node(0)

    dummy = Node(0)
    current = dummy
    for digit in result:
        current.next = Node(digit)
        current = current.next

    return dummy.next


if __name__ == "__main__":
    ll1 = LinkedList()
    for val in [2, 5]:
        ll1.insert_at_end(val)

    ll2 = LinkedList()
    for val in [3, 4]:
        ll2.insert_at_end(val)

    print("Number 1:")
    ll1.print_list()
    print("Number 2:")
    ll2.print_list()

    result = multiply_linked_lists(ll1.head, ll2.head)
    print(f"Product ({ll1.to_number()} * {ll2.to_number()}):")
    current = result
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    for val in [1, 2, 3]:
        ll3.insert_at_end(val)

    ll4 = LinkedList()
    for val in [4, 5]:
        ll4.insert_at_end(val)

    print("Number 1:")
    ll3.print_list()
    print("Number 2:")
    ll4.print_list()

    result2 = multiply_linked_lists_direct(ll3.head, ll4.head)
    print(f"Product ({ll3.to_number()} * {ll4.to_number()}):")
    current = result2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll5 = LinkedList()
    for val in [9, 9, 9]:
        ll5.insert_at_end(val)

    ll6 = LinkedList()
    for val in [9, 9, 9]:
        ll6.insert_at_end(val)

    print("Number 1:")
    ll5.print_list()
    print("Number 2:")
    ll6.print_list()

    result3 = multiply_linked_lists(ll5.head, ll6.head)
    print(f"Product ({ll5.to_number()} * {ll6.to_number()}):")
    current = result3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll7 = LinkedList()
    for val in [5]:
        ll7.insert_at_end(val)

    ll8 = LinkedList()
    for val in [0]:
        ll8.insert_at_end(val)

    print("Number 1:")
    ll7.print_list()
    print("Number 2:")
    ll8.print_list()

    result4 = multiply_linked_lists(ll7.head, ll8.head)
    print(f"Product ({ll7.to_number()} * {ll8.to_number()}):")
    current = result4
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
