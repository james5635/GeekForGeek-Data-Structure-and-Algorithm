from collections import deque


def reverseQueueUsingStack(q: deque) -> deque:
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q


def reverseQueueUsingRecursion(q: deque) -> deque:
    if not q:
        return q
    item = q.popleft()
    reverseQueueUsingRecursion(q)
    q.append(item)
    return q


if __name__ == "__main__":
    q = deque([5, 10, 15, 20, 25])
    print("Original queue:", list(q))
    print("Expected: 25 20 15 10 5")
    print()

    q1 = deque([5, 10, 15, 20, 25])
    print("Using Stack - O(n) time, O(n) space:")
    print("Reversed:", list(reverseQueueUsingStack(q1)))

    q2 = deque([5, 10, 15, 20, 25])
    print("\nUsing Recursion - O(n) time, O(n) space (call stack):")
    print("Reversed:", list(reverseQueueUsingRecursion(q2)))
