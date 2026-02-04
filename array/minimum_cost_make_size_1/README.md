# Minimum Cost to Make Array Size 1 by Removing Larger Pairs

This directory contains the implementation to find the minimum cost to reduce an array to a single element by repeatedly removing the larger of a pair.

## Problem Statement

Given an array of n integers, reduce the size of the array to one. We are allowed to select a pair of integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation is equal to the value of the smaller one. Find the minimum sum of costs of operations needed to convert the array into a single element.

### Examples

**Input:** `arr[] = [4, 3, 2]`  
**Output:** `4`  
**Explanation:** Choose (4, 2) so 4 is removed, new array = {2, 3}, cost = 2. Now choose (2, 3) so 3 is removed, cost = 2. Total cost = 2 + 2 = 4.

**Input:** `arr[] = [3, 4]`  
**Output:** `3`  
**Explanation:** Choose (3, 4) so cost is 3.

## Algorithm Approach

### Greedy Approach - Single Pass
- **File:** `min_cost_make_size_1.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Find the minimum element in the array
  - The minimum cost is `(n - 1) * min_element`
  - This is because we need (n-1) operations to reduce array to size 1
  - In each operation, we pair the minimum with another element and pay the minimum value

### Key Insight
The optimal strategy is to always pair the minimum element with other elements. Since the cost of each operation is the smaller value in the pair, we want the smallest element to be the "cost payer" in all operations. There are exactly (n-1) operations needed to reduce an array of size n to 1 element.

## Usage

The implementation file can be run independently:

```bash
python min_cost_make_size_1.py
```

The file includes comprehensive test cases to demonstrate functionality.

## Algorithm Steps

1. Find the minimum element in the array
2. Calculate the cost as `(n - 1) * min_element`
3. Return the result

## Mathematical Proof

**Why is this optimal?**
- To reduce array size from n to 1, we need exactly (n-1) removal operations
- Each operation removes one element by pairing it with another
- The cost of removing an element is the value of the smaller element in the pair
- To minimize total cost, we want the smallest possible cost for each operation
- The minimum element in the array is the smallest possible cost for any operation
- By always pairing the minimum element with other elements, we ensure:
  - All (n-1) operations cost exactly the minimum element value
  - This is the absolute minimum possible since no smaller value exists
- Therefore, minimum cost = (n-1) × minimum_element

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Greedy | O(n) | O(1) |

The greedy approach is optimal with O(n) time and O(1) space complexity.
