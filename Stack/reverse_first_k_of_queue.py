from collections import deque


def reverse_first_k(queue, k):
    if k <= 0 or k > len(queue):
        return queue

    stack = []
    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


if __name__ == "__main__":
    q = deque([1, 2, 3, 4, 5])
    k = 3
    print("Original:", list(q))
    result = reverse_first_k(q, k)
    print(f"Reversed first {k}:", list(result))
