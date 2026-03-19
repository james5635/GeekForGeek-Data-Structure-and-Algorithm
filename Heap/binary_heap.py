# Python program to demonstrate working of Binary Heap
# This code is based on the GeeksforGeeks article on Binary Heap


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * float("inf")
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (
                self.Heap[pos] > self.Heap[self.leftChild(pos)]
                or self.Heap[pos] > self.Heap[self.rightChild(pos)]
            ):
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insertKey(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(
                " PARENT : "
                + str(self.Heap[i])
                + " LEFT CHILD : "
                + str(self.Heap[2 * i])
                + " RIGHT CHILD : "
                + str(self.Heap[2 * i + 1])
            )

    # Function to remove and return the minimum
    # element from the heap
    def extractMin(self):
        if self.size <= 0:
            return float("inf")
        if self.size == 1:
            self.size -= 1
            return self.Heap[1]
        popped = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(1)
        return popped

    # Function to get the minimum element from the heap
    def getMin(self):
        return self.Heap[1]

    # Function to decrease the value of key at
    # index 'i' to new_val. It is assumed that
    # new_val is smaller than Heap[i].
    def decreaseKey(self, i, new_val):
        self.Heap[i] = new_val
        while self.Heap[i] < self.Heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # Function to delete a key at index i.
    # It works by first decreasing the key to
    # negative infinity and then removing it.
    def deleteKey(self, i):
        self.decreaseKey(i, -1 * float("inf"))
        self.extractMin()


# Driver Code
if __name__ == "__main__":
    print("The MinHeap is:")
    minHeap = MinHeap(15)
    minHeap.insertKey(5)
    minHeap.insertKey(3)
    minHeap.insertKey(17)
    minHeap.insertKey(10)
    minHeap.insertKey(84)
    minHeap.insertKey(19)
    minHeap.insertKey(6)
    minHeap.insertKey(22)
    minHeap.insertKey(9)

    minHeap.Print()

    print("The Min val is " + str(minHeap.getMin()))
    minHeap.decreaseKey(2, 1)
    print("The Min val after decreaseKey is " + str(minHeap.getMin()))
    print("The extracted min is " + str(minHeap.extractMin()))
    print("The Min val after extractMin is " + str(minHeap.getMin()))
    minHeap.deleteKey(5)
    print("The Min val after deleteKey is " + str(minHeap.getMin()))
