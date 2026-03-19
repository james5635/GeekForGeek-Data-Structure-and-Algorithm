class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    node1.next = node2
    node2.next = node3
    node3.next = node1

    print(f"Node 1 data: {node1.data}, next: {node1.next.data}")
    print(f"Node 2 data: {node2.data}, next: {node2.next.data}")
    print(f"Node 3 data: {node3.data}, next: {node3.next.data}")
