# Space Optimization using Bit Manipulations

## Problem Description

This module demonstrates common space optimization techniques using bit manipulations for array operations. Bit manipulation can significantly reduce space complexity in various scenarios.

## Techniques Covered

### 1. Check if K-th Bit is Set
Determine if the k-th bit of a number is set (1) or not (0).

### 2. Count Set Bits
Count the number of 1s in binary representation (population count).

### 3. Find Single Number
Find the only element that appears once when all others appear twice (using XOR).

### 4. Find Two Single Numbers
Find two elements that appear once when all others appear twice.

### 5. Swap Without Temp
Swap two numbers without using a temporary variable.

### 6. Check Power of Two
Determine if a number is a power of two.

### 7. Find Missing Number
Find missing number in array of 0 to n using XOR.

### 8. Bitmask Subset Generation
Generate all subsets using bitmasking.

## Functions

### `is_kth_bit_set(n, k)`
Check if k-th bit of n is set.

### `count_set_bits(n)`
Count number of set bits in n.

### `find_single_number(arr)`
Find element appearing once (others appear twice).

### `find_two_single_numbers(arr)`
Find two elements appearing once (others appear twice).

### `swap_without_temp(a, b)`
Swap two numbers without temporary variable.

### `is_power_of_two(n)`
Check if n is a power of two.

### `find_missing_number(arr)`
Find missing number in sequence 0 to n.

### `generate_subsets(arr)`
Generate all subsets using bitmasking.

## Usage Examples

```python
from solution import *

# Check if 3rd bit is set in 10 (1010)
result = is_kth_bit_set(10, 3)
print(result)  # True

# Count set bits in 7 (111)
count = count_set_bits(7)
print(count)  # 3

# Find single number
arr = [2, 3, 5, 4, 5, 3, 4]
single = find_single_number(arr)
print(single)  # 2

# Swap without temp
a, b = 5, 10
a, b = swap_without_temp(a, b)
print(a, b)  # 10, 5

# Check power of two
print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False

# Generate subsets
arr = [1, 2, 3]
subsets = generate_subsets(arr)
print(subsets)  # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **XOR Properties:**
   - a ^ a = 0
   - a ^ 0 = a
   - a ^ b = b ^ a (commutative)

2. **Bit Masking:** Use (1 << k) to create masks for k-th bit

3. **Space Savings:** Can reduce O(N) space to O(1) in many problems

4. **Common Patterns:**
   - XOR for finding unique elements
   - Bitmask for subset generation
   - & and | for bit manipulation

## Space Optimization Examples

| Problem | Naive Space | Optimized Space |
|---------|-------------|-----------------|
| Find single element | O(N) hash set | O(1) using XOR |
| Subset generation | O(2^N) recursive | O(1) per subset using bitmask |
| Missing number | O(N) hash set | O(1) using XOR |

## References

- [GeeksForGeeks - Space Optimization using Bit Manipulations](https://www.geeksforgeeks.org/dsa/space-optimization-using-bit-manipulations/)
