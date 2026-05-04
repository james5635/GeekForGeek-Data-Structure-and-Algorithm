"""
Find Itinerary from a Given List of Tickets

Given a list of tickets where each ticket is [from, to], find the complete
itinerary in order.

Assumptions:
- The input is not cyclic
- There is one ticket from every city except the final destination
- The starting city has no incoming ticket

Approach 1 (Hash Map): Build a forward map and a reverse map. Find the
start city (appears in forward map but not in reverse map), then follow
the chain.

Approach 2 (Topological Sort): Since this forms a linear chain, topological
sort also works.

Time Complexity: O(N) where N is number of tickets
Space Complexity: O(N)
"""

from typing import List, Dict, Tuple, Optional


def find_itinerary_hashing(tickets: List[List[str]]) -> List[List[str]]:
    """
    Find itinerary using hashing approach.

    Args:
        tickets: List of [from, to] ticket pairs

    Returns:
        List of [from, to] pairs in itinerary order
    """
    forward: Dict[str, str] = {}
    reverse: Dict[str, str] = {}

    for src, dst in tickets:
        forward[src] = dst
        reverse[dst] = src

    # Find the starting point (source not in reverse map)
    start: Optional[str] = None
    for src in forward:
        if src not in reverse:
            start = src
            break

    if start is None:
        return []  # Cyclic input

    # Follow the chain
    result = []
    current = start
    while current in forward:
        next_city = forward[current]
        result.append([current, next_city])
        current = next_city

    return result


def find_itinerary_cities(tickets: List[List[str]]) -> List[str]:
    """
    Find itinerary and return as a list of cities in order.

    Args:
        tickets: List of [from, to] ticket pairs

    Returns:
        List of cities in itinerary order
    """
    forward: Dict[str, str] = {}
    reverse: Dict[str, str] = {}

    for src, dst in tickets:
        forward[src] = dst
        reverse[dst] = src

    start: Optional[str] = None
    for src in forward:
        if src not in reverse:
            start = src
            break

    if start is None:
        return []

    result = [start]
    current = start
    while current in forward:
        current = forward[current]
        result.append(current)

    return result


def find_itinerary_with_start(tickets: List[List[str]], start_city: str) -> List[str]:
    """
    Find itinerary when the starting city is known.

    Args:
        tickets: List of [from, to] ticket pairs
        start_city: Known starting city

    Returns:
        List of cities in itinerary order
    """
    forward: Dict[str, str] = {src: dst for src, dst in tickets}

    result = [start_city]
    current = start_city
    while current in forward:
        current = forward[current]
        result.append(current)

    return result


def find_itinerary_topological(tickets: List[List[str]]) -> List[str]:
    """
    Find itinerary using topological sort approach.

    Args:
        tickets: List of [from, to] ticket pairs

    Returns:
        List of cities in itinerary order
    """
    adj: Dict[str, str] = {}
    for src, dst in tickets:
        adj[src] = dst

    visited: Dict[str, bool] = {}
    stack: List[str] = []

    def dfs_util(city: str) -> None:
        visited[city] = True
        if city in adj and not visited.get(adj[city], False):
            dfs_util(adj[city])
        stack.append(city)

    for city in adj:
        if not visited.get(city, False):
            dfs_util(city)

    return stack[::-1]


if __name__ == "__main__":
    # Example 1: Basic itinerary
    print("=== Example 1: Hashing approach ===")
    tickets = [
        ["Chennai", "Bangalore"],
        ["Bombay", "Delhi"],
        ["Goa", "Chennai"],
        ["Delhi", "Goa"],
    ]
    itinerary = find_itinerary_hashing(tickets)
    for src, dst in itinerary:
        print(f"{src} -> {dst}")

    # Example 2: As city list
    print("\n=== Example 2: City list ===")
    cities = find_itinerary_cities(tickets)
    print(" -> ".join(cities))

    # Example 3: Airport codes
    print("\n=== Example 3: Airport itinerary ===")
    flights = [["SFO", "HKO"], ["YYZ", "SFO"], ["YUL", "YYZ"], ["HKO", "ORD"]]
    route = find_itinerary_cities(flights)
    print(" -> ".join(route))

    # Example 4: Topological sort approach
    print("\n=== Example 4: Topological sort approach ===")
    route2 = find_itinerary_topological(tickets)
    print(" -> ".join(route2))
