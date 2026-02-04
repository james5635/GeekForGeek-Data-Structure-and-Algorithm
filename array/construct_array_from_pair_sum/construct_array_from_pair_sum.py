"""
Construct array from pair sum array
Given a pair-sum array of n*(n-1)/2 elements, construct the original array.

Key Insight:
- If original array is [a, b, c, d], pair sum array is [a+b, a+c, a+d, b+c, b+d, c+d]
- First three elements of pair sum can help find a, b, c
- a+b + a+c + b+c = 2a + 2b + 2c
- pair[0] + pair[1] + pair[2] = a+b + a+c + b+c = 2(a+b+c)
- So a+b+c = (pair[0] + pair[1] + pair[2]) / 2
- a = (a+b+c) - (b+c) = (a+b+c) - pair[3] (but need to find b+c)
"""

from typing import List


def construct_from_pair_sum_brute_force(pair_sum: List[int]) -> List[int]:
    """
    Brute force: Try all possible combinations (very slow).
    Time: O(n!)
    Space: O(n) for storing array
    """
    n = int((1 + (1 + 8 * len(pair_sum)) ** 0.5) / 2)
    # For n elements, we have n*(n-1)/2 pair sums
    # Too complex for brute force, use mathematical approach
    return construct_from_pair_sum_optimal(pair_sum)


def construct_from_pair_sum_mathematical(pair_sum: List[int]) -> List[int]:
    """
    Mathematical approach using first few pair sums.
    For array [a, b, c, d], pair sums start with [a+b, a+c, a+d, b+c, b+d, c+d]

    Time: O(n^2)
    Space: O(n)
    """
    if not pair_sum:
        return []

    # Calculate n from n*(n-1)/2 = len(pair_sum)
    n = int((1 + (1 + 8 * len(pair_sum)) ** 0.5) / 2)

    if len(pair_sum) != n * (n - 1) // 2:
        return []  # Invalid pair sum array

    result = [0] * n

    if n == 1:
        return result  # Single element, all pair sums are 0
    elif n == 2:
        # Only one pair sum: a+b
        result[0] = pair_sum[0] // 2
        result[1] = pair_sum[0] - result[0]
        return result

    # For n >= 3, use first three pair sums to find a, b, c
    # a+b, a+c, b+c are the first three consecutive pair sums
    ab = pair_sum[0]
    ac = pair_sum[1]
    bc = pair_sum[2]

    # a+b + a+c + b+c = 2(a+b+c)
    # So a+b+c = (ab + ac + bc) / 2
    abc_sum = (ab + ac + bc) // 2

    result[0] = abc_sum - bc  # a = (a+b+c) - (b+c)
    result[1] = abc_sum - ac  # b = (a+b+c) - (a+c)
    result[2] = abc_sum - ab  # c = (a+b+c) - (a+b)

    # Find remaining elements
    for i in range(3, n):
        # result[i] = pair_sum starting with result[0] - result[0]
        # pair[i-1] corresponds to a + result[i]
        result[i] = pair_sum[i - 1] - result[0]

    return result


def construct_from_pair_sum_optimal(pair_sum: List[int]) -> List[int]:
    """
    Optimal solution - similar to mathematical approach but cleaner.
    Time: O(n^2)
    Space: O(n)
    """
    if not pair_sum:
        return []

    # Calculate n from pair sum size
    m = len(pair_sum)
    # n*(n-1)/2 = m => n^2 - n - 2m = 0
    n = int((1 + (1 + 8 * m) ** 0.5) / 2)

    if n * (n - 1) // 2 != m:
        return []  # Invalid input

    if n <= 1:
        return [0] * n
    if n == 2:
        return [pair_sum[0] // 2, pair_sum[0] - pair_sum[0] // 2]

    result = [0] * n

    # Use the first three pair sums to derive first three elements
    # pair[0] = a+b, pair[1] = a+c, pair[2] = b+c
    sum_all = (pair_sum[0] + pair_sum[1] + pair_sum[2]) // 2

    result[0] = sum_all - pair_sum[2]  # a
    result[1] = sum_all - pair_sum[1]  # b
    result[2] = sum_all - pair_sum[0]  # c

    # Derive rest of the elements
    for i in range(3, n):
        result[i] = pair_sum[i - 1] - result[0]

    return result


def test_construct_from_pair_sum():
    """Test all implementations with various test cases"""
    test_cases = [
        # (pair_sum, expected_original)
        ([5, 6, 7, 8, 9, 10], [2, 3, 4, 5]),  # [a+b, a+c, a+d, b+c, b+d, c+d]
        ([5, 7, 9, 8, 10, 12], [3, 4, 5, 6]),
        ([10], [5, 5]),  # n=2 case
        ([], []),  # n=0 case
        ([6, 7, 8, 7, 8, 9], [3, 3, 4, 5]),  # duplicates
    ]

    implementations = [
        ("Mathematical", construct_from_pair_sum_mathematical),
        ("Optimal", construct_from_pair_sum_optimal),
    ]

    print("=" * 60)
    print("CONSTRUCT ARRAY FROM PAIR SUM - TEST RESULTS")
    print("=" * 60)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 40)

        all_passed = True
        for i, (pair_sum, expected) in enumerate(test_cases):
            try:
                result = func(pair_sum)
                # Check if result matches expected
                passed = (
                    sorted(result) == sorted(expected)
                    if result and expected
                    else result == expected
                )
                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_passed = False
                print(f"  Test {i + 1}: {status} - Input: {pair_sum}")
                if not passed:
                    print(f"           Expected: {expected}, Got: {result}")
            except Exception as e:
                all_passed = False
                print(f"  Test {i + 1}: ERROR - {e}")

        print(f"  Overall: {'ALL PASSED' if all_passed else 'SOME FAILED'}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_construct_from_pair_sum()
