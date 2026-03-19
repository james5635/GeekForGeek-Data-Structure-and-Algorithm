def generate_binary_naive(n):
    result = []
    for i in range(1, n + 1):
        result.append(bin(i)[2:])
    return result


def generate_binary_queue(n):
    if n == 0:
        return []
    from collections import deque

    result = []
    queue = deque(["1"])
    for _ in range(n):
        front = queue.popleft()
        result.append(int(front))
        queue.append(front + "0")
        queue.append(front + "1")
    return result


if __name__ == "__main__":
    print(generate_binary_naive(6))
    print(generate_binary_queue(6))
    print(generate_binary_naive(10))
    print(generate_binary_queue(10))
    print(generate_binary_naive(1))
    print(generate_binary_queue(1))
    print(generate_binary_naive(0))
    print(generate_binary_queue(0))
