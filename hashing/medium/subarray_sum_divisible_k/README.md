# Find Subarray Sum Divisible by K

## Problem Statement
Given an array arr[] and an integer k, count all subarrays whose sum is divisible by k.

## Approach
Use prefix sum with hashing:
- Track prefix sum modulo k
- If same remainder seen at indices i and j, subarray (i+1 to j) sum is divisible by k
- Store frequency of each remainder in hashmap
- For each element, add count of previous same remainders

## Complexity
- **Time**: O(N) - Single pass through array
- **Space**: O(K) - Hashmap for remainders

## Example
```
Input: arr[] = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: 7 subarrays have sum divisible by 5
```
