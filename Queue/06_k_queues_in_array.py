class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1
        self.freeIndex = 0

    def isEmpty(self, qn):
        return self.front[qn] == -1

    def isFull(self):
        return self.freeIndex == -1

    def enqueue(self, x, qn):
        if self.isFull():
            print(f"Queue is full. Cannot enqueue {x} to Queue {qn}")
            return
        i = self.freeIndex
        self.freeIndex = self.next[i]
        if self.isEmpty(qn):
            self.front[qn] = i
        else:
            self.next[self.rear[qn]] = i
        self.next[i] = -1
        self.rear[qn] = i
        self.arr[i] = x
        print(f"Enqueued {x} to Queue {qn}")

    def dequeue(self, qn):
        if self.isEmpty(qn):
            print(f"Queue {qn} is empty. Cannot dequeue.")
            return -1
        i = self.front[qn]
        self.front[qn] = self.next[i]
        self.next[i] = self.freeIndex
        self.freeIndex = i
        if self.front[qn] == -1:
            self.rear[qn] = -1
        return self.arr[i]


if __name__ == "__main__":
    kq = kQueues(10, 3)

    kq.enqueue(10, 0)
    kq.enqueue(20, 0)
    kq.enqueue(30, 0)
    kq.enqueue(40, 1)
    kq.enqueue(50, 1)
    kq.enqueue(60, 2)
    kq.enqueue(70, 2)
    kq.enqueue(80, 2)
    kq.enqueue(90, 2)

    print(f"\nDequeued from Queue 0: {kq.dequeue(0)}")
    print(f"Dequeued from Queue 0: {kq.dequeue(0)}")
    print(f"Dequeued from Queue 1: {kq.dequeue(1)}")
    print(f"Dequeued from Queue 2: {kq.dequeue(2)}")

    kq.enqueue(100, 0)
    kq.enqueue(110, 1)

    print(f"\nDequeued from Queue 0: {kq.dequeue(0)}")
    print(f"Dequeued from Queue 0: {kq.dequeue(0)}")
    print(f"Dequeued from Queue 1: {kq.dequeue(1)}")
    print(f"Dequeued from Queue 1: {kq.dequeue(1)}")
    print(f"Dequeued from Queue 2: {kq.dequeue(2)}")
    print(f"Dequeued from Queue 2: {kq.dequeue(2)}")
