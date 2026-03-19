from collections import deque


def reverse_queue_stack(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q


def reverse_queue_recursive(q):
    if not q:
        return
    item = q.popleft()
    reverse_queue_recursive(q)
    q.append(item)


if __name__ == "__main__":
    q1 = deque([5, 10, 15, 20, 25])
    print(f"Original Queue: {list(q1)}")
    reverse_queue_stack(q1)
    print(f"Reversed (Stack): {list(q1)}")
    print()

    q2 = deque([5, 10, 15, 20, 25])
    print(f"Original Queue: {list(q2)}")
    reverse_queue_recursive(q2)
    print(f"Reversed (Recursive): {list(q2)}")
    print()

    q3 = deque([1, 2, 3])
    print(f"Original Queue: {list(q3)}")
    reverse_queue_stack(q3)
    print(f"Reversed (Stack): {list(q3)}")
    print()

    q4 = deque([42])
    print(f"Original Queue: {list(q4)}")
    reverse_queue_recursive(q4)
    print(f"Reversed (Recursive): {list(q4)}")
