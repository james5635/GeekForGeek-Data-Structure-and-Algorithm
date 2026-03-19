from collections import deque


def move_k_to_end(queue, k):
    if k == 0:
        return
    front = queue.popleft()
    move_k_to_end(queue, k - 1)
    queue.append(front)


def reverse_first_k_recursive(queue, k):
    if not queue or k <= 0:
        return queue
    size = len(queue)
    k = min(k, size)
    move_k_to_end(queue, k)
    for _ in range(size - k):
        queue.append(queue.popleft())
    return queue


def reverse_first_k_stack(queue, k):
    if not queue or k <= 0:
        return queue
    stack = []
    for i in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    size = len(queue)
    for _ in range(size - k):
        queue.append(queue.popleft())
    return queue


def reverse_first_k_deque(queue, k):
    if not queue or k <= 0:
        return queue
    dq = deque(queue)
    stack = []
    for i in range(k):
        stack.append(dq.popleft())
    result = deque()
    while stack:
        result.append(stack.pop())
    while dq:
        result.append(dq.popleft())
    return result


if __name__ == "__main__":
    q1 = deque([1, 2, 3, 4, 5])
    print(list(reverse_first_k_recursive(q1, 3)))

    q2 = deque([1, 2, 3, 4, 5])
    print(list(reverse_first_k_stack(q2, 3)))

    q3 = deque([1, 2, 3, 4, 5])
    print(list(reverse_first_k_deque(q3, 3)))
