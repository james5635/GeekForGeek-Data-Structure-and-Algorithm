from typing import Optional
from node import Node


def delete_node_without_head(node: Optional[Node]) -> None:
    if node is None or node.next is None:
        return
    node.data = node.next.data
    node.next = node.next.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ", end="")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    node_to_delete = head.next.next
    print(f"Deleting node with value {node_to_delete.data}")
    delete_node_without_head(node_to_delete)

    print("After deletion: ", end="")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
