from collections import deque


def reverseFirstKUsingRecursion(q: deque, k: int) -> deque:
    if k <= 0:
        return q

    def helper(q: deque, k: int) -> list:
        if k == 0:
            return []
        item = q.popleft()
        result = helper(q, k - 1)
        result.append(item)
        return result

    temp = helper(q, k)
    q.extend(temp)
    for _ in range(len(q) - k):
        q.append(q.popleft())

    return q


def reverseFirstKUsingStack(q: deque, k: int) -> deque:
    if k <= 0:
        return q

    stack = []
    for _ in range(k):
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())

    for _ in range(len(q) - k):
        q.append(q.popleft())

    return q


def reverseFirstKUsingDeque(q: deque, k: int) -> deque:
    if k <= 0:
        return q

    dq = deque()
    for _ in range(k):
        dq.appendleft(q.popleft())

    while dq:
        q.append(dq.popleft())

    for _ in range(len(q) - k):
        q.append(q.popleft())

    return q


if __name__ == "__main__":
    queue = deque([1, 2, 3, 4, 5])
    k = 3
    print("Original queue:", list(queue))
    print(f"k = {k}")
    print("Expected: 3 2 1 4 5")
    print()

    q1 = deque([1, 2, 3, 4, 5])
    print("Using Recursion - O(n) time, O(n) space:")
    print("Result:", list(reverseFirstKUsingRecursion(q1, k)))

    q2 = deque([1, 2, 3, 4, 5])
    print("\nUsing Stack - O(n+k) time, O(k) space:")
    print("Result:", list(reverseFirstKUsingStack(q2, k)))

    q3 = deque([1, 2, 3, 4, 5])
    print("\nUsing Deque - O(n+k) time, O(k) space:")
    print("Result:", list(reverseFirstKUsingDeque(q3, k)))
