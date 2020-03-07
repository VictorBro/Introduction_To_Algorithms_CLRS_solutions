class Node:
    def __init__(self, val, next=None):
        self.key = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, key):
        if self.head is None:
            self.tail = Node(key)
            self.head = self.tail
        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            raise Exception("Underflow")
        x = self.head
        self.head = self.head.next
        return x.key

    def __str__(self):
        L = []
        x = self.head
        while x is not None:
            L.append(x.key)
            x = x.next
        return str(L)


def main():
    Q = Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    print(Q.dequeue())
    Q.enqueue(5)
    print(Q)


if __name__ == "__main__":
    main()
