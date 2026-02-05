"""
Reconstruct Itinerary from List of Tickets

Problem Description:
Given a list of tickets, find the itinerary in order. It is assumed that:
- The input list is not cyclic
- There is one ticket from every city except the final destination
- Each ticket is represented as (from, to) pair

Examples:
Input:
[Chennai, Bangalore], [Bombay, Delhi], [Goa, Chennai], [Delhi, Goa]

Output:
Bombay -> Delhi -> Goa -> Chennai -> Bangalore

Approach:
Use two HashMaps:
1. Store all tickets in a map (from -> to)
2. Create reverse map to find starting point (city not in reverse map)
3. Starting from start city, follow tickets to build itinerary

Time Complexity: O(N)
Space Complexity: O(N)
"""


def reconstruct_itinerary(tickets):
    """
    Reconstruct itinerary from list of tickets.

    Args:
        tickets: List of [from, to] pairs representing tickets

    Returns:
        List of cities in itinerary order
    """
    if not tickets:
        return []

    # Build ticket map and reverse map
    ticket_map = {}
    reverse_map = {}

    for from_city, to_city in tickets:
        ticket_map[from_city] = to_city
        reverse_map[to_city] = from_city

    # Find starting city (city not in reverse_map)
    start = None
    for from_city in ticket_map:
        if from_city not in reverse_map:
            start = from_city
            break

    # If no clear start found, use first ticket's from city
    if start is None:
        start = tickets[0][0]

    # Build itinerary
    itinerary = [start]
    current = start

    while current in ticket_map:
        current = ticket_map[current]
        itinerary.append(current)

    return itinerary


def reconstruct_itinerary_with_path(tickets):
    """
    Reconstruct itinerary and return as formatted path string.

    Args:
        tickets: List of [from, to] pairs

    Returns:
        String representation of itinerary
    """
    itinerary = reconstruct_itinerary(tickets)
    return " -> ".join(itinerary)


def test_reconstruct_itinerary():
    """Test cases for reconstruct_itinerary function."""
    # Test Case 1: Example from problem
    tickets1 = [
        ["Chennai", "Bangalore"],
        ["Bombay", "Delhi"],
        ["Goa", "Chennai"],
        ["Delhi", "Goa"],
    ]
    result1 = reconstruct_itinerary(tickets1)
    path1 = reconstruct_itinerary_with_path(tickets1)
    print(f"Test 1:")
    print(f"Tickets: {tickets1}")
    print(f"Itinerary: {result1}")
    print(f"Path: {path1}")
    print(f"Expected: ['Bombay', 'Delhi', 'Goa', 'Chennai', 'Bangalore']")
    print(
        f"{'PASS' if result1 == ['Bombay', 'Delhi', 'Goa', 'Chennai', 'Bangalore'] else 'FAIL'}"
    )
    print()

    # Test Case 2: US cities example
    tickets2 = [
        ["New York", "Chicago"],
        ["Denver", "San Francisco"],
        ["Chicago", "Denver"],
        ["San Francisco", "Los Angeles"],
    ]
    result2 = reconstruct_itinerary(tickets2)
    path2 = reconstruct_itinerary_with_path(tickets2)
    print(f"Test 2:")
    print(f"Tickets: {tickets2}")
    print(f"Itinerary: {result2}")
    print(f"Path: {path2}")
    print(
        f"Expected: ['New York', 'Chicago', 'Denver', 'San Francisco', 'Los Angeles']"
    )
    print(
        f"{'PASS' if result2 == ['New York', 'Chicago', 'Denver', 'San Francisco', 'Los Angeles'] else 'FAIL'}"
    )
    print()

    # Test Case 3: Single ticket
    tickets3 = [["A", "B"]]
    result3 = reconstruct_itinerary(tickets3)
    print(f"Test 3:")
    print(f"Tickets: {tickets3}")
    print(
        f"Result: {result3}, Expected: ['A', 'B'], {'PASS' if result3 == ['A', 'B'] else 'FAIL'}"
    )
    print()

    # Test Case 4: Empty tickets
    tickets4 = []
    result4 = reconstruct_itinerary(tickets4)
    print(f"Test 4:")
    print(f"Tickets: {tickets4}")
    print(f"Result: {result4}, Expected: [], {'PASS' if result4 == [] else 'FAIL'}")
    print()

    # Test Case 5: Linear chain
    tickets5 = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]]
    result5 = reconstruct_itinerary(tickets5)
    print(f"Test 5:")
    print(f"Tickets: {tickets5}")
    print(f"Result: {result5}")
    print(f"Expected: ['A', 'B', 'C', 'D', 'E']")
    print(f"{'PASS' if result5 == ['A', 'B', 'C', 'D', 'E'] else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_reconstruct_itinerary()
