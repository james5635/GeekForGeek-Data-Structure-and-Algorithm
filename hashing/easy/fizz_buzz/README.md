# Fizz Buzz

## Problem Statement

Print numbers from 1 to n with the following rules:
- Print "FizzBuzz" if the number is divisible by both 3 and 5
- Print "Fizz" if the number is divisible by 3
- Print "Buzz" if the number is divisible by 5
- Print the number itself if none of the above conditions are met

## Examples

- **Input:** n = 15  
  **Output:** 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

## Approach

1. **Standard Method:** Use modulo operator to check divisibility by 3 and 5.

2. **Hash Map Method:** Store divisors and their corresponding strings in a hash map. This approach is more scalable when adding new rules (e.g., "Jazz" for 7).

3. **Optimized Method:** Use counters instead of modulo operations for better performance.

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** 
  - O(1) for basic version (excluding output)
  - O(k) for hash map version where k is number of rules

## Files

- `solution.py` - Contains implementation with test cases
