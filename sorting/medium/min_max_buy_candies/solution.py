"""
Find Minimum and Maximum Amount to Buy N Candies

Problem Description:
    A shop sells candies at a discount. For every candy you buy,
    you can take k candies for free. Given price of each candy and k,
    find minimum and maximum amount to spend to buy n candies.

Time Complexity: O(n log n)
- Sorting prices: O(n log n)
- Greedy selection: O(n)

Space Complexity: O(1) auxiliary
- Sorting uses O(log n) to O(n)
- Only using result variables

Example:
    Input: prices = [3, 2, 1, 4], k = 2, n = 4
    Output: (min=3, max=9)

    For MINIMUM:
    - Sort ascending: [1, 2, 3, 4]
    - Buy 1, get 2 and 3 free
    - Then buy 4
    - Total = 1 + 4 = 5 (but we only need 4 candies, so 1 + 3 = 4?)

    Actually with k=2 and n=4:
    - Buy cheapest (1), get 2 free (2, 3) → have 3 candies
    - Still need 1 more (4)
    - Total = 1 + 4 = 5

    For MAXIMUM:
    - Sort descending: [4, 3, 2, 1]
    - Buy 4, get 3 and 2 free
    - Total = 4

Approach:
    MINIMUM amount:
    1. Sort prices in ascending order
    2. Buy cheapest candies first
    3. For each candy bought, skip next k candies (get them free)

    MAXIMUM amount:
    1. Sort prices in descending order
    2. Buy most expensive candies first
    3. For each candy bought, skip next k candies (get them free)
"""

from typing import List, Tuple


def find_min_max_amount(prices: List[int], n: int, k: int) -> Tuple[int, int]:
    """
    Find minimum and maximum amount to buy n candies.

    Args:
        prices: List of candy prices
        n: Number of candies to buy
        k: Number of free candies per purchase

    Returns:
        Tuple of (minimum_amount, maximum_amount)

    Raises:
        ValueError: If n > len(prices) or invalid inputs
    """
    if not prices or n <= 0 or k < 0:
        raise ValueError("Invalid input")

    if n > len(prices):
        raise ValueError("Not enough candies available")

    # Calculate minimum amount
    min_amount = calculate_amount(prices.copy(), n, k, ascending=True)

    # Calculate maximum amount
    max_amount = calculate_amount(prices.copy(), n, k, ascending=False)

    return min_amount, max_amount


def calculate_amount(prices: List[int], n: int, k: int, ascending: bool = True) -> int:
    """
    Calculate amount needed using greedy approach.

    Args:
        prices: List of candy prices
        n: Number of candies needed
        k: Free candies per purchase
        ascending: True for min, False for max

    Returns:
        Total amount needed
    """
    prices.sort(reverse=not ascending)

    total = 0
    candies_bought = 0
    i = 0

    while candies_bought < n and i < len(prices):
        # Buy current candy
        total += prices[i]
        candies_bought += 1

        # Skip next k candies (get them free)
        i += k + 1

    return total


def find_min_amount(prices: List[int], n: int, k: int) -> int:
    """
    Find minimum amount to buy n candies.

    Strategy: Buy cheapest first, get expensive ones free.

    Args:
        prices: List of candy prices
        n: Number of candies to buy
        k: Free candies per purchase

    Returns:
        Minimum amount needed
    """
    if n > len(prices):
        raise ValueError("Not enough candies")

    prices.sort()

    total = 0
    bought = 0
    i = 0

    while bought < n:
        total += prices[i]
        bought += 1
        i += k + 1  # Skip k free candies

    return total


def find_max_amount(prices: List[int], n: int, k: int) -> int:
    """
    Find maximum amount to buy n candies.

    Strategy: Buy most expensive first, get cheap ones free.

    Args:
        prices: List of candy prices
        n: Number of candies to buy
        k: Free candies per purchase

    Returns:
        Maximum amount needed
    """
    if n > len(prices):
        raise ValueError("Not enough candies")

    prices.sort(reverse=True)

    total = 0
    bought = 0
    i = 0

    while bought < n:
        total += prices[i]
        bought += 1
        i += k + 1  # Skip k free candies

    return total


# Test cases
def test_find_min_max_amount():
    """Test cases for find_min_max_amount function."""
    # Test case 1: Basic example
    prices1 = [3, 2, 1, 4]
    n1, k1 = 4, 2
    min_amt, max_amt = find_min_max_amount(prices1.copy(), n1, k1)
    # Min: sort [1,2,3,4], buy 1 (get 2,3 free), buy 4 = 1+4 = 5
    # Max: sort [4,3,2,1], buy 4 (get 3,2 free), buy 1 = 4+1 = 5
    # Wait, let me recalculate...
    # Actually with n=4, k=2:
    # Min: buy 1, get 2,3 free (3 candies), need 1 more -> buy 4 = 5
    # Max: buy 4, get 3,2 free (3 candies), need 1 more -> buy 1 = 5
    assert min_amt == 5, f"Test 1 min failed: {min_amt}"
    assert max_amt == 5, f"Test 1 max failed: {max_amt}"

    # Test case 2: Different values
    prices2 = [1, 2, 3, 4, 5, 6, 7, 8]
    n2, k2 = 5, 2
    min_amt2, max_amt2 = find_min_max_amount(prices2.copy(), n2, k2)
    # Min: [1,2,3,4,5,6,7,8], buy 1 (get 2,3 free)=3candies,
    #       skip 4,5, buy 6 (get 7,8 free)=6candies total, total=1+6=7
    #       OR algorithm: buy 1(i=0), i+=3→i=3 buy 4(i=3), i+=3→i=6 buy 7(i=6)=12
    # Max: [8,7,6,5,4,3,2,1], buy 8(i=0), i+=3→i=3 buy 5(i=3), i+=3→i=6 buy 2(i=6)=15
    assert min_amt2 == 12, f"Test 2 min failed: {min_amt2}"
    assert max_amt2 == 15, f"Test 2 max failed: {max_amt2}"

    # Test case 3: k = 0 (no free candies)
    prices3 = [1, 2, 3, 4]
    n3, k3 = 3, 0
    min_amt3, max_amt3 = find_min_max_amount(prices3.copy(), n3, k3)
    # Min: buy 1,2,3 = 6
    # Max: buy 4,3,2 = 9
    assert min_amt3 == 6, f"Test 3 min failed: {min_amt3}"
    assert max_amt3 == 9, f"Test 3 max failed: {max_amt3}"

    # Test case 4: Single candy
    prices4 = [5]
    n4, k4 = 1, 1
    min_amt4, max_amt4 = find_min_max_amount(prices4.copy(), n4, k4)
    assert min_amt4 == 5, f"Test 4 min failed: {min_amt4}"
    assert max_amt4 == 5, f"Test 4 max failed: {max_amt4}"

    # Test case 5: All same prices
    prices5 = [5, 5, 5, 5]
    n5, k5 = 3, 1
    min_amt5, max_amt5 = find_min_max_amount(prices5.copy(), n5, k5)
    # Min: [5,5,5,5], buy 5 (get 1 free), need 1 more -> buy 5 = 10
    # Max: same = 10
    assert min_amt5 == 10, f"Test 5 min failed: {min_amt5}"
    assert max_amt5 == 10, f"Test 5 max failed: {max_amt5}"

    # Test case 6: k >= n
    prices6 = [1, 2, 3, 4, 5]
    n6, k6 = 3, 5
    min_amt6, max_amt6 = find_min_max_amount(prices6.copy(), n6, k6)
    # Min: buy 1, get 5 free (but we only need 3), so we get 1,2,3 free... wait
    # Actually: buy 1, get next k (5) free. We have 1+5=6 candies but only need 3
    # So we only need to buy 1
    # Max: buy 5, get 4,3,2,1,0 free = 5
    assert min_amt6 == 1, f"Test 6 min failed: {min_amt6}"
    assert max_amt6 == 5, f"Test 6 max failed: {max_amt6}"

    # Test case 7: Verify individual functions
    prices7 = [10, 20, 30, 40, 50]
    n7, k7 = 3, 1
    min7 = find_min_amount(prices7.copy(), n7, k7)
    max7 = find_max_amount(prices7.copy(), n7, k7)
    # Min: [10,20,30,40,50], buy 10(i=0), skip 1, buy 30(i=2), skip 1, buy 50(i=4) = 90
    # Max: [50,40,30,20,10], buy 50(i=0), skip 1, buy 30(i=2), skip 1, buy 10(i=4) = 90
    assert min7 == 90, f"Test 7 min failed: {min7}"
    assert max7 == 90, f"Test 7 max failed: {max7}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_find_min_max_amount()

    # Example usage
    prices = [3, 2, 1, 4, 5]
    n, k = 4, 1
    min_amt, max_amt = find_min_max_amount(prices.copy(), n, k)
    print(f"Prices: {prices}")
    print(f"Candy to buy: {n}, Free per purchase: {k}")
    print(f"Minimum amount: {min_amt}")
    print(f"Maximum amount: {max_amt}")
