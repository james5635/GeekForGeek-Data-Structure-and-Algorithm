# Majority Element

An element is called a **majority element** if it appears **more than n/2 times** in an array of size n.

## Problem Statement

Given an array of size n, find the majority element (the element that appears more than ⌊n/2⌋ times). If no majority element exists, return -1.

### Examples

**Input:** `arr[] = [3, 3, 4, 2, 4, 4, 2, 4, 4]`  
**Output:** `4`  
**Explanation:** 4 appears 5 times, which is > 9/2 = 4.5

**Input:** `arr[] = [3, 3, 4, 2, 4, 4, 2, 4]`  
**Output:** `-1`  
**Explanation:** No element appears more than 4 times (8/2 = 4)

**Input:** `arr[] = [1, 1, 1, 1, 1]`  
**Output:** `1`  
**Explanation:** 1 appears 5 times > 5/2 = 2.5

## Algorithm Approaches

### 1. Naive Approach - Count Each Element
- **File:** `majority_element.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - For each element, count its occurrences in entire array
  - Return element if count > n/2
  - Simple but inefficient for large arrays

### 2. Better Approach - Sort and Check Middle
- **File:** `majority_element.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - If majority exists, it must be at index n//2
  - Verify by counting occurrences

### 3. Optimal Approach - Moore's Voting Algorithm
- **File:** `majority_element.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - **Phase 1:** Find a candidate for majority
  - **Phase 2:** Verify if candidate is actually majority
  - Cancel out pairs of different elements
  - Majority element survives the cancellation

## Usage

```bash
python majority_element.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Too slow for large n |
| Sort | O(n log n) | O(1)/O(n) | Simple, but not optimal |
| Moore's Voting | O(n) | O(1) | **Preferred** - optimal |
| Hash Map | O(n) | O(n) | Good for multiple queries |

## Boyer-Moore Voting Algorithm Explained

### Phase 1: Find Candidate

```
Initialize:
  candidate = None
  count = 0

For each element in array:
  If count == 0:
    candidate = current_element
    count = 1
  Else if current_element == candidate:
    count += 1
  Else:
    count -= 1

Return candidate
```

### Phase 2: Verify Candidate

```
count = 0
For each element in array:
  If element == candidate:
    count += 1

If count > n/2:
  Return candidate
Else:
  Return -1 (no majority)
```

### Example Walkthrough

```
Array: [3, 3, 4, 2, 4, 4, 2, 4, 4]

Phase 1 - Finding candidate:
  i=0: candidate=3, count=1
  i=1: count=2 (3==3)
  i=2: count=1 (4!=3)
  i=3: count=0 (2!=3)
  i=4: candidate=4, count=1
  i=5: count=2 (4==4)
  i=6: count=1 (2!=4)
  i=7: count=2 (4==4)
  i=8: count=3 (4==4)
  
  Candidate: 4

Phase 2 - Verification:
  Count of 4 = 5 > 9/2 = 4.5 ✓
  
Result: 4
```

## Key Insights

- **Cancellation Principle:** Pair up different elements and cancel them
- **Survivor Property:** Majority element always survives cancellation
- **Two-Pass Guarantee:** First pass finds candidate, second verifies
- **Optimal Efficiency:** Linear time with constant space

## Why Verification is Necessary

Moore's algorithm finds a **candidate**, but we must verify:
- Example: `[1, 2, 3]` - no majority, but algorithm might return 3
- Always count occurrences to confirm count > n/2

## Edge Cases

- **Single element:** That element is majority
- **All unique:** No majority
- **Exactly n/2:** Not a majority (must be strictly > n/2)
- **Two elements:** Either one has majority or none

## Variations

- **Elements > n/3:** Extended Boyer-Moore for k candidates
- **Stream processing:** Online majority detection
- **Distributed systems:** Finding majority across multiple machines

## Applications

- **Voting systems:** Determining election winner
- **Fault tolerance:** Finding most common sensor reading
- **Data streams:** Finding frequent items
- **Consensus algorithms:** Distributed agreement

## References

- [GeeksforGeeks - Majority Element](https://www.geeksforgeeks.org/majority-element/)
- [Boyer-Moore Majority Vote Algorithm (1981)](https://www.cs.utexas.edu/~moore/best-ideas/mjrty/)
