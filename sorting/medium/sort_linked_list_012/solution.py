"""
Sort a Linked List of 0s, 1s, and 2s

Given a linked list containing only 0s, 1s, and 2s, sort the linked list.

Algorithm (Approach 1 - Counting):
1. Traverse the list and count occurrences of 0, 1, and 2
2. Traverse again and overwrite node values based on counts

Algorithm (Approach 2 - Dutch National Flag):
1. Create three separate lists for 0s, 1s, and 2s
2. Link them together in order

Time Complexity: O(n) - Single or two passes through the list
Space Complexity: O(1) - Only using a few pointers
"""


class ListNode:
    """Node class for linked list."""

    def __init__(self, data=0):
        self.data = data
        self.next = None


def sort_list_counting(head):
    """
    Sort linked list using counting approach.

    Args:
        head: Head node of the linked list

    Returns:
        ListNode: Head of the sorted linked list
    """
    if not head or not head.next:
        return head

    # Count occurrences of 0, 1, and 2
    count = [0, 0, 0]
    curr = head

    while curr:
        count[curr.data] += 1
        curr = curr.next

    # Overwrite values
    curr = head
    idx = 0

    while curr:
        if count[idx] == 0:
            idx += 1
        else:
            curr.data = idx
            count[idx] -= 1
            curr = curr.next

    return head


def sort_list_dutch_national_flag(head):
    """
    Sort linked list using Dutch National Flag approach.
    Rearranges links instead of changing values.

    Args:
        head: Head node of the linked list

    Returns:
        ListNode: Head of the sorted linked list
    """
    if not head or not head.next:
        return head

    # Create dummy heads for three lists
    zero_dummy = ListNode(0)
    one_dummy = ListNode(0)
    two_dummy = ListNode(0)

    # Pointers to current tail of each list
    zero_tail = zero_dummy
    one_tail = one_dummy
    two_tail = two_dummy

    # Traverse and distribute nodes
    curr = head
    while curr:
        next_node = curr.next

        if curr.data == 0:
            zero_tail.next = curr
            zero_tail = curr
        elif curr.data == 1:
            one_tail.next = curr
            one_tail = curr
        else:  # curr.data == 2
            two_tail.next = curr
            two_tail = curr

        curr = next_node

    # Connect the three lists
    zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
    one_tail.next = two_dummy.next
    two_tail.next = None

    return zero_dummy.next


def create_linked_list(values):
    """
    Create a linked list from a list of values.

    Args:
        values: List of integers

    Returns:
        ListNode: Head of the created linked list
    """
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def linked_list_to_list(head):
    """
    Convert linked list to Python list.

    Args:
        head: Head node of the linked list

    Returns:
        list: List of values from the linked list
    """
    result = []
    curr = head

    while curr:
        result.append(curr.data)
        curr = curr.next

    return result


def test_sort_linked_list():
    """Test cases for sorting linked list of 0s, 1s, and 2s."""
    # Test Case 1: Basic case
    values = [1, 1, 2, 0, 2, 0, 1]
    head = create_linked_list(values)
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    expected = [0, 0, 1, 1, 1, 2, 2]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case (counting)")

    # Test Case 2: Using Dutch National Flag
    values = [1, 1, 2, 0, 2, 0, 1]
    head = create_linked_list(values)
    head = sort_list_dutch_national_flag(head)
    result = linked_list_to_list(head)
    expected = [0, 0, 1, 1, 1, 2, 2]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Basic case (Dutch National Flag)")

    # Test Case 3: Already sorted
    values = [0, 0, 1, 1, 2, 2]
    head = create_linked_list(values)
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    expected = [0, 0, 1, 1, 2, 2]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: Already sorted")

    # Test Case 4: Reverse sorted
    values = [2, 2, 1, 1, 0, 0]
    head = create_linked_list(values)
    head = sort_list_dutch_national_flag(head)
    result = linked_list_to_list(head)
    expected = [0, 0, 1, 1, 2, 2]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Reverse sorted")

    # Test Case 5: Single element
    values = [1]
    head = create_linked_list(values)
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    expected = [1]
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Single element")

    # Test Case 6: Empty list
    values = []
    head = create_linked_list(values)
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    expected = []
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Empty list")

    # Test Case 7: Only zeros
    values = [0, 0, 0, 0]
    head = create_linked_list(values)
    head = sort_list_dutch_national_flag(head)
    result = linked_list_to_list(head)
    expected = [0, 0, 0, 0]
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("Test 7 passed: Only zeros")

    # Test Case 8: Only ones
    values = [1, 1, 1, 1]
    head = create_linked_list(values)
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    expected = [1, 1, 1, 1]
    assert result == expected, f"Test 8 failed: Expected {expected}, got {result}"
    print("Test 8 passed: Only ones")

    # Test Case 9: Only twos
    values = [2, 2, 2, 2]
    head = create_linked_list(values)
    head = sort_list_dutch_national_flag(head)
    result = linked_list_to_list(head)
    expected = [2, 2, 2, 2]
    assert result == expected, f"Test 9 failed: Expected {expected}, got {result}"
    print("Test 9 passed: Only twos")

    # Test Case 10: Verify both approaches give same result
    test_cases = [
        [1, 0, 2, 1, 0, 2],
        [2, 2, 1, 0],
        [0, 1, 2, 0, 1, 2],
        [1, 1, 1, 0, 2],
    ]

    for i, values in enumerate(test_cases, 10):
        head1 = create_linked_list(values)
        head2 = create_linked_list(values)

        head1 = sort_list_counting(head1)
        head2 = sort_list_dutch_national_flag(head2)

        result1 = linked_list_to_list(head1)
        result2 = linked_list_to_list(head2)

        assert result1 == result2 == sorted(values), (
            f"Test {i} failed: Approaches differ"
        )
        print(f"Test {i} passed: Both approaches match")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sort_linked_list()

    # Example usage
    print("\nExample 1 (Counting approach):")
    values = [1, 1, 2, 0, 2, 0, 1]
    head = create_linked_list(values)
    print(f"Input:  {values}")
    head = sort_list_counting(head)
    result = linked_list_to_list(head)
    print(f"Output: {result}")

    print("\nExample 2 (Dutch National Flag):")
    values = [1, 1, 2, 0, 2, 0, 1]
    head = create_linked_list(values)
    print(f"Input:  {values}")
    head = sort_list_dutch_national_flag(head)
    result = linked_list_to_list(head)
    print(f"Output: {result}")
