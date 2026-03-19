import heapq


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


def merge_k_sorted(lists):
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, (head.data, id(head), head))

    dummy = Node(0)
    current = dummy

    while heap:
        data, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.data, id(node.next), node.next))

    return dummy.next


if __name__ == "__main__":
    lists = []
    for arr in [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]:
        ll = LinkedList()
        for val in arr:
            ll.insert_at_end(val)
        lists.append(ll.head)

    print("Input Lists:")
    for i, head in enumerate(lists):
        print(f"List {i + 1}:", end=" ")
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    merged = merge_k_sorted(lists)
    print("\nMerged List:")
    current = merged
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    lists2 = []
    for arr in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]:
        ll = LinkedList()
        for val in arr:
            ll.insert_at_end(val)
        lists2.append(ll.head)

    print("Input Lists:")
    for i, head in enumerate(lists2):
        print(f"List {i + 1}:", end=" ")
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    merged2 = merge_k_sorted(lists2)
    print("\nMerged List:")
    current = merged2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    lists3 = [[1], [2], [3]]
    heads3 = []
    for arr in lists3:
        ll = LinkedList()
        for val in arr:
            ll.insert_at_end(val)
        heads3.append(ll.head)

    merged3 = merge_k_sorted(heads3)
    print("Merged Single Element Lists:")
    current = merged3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
