class Queue:
    def __init__(self, n):
        self._Q = [0] * n
        self._head = self._tail = 0
        self._n = n

    def enqueue(self, x):
        next = (self._tail + 1) % self._n
        if next == self._head:
            raise Exception("Overflow")
        self._Q[self._tail] = x
        self._tail = next

    def dequeue(self):
        if self._tail == self._head:
            raise Exception("Underflow")
        x = self._Q[self._tail]
        self._tail = (self._n + self._tail - 1) % self._n
        return x

    def __str__(self):
        ret = []
        i = self._head
        while i != self._tail:
            ret.append(self._Q[i])
            i = (i + 1) % self._n

        return str(ret) + str(self._head) + "," + str(self._tail)


def main():
    q = Queue(5)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(8)
    q.dequeue()
    q.dequeue()
    q.enqueue(8)
    q.enqueue(5)
    q.enqueue(9)
    print(q)


if __name__ == "__main__":
    main()
