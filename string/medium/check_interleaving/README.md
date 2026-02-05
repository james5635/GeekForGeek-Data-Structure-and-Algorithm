# Check Interleaving

Check whether a string is formed by interleaving two other strings.

## Approach
- Use Dynamic Programming to solve the problem
- dp[i][j] represents whether c[0:i+j] can be formed by interleaving a[0:i] and b[0:j]
- Each character in c must come from either a or b, maintaining relative order
- Space optimization is possible using only O(n) space where n is the length of the shorter string

## Complexity
- **Time Complexity**: O(m*n) where m and n are lengths of the input strings
- **Space Complexity**: O(m*n) for the DP table, can be optimized to O(min(m,n))

## Usage
```python
from solution import are_interleaving

result = are_interleaving("abc", "def", "adbcef")
print(result)  # Output: True
```