"""
Word Wrap Problem

Given a sequence of words and a maximum line width k, arrange the words
such that each line contains at most k characters. The goal is to minimize
the sum of cubes of extra spaces in each line (or sum of squares in some variations).

If a line contains words from i to j with extra spaces at the end,
cost = (extra_spaces)^3 (or ^2)

Examples:
words = ["Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"]
k = 15

Optimal arrangement:
Line 1: Geeks for Geeks (extra spaces: 0, cost: 0)
Line 2: presents word   (extra spaces: 2, cost: 8)
Line 3: wrap problem    (extra spaces: 1, cost: 1)
Total cost: 9

Time Complexity: O(n^2) for DP solution
Space Complexity: O(n)
"""

import sys


def wordWrap(words, k):
    """
    Solve word wrap problem using dynamic programming
    Minimize sum of cubes of extra spaces
    """
    n = len(words)

    # extras[i][j] = extra spaces if words[i..j] are put in one line
    # -1 if it's not possible
    extras = [[0] * n for _ in range(n)]

    # Calculate extra spaces for all possible lines
    for i in range(n):
        extras[i][i] = k - len(words[i])
        for j in range(i + 1, n):
            extras[i][j] = extras[i][j - 1] - len(words[j]) - 1

    # lc[i][j] = cost of putting words[i..j] in one line
    # If not possible, set to a large number
    INF = 10**9  # Use large integer instead of float('inf')
    lc = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if extras[i][j] < 0:
                lc[i][j] = INF
            elif j == n - 1 and extras[i][j] >= 0:
                lc[i][j] = 0  # No cost for last line
            else:
                lc[i][j] = extras[i][j] ** 2  # Using square instead of cube

    # c[j] = minimum cost to arrange words[0..j]
    # p[j] = index of last word in previous line
    c = [0] * n
    p = [0] * n

    c[0] = 0
    for j in range(1, n):
        c[j] = INF
        for i in range(j + 1):
            if lc[i][j] != INF and (i == 0 or c[i - 1] != INF):
                cost = (c[i - 1] if i > 0 else 0) + lc[i][j]
                if cost < c[j]:
                    c[j] = cost
                    p[j] = i

    return c[n - 1], p


def printSolution(words, p, n):
    """
    Print the wrapped text
    """
    if n < 0:
        return

    printSolution(words, p, p[n] - 1)

    # Print words from p[n] to n
    line = " ".join(words[p[n] : n + 1])
    print(f"  {line}")


def wordWrapGreedy(words, k):
    """
    Greedy approach: fill each line as much as possible
    Not optimal but simple
    """
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        # Check if word fits in current line
        if current_length + len(word) + len(current_line) <= k:
            current_line.append(word)
            current_length += len(word)
        else:
            # Start new line
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(current_line)

    # Calculate cost
    total_cost = 0
    for i, line in enumerate(lines[:-1]):  # Skip last line
        line_length = sum(len(w) for w in line) + len(line) - 1
        extra = k - line_length
        total_cost += extra**2

    return lines, total_cost


# Test the function
if __name__ == "__main__":
    test_cases = [
        (["Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"], 15),
        (["aaa", "bb", "cc", "dd", "eee"], 6),
        (["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16),
    ]

    print("Word Wrap Problem")
    print("=" * 50)

    for words, k in test_cases:
        print(f"Words: {words}")
        print(f"Max line width: {k}")
        print()

        # Dynamic Programming solution
        cost, p = wordWrap(words, k)
        print(f"DP Solution (min cost: {cost}):")
        printSolution(words, p, len(words) - 1)
        print()

        # Greedy solution
        lines, greedy_cost = wordWrapGreedy(words, k)
        print(f"Greedy Solution (cost: {greedy_cost}):")
        for line in lines:
            print(f"  {' '.join(line)}")
        print()

        print("-" * 50)
        print()
