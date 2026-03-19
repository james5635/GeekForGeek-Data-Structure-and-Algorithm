import heapq
from collections import Counter
from typing import List, Optional


# 1. Priority Queue Implementation using heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # To handle tie-breaking for same priority

    def push(self, item, priority):
        # heapq is a min-heap, so we push (priority, index, item)
        # index ensures that if two items have the same priority,
        # the one pushed first comes out first (FIFO for same priority)
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._queue)[-1]  # Return the item

    def is_empty(self):
        return len(self._queue) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._queue[0][-1]


# 2. K most frequent elements
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in the given list.
    Uses a min-heap of size k to keep track of top k frequent elements.
    """
    # Count frequencies
    freq = Counter(nums)

    # Use a min-heap to store the k most frequent elements
    # We'll store tuples of (-frequency, number) to simulate max-heap behavior with min-heap
    # But we can also use min-heap of size k: we push (freq, num) and if size>k, pop the smallest freq
    min_heap = []
    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract the numbers from the heap
    return [num for count, num in min_heap]


# Alternative: Using heapq.nlargest (which is also heap-based)
def top_k_frequent_alt(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    # heapq.nlargest returns the k largest elements from the iterable
    # We use the frequency as the key
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


# 3. Merge k sorted arrays (using heap)
def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merge k sorted arrays into one sorted array using a min-heap.
    """
    # We'll store tuples (value, array_index, element_index) in the heap
    min_heap = []
    result = []

    # Push the first element of each array into the heap
    for i, arr in enumerate(arrays):
        if arr:  # Check if array is not empty
            heapq.heappush(min_heap, (arr[0], i, 0))

    # Extract the smallest from the heap and push the next element from the same array
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        # If there is a next element in the same array, push it
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_elem = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, arr_idx, elem_idx + 1))

    return result


# 4. Median of stream (using two heaps)
class MedianOfStream:
    def __init__(self):
        # max-heap for the lower half (we store negatives to simulate max-heap)
        self.max_heap = []  # will store the smaller half, as negatives
        # min-heap for the upper half
        self.min_heap = []  # will store the larger half

    def add_num(self, num: int) -> None:
        # Add to max_heap (as negative) first, then balance
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps: we want len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move one element from max_heap to min_heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            # Move one element from min_heap to max_heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# 5. Huffman coding concept (simplified)
# We'll build a Huffman tree and generate codes (without actual encoding/decoding)
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heapq to compare nodes, we define __lt__
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text: str) -> Optional[HuffmanNode]:
    if not text:
        return None

    # Count frequency of each character
    freq = Counter(text)

    # Create a priority queue (min-heap) of HuffmanNode
    heap = []
    for char, count in freq.items():
        node = HuffmanNode(char, count)
        heapq.heappush(heap, node)

    # Build the tree
    while len(heap) > 1:
        # Extract two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with these two as children
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # The remaining node is the root
    return heap[0] if heap else None


def generate_huffman_codes(root: HuffmanNode) -> dict:
    """
    Generate Huffman codes by traversing the tree.
    Returns a dictionary mapping characters to their binary codes.
    """
    codes = {}

    def traverse(node, current_code):
        if node is None:
            return

        # If it's a leaf node (has a character)
        if node.char is not None:
            codes[node.char] = (
                current_code if current_code else "0"
            )  # Handle single character case
            return

        # Traverse left (0) and right (1)
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes


# 6. Connect n ropes with minimum cost
def min_cost_to_connect_ropes(ropes: List[int]) -> int:
    """
    Given n ropes of different lengths, we need to connect these ropes into one rope.
    The cost to connect two ropes is equal to the sum of their lengths.
    We need to minimize the total cost.
    """
    if not ropes:
        return 0

    # Convert the list into a min-heap
    heapq.heapify(ropes)
    total_cost = 0

    # Continue until there is only one rope left
    while len(ropes) > 1:
        # Extract the two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        # Cost to connect these two ropes
        cost = first + second
        total_cost += cost

        # Push the connected rope back into the heap
        heapq.heappush(ropes, cost)

    return total_cost


# Main function with example test cases
def main():
    print("=== Heap Applications Demo ===\n")

    # 1. Priority Queue
    print("1. Priority Queue:")
    pq = PriorityQueue()
    pq.push("Task A", 3)
    pq.push("Task B", 1)
    pq.push("Task C", 2)
    pq.push("Task D", 1)  # Same priority as Task B

    while not pq.is_empty():
        print(f"  Popped: {pq.pop()}")
    print()

    # 2. K most frequent elements
    print("2. K most frequent elements:")
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f"  Input: {nums}, k={k}")
    print(f"  Top {k} frequent elements: {result}")

    # Alternative method
    result_alt = top_k_frequent_alt(nums, k)
    print(f"  Alternative method: {result_alt}")
    print()

    # 3. Merge k sorted arrays
    print("3. Merge k sorted arrays:")
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    merged = merge_k_sorted_arrays(arrays)
    print(f"  Arrays: {arrays}")
    print(f"  Merged: {merged}")
    print()

    # 4. Median of stream
    print("4. Median of stream:")
    median_finder = MedianOfStream()
    stream = [5, 15, 1, 3]
    for num in stream:
        median_finder.add_num(num)
        median = median_finder.find_median()
        print(f"  After adding {num}, median = {median}")
    print()

    # 5. Huffman coding concept
    print("5. Huffman coding concept (simplified):")
    text = "aaabbbcc"
    print(f"  Input text: '{text}'")
    root = build_huffman_tree(text)
    if root:
        codes = generate_huffman_codes(root)
        print(f"  Huffman codes: {codes}")
    else:
        print("  Could not build Huffman tree (empty input)")
    print()

    # 6. Connect n ropes with minimum cost
    print("6. Connect n ropes with minimum cost:")
    ropes = [4, 3, 2, 6]
    cost = min_cost_to_connect_ropes(ropes)
    print(f"  Rope lengths: {ropes}")
    print(f"  Minimum cost to connect: {cost}")
    print()


if __name__ == "__main__":
    main()
