# K-th Smallest Element After Removing Integers

## Problem Description

Given an array `arr[]` of size 'n' and a positive integer k. Consider series of natural numbers and remove arr[0], arr[1], ..., arr[n-1] from it. Find the k-th smallest number in the remaining set of natural numbers.

## Algorithm

**Approach 1: Set-based (O(n + k) time, O(n) space)**
1. Create a set of removed elements for O(1) lookup
2. Iterate through natural numbers starting from 1
3. Count valid numbers (not in removed set)
4. Return the k-th valid number

**Approach 2: Sorting-based (O(n log n) time, O(n) space)**
1. Sort the removed array and remove duplicates
2. Iterate through removed elements
3. For each removed element <= current k, increment k
4. Return the final k value

## Complexity Analysis

### Set-based Approach
| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n + k) | O(n) |
| Average | O(n + k) | O(n) |
| Worst | O(n + k) | O(n) |

### Sorting-based Approach
| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

## Example

```
Input:  arr = [1], k = 1
Output: 2
Explanation: After removing 1, natural numbers become {2, 3, 4, ...}
             1st smallest = 2
```

## Key Points

- Sorting approach is more efficient when k is large
- Set approach is simpler and works well for small k
- Both approaches handle duplicates correctly