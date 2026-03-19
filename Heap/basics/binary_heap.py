"""
Binary Heap Implementation in Python

A Binary Heap is a complete binary tree where elements are arranged in a specific order:
- Min Heap: Parent node is smaller than its children (root is minimum)
- Max Heap: Parent node is larger than its children (root is maximum)

Array Representation:
- Root element: arr[0]
- Parent of node i: arr[(i-1)//2]
- Left child of node i: arr[2*i + 1]
- Right child of node i: arr[2*i + 2]

Time Complexity: O(log n) for insert, delete, extract operations
Space Complexity: O(n) for storing n elements

Source: https://www.geeksforgeeks.org/binary-heap/
"""

from typing import Optional, Union
import math


class MinHeap:
    """Min Heap implementation using array representation."""

    def __init__(self):
        self.arr: list = []

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def get_min(self) -> Optional[int]:
        return self.arr[0] if self.arr else None

    def insert(self, k: int) -> None:
        self.arr.append(k)
        i = len(self.arr) - 1
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def decrease_key(self, i: int, new_val: Union[int, float]) -> None:
        self.arr[i] = new_val
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_min(self) -> Optional[int]:
        if len(self.arr) <= 0:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()

        res = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.min_heapify(0)
        return res

    def delete_key(self, i: int) -> None:
        self.decrease_key(i, -float("inf"))
        self.extract_min()

    def min_heapify(self, i: int) -> None:
        l, r, n = self.left(i), self.right(i), len(self.arr)
        smallest = i
        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

    def increase_key(self, i: int, new_val: int) -> None:
        self.arr[i] = new_val
        self.min_heapify(i)

    def change_value(self, i: int, new_val: int) -> None:
        if self.arr[i] < new_val:
            self.increase_key(i, new_val)
        else:
            self.decrease_key(i, new_val)

    def size(self) -> int:
        return len(self.arr)

    def is_empty(self) -> bool:
        return len(self.arr) == 0


class MaxHeap:
    """Max Heap implementation using array representation."""

    def __init__(self):
        self.arr: list = []

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def get_max(self) -> Optional[int]:
        return self.arr[0] if self.arr else None

    def insert(self, k: int) -> None:
        self.arr.append(k)
        i = len(self.arr) - 1
        while i > 0 and self.arr[self.parent(i)] < self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_max(self) -> Optional[int]:
        if len(self.arr) <= 0:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()

        res = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.max_heapify(0)
        return res

    def max_heapify(self, i: int) -> None:
        l, r, n = self.left(i), self.right(i), len(self.arr)
        largest = i
        if l < n and self.arr[l] > self.arr[largest]:
            largest = l
        if r < n and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)


if __name__ == "__main__":
    print("=== MinHeap Demo ===")
    h = MinHeap()
    h.insert(3)
    h.insert(2)
    h.delete_key(1)
    h.insert(15)
    h.insert(5)
    h.insert(4)
    h.insert(45)

    print(f"Extract min: {h.extract_min()}")  # 2
    print(f"Get min: {h.get_min()}")  # 4
    h.decrease_key(2, 1)
    print(f"After decrease key: {h.extract_min()}")  # 1

    print("\n=== MaxHeap Demo ===")
    mh = MaxHeap()
    mh.insert(3)
    mh.insert(2)
    mh.insert(15)
    mh.insert(5)
    mh.insert(4)
    mh.insert(45)

    print(f"Extract max: {mh.extract_max()}")  # 45
    print(f"Get max: {mh.get_max()}")  # 15
