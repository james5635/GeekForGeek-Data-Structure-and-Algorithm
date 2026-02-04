# Missing and Repeating

Given an unsorted array `arr[]` of size `n` containing distinct integers from 1 to n with one number missing and one number appearing twice, find both the missing and repeating numbers.

## Problem Statement

In an array of size n containing integers from 1 to n, one number is missing and one number appears twice. Find both numbers.

### Examples

**Input:** `arr[] = [3, 1, 2, 5, 3]`, n = 5  
**Output:** `(3, 4)` - Repeating: 3, Missing: 4  
**Explanation:** 3 appears twice, 4 is missing from [1,2,3,4,5].

**Input:** `arr[] = [1, 2, 2, 4]`, n = 4  
**Output:** `(2, 3)` - Repeating: 2, Missing: 3  
**Explanation:** 2 appears twice, 3 is missing.

**Input:** `arr[] = [2, 2]`, n = 2  
**Output:** `(2, 1)` - Repeating: 2, Missing: 1

## Algorithm Approaches

### 1. Visited Array Approach
- **File:** `missing_and_repeating.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Create a boolean array of size n+1
  - Mark elements as visited
  - Element visited twice = repeating
  - Element never visited = missing

### 2. Array Marking Approach (Modifies Input)
- **File:** `missing_and_repeating.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Use the array itself as a marker
  - Negate the value at index abs(arr[i])-1
  - If already negative, it's the repeating number
  - Positive index + 1 indicates missing number

### 3. Mathematical Equations Approach
- **File:** `missing_and_repeating.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Let x = repeating, y = missing
  - Equation 1: (Sum 1..n) - (Sum arr) = y - x
  - Equation 2: (Sum of squares 1..n) - (Sum of squares arr) = y² - x²
  - Solve the two equations to find x and y

### 4. XOR Approach (Optimal)
- **File:** `missing_and_repeating.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - XOR all elements and numbers 1..n to get x ^ y
  - Find rightmost set bit in the result
  - Partition based on this bit
  - XOR within partitions to isolate x and y
  - Verify which is repeating

## Usage

```bash
python missing_and_repeating.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Modifies Input | Notes |
|----------|----------------|------------------|----------------|-------|
| Visited Array | O(n) | O(n) | No | Simple, extra space |
| Array Marking | O(n) | O(1) | Yes | No extra space, destructive |
| Math Equations | O(n) | O(1) | No | May overflow |
| XOR | O(n) | O(1) | No | **Preferred** - no overflow |

## Mathematical Derivation

### Using Sum and Sum of Squares

```
Let:
  S = Sum of 1..n = n(n+1)/2
  S_arr = Sum of array elements
  
  Sq = Sum of squares 1..n = n(n+1)(2n+1)/6
  Sq_arr = Sum of squares of array elements

Then:
  y - x = S - S_arr                    (Equation 1)
  y² - x² = Sq - Sq_arr                (Equation 2)

From Equation 2:
  (y-x)(y+x) = Sq - Sq_arr

Therefore:
  y + x = (Sq - Sq_arr) / (S - S_arr)  (Equation 3)

Solving Equations 1 and 3:
  y = [(y-x) + (y+x)] / 2
  x = y - (y-x)
```

### Using XOR

```
xor_all = XOR of all elements XOR XOR of 1..n
        = x ^ y (since all other pairs cancel)

Find rightmost set bit in xor_all:
  This bit differs between x and y

Partition all numbers by this bit and XOR within partitions:
  One partition gives x, other gives y
```

## Key Insights

- **Two Unknowns:** We need two equations to solve for two unknowns
- **XOR Advantage:** Avoids arithmetic overflow issues
- **Array as Hash:** The marking approach cleverly uses array indices as a hash
- **Non-destructive:** XOR and Math approaches don't modify input

## Edge Cases

- n = 2: Simplest case
- Repeating at boundaries (1 or n)
- Large n: XOR preferred to prevent overflow

## References

- [GeeksforGeeks - Find the repeating and the missing](https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/)
