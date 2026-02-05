# Minimum Number of Jumps to Reach End

## Problem Description

Given an array of integers where each element represents the maximum jump length from that position, find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, you cannot move through that element.

**Example:**
```
Array: [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3

Explanation:
- Jump 1: 0 -> 1 (arr[0]=1, can jump 1 step)
- Jump 2: 1 -> 4 (arr[1]=3, can jump up to 3 steps, reach index 4)
- Jump 3: 4 -> 10 (arr[4]=9, can reach end)
```

## Algorithms

### 1. Greedy Approach (Optimal)
**Time:** O(N), **Space:** O(1)

Track current range and farthest reachable position. When we exhaust current range, make a jump.

### 2. Dynamic Programming
**Time:** O(N²), **Space:** O(N)

DP[i] = minimum jumps to reach index i from start.

### 3. BFS
**Time:** O(N), **Space:** O(N)

Treat as graph where edges represent possible jumps.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Greedy | O(N) | O(1) |
| Dynamic Programming | O(N²) | O(N) |
| BFS | O(N) | O(N) |

## Functions

### `min_jumps_greedy(arr)`
Find minimum jumps using greedy approach.

**Parameters:**
- `arr`: Array where arr[i] = max jump length from position i

**Returns:**
- Minimum number of jumps to reach end, or -1 if not possible

### `min_jumps_dp(arr)`
DP approach for comparison (slower but intuitive).

### `min_jumps_bfs(arr)`
BFS approach.

## Usage

```python
from solution import min_jumps_greedy

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
jumps = min_jumps_greedy(arr)
print(jumps)  # 3

# Edge case: single element
arr = [0]
jumps = min_jumps_greedy(arr)
print(jumps)  # 0 (already at end)
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Greedy Choice:** Always try to reach farthest in minimum jumps
2. **Range Tracking:** Track current jump range and next jump range
3. **Impossible Case:** If element is 0 and it's not the last, can't proceed
4. **Single Element:** Already at end, 0 jumps needed

## Algorithm Steps (Greedy)

```
1. If array has 0 or 1 element, return 0
2. If first element is 0, return -1 (can't move)
3. Initialize: max_reach = arr[0], steps = arr[0], jumps = 1
4. For i from 1 to n-1:
   a. If i == n-1, return jumps
   b. Update max_reach = max(max_reach, i + arr[i])
   c. Decrement steps
   d. If steps == 0, increment jumps, steps = max_reach - i
5. Return jumps
```

## References

- [GeeksForGeeks - Minimum Number of Jumps to Reach End](https://www.geeksforgeeks.org/dsa/minimum-number-of-jumps-to-reach-end-of-a-given-array/)
