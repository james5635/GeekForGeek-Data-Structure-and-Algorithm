# Dynamic Programming

Collection of Dynamic Programming algorithm implementations from [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/).

## Algorithms

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `fibonacci.py` | Fibonacci Number | Nth Fibonacci number using recursion, memoization, tabulation, space optimization, and matrix exponentiation | [Link](https://www.geeksforgeeks.org/dsa/program-for-nth-fibonacci-number/) |
| `lucas_numbers.py` | Lucas Numbers | Lucas numbers sequence (L(n) = L(n-1) + L(n-2), L(0)=2, L(1)=1) | [Link](https://www.geeksforgeeks.org/dsa/lucas-numbers/) |
| `tribonacci_numbers.py` | Tribonacci Numbers | Tribonacci numbers (T(n) = T(n-1) + T(n-2) + T(n-3)) | [Link](https://www.geeksforgeeks.org/dsa/tribonacci-numbers/) |
| `longest_common_subsequence.py` | Longest Common Subsequence | Find length of LCS of two strings | [Link](https://www.geeksforgeeks.org/dsa/longest-common-subsequence-dp-4/) |
| `longest_increasing_subsequence.py` | Longest Increasing Subsequence | Find length of LIS in an array | [Link](https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/) |
| `edit_distance.py` | Edit Distance | Minimum operations (insert, delete, replace) to convert one string to another | [Link](https://www.geeksforgeeks.org/dsa/edit-distance-dp-5/) |
| `min_cost_path.py` | Minimum Cost Path | Minimum cost path in a 2D matrix from (0,0) to (m-1,n-1) | [Link](https://www.geeksforgeeks.org/dsa/min-cost-path-dp-6/) |
| `coin_change.py` | Coin Change | Count number of ways to make sum using given coin denominations | [Link](https://www.geeksforgeeks.org/dsa/coin-change-dp-7/) |
| `matrix_chain_multiplication.py` | Matrix Chain Multiplication | Optimal parenthesization to minimize scalar multiplications | [Link](https://www.geeksforgeeks.org/dsa/matrix-chain-multiplication-dp-8/) |
| `knapsack_01.py` | 0/1 Knapsack Problem | Maximize value with given weight capacity | [Link](https://www.geeksforgeeks.org/dsa/0-1-knapsack-problem-dp-10/) |
| `subset_sum.py` | Subset Sum Problem | Check if subset with given sum exists | [Link](https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/) |
| `partition_min_subset_diff.py` | Partition Minimum Subset Difference | Partition array into two subsets with minimum sum difference | [Link](https://www.geeksforgeeks.org/dsa/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/) |
| `catalan_number.py` | Catalan Number | Nth Catalan number using iterative and binomial coefficient methods | [Link](https://www.geeksforgeeks.org/dsa/program-nth-catalan-number/) |

## Running Tests

Each file includes example usage and test cases in the `__main__` block. Run any file directly:

```bash
python dynamic_programming/fibonacci.py
python dynamic_programming/knapsack_01.py
```

## Approaches

Most implementations include multiple approaches:
- **Recursive** - Top-down with exponential time (where applicable)
- **Memoization** - Top-down with caching
- **Tabulation** - Bottom-up DP
- **Space Optimized** - Reduced space complexity versions
