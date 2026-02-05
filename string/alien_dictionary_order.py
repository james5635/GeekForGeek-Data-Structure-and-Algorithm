"""
Alien Dictionary Order

Given an array of strings words[], sorted in an alien language.
Determine the correct order of letters in this alien language based on the given words.

Examples:
- Input: ["baa", "abcd", "abca", "cab", "cad"] -> Output: "bdac"
- Input: ["caa", "aaa", "aab"] -> Output: "cab"

This problem uses Topological Sort (Kahn's Algorithm or DFS)

Time Complexity: O(n * m) where n is number of words and m is average word length
Space Complexity: O(1) since we only have 26 characters
"""

from collections import deque


def findOrder(words):
    """
    Find the order of characters in an alien dictionary using Kahn's algorithm
    """
    # Adjacency list
    graph = [[] for _ in range(26)]

    # In-degree array
    inDegree = [0] * 26

    # To track which letters exist in input
    exists = [False] * 26

    # Mark existing characters
    for word in words:
        for ch in word:
            exists[ord(ch) - ord("a")] = True

    # Build graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
        j = 0
        while j < minlen and w1[j] == w2[j]:
            j += 1

        if j < minlen:
            u = ord(w1[j]) - ord("a")
            v = ord(w2[j]) - ord("a")
            graph[u].append(v)
            inDegree[v] += 1
        elif len(w1) > len(w2):
            # Invalid case: longer word comes before shorter word
            return ""

    # Topological sort
    q = deque([i for i in range(26) if exists[i] and inDegree[i] == 0])
    result = []

    while q:
        u = q.popleft()
        result.append(chr(u + ord("a")))
        for v in graph[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                q.append(v)

    if len(result) != sum(exists):
        # Cycle detected or incomplete order
        return ""

    return "".join(result)


def findOrderDFS(words):
    """
    Alternative implementation using DFS with cycle detection
    """
    graph = [[0] * 26 for _ in range(26)]
    exist = [0] * 26
    vis = [0] * 26
    rec = [0] * 26
    ans = []

    # Mark all characters that appear in the input
    for word in words:
        for ch in word:
            exist[ord(ch) - ord("a")] = 1

    # Build the graph
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        n, m, ind = len(a), len(b), 0

        # Find the first different character between a and b
        while ind < n and ind < m and a[ind] == b[ind]:
            ind += 1

        if ind != n and ind == m:
            return ""

        if ind < n and ind < m:
            graph[ord(a[ind]) - ord("a")][ord(b[ind]) - ord("a")] = 1

    def dfs(u):
        # Mark the node as visited and part of the current recursion stack
        vis[u] = rec[u] = 1

        for v in range(26):
            if graph[u][v]:
                if not vis[v]:
                    # Recurse and check for cycle
                    if not dfs(v):
                        return False
                elif rec[v]:
                    # A cycle is detected if v is already
                    # in the current recursion stack
                    return False

        # Add the character to the result after visiting all dependencies
        ans.append(chr(ord("a") + u))

        # Remove from recursion stack
        rec[u] = 0
        return True

    for i in range(26):
        if exist[i] and not vis[i]:
            x = dfs(i)
            # Return empty string if a cycle is found
            if not x:
                return ""

    # Reverse to get the correct topological order
    ans.reverse()
    return "".join(ans)


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ["baa", "abcd", "abca", "cab", "cad"],
        ["caa", "aaa", "aab"],
        ["abc", "acd", "bcd"],
    ]

    print("Alien Dictionary Order")
    print("=" * 40)

    for words in test_cases:
        order_kahn = findOrder(words)
        order_dfs = findOrderDFS(words)

        print(f"Words: {words}")
        print(f"  Order (Kahn's): {order_kahn}")
        print(f"  Order (DFS):    {order_dfs}")
        print()

    print("Explanation for ['baa', 'abcd', 'abca', 'cab', 'cad']:")
    print("- 'baa' < 'abcd' implies 'b' < 'a'")
    print("- 'abcd' < 'abca' implies 'd' < 'a'")
    print("- 'abca' < 'cab' implies 'a' < 'c'")
    print("- 'cab' < 'cad' implies 'b' < 'd'")
    print("- Combined order: b < d < a < c")
    print("- Result: 'bdac'")
