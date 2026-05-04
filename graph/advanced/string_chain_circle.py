"""
String Chain to Form a Circle

Given a list of strings, determine if they can be chained to form a circle.
A string can be chained with another if the last character of the first
equals the first character of the second.

A circle is formed if:
- strings[0].last == strings[1].first
- strings[1].last == strings[2].first
- ...
- strings[n-1].last == strings[0].first

This is an Eulerian circuit problem:
- Model each character as a vertex (a-z)
- Each string is a directed edge from first char to last char
- A valid circle chain exists iff the graph has an Eulerian circuit

Conditions for Eulerian circuit in directed graph:
1. in_degree == out_degree for all vertices
2. All non-zero degree vertices belong to single strongly connected component

Time Complexity: O(N * L) where N is number of strings, L is max string length
Space Complexity: O(1) - at most 26 vertices
"""

from typing import List, Dict
from collections import defaultdict


def can_form_circle_chain(strings: List[str]) -> bool:
    """
    Check if strings can be chained to form a circle.

    Args:
        strings: List of strings

    Returns:
        True if a circular chain is possible
    """
    if not strings:
        return True

    # Build graph: vertices are characters, edges are strings
    # Only track in/out degrees for characters that appear
    out_degree: Dict[str, int] = defaultdict(int)
    in_degree: Dict[str, int] = defaultdict(int)
    adj: Dict[str, List[str]] = defaultdict(list)

    for s in strings:
        first = s[0]
        last = s[-1]
        out_degree[first] += 1
        in_degree[last] += 1
        adj[first].append(last)

    # Condition 1: in_degree == out_degree for all vertices
    all_chars = set(out_degree.keys()) | set(in_degree.keys())
    for char in all_chars:
        if out_degree[char] != in_degree[char]:
            return False

    # Condition 2: All non-zero degree vertices in single SCC
    # Since max 26 characters, we can use simple DFS
    return _is_strongly_connected(adj, all_chars)


def _is_strongly_connected(adj: Dict[str, List[str]], vertices: set) -> bool:
    """Check if all vertices belong to a single strongly connected component."""
    if not vertices:
        return True

    start = next(iter(vertices))

    # DFS on original graph
    visited_forward = set()
    _dfs(start, adj, visited_forward)

    if visited_forward != vertices:
        return False

    # Build reverse graph
    rev_adj: Dict[str, List[str]] = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            rev_adj[v].append(u)

    # DFS on reverse graph
    visited_reverse = set()
    _dfs(start, rev_adj, visited_reverse)

    return visited_reverse == vertices


def _dfs(start: str, adj: Dict[str, List[str]], visited: set) -> None:
    """DFS traversal."""
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)


def find_circle_chain(strings: List[str]) -> List[str]:
    """
    Find a circular chain if one exists.

    Uses Hierholzer's algorithm for Eulerian circuit.

    Args:
        strings: List of strings

    Returns:
        Ordered list of strings forming a circle, or empty list if impossible
    """
    if not can_form_circle_chain(strings):
        return []

    # Build adjacency list with string indices
    adj: Dict[str, List[int]] = defaultdict(list)
    for i, s in enumerate(strings):
        adj[s[0]].append(i)

    # Hierholzer's algorithm
    stack = [strings[0][0]]  # Start from first string's first char
    circuit: List[int] = []  # Store string indices
    current = strings[0][0]

    while adj.get(current):
        idx = adj[current].pop()
        s = strings[idx]
        circuit.append(idx)
        current = s[-1]

    if len(circuit) != len(strings):
        return []

    return [strings[i] for i in circuit]


def verify_circle_chain(strings: List[str]) -> bool:
    """Verify that a list of strings forms a valid circular chain."""
    if not strings:
        return True
    n = len(strings)
    for i in range(n):
        if strings[i][-1] != strings[(i + 1) % n][0]:
            return False
    return True


if __name__ == "__main__":
    # Example 1: Can form circle
    print("=== Example 1: Can Form Circle ===")
    strings1 = ["abc", "cde", "efa", "ghi", "ihg"]
    # abc -> cde -> efa -> (a matches abc's first... but need circular)
    # Actually: abc(last=c) -> cde(first=c), cde(last=e) -> efa(first=e)
    # efa(last=a) -> ? , ghi -> ihg -> g... doesn't connect
    # Let me fix the example
    strings1 = ["abc", "cde", "efa"]
    # abc->cde->efa->(a matches abc's first 'a') YES!
    print(f"Strings: {strings1}")
    print(f"Can form circle: {can_form_circle_chain(strings1)}")

    # Example 2: Cannot form circle
    print("\n=== Example 2: Cannot Form Circle ===")
    strings2 = ["ab", "bc", "cd"]
    # ab->bc->cd, but cd's last 'd' != ab's first 'a'
    print(f"Strings: {strings2}")
    print(f"Can form circle: {can_form_circle_chain(strings2)}")

    # Example 3: Find the chain
    print("\n=== Example 3: Find Circle Chain ===")
    strings3 = ["geeks", "forgeeks", "quiz", "que"]
    # geeks->s? forgeeks->s? Let me use a better example
    # ab, bc, ca -> ab->bc->ca->a(ab's first) = circle!
    strings3 = ["ab", "bc", "ca"]
    print(f"Strings: {strings3}")
    chain = find_circle_chain(strings3)
    print(f"Circle chain: {chain}")
    print(f"Verified: {verify_circle_chain(chain)}")

    # Example 4: More complex
    print("\n=== Example 4: Complex Example ===")
    strings4 = ["aab", "bac", "cda", "adb", "bda"]
    print(f"Strings: {strings4}")
    print(f"Can form circle: {can_form_circle_chain(strings4)}")
