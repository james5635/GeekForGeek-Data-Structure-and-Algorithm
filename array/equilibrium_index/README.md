# Equilibrium Index

Given an array `arr[]` of size `n`, find an index `i` such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. If no such index exists, return -1.

## Problem Statement

Find equilibrium index where:  
`sum(arr[0..i-1]) == sum(arr[i+1..n-1])`

### Examples

**Input:** `arr[] = [-7, 1, 5, 2, -4, 3, 0]`  
**Output:** `3` or `6`  
**Explanation:** 
- At index 3: Left sum = -7+1+5 = -1, Right sum = -4+3+0 = -1
- At index 6: Left sum = -7+1+5+2-4+3 = 0, Right sum = 0

**Input:** `arr[] = [1, 2, 3]`  
**Output:** `-1`  
**Explanation:** No equilibrium index exists.

**Input:** `arr[] = [1, 2, 3, 0, 3, 2, 1]`  
**Output:** `3`  
**Explanation:** At index 3 (value 0), left sum = 1+2+3 = 6, right sum = 3+2+1 = 6

## Algorithm Approaches

### 1. Naive Approach - Check All Indices
- **File:** `equilibrium_index.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - For each index, calculate left sum and right sum separately
  - Return index where sums are equal

### 2. Better Approach - Prefix/Suffix Arrays
- **File:** `equilibrium_index.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Precompute prefix sum array (sum from start to each index)
  - Precompute suffix sum array (sum from each index to end)
  - Compare prefix[i-1] with suffix[i+1] for each i

### 3. Optimal Approach - Running Sum
- **File:** `equilibrium_index.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Calculate total sum first
  - Traverse array, maintaining running left sum
  - At each index: `right_sum = total_sum - left_sum - arr[i]`
  - If `left_sum == right_sum`, return index

## Usage

```bash
python equilibrium_index.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow |
| Prefix/Suffix | O(n) | O(n) | Faster, uses extra space |
| Running Sum | O(n) | O(1) | **Preferred** - optimal |

## How Running Sum Approach Works

```
Array: [-7, 1, 5, 2, -4, 3, 0]

Step 1: Calculate total sum
  total = -7 + 1 + 5 + 2 + (-4) + 3 + 0 = 0

Step 2: Traverse with running left sum
  i=0: left=0, right=0-0-(-7)=7, not equal
       left becomes -7
  i=1: left=-7, right=0-(-7)-1=6, not equal
       left becomes -6
  i=2: left=-6, right=0-(-6)-5=1, not equal
       left becomes -1
  i=3: left=-1, right=0-(-1)-2=-1, EQUAL! → Return 3
       
  (Continue to find index 6)
```

## Mathematical Formula

```
For index i:
  left_sum = sum(arr[0..i-1])
  right_sum = sum(arr[i+1..n-1])
  
Since total_sum = left_sum + arr[i] + right_sum:
  right_sum = total_sum - left_sum - arr[i]

Equilibrium condition:
  left_sum = total_sum - left_sum - arr[i]
  2 * left_sum = total_sum - arr[i]
```

## Key Insights

- **Single Pass:** After computing total sum, we can find equilibrium in one pass
- **Left Accumulation:** We only need to track left sum, right sum is derived
- **Multiple Equilibria:** An array can have multiple equilibrium indices
- **Edge Indices:** Index 0 can be equilibrium if right sum is 0

## Edge Cases

- Empty array: return -1
- Single element: return 0 (empty sums on both sides = 0)
- All zeros: all indices are equilibrium
- No equilibrium: return -1

## Variations

- **Find All Equilibrium Indices:** Return list instead of single index
- **Pivot Index:** Similar concept, different problem constraints
- **Balance Point:** Physical interpretation of equilibrium

## Applications

- Load balancing: Finding balanced partition points
- Array partitioning: Divide array into equal sum parts
- Game theory: Fair division problems

## References

- [GeeksforGeeks - Equilibrium index of an array](https://www.geeksforgeeks.org/equilibrium-index-of-an-array/)
