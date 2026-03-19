from collections import deque


def check_queue_sortable(queue):
    stack = []
    expected = 1
    temp_queue = deque(queue)

    while temp_queue:
        if temp_queue[0] == expected:
            temp_queue.popleft()
            expected += 1
        elif stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            stack.append(temp_queue.popleft())

    while stack:
        if stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            return False
    return True


if __name__ == "__main__":
    q1 = [5, 1, 2, 3, 4]
    print(f"Queue {q1}: {check_queue_sortable(q1)}")

    q2 = [5, 1, 2, 6, 3, 4]
    print(f"Queue {q2}: {check_queue_sortable(q2)}")
