import random


def rand5() -> int:
    """Generate random integer from 1 to 5 with equal probability."""
    return random.randint(1, 5)


def generate_1_to_7() -> int:
    """Generate integer from 1 to 7 with equal probability using rand5()."""
    while True:
        num = 5 * (rand5() - 1) + (rand5() - 1)
        if num < 21:
            return num % 7 + 1


if __name__ == "__main__":
    results = [generate_1_to_7() for _ in range(10000)]
    counts = {i: results.count(i) for i in range(1, 8)}
    print("Distribution of 1-7 generator:")
    for i in range(1, 8):
        print(f"  {i}: {counts[i]:4d} ({counts[i] / len(results) * 100:.2f}%)")
