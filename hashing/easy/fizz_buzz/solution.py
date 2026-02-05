"""
Fizz Buzz Implementation

Problem: Print numbers from 1 to n with the following replacements:
    - Print "FizzBuzz" if number is divisible by both 3 and 5
    - Print "Fizz" if number is divisible by 3
    - Print "Buzz" if number is divisible by 5
    - Print the number itself if none of the above conditions are met

Example:
    Input: n = 15
    Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

Approach:
    Iterate from 1 to n and use modulo operator to check divisibility.
    Can also use a hash map to store divisors and their corresponding strings.

Time Complexity: O(n)
Space Complexity: O(1) for basic version, O(k) for hash map version where k is number of rules
"""


def fizz_buzz(n):
    """
    Standard FizzBuzz implementation.

    Args:
        n: Upper limit (inclusive)

    Returns:
        list: List of strings/numbers representing FizzBuzz sequence
    """
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


def fizz_buzz_hash_map(n):
    """
    FizzBuzz using hash map approach - more scalable for adding new rules.

    Args:
        n: Upper limit (inclusive)

    Returns:
        list: List of strings representing FizzBuzz sequence
    """
    # Hash map of divisors and their corresponding strings
    divisors = {3: "Fizz", 5: "Buzz"}

    result = []

    for i in range(1, n + 1):
        current = ""

        # Check all divisors in the hash map
        for divisor, word in divisors.items():
            if i % divisor == 0:
                current += word

        # If no divisor matched, use the number itself
        if not current:
            current = str(i)

        result.append(current)

    return result


def fizz_buzz_optimized(n):
    """
    Optimized FizzBuzz without using modulo operation.
    Uses counters to track divisibility.

    Args:
        n: Upper limit (inclusive)

    Returns:
        list: List of strings/numbers representing FizzBuzz sequence
    """
    result = []
    fizz_count = 0
    buzz_count = 0

    for i in range(1, n + 1):
        fizz_count += 1
        buzz_count += 1

        current = ""

        if fizz_count == 3:
            current += "Fizz"
            fizz_count = 0

        if buzz_count == 5:
            current += "Buzz"
            buzz_count = 0

        if not current:
            current = str(i)

        result.append(current)

    return result


if __name__ == "__main__":
    # Test Case 1: Standard FizzBuzz up to 15
    print("Test 1 - Standard FizzBuzz (n=15):")
    result = fizz_buzz(15)
    print(", ".join(result))
    # Expected: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

    # Test Case 2: Hash Map version
    print("\nTest 2 - Hash Map FizzBuzz (n=15):")
    result = fizz_buzz_hash_map(15)
    print(", ".join(result))

    # Test Case 3: Optimized version
    print("\nTest 3 - Optimized FizzBuzz (n=15):")
    result = fizz_buzz_optimized(15)
    print(", ".join(result))

    # Test Case 4: n = 1
    print("\nTest 4 - n=1:")
    print(fizz_buzz(1))  # Expected: ['1']

    # Test Case 5: n = 5
    print("\nTest 5 - n=5:")
    print(fizz_buzz(5))  # Expected: ['1', '2', 'Fizz', '4', 'Buzz']

    # Test Case 6: Large n
    print("\nTest 6 - n=30 (last 5 elements):")
    result = fizz_buzz(30)
    print(result[-5:])  # Expected: ['29', 'FizzBuzz', '31', '32', 'Fizz']
