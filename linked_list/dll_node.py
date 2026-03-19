class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


if __name__ == "__main__":
    node1 = DLLNode(10)
    node2 = DLLNode(20)
    node3 = DLLNode(30)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    print("DLL nodes created successfully")
    print(f"Node 1: data={node1.data}, prev={node1.prev}, next={node1.next.data}")
    print(f"Node 2: data={node2.data}, prev={node2.prev.data}, next={node2.next.data}")
    print(f"Node 3: data={node3.data}, prev={node3.prev.data}, next={node3.next}")
