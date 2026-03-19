import math


def heap_height(n):
    """
    Calculate the height of a heap with n nodes.
    Height of a heap (complete binary tree) is floor(log2(n)).

    Args:
        n (int): Number of nodes in the heap

    Returns:
        int: Height of the heap
    """
    if n <= 0:
        return 0
    return math.floor(math.log2(n))


def main():
    # Test cases
    test_cases = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        15,
        16,
        17,
        31,
        32,
        33,
        63,
        64,
        65,
        100,
        1000,
    ]

    print("Heap Height Calculation:")
    print("n\tHeight")
    print("----------------")
    for n in test_cases:
        height = heap_height(n)
        print(f"{n}\t{height}")


if __name__ == "__main__":
    main()
