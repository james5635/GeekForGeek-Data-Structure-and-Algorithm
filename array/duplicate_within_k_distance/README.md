# Duplicate Within K Distance

Given an array of integers `arr[]` and an integer `k`, check if the array contains any duplicate elements within distance `k` from each other. In other words, check if there exists any index `i` and `j` such that `arr[i] == arr[j]` and `|i - j| <= k`.

## Problem Statement

Find if there are any duplicate elements in the array that are at most `k` distance apart.

### Examples

**Input:** `arr[] = [1, 2, 3, 4, 1, 2, 3, 4]`, `k = 3`  
**Output:** `True`  
**Explanation:** The element 1 repeats at index 0 and 4, which are 4 positions apart (> k=3). However, element 2 repeats at index 1 and 5, which are also 4 positions apart. Let's check another case:  
**Input:** `arr[] = [1, 2, 3, 1, 4, 5]`, `k = 3`  
**Output:** `True`  
**Explanation:** The element 1 repeats at index 0 and 3, which are exactly 3 positions apart (<= k=3).

**Input:** `arr[] = [1, 2, 3, 4, 5]`, `k = 3`  
**Output:** `False`  
**Explanation:** No duplicate elements exist in the array.

**Input:** `arr[] = [1, 2, 3, 4, 4]`, `k = 3`  
**Output:** `True`  
**Explanation:** The element 4 repeats at index 3 and 4, which are 1 position apart (<= k=3).

## Algorithm Approaches

### 1. Naive Approach - Check All Pairs
- **File:** `duplicate_within_k_distance.py`
- **Time Complexity:** O(n × k)
- **Space Complexity:** O(1)
- **Description:** 
  - For each element, check the next k elements
  - If any match found, return True
  - If loop completes without finding match, return False

### 2. Optimal Approach - HashSet Window
- **File:** `duplicate_within_k_distance.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(k)
- **Description:** 
  - Use a HashSet to maintain a sliding window of last k elements
  - For each element, check if it exists in the set
  - If yes, duplicate found within k distance
  - Add current element and remove element that is now k+1 distance away

## Usage

```bash
python duplicate_within_k_distance.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n × k) | O(1) | Simple but slow for large k |
| HashSet | O(n) | O(k) | Optimal, uses extra space |

## Key Insights

- **Sliding Window:** The optimal solution uses a sliding window of size k to track seen elements
- **Trade-off:** We trade O(k) space for O(n) time complexity
- **Edge Cases:**
  - Empty array returns False
  - k >= n-1 means checking entire array for duplicates
  - Single element array returns False

## References

- [GeeksforGeeks - Check if array elements are consecutive](https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/)
