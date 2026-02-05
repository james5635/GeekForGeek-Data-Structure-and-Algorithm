# Find a Triplet in an Array Whose Sum is Closest to a Given Number

## Problem Statement

Given an array of integers and a target number, find a triplet in the array whose sum is closest to the target. Return the sum of the triplet.

## Examples

**Example 1:**
```
Input: arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: 
- [-1, 2, 1] sum = 2 (closest to 1)
- [-1, 2, -4] sum = -3
- [2, 1, -4] sum = -1
- [-1, 1, -4] sum = -4
The closest sum to target 1 is 2
```

**Example 2:**
```
Input: arr = [1, 2, 3, 4, 5], target = 10
Output: 10
Explanation: Triplets [1, 4, 5] or [2, 3, 5] both sum to exactly 10
```

## Approach

### Two-Pointer Technique (Optimal)

Similar to 3Sum problem, but we track the closest sum instead of looking for exact match:

1. **Sort the array** - O(n log n)
2. **Initialize** `closest_sum` with sum of first three elements
3. **For each index i** from `0` to `n-3`:
   - Use two pointers: `left = i+1`, `right = n-1`
   - While `left < right`:
     - Calculate `current_sum = arr[i] + arr[left] + arr[right]`
     - If `|current_sum - target| < |closest_sum - target|`: update `closest_sum`
     - If `current_sum == target`: return immediately (can't get closer!)
     - If `current_sum < target`: `left++` (need larger sum)
     - If `current_sum > target`: `right--` (need smaller sum)

## Complexity Analysis

- **Time Complexity:** O(n²)
  - Sorting: O(n log n)
  - Outer loop: O(n)
  - Inner two-pointer scan: O(n)
  - Total: O(n²)
- **Space Complexity:** O(1) auxiliary
  - In-place sorting
  - Only using indices and variables

## Implementation

```python
def three_sum_closest(arr, target):
    if not arr or len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    arr.sort()
    n = len(arr)
    
    # Initialize with first three elements
    closest_sum = arr[0] + arr[1] + arr[2]
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            # Exact match - can't get closer!
            if current_sum == target:
                return target
            
            # Update if current is closer
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            # Move pointers
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum
```

## Key Differences from 3Sum

| Aspect | 3Sum | 3Sum Closest |
|--------|------|--------------|
| Return | Boolean/All triplets | Closest sum value |
| Goal | Exact match | Minimum difference |
| Early exit | When sum == target | Also when sum == target |
| Tracking | Triplets | Closest sum |

## Edge Cases

- **Array size < 3:** Raise error
- **Exact match exists:** Return target immediately
- **Multiple equally close sums:** Return any
- **All same elements:** Simple calculation
- **Large target:** Return max possible sum
- **Small target:** Return min possible sum

## Applications

- Approximation problems
- Financial calculations (closest portfolio value)
- Geometric applications
- Optimization with constraints

## Related Problems

- 3Sum (exact match)
- 4Sum Closest
- Two Sum Closest
- K-Sum variations

## Reference

- [GeeksforGeeks - Find a Triplet in an Array Whose Sum is Closest to a Given Number](https://www.geeksforgeeks.org/dsa/find-a-triplet-in-an-array-whose-sum-is-closest-to-a-given-number/)