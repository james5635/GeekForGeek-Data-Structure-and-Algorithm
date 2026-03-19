from collections import deque


class StackTwoQueuesPushCostly:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return -1
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            return -1
        return self.q1[0]

    def size(self):
        return len(self.q1)


class StackTwoQueuesPopCostly:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        if not self.q1:
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return val

    def size(self):
        return len(self.q1)


class StackSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return -1
        return self.q.popleft()

    def top(self):
        if not self.q:
            return -1
        return self.q[0]

    def size(self):
        return len(self.q)


if __name__ == "__main__":
    print("Approach 1: Two Queues - Push O(n), Pop O(1)")
    s1 = StackTwoQueuesPushCostly()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    print("Top:", s1.top())
    print("Pop:", s1.pop())
    print("Top:", s1.top())
    print("Pop:", s1.pop())
    print("Pop:", s1.pop())
    print("Pop:", s1.pop())
    print("Size:", s1.size())
    print()

    print("Approach 2: Two Queues - Push O(1), Pop O(n)")
    s2 = StackTwoQueuesPopCostly()
    s2.push(1)
    s2.push(2)
    s2.push(3)
    print("Top:", s2.top())
    print("Pop:", s2.pop())
    print("Top:", s2.top())
    print("Pop:", s2.pop())
    print("Pop:", s2.pop())
    print("Pop:", s2.pop())
    print("Size:", s2.size())
    print()

    print("Approach 3: Single Queue - Push O(n), Pop O(1)")
    s3 = StackSingleQueue()
    s3.push(1)
    s3.push(2)
    s3.push(3)
    print("Top:", s3.top())
    print("Pop:", s3.pop())
    print("Top:", s3.top())
    print("Pop:", s3.pop())
    print("Pop:", s3.pop())
    print("Pop:", s3.pop())
    print("Size:", s3.size())
