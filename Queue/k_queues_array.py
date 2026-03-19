class KQueuesNaive:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [None] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        segment_size = n // k

        for i in range(k):
            self.front[i] = i * segment_size
            self.rear[i] = i * segment_size - 1

    def enqueue(self, x, qn):
        if qn < 0 or qn >= self.k:
            print(f"Queue {qn} does not exist")
            return
        segment_size = self.n // self.k
        start = qn * segment_size
        end = start + segment_size - 1

        if self.rear[qn] < end:
            self.rear[qn] += 1
            self.arr[self.rear[qn]] = x
        else:
            print(f"Queue {qn} is full")

    def dequeue(self, qn):
        if qn < 0 or qn >= self.k:
            print(f"Queue {qn} does not exist")
            return -1
        if self.front[qn] == -1 or self.front[qn] >= self.n // self.k * (qn + 1):
            print(f"Queue {qn} is empty")
            return -1
        x = self.arr[self.front[qn]]
        self.front[qn] += 1
        return x

    def isEmpty(self, qn):
        segment_size = self.n // self.k
        if self.front[qn] == -1 or self.front[qn] >= self.n // self.k * (qn + 1):
            return True
        return False


class KQueuesOptimized:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [None] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [i + 1 for i in range(n)]
        self.next[-1] = -1
        self.free = 0

    def isFull(self):
        return self.free == -1

    def isEmpty(self, qn):
        return self.front[qn] == -1

    def enqueue(self, x, qn):
        if self.isFull():
            print(f"Queue {qn} is full")
            return

        index = self.free
        self.free = self.next[index]

        if self.front[qn] == -1:
            self.front[qn] = index
        else:
            self.next[self.rear[qn]] = index

        self.next[index] = -1
        self.rear[qn] = index
        self.arr[index] = x

    def dequeue(self, qn):
        if self.isEmpty(qn):
            print(f"Queue {qn} is empty")
            return -1

        front_index = self.front[qn]
        self.front[qn] = self.next[front_index]

        self.next[front_index] = self.free
        self.free = front_index

        return self.arr[front_index]


if __name__ == "__main__":
    n, k = 10, 3

    print("=== Naive Approach ===")
    kq_naive = KQueuesNaive(n, k)
    kq_naive.enqueue(10, 0)
    kq_naive.enqueue(20, 0)
    kq_naive.enqueue(30, 1)
    kq_naive.enqueue(40, 2)
    print(f"Dequeue Q0: {kq_naive.dequeue(0)}")
    print(f"Dequeue Q0: {kq_naive.dequeue(0)}")
    print(f"Dequeue Q1: {kq_naive.dequeue(1)}")
    print(f"Dequeue Q2: {kq_naive.dequeue(2)}")

    print("\n=== Space Optimized Approach ===")
    kq_opt = KQueuesOptimized(n, k)
    kq_opt.enqueue(10, 0)
    kq_opt.enqueue(20, 0)
    kq_opt.enqueue(30, 1)
    kq_opt.enqueue(40, 2)
    kq_opt.enqueue(50, 0)
    kq_opt.enqueue(60, 1)
    kq_opt.enqueue(70, 2)
    print(f"Dequeue Q0: {kq_opt.dequeue(0)}")
    print(f"Dequeue Q0: {kq_opt.dequeue(0)}")
    print(f"Dequeue Q1: {kq_opt.dequeue(1)}")
    print(f"Dequeue Q2: {kq_opt.dequeue(2)}")
