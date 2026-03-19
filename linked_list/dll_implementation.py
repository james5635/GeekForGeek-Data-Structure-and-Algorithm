from dll_node import DLLNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty list")

    def display_reverse(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements) if elements else "Empty list")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)

    print("Forward: ", end="")
    dll.display()

    print("Reverse: ", end="")
    dll.display_reverse()
