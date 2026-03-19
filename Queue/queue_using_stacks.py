class QueueEnqueueCostly:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            return -1
        return self.s1.pop()

    def front(self):
        if not self.s1:
            return -1
        return self.s1[-1]

    def size(self):
        return len(self.s1)


class QueueDequeueCostly:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def front(self):
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def size(self):
        return len(self.s1) + len(self.s2)


class QueueRecursion:
    def __init__(self):
        self.s = []

    def enqueue(self, x):
        self.s.append(x)

    def dequeue(self):
        if not self.s:
            return -1
        if len(self.s) == 1:
            return self.s.pop()
        item = self.s.pop()
        res = self.dequeue()
        self.s.append(item)
        return res

    def front(self):
        if not self.s:
            return -1
        if len(self.s) == 1:
            return self.s[-1]
        item = self.s.pop()
        res = self.front()
        self.s.append(item)
        return res

    def size(self):
        return len(self.s)


if __name__ == "__main__":
    print("Approach 1: Enqueue Costly, Dequeue O(1)")
    q1 = QueueEnqueueCostly()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print("Front:", q1.front())
    print("Dequeue:", q1.dequeue())
    print("Front:", q1.front())
    print("Dequeue:", q1.dequeue())
    print("Dequeue:", q1.dequeue())
    print("Dequeue:", q1.dequeue())
    print("Size:", q1.size())
    print()

    print("Approach 2: Dequeue Costly, Enqueue O(1)")
    q2 = QueueDequeueCostly()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print("Front:", q2.front())
    print("Dequeue:", q2.dequeue())
    print("Front:", q2.front())
    print("Dequeue:", q2.dequeue())
    print("Dequeue:", q2.dequeue())
    print("Dequeue:", q2.dequeue())
    print("Size:", q2.size())
    print()

    print("Approach 3: One Stack with Recursion")
    q3 = QueueRecursion()
    q3.enqueue(1)
    q3.enqueue(2)
    q3.enqueue(3)
    print("Front:", q3.front())
    print("Dequeue:", q3.dequeue())
    print("Front:", q3.front())
    print("Dequeue:", q3.dequeue())
    print("Dequeue:", q3.dequeue())
    print("Dequeue:", q3.dequeue())
    print("Size:", q3.size())
