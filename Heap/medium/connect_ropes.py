"""
Connect N Ropes with Minimum Cost - GeeksforGeeks
https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

Problem: Given an array of rope lengths, connect all ropes into a single rope with
minimum total cost. Cost to connect two ropes = sum of their lengths.

Approach: Greedy with Min Heap
- Always connect the two shortest ropes first (like Huffman coding)
- This minimizes the total cost

Time Complexity: O(n*log(n))
Space Complexity: O(n)
"""

import heapq


def min_cost(arr):
    """
    Calculate minimum cost to connect all ropes.

    Args:
        arr: List of rope lengths

    Returns:
        Minimum total cost to connect all ropes
    """
    heapq.heapify(arr)
    res = 0

    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        cost = first + second
        res += cost

        heapq.heappush(arr, cost)

    return res


def min_cost_verbose(arr):
    """
    Calculate minimum cost with step-by-step explanation.
    """
    heapq.heapify(arr)
    res = 0
    steps = []

    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        cost = first + second
        res += cost
        steps.append(f"Connect {first} + {second} = {cost}")

        heapq.heappush(arr, cost)

    return res, steps


if __name__ == "__main__":
    # Example 1
    ropes = [4, 3, 2, 6]
    print(f"Minimum cost: {min_cost(ropes)}")  # Output: 29

    # Step-by-step
    cost, steps = min_cost_verbose([4, 3, 2, 6])
    print(f"\nSteps:")
    for step in steps:
        print(f"  {step}")
    print(f"Total cost: {cost}")

    # Example 2: Single rope
    ropes = [10]
    print(f"\nMinimum cost (single rope): {min_cost(ropes)}")  # Output: 0

    # Example 3
    ropes = [1, 2, 3, 4, 5]
    cost, steps = min_cost_verbose(ropes)
    print(f"\nFor ropes [1,2,3,4,5]:")
    for step in steps:
        print(f"  {step}")
    print(f"Total cost: {cost}")
