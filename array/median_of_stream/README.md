# Median of a Stream of Integers

## Problem Description

Given a stream of integers, find the median after each new integer is added. The median is the middle value in an ordered integer list.
- If the list size is odd, the median is the middle element
- If the list size is even, the median is the average of two middle elements

**Example:**
```
Input: stream = [5, 15, 1, 3]
Output: [5.0, 10.0, 5.0, 4.0]

Explanation:
- After 5: [5] -> median = 5.0
- After 15: [5, 15] -> median = (5+15)/2 = 10.0
- After 1: [1, 5, 15] -> median = 5.0
- After 3: [1, 3, 5, 15] -> median = (3+5)/2 = 4.0
```

## Algorithms

### 1. Two Heaps (Optimal)
**Time:** O(log n) per insertion, **Space:** O(n)

Use two heaps:
- **Max heap (left half)**: Contains smaller half of numbers
- **Min heap (right half)**: Contains larger half of numbers
- **Balance**: Size of max heap = size of min heap or 1 more

### 2. Insertion Sort
**Time:** O(n) per insertion, **Space:** O(n)

Maintain sorted list and insert each new element in correct position.

### 3. Simple Sorting
**Time:** O(n² log n) total, **Space:** O(n)

Sort entire array after each insertion.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Two Heaps | O(log n) per op | O(n) |
| Insertion Sort | O(n) per op | O(n) |
| Simple Sorting | O(n² log n) | O(n) |

## Classes and Functions

### `MedianFinder`
Class to find running median of a stream of integers using two heaps.

**Methods:**
- `add_num(num)`: Add a number to the data structure
- `find_median()`: Find the median of all numbers seen so far

### `find_running_median(stream)`
Find running median for a stream of integers.

**Parameters:**
- `stream`: List of integers representing the stream

**Returns:**
- List of medians after each insertion

### `MedianFinderInsertionSort`
Alternative implementation using insertion sort.

## Usage

```python
from solution import MedianFinder

mf = MedianFinder()
mf.add_num(5)
mf.add_num(15)
print(mf.find_median())  # 10.0

# Or for entire stream
from solution import find_running_median
stream = [5, 15, 1, 3]
medians = find_running_median(stream)
print(medians)  # [5.0, 10.0, 5.0, 4.0]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Heap Balance**: Maintain size property - max heap can have at most 1 more element than min heap
2. **Median Extraction**: 
   - Odd count: Top of max heap
   - Even count: Average of both heap tops
3. **Element Distribution**: All elements in max heap <= all elements in min heap
4. **Python Heap**: Only min heap available, use negatives for max heap

## References

- [GeeksForGeeks - Median of Stream of Integers](https://www.geeksforgeeks.org/dsa/median-of-stream-of-integers-running-integers/)
