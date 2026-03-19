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


def sublist_search(head, sub_head):
    if not head or not sub_head:
        return False

    current = head
    while current:
        temp = current
        sub_temp = sub_head

        while sub_temp and temp and temp.data == sub_temp.data:
            temp = temp.next
            sub_temp = sub_temp.next

        if not sub_temp:
            return True

        current = current.next

    return False


def sublist_search_kmp(head, sub_head):
    if not sub_head:
        return True
    if not head:
        return False

    def get_failure_array(sub_head):
        arr = []
        current = sub_head
        i = 0
        while current:
            if i == 0:
                arr.append(0)
                i = 1
            elif i > 0:
                while i > 0 and current.data != get_data_at_index(sub_head, i):
                    i = arr[i - 1]
                if current.data == get_data_at_index(sub_head, i):
                    i += 1
                arr.append(i)
            if current.next:
                current = current.next
            else:
                break
        return arr

    def get_data_at_index(head, index):
        current = head
        for _ in range(index):
            if current:
                current = current.next
        return current.data if current else None

    failure = get_failure_array(sub_head)

    current = head
    i = 0

    while current:
        while i > 0 and current.data != get_data_at_index(sub_head, i):
            i = failure[i - 1]

        if current.data == get_data_at_index(sub_head, i):
            i += 1

        if i == len(failure):
            return True

        current = current.next

    return False


if __name__ == "__main__":
    main_ll = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        main_ll.insert_at_end(val)

    sub_ll = LinkedList()
    for val in [4, 5, 6]:
        sub_ll.insert_at_end(val)

    sub_ll2 = LinkedList()
    for val in [7, 8, 9]:
        sub_ll2.insert_at_end(val)

    sub_ll3 = LinkedList()
    for val in [5, 6, 7]:
        sub_ll3.insert_at_end(val)

    print("Main List:")
    main_ll.print_list()

    print("\nSublist 1 (4 -> 5 -> 6):")
    sub_ll.print_list()
    print(f"Found: {sublist_search(main_ll.head, sub_ll.head)}")

    print("\nSublist 2 (7 -> 8 -> 9):")
    sub_ll2.print_list()
    print(f"Found: {sublist_search(main_ll.head, sub_ll2.head)}")

    print("\nSublist 3 (5 -> 6 -> 7) - Not a sublist:")
    sub_ll3.print_list()
    print(f"Found: {sublist_search(main_ll.head, sub_ll3.head)}")

    print("\n" + "=" * 40 + "\n")

    main_ll2 = LinkedList()
    for val in [1, 2, 1, 2, 1, 2, 1]:
        main_ll2.insert_at_end(val)

    sub_ll4 = LinkedList()
    for val in [1, 2, 1]:
        sub_ll4.insert_at_end(val)

    print("Main List:")
    main_ll2.print_list()
    print("Sublist (1 -> 2 -> 1):")
    sub_ll4.print_list()
    print(f"Found: {sublist_search(main_ll2.head, sub_ll4.head)}")

    print("\n" + "=" * 40 + "\n")

    ll5 = LinkedList()
    for val in [1, 2, 3]:
        ll5.insert_at_end(val)

    sub_ll5 = LinkedList()
    print("Empty sublist:")
    sub_ll5.print_list()
    print(f"Found: {sublist_search(ll5.head, sub_ll5.head)}")

    print("\n" + "=" * 40 + "\n")

    ll6 = LinkedList()
    for val in [1]:
        ll6.insert_at_end(val)

    sub_ll6 = LinkedList()
    for val in [1, 2]:
        sub_ll6.insert_at_end(val)

    print("Single element list:")
    ll6.print_list()
    print("Sublist (1 -> 2):")
    sub_ll6.print_list()
    print(f"Found: {sublist_search(ll6.head, sub_ll6.head)}")
