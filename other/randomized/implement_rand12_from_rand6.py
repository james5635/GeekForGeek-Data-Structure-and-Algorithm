import random


def rand6() -> int:
    """Generate random integer from 1 to 6."""
    return random.randint(1, 6)


def rand12_from_rand6() -> int:
    """Implement rand12() using rand6() in one line."""
    return rand6() + 6 * (rand6() % 2)


if __name__ == "__main__":
    results = [rand12_from_rand6() for _ in range(10000)]
    counts = {i: results.count(i) for i in range(1, 13)}
    print("Distribution of rand12():")
    for i in range(1, 13):
        print(f"  {i:2d}: {counts[i]:4d} ({counts[i] / len(results) * 100:.2f}%)")
