"""
Smallest Subarray with given GCD

Implements an algorithm to find the length of the smallest subarray
with GCD equal to a given integer k. Uses segment trees for efficient
range GCD queries and binary search to determine minimal subarray length.

Time Complexity: O(n (log n)^2)
Space Complexity: O(n)
"""

import math


def gcd(a: int, b: int) -> int:
    """Compute GCD of two integers using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


class SegmentTree:
    """Segment Tree for range GCD queries."""

    def __init__(self, arr: list):
        self.n = len(arr)
        self.height = math.ceil(math.log2(self.n))
        self.size = 2 * (2**self.height) - 1
        self.tree = [0] * self.size
        self._construct(arr, 0, self.n - 1, 0)

    def _construct(self, arr: list, ss: int, se: int, si: int) -> int:
        """Recursively construct segment tree."""
        if ss == se:
            self.tree[si] = arr[ss]
            return arr[ss]
        mid = ss + (se - ss) // 2
        left = self._construct(arr, ss, mid, si * 2 + 1)
        right = self._construct(arr, mid + 1, se, si * 2 + 2)
        self.tree[si] = gcd(left, right)
        return self.tree[si]

    def _range_gcd(self, ss: int, se: int, qs: int, qe: int, si: int) -> int:
        """Recursive helper for range GCD query."""
        if ss > qe or se < qs:
            return 0
        if qs <= ss and qe >= se:
            return self.tree[si]
        mid = ss + (se - ss) // 2
        left = self._range_gcd(ss, mid, qs, qe, si * 2 + 1)
        right = self._range_gcd(mid + 1, se, qs, qe, si * 2 + 2)
        return gcd(left, right)

    def range_gcd(self, qs: int, qe: int) -> int:
        """Return GCD of elements from index qs to qe (inclusive)."""
        if qs < 0 or qe >= self.n or qs > qe:
            raise ValueError("Invalid query range")
        return self._range_gcd(0, self.n - 1, qs, qe, 0)


def find_smallest_subarray_gcd(arr: list, k: int) -> int:
    """
    Find length of smallest subarray with GCD equal to k.

    Args:
        arr: List of integers
        k: Target GCD value

    Returns:
        Minimal subarray length, or -1 if no such subarray exists
    """
    n = len(arr)

    # Check if k exists directly
    for num in arr:
        if num == k:
            return 1

    # Check if any multiple of k exists
    found = any(num % k == 0 for num in arr)
    if not found:
        return -1

    # Build segment tree
    st = SegmentTree(arr)

    min_len = n + 1

    for i in range(n - 1):
        # Skip if current element is not a multiple of k
        if arr[i] % k != 0:
            continue

        low = i + 1
        high = n - 1
        closest = -1

        # Binary search for the closest end index with GCD k
        while high - low > 1:
            mid = (low + high) // 2
            current_gcd = st.range_gcd(i, mid)
            if current_gcd > k:
                low = mid
            elif current_gcd == k:
                high = mid
                closest = mid
            else:
                high = mid

        # Check remaining candidates
        for j in [low, high]:
            if j < n and st.range_gcd(i, j) == k:
                closest = j
                break

        if closest != -1:
            min_len = min(min_len, closest - i + 1)

    return min_len if min_len != n + 1 else -1


if __name__ == "__main__":
    # Test case 1
    arr1 = [6, 9, 7, 10, 12, 24, 36, 27]
    k1 = 3
    result1 = find_smallest_subarray_gcd(arr1, k1)
    print(f"Test 1 - Smallest subarray length for GCD {k1}: {result1} (Expected: 2)")

    # Test case 2: No k present
    arr2 = [2, 4, 6]
    k2 = 3
    result2 = find_smallest_subarray_gcd(arr2, k2)
    print(f"Test 2 - Smallest subarray length for GCD {k2}: {result2} (Expected: -1)")
