# Frequent Element in Array

## Problem Statement

Given an array, find the most frequent element(s) in the array. If multiple elements have the same maximum frequency, return any or all of them.

## Examples

- **Input:** arr[] = {1, 3, 2, 1, 4, 1}  
  **Output:** 1 (frequency = 3)

- **Input:** arr[] = {10, 20, 10, 20, 30, 20, 20}  
  **Output:** 20 (frequency = 4)

## Approach

Use a **hash map (dictionary)** to count frequencies:
1. Iterate through the array and count occurrences of each element
2. Track the maximum frequency while counting
3. Return the element(s) with maximum frequency

## Variations Implemented

- **most_frequent()**: Returns a single most frequent element
- **most_frequent_all()**: Returns all elements with maximum frequency
- **most_frequent_with_count()**: Returns element along with its count
- **top_k_frequent()**: Returns top k most frequent elements
- **least_frequent()**: Returns elements with minimum frequency
- **frequency_distribution()**: Returns complete frequency map

## Complexity Analysis

- **Time Complexity:** O(n) where n is the size of the array
- **Space Complexity:** O(n) for storing frequency counts

## Files

- `solution.py` - Contains implementation with test cases
