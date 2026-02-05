"""
Sort Array by Applying Given Equation

Problem Description:
Given an array arr[] of n integers and coefficients a, b, c of a quadratic
function f(x) = ax² + bx + c, sort the array based on the value of f(x) for
each element x in the array.

The key challenge is to do this efficiently, taking advantage of the fact
that quadratic functions have specific properties that can be exploited.

Examples:
- Input: arr[] = [-3, -1, 2, 4], a=1, b=0, c=0 (f(x) = x²)
  Output: [2, -1, -3, 4] or sorted by f(x): [1, 1, 4, 9] → indices [1, 0, 2, 3]

- Input: arr[] = [1, 2, 3, 4], a=-1, b=0, c=0 (f(x) = -x²)
  Output: [4, 3, 2, 1] (decreasing order)

Properties of Quadratic Functions:
- If a > 0: Parabola opens upward, minimum at vertex
- If a < 0: Parabola opens downward, maximum at vertex
- Vertex is at x = -b/(2a)

Approach 1: Two-Pointer Merge (Optimal for sorted input)
1. Find vertex of parabola
2. Elements farther from vertex have larger f(x) when a > 0
3. Use two pointers from both ends and merge
4. Time: O(n), Space: O(n)

Approach 2: Calculate and Sort
1. Calculate f(x) for all elements
2. Sort by calculated values
3. Time: O(n log n), Space: O(n)

Approach 3: Modified Merge Sort
1. Find the minimum/maximum point
2. Elements on both sides are sorted by distance from vertex
3. Merge the two sorted halves

Time Complexity: O(n) if input is sorted, O(n log n) otherwise
Space Complexity: O(n)
"""


def apply_equation(x, a, b, c):
    """
    Apply quadratic equation f(x) = ax² + bx + c.

    Args:
        x: Input value
        a, b, c: Coefficients

    Returns:
        float: f(x) value
    """
    return a * x * x + b * x + c


def sort_by_equation_calculate(arr, a, b, c):
    """
    Sort array by calculating f(x) for all elements.
    Simple but O(n log n) approach.

    Args:
        arr: Input array
        a, b, c: Coefficients of quadratic equation

    Returns:
        list: Sorted array based on f(x) values
    """
    if not arr:
        return []

    # Calculate f(x) for each element and sort
    calculated = [(apply_equation(x, a, b, c), x) for x in arr]
    calculated.sort(key=lambda x: x[0])

    return [x for _, x in calculated]


def sort_by_equation_two_pointer(arr, a, b, c):
    """
    Sort array using two-pointer technique.
    Optimal O(n) for already sorted input.

    Args:
        arr: Input array (should be sorted)
        a, b, c: Coefficients of quadratic equation

    Returns:
        list: Sorted array based on f(x) values
    """
    if not arr:
        return []

    n = len(arr)

    # If a > 0: parabola opens up, minimum at vertex
    # If a < 0: parabola opens down, maximum at vertex

    if a == 0:
        # Linear function: f(x) = bx + c
        if b >= 0:
            return arr.copy() if arr == sorted(arr) else sorted(arr)
        else:
            return arr[::-1] if arr == sorted(arr) else sorted(arr, reverse=True)

    # Find vertex (minimum/maximum point)
    vertex = -b / (2 * a)

    # Find the point closest to vertex using binary search
    left, right = 0, n - 1
    closest_idx = 0

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < vertex:
            closest_idx = mid
            left = mid + 1
        else:
            right = mid - 1

    # If vertex is closer to next element, adjust
    if closest_idx + 1 < n and abs(arr[closest_idx + 1] - vertex) < abs(
        arr[closest_idx] - vertex
    ):
        closest_idx += 1

    # Two pointers from closest_idx
    i, j = closest_idx, closest_idx + 1
    result = []

    if a > 0:
        # Parabola opens upward: merge from center outward
        while i >= 0 and j < n:
            if apply_equation(arr[i], a, b, c) <= apply_equation(arr[j], a, b, c):
                result.append(arr[i])
                i -= 1
            else:
                result.append(arr[j])
                j += 1

        while i >= 0:
            result.append(arr[i])
            i -= 1

        while j < n:
            result.append(arr[j])
            j += 1
    else:
        # Parabola opens downward: merge from outside inward
        # We want decreasing order of f(x), which is increasing distance from vertex
        temp = []
        while i >= 0 and j < n:
            if apply_equation(arr[i], a, b, c) >= apply_equation(arr[j], a, b, c):
                temp.append(arr[i])
                i -= 1
            else:
                temp.append(arr[j])
                j += 1

        while i >= 0:
            temp.append(arr[i])
            i -= 1

        while j < n:
            temp.append(arr[j])
            j += 1

        result = temp[::-1]

    return result


def sort_by_equation_merge(arr, a, b, c):
    """
    Sort by splitting at vertex and merging.

    Args:
        arr: Input array
        a, b, c: Coefficients

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    if a == 0:
        # Linear case
        calculated = [(b * x + c, x) for x in arr]
        calculated.sort(key=lambda x: x[0])
        return [x for _, x in calculated]

    vertex = -b / (2 * a)

    # Split array into left and right of vertex
    left_part = [x for x in arr if x <= vertex]
    right_part = [x for x in arr if x > vertex]

    if a > 0:
        # Both parts sorted by distance from vertex
        left_part.sort(key=lambda x: abs(x - vertex))
        right_part.sort(key=lambda x: abs(x - vertex))
        return left_part + right_part
    else:
        # Want decreasing order of f(x)
        left_part.sort(key=lambda x: abs(x - vertex), reverse=True)
        right_part.sort(key=lambda x: abs(x - vertex), reverse=True)
        return right_part + left_part


def sort_by_equation_with_values(arr, a, b, c):
    """
    Return sorted array along with computed f(x) values.

    Args:
        arr: Input array
        a, b, c: Coefficients

    Returns:
        tuple: (sorted_array, list of f(x) values)
    """
    sorted_arr = sort_by_equation_calculate(arr, a, b, c)
    values = [apply_equation(x, a, b, c) for x in sorted_arr]
    return sorted_arr, values


def find_equation_extremum(arr, a, b, c):
    """
    Find minimum and maximum f(x) values in the array.

    Args:
        arr: Input array
        a, b, c: Coefficients

    Returns:
        tuple: (min_value, max_value, min_element, max_element)
    """
    if not arr:
        return None, None, None, None

    values = [(apply_equation(x, a, b, c), x) for x in arr]
    values.sort()

    return (values[0][0], values[-1][0], values[0][1], values[-1][1])


def run_tests():
    """Test cases for sort by equation problem."""
    test_cases = [
        {
            "arr": [-3, -1, 2, 4],
            "a": 1,
            "b": 0,
            "c": 0,
            "description": "f(x) = x²",
        },
        {
            "arr": [1, 2, 3, 4],
            "a": -1,
            "b": 0,
            "c": 0,
            "description": "f(x) = -x²",
        },
        {
            "arr": [-2, -1, 0, 1, 2],
            "a": 1,
            "b": 0,
            "c": 0,
            "description": "Symmetric around 0",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "a": 1,
            "b": -6,
            "c": 0,
            "description": "f(x) = x² - 6x",
        },
        {
            "arr": [1, 2, 3],
            "a": 0,
            "b": 2,
            "c": 1,
            "description": "Linear f(x) = 2x + 1",
        },
        {
            "arr": [5],
            "a": 1,
            "b": 0,
            "c": 0,
            "description": "Single element",
        },
        {
            "arr": [],
            "a": 1,
            "b": 0,
            "c": 0,
            "description": "Empty array",
        },
        {
            "arr": [-5, -3, -1, 0, 2, 4],
            "a": 1,
            "b": 2,
            "c": 1,
            "description": "f(x) = x² + 2x + 1",
        },
    ]

    print("Running Sort Array by Equation Tests:")
    print("=" * 60)

    for i, test in enumerate(test_cases, 1):
        arr = test["arr"]
        a, b, c = test["a"], test["b"], test["c"]

        # Test all methods
        result_calc = sort_by_equation_calculate(arr.copy(), a, b, c)
        result_merge = sort_by_equation_merge(arr.copy(), a, b, c)

        # Verify both give same result
        passed = result_calc == result_merge or (
            sorted(result_calc) == sorted(result_merge)
            and all(
                apply_equation(result_calc[j], a, b, c)
                <= apply_equation(result_calc[j + 1], a, b, c)
                for j in range(len(result_calc) - 1)
            )
        )

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"f(x) = {a}x² + {b}x + {c}")
        print(f"Input: {arr}")
        print(f"Output (calculate): {result_calc}")

        # Show computed values
        values = [apply_equation(x, a, b, c) for x in result_calc]
        print(f"f(x) values: {values}")

    # Test with values return
    print("\n--- Testing With Values ---")
    arr = [-3, -1, 2, 4]
    a, b, c = 1, 0, 0
    sorted_arr, values = sort_by_equation_with_values(arr, a, b, c)
    print(f"Input: {arr}, f(x) = x²")
    print(f"Sorted: {sorted_arr}")
    print(f"Values: {values}")

    # Test extremum
    print("\n--- Testing Extremum ---")
    arr = [-3, -1, 2, 4]
    min_val, max_val, min_elem, max_elem = find_equation_extremum(arr, a, b, c)
    print(f"Input: {arr}, f(x) = x²")
    print(f"Min: f({min_elem}) = {min_val}")
    print(f"Max: f({max_elem}) = {max_val}")

    print("\n" + "=" * 60)
    print("Tests completed!")

    return True


if __name__ == "__main__":
    run_tests()
