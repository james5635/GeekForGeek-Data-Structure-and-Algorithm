"""
Sort the Queue using Recursion
https://www.geeksforgeeks.org/dsa/sort-the-queue-using-recursion/

Given a queue, the task is to sort it using recursion without using any loop.
Time Complexity: O(n^2)
Auxiliary Space: O(n)
"""


def front_to_end_n(q, qsize):
    """
    One by one moves qsize elements from front to rear of the queue.
    """
    if qsize <= 0:
        return

    # Pop front element and push this last in a queue
    q.append(q.pop(0))

    # Recursive call for pushing element
    front_to_end_n(q, qsize - 1)


def sorted_insert(q, temp, qsize):
    """
    Function to push an element in the queue with qsize in sorted order.
    """
    # Base condition
    if not q or qsize == 0:
        q.append(temp)
        return
    elif temp <= q[0]:
        # Call stack with front of queue
        q.append(temp)
        # One by one move n-1 (old q size elements front to back)
        front_to_end_n(q, qsize)
    else:
        # Push front element into last in a queue
        q.append(q.pop(0))
        # Recursively move all smaller items to back and then insert
        sorted_insert(q, temp, qsize - 1)


def sort_queue(q):
    """
    Function to sort the given queue using recursion.
    """
    if not q:
        return

    # Get the front element which will be stored in this variable
    # throughout the recursion stack
    temp = q.pop(0)
    sort_queue(q)

    # Push the current element into the queue according to the sorting order
    sorted_insert(q, temp, len(q))


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1
    print("Test Case 1:")
    qu = [10, 7, 16, 9, 20, 5]
    print(f"Original queue: {qu}")
    sort_queue(qu)
    print(f"Sorted queue:   {qu}")
    print()

    # Test case 2
    print("Test Case 2:")
    qu = [0, -2, -1, 2, 3, 1]
    print(f"Original queue: {qu}")
    sort_queue(qu)
    print(f"Sorted queue:   {qu}")
    print()

    # Test case 3 - already sorted
    print("Test Case 3 (Already sorted):")
    qu = [1, 2, 3, 4, 5]
    print(f"Original queue: {qu}")
    sort_queue(qu)
    print(f"Sorted queue:   {qu}")


if __name__ == "__main__":
    main()
