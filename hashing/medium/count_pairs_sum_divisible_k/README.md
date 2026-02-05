# Count Pairs Sum Divisible by K

## Problem Statement
Given an array A[] and positive integer K, count the total number of pairs in the array whose sum is divisible by K.

## Approach
Use hashing to store frequency of remainders when elements are divided by K:
- Elements with remainder `r` can pair with elements having remainder `(K - r) % K`
- Elements with remainder 0 can pair among themselves
- Handle middle element separately when K is even

## Complexity
- **Time**: O(N) - Single pass to count remainders
- **Space**: O(K) - Frequency array of size K

## Example
```
Input: A[] = {2, 2, 1, 7, 5, 3}, K = 4
Output: 5
Pairs: (2, 2), (1, 7), (7, 5), (1, 3), (5, 3)
```
