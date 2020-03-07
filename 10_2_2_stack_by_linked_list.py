class Node:
    def __init__(self, val, next=None):
        self.key = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        x = self.head
        prev = None
        while x is not None and x.key != key:
            prev = x
            x = x.next
        if x is not None:
            if prev is None:
                self.head = x.next
            else:
                prev.next = x.next

    def __str__(self):
        L = []
        x = self.head
        while x is not None:
            L.append(x.key)
            x = x.next
        return str(L)


class Stack:
    def __init__(self):
        self._L = LinkedList()

    def push(self, key):
        self._L.insert(Node(key))

    def pop(self):
        if self._L.head is None:
            raise Exception("Underflow")
        x = self._L.head
        self._L.head = self._L.head.next
        return x.key

    def __str__(self):
        return str(self._L)


def main():
    S = Stack()
    S.push(14)
    S.push(3)
    S.push(6)
    print(S.pop())
    print(S)


if __name__ == "__main__":
    main()
