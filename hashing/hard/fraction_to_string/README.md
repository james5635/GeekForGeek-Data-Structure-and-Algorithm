# Fraction to String

## Problem Description

Given two integers **a** and **b** (b != 0), return the fraction **a/b** in string format. If the fractional part is repeating, enclose the repeating part in parentheses.

## Examples

- **Input**: a = 1, b = 2  
  **Output**: "0.5"  
  **Explanation**: 1/2 = 0.5 with no repeating part.

- **Input**: a = 50, b = 22  
  **Output**: "2.(27)"  
  **Explanation**: 50/22 = 2.27272727... Since fractional part (27) is repeating, it is enclosed in parentheses.

## Approach

1. Handle the sign separately based on XOR of numerator and denominator signs
2. Calculate the integral part (before decimal point)
3. For the fractional part, use a hash map to track remainders and their positions
4. If a remainder repeats, it indicates a repeating decimal
5. Insert parentheses around the repeating part

## Complexity Analysis

- **Time Complexity**: O(max(log₁₀(a), log₁₀(b)))
- **Space Complexity**: O(max(log₁₀(a), log₁₀(b)))

## Key Insight

When performing long division, if a remainder repeats, the subsequent digits will also repeat. By storing the position of each remainder in a hash map, we can detect cycles and insert parentheses accordingly.
