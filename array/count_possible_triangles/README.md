# Count Possible Triangles

Given an array of positive integers representing side lengths, count how many triangles can be formed using three different elements from the array.

## Problem Statement

Three numbers can form a triangle if and only if they satisfy the **Triangle Inequality Theorem**: the sum of any two sides must be greater than the third side.

For sorted sides a ≤ b ≤ c, we only need to check: **a + b > c**

### Examples

**Input:** `arr[] = [4, 6, 3, 7]`  
**Output:** `3`  
**Explanation:** Possible triangles: (3, 4, 6), (3, 6, 7), (4, 6, 7)

**Input:** `arr[] = [10, 21, 22, 100, 101, 200, 300]`  
**Output:** `6`  

**Input:** `arr[] = [1, 2, 3]`  
**Output:** `0`  
**Explanation:** 1 + 2 = 3, not greater than 3, so no triangle possible

## Algorithm Approaches

### 1. Naive Approach - Try All Triplets
- **File:** `count_possible_triangles.py`
- **Time Complexity:** O(n³)
- **Space Complexity:** O(1)
- **Description:** 
  - Check all combinations of three elements
  - Verify all three triangle inequalities
  - Very slow for large arrays

### 2. Better Approach - Sort + Binary Search
- **File:** `count_possible_triangles.py`
- **Time Complexity:** O(n² log n)
- **Space Complexity:** O(1)
- **Description:** 
  - Sort the array first
  - Fix two sides, binary search for valid range of third side
  - Count valid triangles efficiently

### 3. Optimal Approach - Sort + Two Pointers
- **File:** `count_possible_triangles.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Sort the array
  - Fix the largest side, use two pointers for other two
  - When arr[i] + arr[j] > arr[k], all elements i to j-1 are valid

## Usage

```bash
python count_possible_triangles.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n³) | O(1) | Too slow for n > 100 |
| Sort + Binary Search | O(n² log n) | O(1) | Good for learning BS |
| Sort + Two Pointers | O(n²) | O(1) | **Preferred** - optimal |

## Two Pointers Algorithm Explained

```
Sort the array

For k from n-1 down to 2:  # Fix largest side
  i = 0
  j = k - 1
  
  While i < j:
    If arr[i] + arr[j] > arr[k]:
      # All elements from i to j-1 form valid triangles
      # with arr[j] and arr[k]
      count += j - i
      j -= 1
    Else:
      i += 1

Return count
```

### Example Walkthrough

```
Array: [4, 6, 3, 7]
Sorted: [3, 4, 6, 7]

k=3 (arr[3]=7, largest side):
  i=0, j=2: arr[0]+arr[2]=3+6=9 > 7 ✓
    count += 2-0 = 2 (triangles: (3,6,7), (4,6,7))
    j=1
  i=0, j=1: arr[0]+arr[1]=3+4=7 not > 7
    i=1
  i=1, j=1: i not < j, stop

k=2 (arr[2]=6):
  i=0, j=1: arr[0]+arr[1]=3+4=7 > 6 ✓
    count += 1-0 = 1 (triangle: (3,4,6))
    j=0
  i=0, j=0: i not < j, stop

Total count: 2 + 1 = 3
Triangles: (3,4,6), (3,6,7), (4,6,7)
```

## Key Insights

- **Sorting Helps:** After sorting, we only need to check a + b > c (largest)
- **Batch Counting:** When arr[i] + arr[j] > arr[k], all i to j-1 are valid
- **Two-pointer Efficiency:** Each k takes O(n) time, total O(n²)

## Triangle Inequality Theorem

For three sides a, b, c to form a triangle:
- a + b > c
- a + c > b  
- b + c > a

**Optimization:** If a ≤ b ≤ c, then a + c > b and b + c > a are always true.
Only need to check: **a + b > c**

## Edge Cases

- **Less than 3 elements:** Return 0 (no triangle possible)
- **All same values:** C(n, 3) triangles possible
- **Degenerate case:** a + b = c (not a valid triangle)
- **Very large numbers:** Use appropriate data types

## Variations

- **Count acute/obtuse triangles:** Additional angle checks
- **Count with duplicates:** Handle repeated side lengths
- **Maximum perimeter triangle:** Find triangle with max perimeter
- **Valid triangle count in range:** Count with constraints

## Applications

- **Computer graphics:** Mesh generation and validation
- **Computational geometry:** Polygon triangulation
- **Physics simulations:** Collision detection
- **Structural engineering:** Truss analysis

## References

- [GeeksforGeeks - Count the number of possible triangles](https://www.geeksforgeeks.org/find-number-of-triangles-possible/)
- [Triangle Inequality Theorem](https://en.wikipedia.org/wiki/Triangle_inequality)
