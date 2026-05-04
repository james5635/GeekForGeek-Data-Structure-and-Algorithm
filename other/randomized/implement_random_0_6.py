import random


def rand01() -> int:
    """Generate random 0 or 1 with equal probability."""
    return random.randint(0, 1)


def random_0_to_6() -> int:
    """Generate random integer from 0 to 6 using random 0-1 generator."""
    while True:
        num = 0
        for _ in range(3):
            num = (num << 1) | rand01()
        if num <= 6:
            return num


if __name__ == "__main__":
    results = [random_0_to_6() for _ in range(10000)]
    counts = {i: results.count(i) for i in range(7)}
    print("Distribution of 0-6 generator:")
    for i in range(7):
        print(f"  {i}: {counts[i]:4d} ({counts[i] / len(results) * 100:.2f}%)")
