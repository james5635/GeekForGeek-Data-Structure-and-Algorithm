"""
Height of a Complete Binary Tree (or Heap) with N nodes

Problem:
Given the number of nodes N in a Binary Heap, find the height of the heap.

Examples:
Input: N = 6
Output: 2

Input: N = 9
Output: 3

Algorithm:
Since a binary heap is a complete binary tree, its height can be calculated
using the mathematical formula:

    Height = floor(log2(N))

The height of a complete binary tree with N nodes is always floor(log2(N)),
where height is defined as the number of edges on the longest path.

Proof:
- Level 0 has 2^0 = 1 node
- Level 1 has 2^1 = 2 nodes
- Level 2 has 2^2 = 4 nodes
- ...
- Level h has at most 2^h nodes

Total nodes in a complete binary tree of height h:
2^0 + 2^1 + 2^2 + ... + 2^h = 2^(h+1) - 1

So: 2^h <= N <= 2^(h+1) - 1
Taking log base 2: h <= log2(N) < h + 1
Therefore: h = floor(log2(N))

Alternative formula using ceil:
Height = ceil(log2(N + 1)) - 1

Time Complexity: O(1)
Space Complexity: O(1)
"""

import math
from typing import Union


def height_of_heap(N: int) -> int:
    """
    Calculate the height of a complete binary tree (heap) with N nodes.

    Args:
        N: Number of nodes in the heap

    Returns:
        Height of the heap (number of edges on longest path from root to leaf)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return int(math.floor(math.log2(N)))


def height_of_heap_ceil(N: int) -> int:
    """
    Calculate height using the ceil formula.

    Formula: ceil(log2(N + 1)) - 1

    Args:
        N: Number of nodes in the heap

    Returns:
        Height of the heap

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return int(math.ceil(math.log2(N + 1))) - 1


def height_of_heap_iterative(N: int) -> int:
    """
    Calculate height without using log function (iterative approach).

    Args:
        N: Number of nodes in the heap

    Returns:
        Height of the heap

    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    height = 0
    nodes_at_level = 1

    while nodes_at_level <= N:
        height += 1
        nodes_at_level *= 2

    return height - 1


def height_of_heap_bitwise(N: int) -> int:
    """
    Calculate height using bit manipulation (most efficient).

    This method counts the number of bits needed to represent N,
    which is essentially floor(log2(N)) + 1 for height.

    Args:
        N: Number of nodes in the heap

    Returns:
        Height of the heap

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if N <= 0:
        return 0

    height = N.bit_length() - 1
    return height


def min_nodes_at_height(h: int) -> int:
    """
    Calculate minimum number of nodes required to have height h.

    A complete binary tree of height h has at least 2^h nodes
    (when only the leftmost path is filled).
    """
    return 2**h


def max_nodes_at_height(h: int) -> int:
    """
    Calculate maximum number of nodes for a complete binary tree of height h.

    A complete binary tree of height h has at most 2^(h+1) - 1 nodes
    (when completely filled).
    """
    return 2 ** (h + 1) - 1


def height_from_nodes(N: int) -> int:
    """
    Find height given N nodes in a complete binary tree.

    Also known as: ceil(log2(N + 1)) - 1 or floor(log2(N))

    Args:
        N: Number of nodes

    Returns:
        Height of the tree
    """
    return int(math.log2(N))


if __name__ == "__main__":
    test_cases = [
        {"N": 1, "expected": 0},
        {"N": 2, "expected": 1},
        {"N": 3, "expected": 1},
        {"N": 4, "expected": 2},
        {"N": 5, "expected": 2},
        {"N": 6, "expected": 2},
        {"N": 7, "expected": 2},
        {"N": 8, "expected": 3},
        {"N": 9, "expected": 3},
        {"N": 15, "expected": 3},
        {"N": 16, "expected": 4},
        {"N": 31, "expected": 4},
        {"N": 32, "expected": 5},
        {"N": 63, "expected": 5},
        {"N": 64, "expected": 6},
    ]

    print("Heap Height Calculation Test Cases")
    print("=" * 60)

    for i, tc in enumerate(test_cases):
        N = tc["N"]
        expected = tc["expected"]

        result_log = height_of_heap(N)
        result_ceil = height_of_heap_ceil(N)
        result_iter = height_of_heap_iterative(N)
        result_bit = height_of_heap_bitwise(N)

        status = (
            "PASS"
            if all(
                r == expected
                for r in [result_log, result_ceil, result_iter, result_bit]
            )
            else "FAIL"
        )

        print(f"\nTest {i + 1}: N = {N}")
        print(f"  Expected height: {expected}")
        print(f"  floor(log2):      {result_log}")
        print(f"  ceil formula:     {result_ceil}")
        print(f"  iterative:        {result_iter}")
        print(f"  bitwise:          {result_bit}")
        print(f"  Status: {status}")

    print("\n" + "=" * 60)
    print("\nVerification with tree levels:")
    print("-" * 40)

    for h in range(6):
        min_n = min_nodes_at_height(h)
        max_n = max_nodes_at_height(h)
        print(f"Height {h}: {min_n} to {max_n} nodes")

    print("\n" + "=" * 60)
    print("\nComplexity Analysis:")
    print("-" * 40)
    print("Time Complexity:  O(1) for log and bitwise methods")
    print("                  O(log N) for iterative method")
    print("Space Complexity: O(1) for all methods")
    print("\nFormulas:")
    print("- floor(log2(N)) - most common")
    print("- ceil(log2(N + 1)) - 1 - alternative")
    print("- N.bit_length() - 1 - bitwise (Python)")
