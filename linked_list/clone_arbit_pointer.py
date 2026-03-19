class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


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

    def set_arbitrary(self, index, target_index):
        current = self.head
        target = self.head

        for _ in range(index):
            if current:
                current = current.next

        for _ in range(target_index):
            if target:
                target = target.next

        if current:
            current.arbit = target

    def print_list(self):
        current = self.head
        while current:
            arbit_data = current.arbit.data if current.arbit else "None"
            print(f"{current.data} (arbit -> {arbit_data})", end=" -> ")
            current = current.next
        print("None")


def clone_with_hash(head):
    if not head:
        return None

    original_to_clone = {}
    current = head
    while current:
        original_to_clone[current] = Node(current.data)
        current = current.next

    current = head
    while current:
        clone = original_to_clone[current]
        if current.next:
            clone.next = original_to_clone[current.next]
        if current.arbit:
            clone.arbit = original_to_clone[current.arbit]
        current = current.next

    return original_to_clone[head]


def clone_in_place(head):
    if not head:
        return None

    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    current = head
    while current:
        if current.arbit:
            current.next.arbit = current.arbit.next
        current = current.next.next

    dummy = Node(0)
    tail = dummy
    current = head
    while current:
        tail.next = current.next
        tail = tail.next
        current.next = current.next.next
        current = current.next

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.insert_at_end(val)

    ll.set_arbitrary(0, 2)
    ll.set_arbitrary(1, 4)
    ll.set_arbitrary(2, 0)
    ll.set_arbitrary(3, 2)
    ll.set_arbitrary(4, 1)

    print("Original List (arbitrary pointers shown):")
    ll.print_list()

    cloned = clone_with_hash(ll.head)
    print("\nCloned List (Method 1 - Hashing):")
    current = cloned
    while current:
        arbit_data = current.arbit.data if current.arbit else "None"
        print(f"{current.data} (arbit -> {arbit_data})", end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll2 = LinkedList()
    for val in [10, 20, 30, 40]:
        ll2.insert_at_end(val)

    ll2.set_arbitrary(0, 3)
    ll2.set_arbitrary(1, 0)
    ll2.set_arbitrary(2, 3)
    ll2.set_arbitrary(3, 1)

    print("Original List:")
    ll2.print_list()

    cloned2 = clone_in_place(ll2.head)
    print("\nCloned List (Method 2 - In Place):")
    current = cloned2
    while current:
        arbit_data = current.arbit.data if current.arbit else "None"
        print(f"{current.data} (arbit -> {arbit_data})", end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    ll3.insert_at_end(100)
    print("Single node list:")
    ll3.set_arbitrary(0, 0)
    ll3.print_list()

    cloned3 = clone_with_hash(ll3.head)
    print("Cloned:")
    current = cloned3
    while current:
        arbit_data = current.arbit.data if current.arbit else "None"
        print(f"{current.data} (arbit -> {arbit_data})", end=" -> ")
        current = current.next
    print("None")
