class Stack:
    def __init__(self, n):
        self._S = [0] * n
        self._n = n
        self._top = -1

    def push(self, x):
        if self._top + 1 == self._n:
            raise Exception("Stack overflow")
        self._top += 1
        self._S[self._top] = x

    def pop(self):
        if self.empty():
            raise Exception("Stack underflow")
        x = self._S[self._top]
        self._top -= 1
        return x

    def empty(self):
        return self._top == -1

    def __str__(self):
        return str(self._S[:self._top + 1])


class Queue:
    def __init__(self, n):
        self._A = Stack(n)
        self._B = Stack(n)
        self._n = n
        self._size = 0

    def enqueue(self, x):
        if self._size == self._n:
            raise Exception("Queue overflow")
        self._B.push(x)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise Exception("Queue underflow")
        if self._A.empty():
            while not self._B.empty():
                self._A.push(self._B.pop())
        x = self._A.pop()
        self._size -= 1
        return x

    def __str__(self):
        return str(self._A) + str(self._B)


def main():
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q)


if __name__ == "__main__":
    main()
