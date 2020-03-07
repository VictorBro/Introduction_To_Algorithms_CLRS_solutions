class Queue:
    def __init__(self, n):
        self._Q = [0] * n
        self._n = n
        self._head = self._tail = 0

    def enqueue(self, x):
        next_idx = (self._tail + 1) % self._n
        if next_idx == self._head:
            raise Exception("Queue overflow")
        self._Q[self._tail] = x
        self._tail = next_idx

    def dequeue(self):
        if self._head == self._tail:
            raise Exception("Queue underflow")
        x = self._Q[self._head]
        self._head = (self._head + 1) % self._n
        return x

    def __str__(self):
        arr = []
        i = self._head
        while i != self._tail:
            arr.append(self._Q[i])
            i = (i + 1) % self._n
        return str(arr)


class Stack:
    def __init__(self, n):
        self._A = Queue(n)
        self._A_active = True
        self._B = Queue(n)
        self._n = n - 1
        self._size = 0

    def push(self, x):
        if self._size == self._n:
            raise Exception("Stack overflow")
        if self._A_active:
            self._A.enqueue(x)
        else:
            self._B.enqueue(x)
        self._size += 1

    def _pop_helper(self, A, B):
        i = self._size
        while i != 1:
            B.enqueue(A.dequeue())
            i -= 1
        self._size -= 1
        return A.dequeue()

    def pop(self):
        if self._size == 0:
            raise Exception("Stack underflow")
        if self._A_active:
            self._A_active = False
            x = self._pop_helper(self._A, self._B)
        else:
            self._A_active = True
            x = self._pop_helper(self._B, self._A)
        return x

    def __str__(self):
        return str(self._A) + str(self._B)


def main():
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    s.push(4)
    s.push(5)
    s.push(6)
    print(s)


if __name__ == "__main__":
    main()
