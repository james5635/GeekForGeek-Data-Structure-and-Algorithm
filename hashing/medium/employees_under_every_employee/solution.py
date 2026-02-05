"""
Employees Under Every Employee

Problem Description:
Given a 2D matrix of strings arr[][] where each arr[i] contains two strings:
- arr[i][0] is the employee
- arr[i][1] is the manager

Find the count of employees under each manager (direct + indirect reports).
Note: Every employee reports to only one manager. The CEO reports to himself.
Print result in sorted order by employee name.

Examples:
Input: arr = [[A, C], [B, C], [C, F], [D, E], [E, F], [F, F]]
Output: [[A, 0], [B, 0], [C, 2], [D, 0], [E, 1], [F, 5]]

Explanation:
- A, B report to C (C has 2 direct reports)
- D reports to E (E has 1 direct report)
- C, E report to F
- F is CEO, has 5 employees under (C, E, A, B, D)

Approach:
Use DFS with memoization:
1. Build adjacency list (manager -> list of employees)
2. For each employee, use DFS to count all subordinates
3. Use memoization to avoid recomputation

Time Complexity: O(N) where N is number of employees
Space Complexity: O(N) for adjacency list and memoization
"""


def count_employees_under_manager(arr):
    """
    Count employees under every manager.

    Args:
        arr: 2D list where each element is [employee, manager]

    Returns:
        Dictionary with employee -> count of employees under them
    """
    if not arr:
        return {}

    # Build adjacency list: manager -> list of direct reports
    manager_map = {}
    all_employees = set()

    for employee, manager in arr:
        all_employees.add(employee)
        all_employees.add(manager)

        if manager not in manager_map:
            manager_map[manager] = []
        if employee != manager:  # CEO reports to himself
            manager_map[manager].append(employee)

    # Memoization cache
    memo = {}

    def count_subordinates(emp):
        """Count all employees under given employee using DFS."""
        if emp in memo:
            return memo[emp]

        count = 0
        if emp in manager_map:
            for subordinate in manager_map[emp]:
                count += 1 + count_subordinates(subordinate)

        memo[emp] = count
        return count

    # Calculate for all employees
    result = {}
    for employee in sorted(all_employees):
        result[employee] = count_subordinates(employee)

    return result


def print_employee_hierarchy(arr):
    """
    Print employee hierarchy with counts in sorted order.

    Args:
        arr: 2D list where each element is [employee, manager]

    Returns:
        List of [employee, count] pairs sorted by employee name
    """
    result = count_employees_under_manager(arr)
    return [[emp, count] for emp, count in result.items()]


def test_employees_under_manager():
    """Test cases for employees under manager function."""
    # Test Case 1: Example from problem
    arr1 = [["A", "C"], ["B", "C"], ["C", "F"], ["D", "E"], ["E", "F"], ["F", "F"]]
    result1 = print_employee_hierarchy(arr1)
    print(f"Test 1:")
    print(f"Input: {arr1}")
    print(f"Result: {result1}")
    expected1 = [["A", 0], ["B", 0], ["C", 2], ["D", 0], ["E", 1], ["F", 5]]
    print(f"Expected: {expected1}")
    print(f"{'PASS' if result1 == expected1 else 'FAIL'}")
    print()

    # Test Case 2: Linear hierarchy
    arr2 = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "D"]]
    result2 = print_employee_hierarchy(arr2)
    print(f"Test 2:")
    print(f"Input: {arr2}")
    print(f"Result: {result2}")
    expected2 = [["A", 0], ["B", 1], ["C", 2], ["D", 3]]
    print(f"Expected: {expected2}")
    print(f"{'PASS' if result2 == expected2 else 'FAIL'}")
    print()

    # Test Case 3: All report to one manager
    arr3 = [["A", "M"], ["B", "M"], ["C", "M"], ["M", "M"]]
    result3 = print_employee_hierarchy(arr3)
    print(f"Test 3:")
    print(f"Input: {arr3}")
    print(f"Result: {result3}")
    expected3 = [["A", 0], ["B", 0], ["C", 0], ["M", 3]]
    print(f"Expected: {expected3}")
    print(f"{'PASS' if result3 == expected3 else 'FAIL'}")
    print()

    # Test Case 4: Empty input
    arr4 = []
    result4 = print_employee_hierarchy(arr4)
    print(f"Test 4:")
    print(f"Input: {arr4}")
    print(f"Result: {result4}, Expected: [], {'PASS' if result4 == [] else 'FAIL'}")
    print()

    # Test Case 5: Single employee (CEO)
    arr5 = [["CEO", "CEO"]]
    result5 = print_employee_hierarchy(arr5)
    print(f"Test 5:")
    print(f"Input: {arr5}")
    print(f"Result: {result5}")
    expected5 = [["CEO", 0]]
    print(f"Expected: {expected5}, {'PASS' if result5 == expected5 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_employees_under_manager()
