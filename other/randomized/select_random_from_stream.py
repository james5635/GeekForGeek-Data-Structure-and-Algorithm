import random


def select_random_from_stream(stream: list[int]) -> int:
    """Select a random number from stream using O(1) space (reservoir sampling with k=1)."""
    result = None
    for i, num in enumerate(stream):
        if random.randint(0, i) == 0:
            result = num
    return result


if __name__ == "__main__":
    stream = list(range(1, 101))
    counts = {i: 0 for i in range(1, 101)}
    for _ in range(10000):
        selected = select_random_from_stream(stream)
        counts[selected] += 1

    print(f"Stream: {stream[:10]}...{stream[-5:]}")
    print(f"Sample distribution (first 10):")
    for i in range(1, 11):
        print(f"  {i:2d}: {counts[i]:4d} ({counts[i] / 100:.2f}%)")
