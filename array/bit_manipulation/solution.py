"""
Space Optimization using Bit Manipulations

Problem: Demonstrate common array bit manipulation tricks and optimizations
including:
1. Checking/setting/clearing bits
2. Finding unique elements (XOR properties)
3. Counting set bits
4. Finding missing numbers
5. Swapping without extra variable
6. Finding two odd occurring numbers
7. Power of 2 check
8. Finding rightmost set bit

Time Complexity: O(1) for most single operations, O(n) for array operations
Space Complexity: O(1) for most operations

Author: Generated for GeekForGeeks DSA Tutorial
"""

from typing import List, Tuple, Set
from collections import Counter


def check_bit(n: int, pos: int) -> bool:
    """Check if bit at position pos is set in n."""
    return (n >> pos) & 1 == 1


def set_bit(n: int, pos: int) -> int:
    """Set bit at position pos in n."""
    return n | (1 << pos)


def clear_bit(n: int, pos: int) -> int:
    """Clear bit at position pos in n."""
    return n & ~(1 << pos)


def toggle_bit(n: int, pos: int) -> int:
    """Toggle bit at position pos in n."""
    return n ^ (1 << pos)


def count_set_bits(n: int) -> int:
    """Count number of set bits (1s) in binary representation of n."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_set_bits_fast(n: int) -> int:
    """Count set bits using Brian Kernighan's algorithm."""
    count = 0
    while n:
        n &= n - 1  # Clears the lowest set bit
        count += 1
    return count


def is_power_of_2(n: int) -> bool:
    """Check if n is power of 2."""
    return n > 0 and (n & (n - 1)) == 0


def get_rightmost_set_bit(n: int) -> int:
    """Get the rightmost set bit (position 0-indexed)."""
    if n == 0:
        return -1
    return (n & -n).bit_length() - 1


def swap_without_temp(a: int, b: int) -> Tuple[int, int]:
    """Swap two numbers without using temporary variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def find_unique_xor(arr: List[int]) -> int:
    """
    Find element that appears odd number of times.
    All other elements appear even number of times.
    """
    result = 0
    for num in arr:
        result ^= num
    return result


def find_two_unique(arr: List[int]) -> Tuple[int, int]:
    """
    Find two elements that appear odd number of times.
    All other elements appear even number of times.
    """
    xor_all = 0
    for num in arr:
        xor_all ^= num

    # Get rightmost set bit
    rightmost_bit = xor_all & -xor_all

    x, y = 0, 0
    for num in arr:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num

    return (x, y)


def find_missing_number(arr: List[int], n: int) -> int:
    """
    Find missing number in array containing 1 to n with one missing.
    """
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


def find_missing_two_numbers(arr: List[int], n: int) -> Tuple[int, int]:
    """
    Find two missing numbers in array containing 1 to n with two missing.
    """
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    xor_missing = xor_all ^ xor_arr

    # Find rightmost set bit
    rightmost_bit = xor_missing & -xor_missing

    x, y = 0, 0
    for i in range(1, n + 1):
        if i & rightmost_bit:
            x ^= i
        else:
            y ^= i

    for num in arr:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num

    return (x, y)


def get_all_subsets(arr: List[int]) -> List[List[int]]:
    """Generate all subsets using bit manipulation."""
    n = len(arr)
    subsets = []

    # 2^n subsets
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        subsets.append(subset)

    return subsets


def find_duplicates_bitmask(arr: List[int]) -> Set[int]:
    """
    Find duplicates in array using bit manipulation (for small integers).
    Works for integers in range 0-63.
    """
    seen = 0
    duplicates = set()

    for num in arr:
        if 0 <= num < 64:
            if seen & (1 << num):
                duplicates.add(num)
            else:
                seen |= 1 << num

    return duplicates


def reverse_bits(n: int, bit_size: int = 32) -> int:
    """Reverse bits of n."""
    result = 0
    for i in range(bit_size):
        if n & (1 << i):
            result |= 1 << (bit_size - 1 - i)
    return result


def next_higher_with_same_set_bits(n: int) -> int:
    """Find next higher number with same number of set bits."""
    c = n
    c0 = c1 = 0

    # Count trailing zeros
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1

    # Count ones
    while c & 1:
        c1 += 1
        c >>= 1

    # If n is of form 0b111...000, there's no larger number
    if c0 + c1 == 0 or c0 + c1 == 31:
        return -1

    # Position of rightmost non-trailing zero
    p = c0 + c1

    # Flip rightmost non-trailing zero
    n |= 1 << p

    # Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Insert (c1-1) ones on the right
    n |= (1 << (c1 - 1)) - 1

    return n


if __name__ == "__main__":
    # Test Case 1: Basic bit operations
    print("=" * 60)
    print("Test Case 1: Basic Bit Operations")
    print("=" * 60)

    n = 0b10110110  # 182 in decimal
    print(f"Number: {n} (binary: {bin(n)})")
    print(f"Check bit 3: {check_bit(n, 3)}")
    print(f"Check bit 4: {check_bit(n, 4)}")
    print(f"Set bit 2: {bin(set_bit(n, 2))}")
    print(f"Clear bit 1: {bin(clear_bit(n, 1))}")
    print(f"Toggle bit 5: {bin(toggle_bit(n, 5))}")

    # Test Case 2: Count set bits
    print("\n" + "=" * 60)
    print("Test Case 2: Count Set Bits")
    print("=" * 60)

    test_numbers = [0, 1, 7, 15, 16, 255, 1023]
    for num in test_numbers:
        count_normal = count_set_bits(num)
        count_fast = count_set_bits_fast(num)
        print(f"{num:4d} ({bin(num):12s}): {count_normal} bits (fast: {count_fast})")

    # Test Case 3: Power of 2
    print("\n" + "=" * 60)
    print("Test Case 3: Power of 2 Check")
    print("=" * 60)

    test_powers = [0, 1, 2, 3, 4, 15, 16, 17, 32, 64, 100]
    for num in test_powers:
        result = is_power_of_2(num)
        print(f"{num:3d} is power of 2: {result}")

    # Test Case 4: Rightmost set bit
    print("\n" + "=" * 60)
    print("Test Case 4: Rightmost Set Bit Position")
    print("=" * 60)

    test_rightmost = [1, 2, 8, 10, 16, 18, 32, 48]
    for num in test_rightmost:
        pos = get_rightmost_set_bit(num)
        print(f"{num:2d} ({bin(num):8s}): rightmost set bit at position {pos}")

    # Test Case 5: Swap without temp
    print("\n" + "=" * 60)
    print("Test Case 5: Swap Without Temporary Variable")
    print("=" * 60)

    a, b = 5, 10
    print(f"Before: a={a}, b={b}")
    a, b = swap_without_temp(a, b)
    print(f"After:  a={a}, b={b}")

    # Test Case 6: Find unique using XOR
    print("\n" + "=" * 60)
    print("Test Case 6: Find Unique Element (XOR)")
    print("=" * 60)

    arr1 = [4, 3, 4, 4, 4, 3, 3, 3, 5]  # 5 appears once
    unique1 = find_unique_xor(arr1)
    print(f"Array: {arr1}")
    print(f"Unique element: {unique1}")

    arr2 = [1, 2, 3, 2, 3, 1, 4]  # 4 appears once
    unique2 = find_unique_xor(arr2)
    print(f"\nArray: {arr2}")
    print(f"Unique element: {unique2}")

    # Test Case 7: Find two unique elements
    print("\n" + "=" * 60)
    print("Test Case 7: Find Two Unique Elements")
    print("=" * 60)

    arr3 = [4, 2, 4, 5, 2, 3, 3, 1]  # 5 and 1 appear once
    unique_two = find_two_unique(arr3)
    print(f"Array: {arr3}")
    print(f"Two unique elements: {unique_two}")

    # Test Case 8: Find missing number
    print("\n" + "=" * 60)
    print("Test Case 8: Find Missing Number")
    print("=" * 60)

    arr4 = [1, 2, 4, 5, 6]  # Missing 3
    missing = find_missing_number(arr4, 6)
    print(f"Array (1-6 with one missing): {arr4}")
    print(f"Missing number: {missing}")

    # Test Case 9: Find two missing numbers
    print("\n" + "=" * 60)
    print("Test Case 9: Find Two Missing Numbers")
    print("=" * 60)

    arr5 = [1, 3, 5, 6]  # Missing 2 and 4
    missing_two = find_missing_two_numbers(arr5, 6)
    print(f"Array (1-6 with two missing): {arr5}")
    print(f"Two missing numbers: {missing_two}")

    # Test Case 10: All subsets
    print("\n" + "=" * 60)
    print("Test Case 10: Generate All Subsets")
    print("=" * 60)

    arr6 = [1, 2, 3]
    subsets = get_all_subsets(arr6)
    print(f"Array: {arr6}")
    print(f"All {len(subsets)} subsets:")
    for i, subset in enumerate(subsets):
        print(f"  {i:2d}: {subset}")

    # Test Case 11: Find duplicates using bitmask
    print("\n" + "=" * 60)
    print("Test Case 11: Find Duplicates (Bitmask)")
    print("=" * 60)

    arr7 = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    duplicates = find_duplicates_bitmask(arr7)
    print(f"Array: {arr7}")
    print(f"Duplicates: {duplicates}")

    # Test Case 12: Next higher with same set bits
    print("\n" + "=" * 60)
    print("Test Case 12: Next Higher with Same Set Bits")
    print("=" * 60)

    test_next = [6, 11, 13948]
    for num in test_next:
        next_num = next_higher_with_same_set_bits(num)
        print(f"{num} ({bin(num)})")
        print(f"  -> {next_num} ({bin(next_num) if next_num > 0 else 'N/A'})")
        if next_num > 0:
            print(f"  Set bits: {count_set_bits(num)} -> {count_set_bits(next_num)}")

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
