"""
Water Jug Problem using BFS

Problem:
Given two jugs with capacities m and n liters, find the minimum number of operations
to measure exactly d liters of water.

Allowed operations:
1. Fill a jug completely
2. Empty a jug
3. Pour water from one jug to another (until source is empty or destination is full)

Algorithm: BFS on state space
- Each state is represented as (jug1_amount, jug2_amount)
- From each state, apply all 6 possible operations
- Track visited states to avoid cycles
- The first time we reach d in either jug, return the number of steps

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque


def water_jug_bfs(m: int, n: int, d: int) -> int:
    """
    Find minimum operations to measure d liters using BFS.

    Args:
        m: Capacity of jug 1
        n: Capacity of jug 2
        d: Target amount to measure

    Returns:
        Minimum number of operations, or -1 if impossible
    """
    # Quick check: d must be achievable
    if d > max(m, n):
        return -1

    import math

    if d % math.gcd(m, n) != 0:
        return -1

    # BFS: state = (jug1, jug2, steps)
    queue = deque()
    queue.append((0, 0, 0))  # Both jugs start empty

    visited = set()
    visited.add((0, 0))

    while queue:
        jug1, jug2, steps = queue.popleft()

        # Check if target is achieved
        if jug1 == d or jug2 == d:
            return steps

        # Generate all 6 possible next states
        next_states = []

        # 1. Fill jug 1
        next_states.append((m, jug2))
        # 2. Fill jug 2
        next_states.append((jug1, n))
        # 3. Empty jug 1
        next_states.append((0, jug2))
        # 4. Empty jug 2
        next_states.append((jug1, 0))
        # 5. Pour jug 1 into jug 2
        pour = min(jug1, n - jug2)
        next_states.append((jug1 - pour, jug2 + pour))
        # 6. Pour jug 2 into jug 1
        pour = min(jug2, m - jug1)
        next_states.append((jug1 + pour, jug2 - pour))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], steps + 1))

    return -1


def water_jug_with_path(
    m: int, n: int, d: int
) -> tuple[int, list[tuple[int, int, str]]]:
    """
    Find minimum operations and return the sequence of states.

    Args:
        m: Capacity of jug 1
        n: Capacity of jug 2
        d: Target amount

    Returns:
        Tuple of (steps, path) where path contains (jug1, jug2, action) tuples
    """
    import math

    if d > max(m, n) or d % math.gcd(m, n) != 0:
        return -1, []

    queue = deque()
    queue.append((0, 0, 0, []))  # (jug1, jug2, steps, path)

    visited = set()
    visited.add((0, 0))

    while queue:
        jug1, jug2, steps, path = queue.popleft()

        if jug1 == d or jug2 == d:
            return steps, path

        operations = [
            (m, jug2, f"Fill Jug 1 ({m}L)"),
            (jug1, n, f"Fill Jug 2 ({n}L)"),
            (0, jug2, "Empty Jug 1"),
            (jug1, 0, "Empty Jug 2"),
        ]

        # Pour jug 1 into jug 2
        pour = min(jug1, n - jug2)
        operations.append((jug1 - pour, jug2 + pour, f"Pour Jug1->Jug2 ({pour}L)"))

        # Pour jug 2 into jug 1
        pour = min(jug2, m - jug1)
        operations.append((jug1 + pour, jug2 - pour, f"Pour Jug2->Jug1 ({pour}L)"))

        for nj1, nj2, action in operations:
            if (nj1, nj2) not in visited:
                visited.add((nj1, nj2))
                new_path = path + [(nj1, nj2, action)]
                queue.append((nj1, nj2, steps + 1, new_path))

    return -1, []


if __name__ == "__main__":
    # Example 1: Classic 3L and 5L jugs, measure 4L
    print("Example 1: 3L and 5L jugs, measure 4L")
    steps1 = water_jug_bfs(3, 5, 4)
    print(f"  Minimum steps: {steps1}")  # Output: 6

    steps1, path1 = water_jug_with_path(3, 5, 4)
    print(f"  Path:")
    for state in path1:
        print(f"    Jug1={state[0]}L, Jug2={state[1]}L - {state[2]}")

    # Example 2: 4L and 3L jugs, measure 2L
    print("\nExample 2: 4L and 3L jugs, measure 2L")
    steps2 = water_jug_bfs(4, 3, 2)
    print(f"  Minimum steps: {steps2}")

    # Example 3: Impossible case
    print("\nExample 3: 2L and 6L jugs, measure 5L (impossible)")
    steps3 = water_jug_bfs(2, 6, 5)
    print(f"  Result: {steps3}")  # Output: -1 (5 is not divisible by gcd(2,6)=2)

    # Example 4: 5L and 3L jugs, measure 1L
    print("\nExample 4: 5L and 3L jugs, measure 1L")
    steps4 = water_jug_bfs(5, 3, 1)
    print(f"  Minimum steps: {steps4}")  # Output: 4
