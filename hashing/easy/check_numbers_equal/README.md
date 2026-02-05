# Check Two Numbers Equal

## Problem Statement

Check if two numbers are equal without using arithmetic and comparison operators.

## Examples

- **Input:** num1 = 10, num2 = 10  
  **Output:** true

- **Input:** num1 = 10, num2 = 20  
  **Output:** false

## Approach

1. **XOR Method:** If two numbers are equal, their XOR result is 0. This works because XOR returns 0 when both bits are the same.

2. **Hash Method:** Store one number in a hash set and check if the other exists (demonstrates hashing concept).

3. **Bitwise Method:** Use bitwise XOR and check if result is all zeros.

## Complexity Analysis

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Files

- `solution.py` - Contains implementation with test cases
