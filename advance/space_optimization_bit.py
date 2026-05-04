"""
Space Optimization using Bit Manipulations

This module demonstrates how to use bit manipulation to optimize space when
storing binary values (presence/absence). Instead of using one integer per index,
we pack 32 boolean flags into a single integer using individual bit positions.

This reduces space usage by a factor of 32 compared to a regular integer array.

Key operations:
    - setbit: Turn on a specific bit at the given index
    - checkbit: Check if a specific bit at the given index is set

Bit manipulation formulas:
    - Array index: index >> 5 (equivalent to index // 32)
    - Bit position: index & 31 (equivalent to index % 32)
    - Set bit: array[index >> 5] |= (1 << (index & 31))
    - Check bit: array[index >> 5] & (1 << (index & 31))

Time Complexity: O(|b - a|) for marking and checking
Space Complexity: O(|b - a| / 32) - 32x more space efficient than array approach
"""

import math


class BitArray:
    """A space-efficient bit array using integer bit manipulation."""

    def __init__(self, size):
        """
        Initialize a bit array of the given size.

        Args:
            size: Number of bits needed
        """
        self.size = size
        self.num_ints = math.ceil(size / 32)
        self.array = [0] * self.num_ints

    def setbit(self, index):
        """
        Set the bit at the given index to 1.

        Args:
            index: The bit position to set
        """
        if 0 <= index < self.size:
            self.array[index >> 5] |= 1 << (index & 31)

    def checkbit(self, index):
        """
        Check if the bit at the given index is set.

        Args:
            index: The bit position to check

        Returns:
            True if bit is set, False otherwise
        """
        if 0 <= index < self.size:
            return bool(self.array[index >> 5] & (1 << (index & 31)))
        return False


def find_multiples(a, b, divisors=None):
    """
    Find all numbers in range [a, b] that are multiples of given divisors
    using bit manipulation for space optimization.

    Args:
        a: Start of range (inclusive)
        b: End of range (inclusive)
        divisors: List of divisors to check (default: [2, 5])

    Returns:
        List of numbers in [a, b] that are multiples of any divisor
    """
    if divisors is None:
        divisors = [2, 5]

    size = abs(b - a) + 1
    bit_array = BitArray(size)

    for i in range(a, b + 1):
        for d in divisors:
            if i % d == 0:
                bit_array.setbit(i - a)
                break

    result = []
    for i in range(a, b + 1):
        if bit_array.checkbit(i - a):
            result.append(i)

    return result


if __name__ == "__main__":
    print("=== Space Optimization using Bit Manipulations ===")
    print()

    print("Test 1: Find multiples of 2 and 5 in range [2, 10]")
    result1 = find_multiples(2, 10)
    print(f"Result: {result1}")
    print(f"Expected: [2, 4, 5, 6, 8, 10]")
    print()

    print("Test 2: Find multiples of 2 and 5 in range [60, 95]")
    result2 = find_multiples(60, 95)
    print(f"Result: {result2}")
    print(
        f"Expected: [60, 62, 64, 65, 66, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 88, 90, 92, 94, 95]"
    )
    print()

    print("=== Bit Array Demo ===")
    bit_array = BitArray(64)

    bit_array.setbit(0)
    bit_array.setbit(31)
    bit_array.setbit(32)
    bit_array.setbit(63)

    print(f"Bit at index 0: {bit_array.checkbit(0)} (expected: True)")
    print(f"Bit at index 31: {bit_array.checkbit(31)} (expected: True)")
    print(f"Bit at index 32: {bit_array.checkbit(32)} (expected: True)")
    print(f"Bit at index 63: {bit_array.checkbit(63)} (expected: True)")
    print(f"Bit at index 15: {bit_array.checkbit(15)} (expected: False)")
    print(f"Number of integers used: {bit_array.num_ints} (for 64 bits)")
