# Single Among Doubles

Given an array where every element appears exactly twice except for one element which appears exactly once, find that single element.

## Problem Statement

Find the element that appears only once in an array where all other elements appear exactly twice.

### Examples

**Input:** `arr[] = [2, 3, 5, 4, 5, 3, 4]`  
**Output:** `2`  
**Explanation:** All elements appear twice except 2.

**Input:** `arr[] = [1, 2, 1, 2, 3]`  
**Output:** `3`  
**Explanation:** 1 and 2 appear twice, 3 appears once.

**Input:** `arr[] = [7]`  
**Output:** `7`  
**Explanation:** Only one element in array.

## Algorithm Approaches

### 1. Optimal Approach - XOR Operation
- **File:** `single_among_doubles.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Use XOR properties: `a ^ a = 0` and `a ^ 0 = a`
  - XOR all elements together
  - Pairs cancel out to 0
  - Single element remains

### 2. Alternative Approach - HashSet
- **File:** `single_among_doubles.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Use a set to track elements
  - Add element if not seen, remove if seen
  - Last remaining element is the answer

### 3. Alternative Approach - Sorting
- **File:** `single_among_doubles.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1)
- **Description:** 
  - Sort the array
  - Check adjacent pairs
  - Element without a pair is the answer

## Usage

```bash
python single_among_doubles.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| XOR | O(n) | O(1) | **Preferred** - optimal in all aspects |
| HashSet | O(n) | O(n) | When XOR not applicable |
| Sorting | O(n log n) | O(1) | When memory is limited |

## XOR Properties

```
1. a ^ a = 0        (XOR of same number is 0)
2. a ^ 0 = a        (XOR with 0 is the number itself)
3. a ^ b = b ^ a    (Commutative)
4. (a ^ b) ^ c = a ^ (b ^ c)    (Associative)
```

## How XOR Approach Works

```
Example: [2, 3, 5, 4, 5, 3, 4]

Step by step:
  result = 0
  result = 0 ^ 2 = 2
  result = 2 ^ 3 = 1
  result = 1 ^ 5 = 4
  result = 4 ^ 4 = 0
  result = 0 ^ 5 = 5
  result = 5 ^ 3 = 6
  result = 6 ^ 4 = 2

Or grouped:
  2 ^ (3 ^ 3) ^ (5 ^ 5) ^ (4 ^ 4)
  = 2 ^ 0 ^ 0 ^ 0
  = 2
```

## Key Insights

- **Bitwise Magic:** XOR operation elegantly handles this problem
- **Constant Space:** O(1) space makes it optimal
- **Linear Time:** Single pass through array
- **Works with Negatives:** XOR handles negative numbers correctly

## Edge Cases

- Single element array: returns that element
- Two elements (one pair): not applicable per problem constraints
- Negative numbers: handled correctly by XOR
- Zero: handled correctly (0 ^ 0 = 0)

## Variations

- Single Among Triples (element appears once, others thrice) - requires different approach
- Two Single Elements - requires modified XOR approach

## References

- [GeeksforGeeks - Find the element that appears once](https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/)
