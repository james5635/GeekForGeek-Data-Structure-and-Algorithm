from collections import deque


def generate_binary_naive(n):
    result = []
    for i in range(1, n + 1):
        binary = ""
        num = i
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        result.append(binary)
    return result


def generate_binary_queue(n):
    if n == 0:
        return []
    result = []
    queue = deque(["1"])

    for _ in range(n):
        front = queue.popleft()
        result.append(front)
        queue.append(front + "0")
        queue.append(front + "1")

    return result


def generateBinary(n):
    return generate_binary_queue(n)


if __name__ == "__main__":
    print("Naive (bit manipulation):", generate_binary_naive(6))
    print("Queue Approach:", generate_binary_queue(6))
    print("generateBinary function:", generateBinary(6))
    print("Expected: ['1', '10', '11', '100', '101', '110']")
