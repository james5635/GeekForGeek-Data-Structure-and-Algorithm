import random


def rand2() -> int:
    """Generate random 0 or 1 with equal probability."""
    return random.randint(0, 1)


def rand3_from_rand2() -> int:
    """Implement rand3() using rand2() by generating 2 bits and rejecting 11."""
    while True:
        val = (rand2() << 1) | rand2()
        if val < 3:
            return val


if __name__ == "__main__":
    results = [rand3_from_rand2() for _ in range(20)]
    print(results)
    counts = [results.count(i) for i in range(3)]
    print(f"Counts: {counts}")
