"""
Sort a Stack using Recursion
https://www.geeksforgeeks.org/dsa/sort-a-stack-using-recursion/

Given a stack of integers, sort the stack in ascending order (smallest element at the bottom and largest at the top).
Time Complexity: O(n^2)
Auxiliary Space: O(n), due to call stack.
"""


def sorted_insert(st, x):
    """
    Insert element into sorted stack.

    Args:
        st: The stack (list)
        x: The element to insert
    """
    # If stack is empty or top element is smaller, push x
    if not st or st[-1] <= x:
        st.append(x)
        return

    top = st.pop()

    # Recursively insert x in sorted order
    sorted_insert(st, x)

    st.append(top)


def sort_stack(st):
    """
    Sort the stack recursively.

    Args:
        st: The stack (list) to sort
    """
    if not st:
        return

    top = st.pop()

    # Recursively sort the remaining stack
    sort_stack(st)

    sorted_insert(st, top)


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1
    print("Test Case 1:")
    st = [41, 3, 32, 2, 11]
    print(f"Original stack: {st}")
    sort_stack(st)
    print("Sorted stack (top to bottom): ", end="")
    while st:
        print(st.pop(), end=" ")
    print()
    print()

    # Test case 2 - reverse sorted
    print("Test Case 2 (Reverse sorted):")
    st = [1, 2, 3, 4, 5]
    print(f"Original stack: {st}")
    sort_stack(st)
    print("Sorted stack (top to bottom): ", end="")
    while st:
        print(st.pop(), end=" ")
    print()
    print()

    # Test case 3 - with duplicates
    print("Test Case 3 (With duplicates):")
    st = [5, 3, 5, 1, 3, 2]
    print(f"Original stack: {st}")
    sort_stack(st)
    print("Sorted stack (top to bottom): ", end="")
    while st:
        print(st.pop(), end=" ")
    print()


if __name__ == "__main__":
    main()
